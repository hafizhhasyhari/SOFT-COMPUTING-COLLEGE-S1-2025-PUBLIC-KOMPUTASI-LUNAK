"""
PROJECT 02: KLASIFIKASI BUAH MENGGUNAKAN NEURAL NETWORK
Dibuat oleh: [Nama Anda]
Tanggal: [Tanggal]
Deskripsi: Perceptron untuk klasifikasi buah (Apel vs Jeruk)
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

class SimplePerceptron:
    """
    Implementasi Perceptron sederhana
    
    Perceptron adalah neural network paling sederhana yang terdiri dari:
    - Input layer
    - Weights (bobot)
    - Activation function (step function)
    - Output layer
    """
    
    def __init__(self, learning_rate=0.01, n_iterations=1000):
        """
        Parameters:
        -----------
        learning_rate : float
            Kecepatan pembelajaran (default: 0.01)
        n_iterations : int
            Jumlah iterasi training (default: 1000)
        """
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.weights = None
        self.bias = None
        self.errors = []
    
    def step_function(self, x):
        """
        Activation function: Step function
        
        Output 1 jika x >= 0, else 0
        """
        return np.where(x >= 0, 1, 0)
    
    def fit(self, X, y):
        """
        Training perceptron
        
        Parameters:
        -----------
        X : array-like, shape (n_samples, n_features)
            Training data
        y : array-like, shape (n_samples,)
            Target values (0 atau 1)
        """
        
        n_samples, n_features = X.shape
        
        # Inisialisasi weights dan bias dengan random kecil
        self.weights = np.random.randn(n_features) * 0.01
        self.bias = 0
        
        print("🚀 Mulai training...")
        print(f"   Jumlah data: {n_samples}")
        print(f"   Jumlah fitur: {n_features}")
        print(f"   Learning rate: {self.learning_rate}")
        print(f"   Iterasi: {self.n_iterations}\n")
        
        # Training loop
        for iteration in range(self.n_iterations):
            errors = 0
            
            for idx, x_i in enumerate(X):
                # Forward propagation
                linear_output = np.dot(x_i, self.weights) + self.bias
                y_predicted = self.step_function(linear_output)
                
                # Hitung error
                error = y[idx] - y_predicted
                
                # Update weights dan bias (Backpropagation sederhana)
                self.weights += self.learning_rate * error * x_i
                self.bias += self.learning_rate * error
                
                errors += int(error != 0)
            
            self.errors.append(errors)
            
            # Print progress setiap 100 iterasi
            if (iteration + 1) % 100 == 0:
                accuracy = (1 - errors/n_samples) * 100
                print(f"   Iterasi {iteration + 1}/{self.n_iterations} - "
                      f"Errors: {errors} - Accuracy: {accuracy:.2f}%")
        
        print("\n✅ Training selesai!")
        print(f"   Final accuracy: {(1 - self.errors[-1]/n_samples) * 100:.2f}%")
    
    def predict(self, X):
        """
        Prediksi class untuk data baru
        
        Parameters:
        -----------
        X : array-like, shape (n_samples, n_features)
            Data yang akan diprediksi
            
        Returns:
        --------
        predictions : array, shape (n_samples,)
            Predicted classes (0 atau 1)
        """
        linear_output = np.dot(X, self.weights) + self.bias
        predictions = self.step_function(linear_output)
        return predictions
    
    def evaluate(self, X, y):
        """Evaluasi model"""
        predictions = self.predict(X)
        accuracy = np.mean(predictions == y) * 100
        return accuracy


def generate_fruit_dataset():
    """
    Generate synthetic dataset untuk klasifikasi buah
    
    Features:
    - Berat (gram)
    - Diameter (cm)
    - Warna (0-255, RGB Red channel)
    
    Classes:
    - 0: Jeruk (Orange) - lebih kecil, lebih ringan, warna oranye
    - 1: Apel (Apple) - lebih besar, lebih berat, warna merah
    """
    
    np.random.seed(42)
    
    # Generate data Jeruk (class 0)
    n_jeruk = 50
    berat_jeruk = np.random.normal(150, 20, n_jeruk)  # mean 150g, std 20g
    diameter_jeruk = np.random.normal(7, 0.5, n_jeruk)  # mean 7cm, std 0.5cm
    warna_jeruk = np.random.normal(255, 15, n_jeruk)  # warna oranye (tinggi)
    
    jeruk = np.column_stack([berat_jeruk, diameter_jeruk, warna_jeruk])
    labels_jeruk = np.zeros(n_jeruk)
    
    # Generate data Apel (class 1)
    n_apel = 50
    berat_apel = np.random.normal(180, 25, n_apel)  # mean 180g, std 25g
    diameter_apel = np.random.normal(8, 0.6, n_apel)  # mean 8cm, std 0.6cm
    warna_apel = np.random.normal(200, 20, n_apel)  # warna merah (sedang)
    
    apel = np.column_stack([berat_apel, diameter_apel, warna_apel])
    labels_apel = np.ones(n_apel)
    
    # Gabungkan dataset
    X = np.vstack([jeruk, apel])
    y = np.hstack([labels_jeruk, labels_apel])
    
    # Shuffle data
    shuffle_idx = np.random.permutation(len(X))
    X = X[shuffle_idx]
    y = y[shuffle_idx]
    
    # Buat DataFrame untuk visualisasi
    df = pd.DataFrame(X, columns=['Berat (g)', 'Diameter (cm)', 'Warna (RGB)'])
    df['Class'] = y
    df['Nama'] = df['Class'].map({0: 'Jeruk', 1: 'Apel'})
    
    return X, y, df


def visualize_data(df):
    """Visualisasi dataset"""
    
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))
    
    colors = {0: 'orange', 1: 'red'}
    
    # Plot 1: Berat vs Diameter
    for class_label in [0, 1]:
        data = df[df['Class'] == class_label]
        axes[0].scatter(data['Berat (g)'], data['Diameter (cm)'], 
                       c=colors[class_label], label=data['Nama'].iloc[0],
                       alpha=0.6, s=100)
    axes[0].set_xlabel('Berat (gram)', fontsize=12)
    axes[0].set_ylabel('Diameter (cm)', fontsize=12)
    axes[0].set_title('Distribusi: Berat vs Diameter', fontsize=13, fontweight='bold')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)
    
    # Plot 2: Berat vs Warna
    for class_label in [0, 1]:
        data = df[df['Class'] == class_label]
        axes[1].scatter(data['Berat (g)'], data['Warna (RGB)'], 
                       c=colors[class_label], label=data['Nama'].iloc[0],
                       alpha=0.6, s=100)
    axes[1].set_xlabel('Berat (gram)', fontsize=12)
    axes[1].set_ylabel('Warna (RGB Red)', fontsize=12)
    axes[1].set_title('Distribusi: Berat vs Warna', fontsize=13, fontweight='bold')
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)
    
    # Plot 3: Diameter vs Warna
    for class_label in [0, 1]:
        data = df[df['Class'] == class_label]
        axes[2].scatter(data['Diameter (cm)'], data['Warna (RGB)'], 
                       c=colors[class_label], label=data['Nama'].iloc[0],
                       alpha=0.6, s=100)
