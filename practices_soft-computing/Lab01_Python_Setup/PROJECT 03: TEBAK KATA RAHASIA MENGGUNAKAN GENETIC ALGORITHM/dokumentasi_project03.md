# 🧬 PROJECT 03: GENETIC ALGORITHM - TEBAK KATA RAHASIA

## 📖 Deskripsi Project

Membuat program yang menggunakan **Genetic Algorithm** untuk menebak kata rahasia. Program akan "berevolusi" dari string random hingga menemukan kata target!

## 🎯 Objektif

- Memahami konsep evolusi dalam algoritma
- Belajar selection, crossover, mutation
- Visualisasi proses evolusi
- Melihat "survival of the fittest" secara langsung

## 🛠️ Tools
```python
pip install numpy matplotlib

## 📁 Struktur Project
project03_genetic_word/
├── README.md
├── genetic_word_guesser.py
├── results/
│   ├── evolution_progress.png
│   └── best_solutions.txt
└── dokumentasi_project03.md

## 1. KONSEP DASAR

### 1.1 Apa itu Genetic Algorithm?
GA adalah teknik optimasi yang terinspirasi dari evolusi biologis Darwin. Komponen utama:

1. **Population:** Sekumpulan kandidat solusi
2. **Genes:** Karakter-karakter dalam string
3. **Fitness:** Seberapa bagus solusinya (similarity ke target)
4. **Selection:** "Survival of the fittest"
5. **Crossover:** Breeding (kombinasi parent)
6. **Mutation:** Variasi genetik

### 1.2 Analogi Biologis
Generasi 1: ABCDE, XYZAB, HELLO (random)
↓ (selection: yang mirip target bertahan)
Generasi 2: HELLO, HALLO, HOLLO (lebih baik)
↓ (crossover + mutation)
Generasi 3: HELLO (sempurna!)


## 2. IMPLEMENTASI

### 2.1 Fitness Function
```python
fitness = jumlah karakter yang sama dengan target

Contoh:
Target: HELLO
Individu: HXLLO
Fitness: 4/5 (H, L, L, O benar)

2.2 Selection Method
Tournament Selection:

Pilih 5 individu random
Yang fitness tertinggi menang
Ulangi untuk dapat 2 parent

2.3 Crossover
Single-Point Crossover:
Parent1: HELLO
Parent2: WORLD
Point: 3
Child: HEL + LD = HELLD

---

2.4 Mutation
Setiap karakter punya probabilitas mutation_rate untuk berubah random.
Before: HELLO
Mutate: H→X (position 0)
After:  XELLO

3. PARAMETER TUNING
3.1 Population Size

Kecil (50): Cepat tapi bisa stuck di local optimum
Sedang (100-200): Balance
Besar (500+): Lambat tapi lebih eksploratif

3.2 Mutation Rate

Terlalu rendah (0.001): Konvergen lambat
Ideal (0.01-0.05): Balance exploration vs exploitation
Terlalu tinggi (0.5): Terlalu acak, tidak konvergen

4. HASIL EKSPERIMEN
4.1 Test "HELLO"

Population: 100
Mutation Rate: 0.01
Hasil: Solved dalam ~50-100 generasi

4.2 Test "SOFT COMPUTING"

Population: 200
Mutation Rate: 0.01
Hasil: Solved dalam ~200-400 generasi

4.3 Observasi
✅ Kata lebih panjang = butuh lebih banyak generasi
✅ Elitism membantu mempertahankan solusi terbaik
✅ Mutation penting untuk avoid stuck
5. APLIKASI REAL-WORLD
GA digunakan untuk:

✈️ Optimasi rute (TSP)
🏭 Scheduling (penjadwalan pabrik)
🎮 Game AI (evolving strategies)
🧬 Bioinformatics (DNA sequencing)
📊 Feature selection (machine learning)
🏗️ Engineering design (struktur optimal)

6. LIMITASI
❌ Tidak garantisolusi optimal (heuristic)
❌ Perlu tuning parameter
❌ Bisa lambat untuk masalah sangat kompleks
7. NEXT STEPS

 Implementasi untuk TSP (Traveling Salesman)
 Multi-objective optimization
 Adaptive mutation rate
 Parallel GA (multi-population)
