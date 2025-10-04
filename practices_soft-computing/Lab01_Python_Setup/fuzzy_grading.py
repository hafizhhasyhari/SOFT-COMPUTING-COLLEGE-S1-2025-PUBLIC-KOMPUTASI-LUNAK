"""
PROJECT 01: SISTEM PENILAIAN MAHASISWA MENGGUNAKAN FUZZY LOGIC
Dibuat oleh: Hafizh Hilman Asyhari
Github : hafizhhasyhari
Tanggal: Rabu, 17 September 2025
Deskripsi: Sistem grading otomatis menggunakan fuzzy logic
Circle : Scrivener Artificial Intelligence
- The Scrivener's Presenter Asia
"""

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

class FuzzyGradingSystem:
    """
    Sistem penilaian mahasiswa menggunakan Fuzzy Logic
    
    Input:
    - Nilai Tugas (0-100)
    - Nilai UTS (0-100)
    - Nilai UAS (0-100)
    
    Output:
    - Grade Akhir (0-100)
    - Huruf Mutu (A, AB, B, BC, C, D, E)
    """
    
    def __init__(self):
        """Inisialisasi sistem fuzzy"""
        self.setup_fuzzy_system()
    
    def setup_fuzzy_system(self):
        """Setup fuzzy variables dan rules"""
        
        # ===== LANGKAH 1: DEFINISI VARIABEL FUZZY =====
        
        # Input: Nilai Tugas (0-100)
        self.tugas = ctrl.Antecedent(np.arange(0, 101, 1), 'tugas')
        
        # Input: Nilai UTS (0-100)
        self.uts = ctrl.Antecedent(np.arange(0, 101, 1), 'uts')
        
        # Input: Nilai UAS (0-100)
        self.uas = ctrl.Antecedent(np.arange(0, 101, 1), 'uas')
        
        # Output: Nilai Akhir (0-100)
        self.nilai_akhir = ctrl.Consequent(np.arange(0, 101, 1), 'nilai_akhir')
        
        # ===== LANGKAH 2: MEMBERSHIP FUNCTIONS =====
        
        # Membership function untuk input (Tugas, UTS, UAS)
        # Menggunakan trapezoid dan triangle
        
        # Kategori: Rendah, Sedang, Tinggi
        for var in [self.tugas, self.uts, self.uas]:
            var['rendah'] = fuzz.trapmf(var.universe, [0, 0, 40, 60])
            var['sedang'] = fuzz.trimf(var.universe, [40, 60, 80])
            var['tinggi'] = fuzz.trapmf(var.universe, [60, 80, 100, 100])
        
        # Membership function untuk output (Nilai Akhir)
        self.nilai_akhir['E'] = fuzz.trapmf(self.nilai_akhir.universe, [0, 0, 40, 50])
        self.nilai_akhir['D'] = fuzz.trimf(self.nilai_akhir.universe, [40, 50, 60])
        self.nilai_akhir['C'] = fuzz.trimf(self.nilai_akhir.universe, [50, 60, 70])
        self.nilai_akhir['BC'] = fuzz.trimf(self.nilai_akhir.universe, [60, 70, 75])
        self.nilai_akhir['B'] = fuzz.trimf(self.nilai_akhir.universe, [70, 75, 80])
        self.nilai_akhir['AB'] = fuzz.trimf(self.nilai_akhir.universe, [75, 80, 90])
        self.nilai_akhir['A'] = fuzz.trapmf(self.nilai_akhir.universe, [80, 90, 100, 100])
        
        # ===== LANGKAH 3: FUZZY RULES =====
        
        # Rule 1: Jika semua tinggi -> A
        rule1 = ctrl.Rule(
            self.tugas['tinggi'] & self.uts['tinggi'] & self.uas['tinggi'],
            self.nilai_akhir['A']
        )
        
        # Rule 2: Jika mayoritas tinggi -> AB
        rule2 = ctrl.Rule(
            (self.tugas['tinggi'] & self.uts['tinggi'] & self.uas['sedang']) |
            (self.tugas['tinggi'] & self.uts['sedang'] & self.uas['tinggi']) |
            (self.tugas['sedang'] & self.uts['tinggi'] & self.uas['tinggi']),
            self.nilai_akhir['AB']
        )
        
        # Rule 3: Jika semua sedang -> B
        rule3 = ctrl.Rule(
            self.tugas['sedang'] & self.uts['sedang'] & self.uas['sedang'],
            self.nilai_akhir['B']
        )
        
        # Rule 4: Jika ada yang rendah tapi ada yang tinggi -> BC
        rule4 = ctrl.Rule(
            (self.tugas['rendah'] & self.uts['tinggi'] & self.uas['sedang']) |
            (self.tugas['sedang'] & self.uts['rendah'] & self.uas['tinggi']) |
            (self.tugas['tinggi'] & self.uts['sedang'] & self.uas['rendah']),
            self.nilai_akhir['BC']
        )
        
        # Rule 5: Jika mayoritas sedang dengan satu rendah -> C
        rule5 = ctrl.Rule(
            (self.tugas['rendah'] & self.uts['sedang'] & self.uas['sedang']) |
            (self.tugas['sedang'] & self.uts['rendah'] & self.uas['sedang']) |
            (self.tugas['sedang'] & self.uts['sedang'] & self.uas['rendah']),
            self.nilai_akhir['C']
        )
        
        # Rule 6: Jika mayoritas rendah -> D
        rule6 = ctrl.Rule(
            (self.tugas['rendah'] & self.uts['rendah'] & self.uas['sedang']) |
            (self.tugas['rendah'] & self.uts['sedang'] & self.uas['rendah']) |
            (self.tugas['sedang'] & self.uts['rendah'] & self.uas['rendah']),
            self.nilai_akhir['D']
        )
        
        # Rule 7: Jika semua rendah -> E
        rule7 = ctrl.Rule(
            self.tugas['rendah'] & self.uts['rendah'] & self.uas['rendah'],
            self.nilai_akhir['E']
        )
        
        # ===== LANGKAH 4: CONTROL SYSTEM =====
        self.grading_ctrl = ctrl.ControlSystem([
            rule1, rule2, rule3, rule4, rule5, rule6, rule7
        ])
        self.grading_sim = ctrl.ControlSystemSimulation(self.grading_ctrl)
    
    def hitung_grade(self, nilai_tugas, nilai_uts, nilai_uas):
        """
        Menghitung grade berdasarkan input
        
        Parameters:
        -----------
        nilai_tugas : float
            Nilai tugas (0-100)
        nilai_uts : float
            Nilai UTS (0-100)
        nilai_uas : float
            Nilai UAS (0-100)
            
        Returns:
        --------
        dict : Dictionary berisi nilai akhir dan grade huruf
        """
        
        # Input ke sistem fuzzy
        self.grading_sim.input['tugas'] = nilai_tugas
        self.grading_sim.input['uts'] = nilai_uts
        self.grading_sim.input['uas'] = nilai_uas
        
        # Compute hasil
        self.grading_sim.compute()
        
        # Ambil output
        nilai_akhir = self.grading_sim.output['nilai_akhir']
        
        # Konversi ke huruf mutu
        huruf = self.nilai_ke_huruf(nilai_akhir)
        
        return {
            'nilai_tugas': nilai_tugas,
            'nilai_uts': nilai_uts,
            'nilai_uas': nilai_uas,
            'nilai_akhir': round(nilai_akhir, 2),
            'huruf_mutu': huruf
        }
    
    def nilai_ke_huruf(self, nilai):
        """Konversi nilai numerik ke huruf mutu"""
        if nilai >= 85:
            return 'A'
        elif nilai >= 80:
            return 'AB'
        elif nilai >= 75:
            return 'B'
        elif nilai >= 70:
            return 'BC'
        elif nilai >= 60:
            return 'C'
        elif nilai >= 50:
            return 'D'
        else:
            return 'E'
    
    def visualisasi_membership(self):
        """Visualisasi membership functions"""
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        
        # Plot input variables
        self.tugas.view(ax=axes[0, 0])
        axes[0, 0].set_title('Membership Function: Nilai Tugas', fontsize=12, fontweight='bold')
        
        self.uts.view(ax=axes[0, 1])
        axes[0, 1].set_title('Membership Function: Nilai UTS', fontsize=12, fontweight='bold')
        
        self.uas.view(ax=axes[1, 0])
        axes[1, 0].set_title('Membership Function: Nilai UAS', fontsize=12, fontweight='bold')
        
        # Plot output variable
        self.nilai_akhir.view(ax=axes[1, 1])
        axes[1, 1].set_title('Membership Function: Nilai Akhir', fontsize=12, fontweight='bold')
        
        plt.tight_layout()
        plt.savefig('results/membership_functions.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        print("✅ Visualisasi membership functions berhasil disimpan!")


def main():
    """Fungsi utama untuk testing"""
    
    print("=" * 60)
    print("🎓 SISTEM PENILAIAN MAHASISWA MENGGUNAKAN FUZZY LOGIC")
    print("=" * 60)
    print()
    
    # Inisialisasi sistem
    sistem = FuzzyGradingSystem()
    
    # Test cases
    test_data = [
        {'nama': 'Mahasiswa A', 'tugas': 90, 'uts': 85, 'uas': 88},
        {'nama': 'Mahasiswa B', 'tugas': 75, 'uts': 78, 'uas': 72},
        {'nama': 'Mahasiswa C', 'tugas': 60, 'uts': 65, 'uas': 58},
        {'nama': 'Mahasiswa D', 'tugas': 45, 'uts': 50, 'uas': 48},
        {'nama': 'Mahasiswa E', 'tugas': 85, 'uts': 60, 'uas': 70},
    ]
    
    print("📊 HASIL PENILAIAN:\n")
    print(f"{'Nama':<15} {'Tugas':<8} {'UTS':<8} {'UAS':<8} {'Akhir':<10} {'Grade':<8}")
    print("-" * 60)
    
    hasil_semua = []
    
    for data in test_data:
        hasil = sistem.hitung_grade(data['tugas'], data['uts'], data['uas'])
        hasil_semua.append(hasil)
        
        print(f"{data['nama']:<15} {hasil['nilai_tugas']:<8} {hasil['nilai_uts']:<8} "
              f"{hasil['nilai_uas']:<8} {hasil['nilai_akhir']:<10} {hasil['huruf_mutu']:<8}")
    
    print("\n" + "=" * 60)
    print("✅ Proses penilaian selesai!")
    print("=" * 60)
    
    # Visualisasi
    print("\n📈 Membuat visualisasi membership functions...")
    sistem.visualisasi_membership()
    
    # Bandingkan dengan crisp system
    print("\n🔍 PERBANDINGAN DENGAN CRISP SYSTEM (Hard Computing):\n")
    print(f"{'Metode':<20} {'Mahasiswa E':<15}")
    print("-" * 35)
    
    # Crisp: rata-rata biasa
    rata_rata_crisp = (85 + 60 + 70) / 3
    grade_crisp = sistem.nilai_ke_huruf(rata_rata_crisp)
    
    # Fuzzy: dari hasil di atas
    grade_fuzzy = hasil_semua[4]['huruf_mutu']
    
    print(f"{'Hard Computing':<20} {rata_rata_crisp:.2f} ({grade_crisp})")
    print(f"{'Soft Computing':<20} {hasil_semua[4]['nilai_akhir']:.2f} ({grade_fuzzy})")
    print("\n💡 Fuzzy logic memberikan penilaian yang lebih 'adil' dengan")
    print("   mempertimbangkan distribusi nilai yang tidak merata!")


if __name__ == "__main__":
    main()
