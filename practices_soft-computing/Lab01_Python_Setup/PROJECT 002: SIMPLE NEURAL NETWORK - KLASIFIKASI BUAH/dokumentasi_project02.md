# DOKUMENTASI PROJECT 02: NEURAL NETWORK FRUIT CLASSIFIER

## 1. PENDAHULUAN

### 1.1 Apa itu Perceptron?
Perceptron adalah neural network paling sederhana yang dibuat oleh Frank Rosenblatt (1958). Terdiri dari:
- **Input layer:** Menerima data (berat, diameter, warna)
- **Weights:** Bobot untuk setiap input
- **Bias:** Nilai threshold
- **Activation function:** Step function (0 atau 1)
- **Output:** Klasifikasi (Jeruk atau Apel)

### 1.2 Cara Kerja
- Input → [Weighted Sum] → [Activation] → Output
- Weighted Sum = (w1x1 + w2x2 + w3*x3) + bias
- Output = Step_Function(Weighted Sum)

## 2. DATASET

### 2.1 Features
1. **Berat (gram):** 
   - Jeruk: ~150g (± 20g)
   - Apel: ~180g (± 25g)

2. **Diameter (cm):**
   - Jeruk: ~7cm (± 0.5cm)
   - Apel: ~8cm (± 0.6cm)

3. **Warna (RGB Red channel):**
   - Jeruk: ~255 (oranye terang)
   - Apel: ~200 (merah sedang)

### 2.2 Classes
- **0:** Jeruk (Orange)
- **1:** Apel (Apple)

## 3. PROSES TRAINING

### 3.1 Forward Propagation
1. Hitung weighted sum: z = w·x + b
2. Aplikasikan activation: y = step(z)
3. Bandingkan dengan target

### 3.2 Backpropagation (Weight Update)
```python
error = y_true - y_predicted
w_new = w_old + learning_rate * error * x
b_new = b_old + learning_rate * error


#### 3.3 Hyperparameters

Learning Rate: 0.01 (kecepatan belajar)
Iterations: 1000 (jumlah epoch)

## 4. HASIL
#### 4.1 Accuracy

Training: ~95-100%
Testing: ~90-95%

4.2 Kesimpulan
✅ Perceptron berhasil memisahkan 2 class (linearly separable)
✅ Model sederhana tapi efektif untuk masalah binary classification
5. LIMITASI
❌ Hanya bisa untuk linearly separable problems
❌ Tidak bisa menyelesaikan XOR problem
❌ Hanya binary classification (2 class)
Solusi: Multi-layer Perceptron (akan dipelajari di Week 6-7)
6. NEXT STEPS

 Coba dengan dataset real (UCI ML Repository)
 Implementasi multi-class classification
 Bandingkan dengan algoritma lain (SVM, Decision Tree)
