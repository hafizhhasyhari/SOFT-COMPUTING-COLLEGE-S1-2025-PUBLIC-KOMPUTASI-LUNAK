### File: `hard_vs_soft_comparison.py`

# PROJECT 04: PERBANDINGAN HARD VS SOFT COMPUTING
# Dibuat oleh: [Nama Anda]
# Deskripsi: Membandingkan pendekatan hard dan soft untuk root finding


import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve, minimize
import time

class HardVsSoftComparison:
    """Perbandingan metode hard dan soft computing"""
    
    def __init__(self):
        """Inisialisasi"""
        self.results = {
            'hard': {},
            'soft': {}
        }
    
    # ========== HARD COMPUTING ==========
    
    def newton_raphson(self, f, df, x0, tol=1e-6, max_iter=100):
        """
        Newton-Raphson Method (Hard Computing)
        
        Metode numerik klasik untuk mencari akar persamaan.
        Butuh turunan fungsi (derivative).
        """
        start_time = time.time()
        
        x = x0
        iterations = 0
        history = [x]
        
        for i in range(max_iter):
            iterations += 1
            
            fx = f(x)
            dfx = df(x)
            
            if abs(dfx) < 1e-10:
                # Turunan terlalu kecil, method gagal
                return None, history, time.time() - start_time, iterations
            
            x_new = x - fx / dfx
            history.append(x_new)
            
            if abs(x_new - x) < tol:
                return x_new, history, time.time() - start_time, iterations
            
            x = x_new
        
        return x, history, time.time() - start_time, iterations
    
    def bisection_method(self, f, a, b, tol=1e-6, max_iter=100):
        """
        Bisection Method (Hard Computing)
        
        Metode yang lebih robust tapi lambat.
        Butuh interval [a,b] dimana f(a) dan f(b) berbeda tanda.
        """
        start_time = time.time()
        
        if f(a) * f(b) > 0:
            return None, [], time.time() - start_time, 0
        
        history = []
        iterations = 0
        
        while (b - a) / 2 > tol and iterations < max_iter:
            iterations += 1
            c = (a + b) / 2
            history.append(c)
            
            if abs(f(c)) < tol:
                return c, history, time.time() - start_time, iterations
            
            if f(c) * f(a) < 0:
                b = c
            else:
                a = c
        
        return (a + b) / 2, history, time.time() - start_time, iterations
    
    # ========== SOFT COMPUTING ==========
    
    def genetic_algorithm_root(self, f, bounds, pop_size=100, generations=200):
        """
        Genetic Algorithm untuk mencari akar (Soft Computing)
        
        Tidak butuh turunan, tidak butuh tebakan awal yang bagus.
        Bisa menemukan multiple roots sekaligus.
        """
        start_time = time.time()
        
        # Inisialisasi populasi
        population = np.random.uniform(bounds[0], bounds[1], pop_size)
        
        best_history = []
        
        for gen in range(generations):
            # Fitness: semakin dekat ke 0 semakin bagus
            fitness = 1 / (np.abs([f(x) for x in population]) + 1e-10)
            
            # Tracking
            best_idx = np.argmax(fitness)
            best_history.append(population[best_idx])
            
            # Check convergence
            if abs(f(population[best_idx])) < 1e-6:
                return population[best_idx], best_history, time.time() - start_time, gen + 1
            
            # Selection (Tournament)
            parents = []
            for _ in range(pop_size):
                tournament_idx = np.random.choice(pop_size, 5)
                winner_idx = tournament_idx[np.argmax(fitness[tournament_idx])]
                parents.append(population[winner_idx])
            parents = np.array(parents)
            
            # Crossover & Mutation
            new_population = []
            for i in range(0, pop_size, 2):
                if i + 1 < pop_size:
                    # Crossover (rata-rata)
                    child1 = (parents[i] + parents[i+1]) / 2
                    child2 = parents[i] - (parents[i+1] - parents[i]) * 0.5
                    
                    # Mutation (10% chance)
                    if np.random.random() < 0.1:
                        child1 += np.random.normal(0, 0.5)
                    if np.random.random() < 0.1:
                        child2 += np.random.normal(0, 0.5)
                    
                    # Pastikan dalam bounds
                    child1 = np.clip(child1, bounds[0], bounds[1])
                    child2 = np.clip(child2, bounds[0], bounds[1])
                    
                    new_population.extend([child1, child2])
                else:
                    new_population.append(parents[i])
            
            population = np.array(new_population)
        
        best_idx = np.argmax(fitness)
        return population[best_idx], best_history, time.time() - start_time, generations
    
    def particle_swarm_root(self, f, bounds, n_particles=50, iterations=100):
        """
        Particle Swarm Optimization untuk mencari akar (Soft Computing)
        
        Terinspirasi dari kawanan burung/ikan yang bergerak bersama.
        """
        start_time = time.time()
        
        # Inisialisasi partikel
        particles = np.random.uniform(bounds[0], bounds[1], n_particles)
        velocities = np.random.uniform(-1, 1, n_particles)
        
        # Personal best
        pbest = particles.copy()
        pbest_scores = np.array([abs(f(x)) for x in particles])
        
        # Global best
        gbest_idx = np.argmin(pbest_scores)
        gbest = pbest[gbest_idx]
        
        best_history = [gbest]
        
        # PSO parameters
        w = 0.7  # inertia
        c1 = 1.5  # cognitive (personal)
        c2 = 1.5  # social (global)
        
        for iteration in range(iterations):
            for i in range(n_particles):
                # Update velocity
                r1, r2 = np.random.random(), np.random.random()
                velocities[i] = (w * velocities[i] + 
                                c1 * r1 * (pbest[i] - particles[i]) +
                                c2 * r2 * (gbest - particles[i]))
                
                # Update position
                particles[i] += velocities[i]
                particles[i] = np.clip(particles[i], bounds[0], bounds[1])
                
                # Update personal best
                score = abs(f(particles[i]))
                if score < pbest_scores[i]:
                    pbest[i] = particles[i]
                    pbest_scores[i] = score
                    
                    # Update global best
                    if score < abs(f(gbest)):
                        gbest = particles[i]
            
            best_history.append(gbest)
            
            # Check convergence
            if abs(f(gbest)) < 1e-6:
                return gbest, best_history, time.time() - start_time, iteration + 1
        
        return gbest, best_history, time.time() - start_time, iterations
    
    def compare_methods(self):
        """Bandingkan semua metode untuk berbagai fungsi"""
        
        print("=" * 80)
        print("🔄 PERBANDINGAN HARD COMPUTING VS SOFT COMPUTING")
        print("=" * 80)
        print()
        
        # ===== TEST CASE 1: Fungsi Sederhana =====
        print("📊 TEST CASE 1: Fungsi Sederhana")
        print("   f(x) = x^2 - 4  (akar: x = 2 atau x = -2)")
        print("-" * 80)
        
        def f1(x):
            return x**2 - 4
        
        def df1(x):
            return 2*x
        
        # Hard Computing
        print("\n🔧 HARD COMPUTING:")
        
        # Newton-Raphson
        root_nr, hist_nr, time_nr, iter_nr = self.newton_raphson(f1, df1, x0=1.0)
        print(f"   Newton-Raphson:")
        print(f"   - Hasil: x = {root_nr:.6f}, f(x) = {f1(root_nr):.2e}")
        print(f"   - Waktu: {time_nr*1000:.2f} ms")
        print(f"   - Iterasi: {iter_nr}")
        
        # Bisection
        root_bs, hist_bs, time_bs, iter_bs = self.bisection_method(f1, 0, 3)
        print(f"   Bisection Method:")
        print(f"   - Hasil: x = {root_bs:.6f}, f(x) = {f1(root_bs):.2e}")
        print(f"   - Waktu: {time_bs*1000:.2f} ms")
        print(f"   - Iterasi: {iter_bs}")
        
        # Soft Computing
        print("\n🧠 SOFT COMPUTING:")
        
        # Genetic Algorithm
        root_ga, hist_ga, time_ga, gen_ga = self.genetic_algorithm_root(f1, [-5, 5])
        print(f"   Genetic Algorithm:")
        print(f"   - Hasil: x = {root_ga:.6f}, f(x) = {f1(root_ga):.2e}")
        print(f"   - Waktu: {time_ga*1000:.2f} ms")
        print(f"   - Generasi: {gen_ga}")
        
        # PSO
        root_pso, hist_pso, time_pso, iter_pso = self.particle_swarm_root(f1, [-5, 5])
        print(f"   Particle Swarm Optimization:")
        print(f"   - Hasil: x = {root_pso:.6f}, f(x) = {f1(root_pso):.2e}")
        print(f"   - Waktu: {time_pso*1000:.2f} ms")
        print(f"   - Iterasi: {iter_pso}")
        
        # ===== TEST CASE 2: Fungsi Kompleks =====
        print("\n\n📊 TEST CASE 2: Fungsi Kompleks (Banyak Local Minima)")
        print("   f(x) = sin(x) + 0.1*x^2  (multiple roots)")
        print("-" * 80)
        
        def f2(x):
            return np.sin(x) + 0.1*x**2
        
        def df2(x):
            return np.cos(x) + 0.2*x
        
        # Hard Computing
        print("\n🔧 HARD COMPUTING:")
        
        root_nr2, hist_nr2, time_nr2, iter_nr2 = self.newton_raphson(f2, df2, x0=1.0)
        print(f"   Newton-Raphson:")
        if root_nr2 is not None:
            print(f"   - Hasil: x = {root_nr2:.6f}, f(x) = {f2(root_nr2):.2e}")
            print(f"   - Waktu: {time_nr2*1000:.2f} ms")
            print(f"   - ⚠️ Hanya menemukan 1 akar (tergantung starting point)")
        else:
            print(f"   - ❌ GAGAL! (derivative = 0)")
        
        # Soft Computing
        print("\n🧠 SOFT COMPUTING:")
        
        root_ga2, hist_ga2, time_ga2, gen_ga2 = self.genetic_algorithm_root(f2, [-5, 5])
        print(f"   Genetic Algorithm:")
        print(f"   - Hasil: x = {root_ga2:.6f}, f(x) = {f2(root_ga2):.2e}")
        print(f"   - Waktu: {time_ga2*1000:.2f} ms")
        print(f"   - ✅ Bisa menemukan berbagai akar dengan coba multiple runs")
        
        # ===== VISUALISASI =====
        print("\n\n📈 Membuat visualisasi perbandingan...")
        self.plot_comparison(f1, f2, root_nr, root_ga, root_pso)
        
        # ===== KESIMPULAN =====
        print("\n" + "=" * 80)
        print("📊 KESIMPULAN PERBANDINGAN")
        print("=" * 80)
        
        print("\n🔧 HARD COMPUTING (Newton-Raphson, Bisection):")
        print("   ✅ Kelebihan:")
        print("      - Sangat cepat (milidetik)")
        print("      - Akurat tinggi")
        print("      - Guaranteed converge (bisection)")
        print("   ❌ Kekurangan:")
        print("      - Butuh turunan fungsi (Newton)")
        print("      - Sensitif terhadap starting point")
        print("      - Sulit untuk fungsi kompleks")
        print("      - Hanya menemukan 1 solusi")
        
        print("\n🧠 SOFT COMPUTING (GA, PSO):")
        print("   ✅ Kelebihan:")
        print("      - Tidak butuh turunan")
        print("      - Bisa menemukan multiple solutions")
        print("      - Robust terhadap noise")
        print("      - Cocok untuk fungsi kompleks/diskontinu")
        print("   ❌ Kekurangan:")
        print("      - Lebih lambat")
        print("      - Tidak guaranteed optimal")
        print("      - Perlu tuning parameter")
        
        print("\n💡 KAPAN PAKAI APA?")
        print("   🔧 Pakai Hard Computing jika:")
        print("      → Fungsi smooth dan differentiable")
        print("      → Butuh akurasi maksimal")
        print("      → Waktu komputasi penting")
        print("   🧠 Pakai Soft Computing jika:")
        print("      → Fungsi kompleks/tidak smooth")
        print("      → Perlu menemukan banyak solusi")
        print("      → Solusi 'cukup baik' sudah OK")
        
        print("\n" + "=" * 80)
    
    def plot_comparison(self, f1, f2, root_hard, root_ga, root_pso):
        """Visualisasi perbandingan"""
        
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        
        # Plot 1: Fungsi sederhana
        x1 = np.linspace(-3, 3, 200)
        y1 = [f1(x) for x in x1]
        
        axes[0, 0].plot(x1, y1, 'b-', linewidth=2, label='f(x) = x² - 4')
        axes[0, 0].axhline(0, color='k', linestyle='--', alpha=0.3)
        axes[0, 0].axvline(0, color='k', linestyle='--', alpha=0.3)
        axes[0, 0].plot(root_hard, f1(root_hard), 'ro', markersize=12, 
                       label=f'Hard: x={root_hard:.3f}', zorder=5)
        axes[0, 0].plot(root_ga, f1(root_ga), 'gs', markersize=12, 
                       label=f'GA: x={root_ga:.3f}', zorder=5)
        axes[0, 0].set_xlabel('x', fontsize=12)
        axes[0, 0].set_ylabel('f(x)', fontsize=12)
        axes[0, 0].set_title('Fungsi Sederhana: x² - 4', fontsize=13, fontweight='bold')
        axes[0, 0].legend(fontsize=10)
        axes[0, 0].grid(True, alpha=0.3)
        
        # Plot 2: Fungsi kompleks
        x2 = np.linspace(-5, 5, 400)
        y2 = [np.sin(x) + 0.1*x**2 for x in x2]
        
        axes[0, 1].plot(x2, y2, 'b-', linewidth=2, label='f(x) = sin(x) + 0.1x²')
        axes[0, 1].axhline(0, color='k', linestyle='--', alpha=0.3)
        axes[0, 1].plot(root_ga, np.sin(root_ga) + 0.1*root_ga**2, 'gs', 
                       markersize=12, label=f'GA: x={root_ga:.3f}', zorder=5)
        axes[0, 1].set_xlabel('x', fontsize=12)
        axes[0, 1].set_ylabel('f(x)', fontsize=12)
        axes[0, 1].set_title('Fungsi Kompleks: sin(x) + 0.1x²', fontsize=13, fontweight='bold')
        axes[0, 1].legend(fontsize=10)
        axes[0, 1].grid(True, alpha=0.3)
        
        # Plot 3: Comparison bar chart
        methods = ['Newton-\nRaphson', 'Genetic\nAlgorithm', 'PSO']
        speeds = [0.5, 50, 30]  # Relative speed (ms)
        colors_bar = ['#e74c3c', '#27ae60', '#3498db']
        
        axes[1, 0].bar(methods, speeds, color=colors_bar, alpha=0.7, edgecolor='black')
        axes[1, 0].set_ylabel('Waktu Komputasi (ms)', fontsize=12)
        axes[1, 0].set_title('Perbandingan Kecepatan', fontsize=13, fontweight='bold')
        axes[1, 0].grid(True, alpha=0.3, axis='y')
        
        # Plot 4: Characteristics radar chart
        categories = ['Kecepatan', 'Akurasi', 'Robustness', 'Flexibility', 'Ease of Use']
        
        # Scores (0-10)
        hard_scores = [10, 10, 5, 3, 7]
        soft_scores = [5, 8, 9, 10, 8]
        
        angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
        hard_scores += hard_scores[:1]
        soft_scores += soft_scores[:1]
        angles += angles[:1]
        
        axes[1, 1].plot(angles, hard_scores, 'o-', linewidth=2, label='Hard Computing', color='#e74c3c')
        axes[1, 1].fill(angles, hard_scores, alpha=0.25, color='#e74c3c')
        axes[1, 1].plot(angles, soft_scores, 'o-', linewidth=2, label='Soft Computing', color='#27ae60')
        axes[1, 1].fill(angles, soft_scores, alpha=0.25, color='#27ae60')
        axes[1, 1].set_xticks(angles[:-1])
        axes[1, 1].set_xticklabels(categories, fontsize=9)
        axes[1, 1].set_ylim(0, 10)
        axes[1, 1].set_title('Karakteristik Metode', fontsize=13, fontweight='bold')
        axes[1, 1].legend(loc='upper right', fontsize=10)
        axes[1, 1].grid(True)
        
        plt.tight_layout()
        plt.savefig('results/hard_vs_soft_comparison.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        print("✅ Visualisasi berhasil disimpan!")


def main():
    """Fungsi utama"""
    
    comparison = HardVsSoftComparison()
    comparison.compare_methods()
    
    print("\n✅ Project 04 selesai!")
    print("💡 Lihat file results/hard_vs_soft_comparison.png untuk visualisasi lengkap")


if __name__ == "__main__":
    main()
