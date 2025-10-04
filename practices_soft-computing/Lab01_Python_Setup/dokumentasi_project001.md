# DOKUMENTASI PROJECT 01: FUZZY GRADING SYSTEM

## 1. PENDAHULUAN

### 1.1 Latar Belakang
Sistem penilaian tradisional (crisp/hard computing) sering kali tidak adil karena:
- Nilai 79.9 dapat grade B, tapi 80.0 dapat grade A
- Tidak mempertimbangkan distribusi nilai
- Terlalu kaku dan matematis

Fuzzy logic memberikan solusi yang lebih "manusiawi" dengan mempertimbangkan zona abu-abu dalam penilaian.

### 1.2 Tujuan
- Implementasi fuzzy logic untuk sistem grading
- Membandingkan dengan metode crisp
- Memahami membership functions dan fuzzy rules

## 2. KONSEP FUZZY LOGIC YANG DIGUNAKAN

### 2.1 Fuzzification
Mengubah nilai crisp (angka pasti) menjadi nilai fuzzy (tingkat keanggotaan).

Contoh:
- Nilai 75 bisa masuk kategori "sedang" (60%) dan "tinggi" (40%)
- Bukan hanya "sedang" ATAU "tinggi"

### 2.2 Fuzzy Rules
IF-THEN rules yang mendefinisikan logika sistem.

Contoh Rule:
