"""
PROJECT 03: TEBAK KATA RAHASIA MENGGUNAKAN GENETIC ALGORITHM
Dibuat oleh: Hafizh Hilman Asyhari
Github : hafizhhasyhari
Tanggal: 17 September 2025
Deskripsi: GA untuk menebak string target melalui evolusi
Mata Kuliah : Soft Computing
Jurusan : Teknik Informatika
"""

import numpy as np
import matplotlib.pyplot as plt
import random
import string

class GeneticWordGuesser:
    """
    Genetic Algorithm untuk menebak kata rahasia
    
    Komponen GA:
    1. Population: Kumpulan kandidat solusi (string)
    2. Fitness: Seberapa mirip dengan target
    3. Selection: Pilih yang terbaik untuk reproduce
    4. Crossover: Kombinasi 2 parent
    5. Mutation: Perubahan acak untuk variasi
    """
    
    def __init__(self, target, population_size=100, mutation_rate=0.01):
        """
        Parameters:
        -----------
        target : str
            Kata yang ingin ditebak
        population_size : int
            Jumlah individu dalam populasi
        mutation_rate : float
            Probabilitas mutasi (0-1)
        """
        self.target = target.upper()
        self.target_length = len(self.target)
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        
        # Karakter yang digunakan (A-Z + space)
        self.genes = string.ascii_uppercase + ' '
        
        # Inisialisasi populasi
        self.population = self.create_initial_population()
        
        # Tracking
        self.best_fitness_history = []
        self.avg_fitness_history = []
        self.generation_count = 0
    
    def create_initial_population(self):
        """Buat populasi awal dengan string random"""
        population = []
        for _ in range(self.population_size):
            individual = ''.join(random.choices(self.genes, k=self.target_length))
            population.append(individual)
        return population
    
    def calculate_fitness(self, individual):
        """
        Hitung fitness (kemiripan dengan target)
        
        Fitness = jumlah karakter yang benar
        
        Parameters:
        -----------
        individual : str
            String kandidat
            
        Returns:
        --------
        fitness : int
            Skor fitness (0 sampai target_length)
        """
        fitness = 0
        for i in range(self.target_length):
            if individual[i] == self.target[i]:
                fitness += 1
        return fitness
    
    def selection(self):
        """
        Tournament Selection: Pilih 2 individu terbaik dari 5 random
        
        Returns:
        --------
        parents : list
            2 parent terpilih
        """
        parents = []
        
        for _ in range(2):
            # Pilih 5 individu random
            tournament = random.sample(self.population, 5)
            
            # Pilih yang terbaik
            best = max(tournament, key=lambda x: self.calculate_fitness(x))
            parents.append(best)
        
        return parents
    
    def crossover(self, parent1, parent2):
        """
        Single-point crossover: Gabung gen dari 2 parent
        
        Example:
        Parent1: HELLO
        Parent2: WORLD
        Crossover point: 3
        Child: HEL + LD = HELLD
        
        Parameters:
        -----------
        parent1, parent2 : str
            Parent strings
            
        Returns:
        --------
        child : str
            Offspring
        """
        # Pilih crossover point random
        crossover_point = random.randint(1, self.target_length - 1)
        
        # Buat child dari kombinasi parent
        child = parent1[:crossover_point] + parent2[crossover_point:]
        
        return child
    
    def mutate(self, individual):
        """
        Mutasi: Ubah karakter random dengan probabilitas mutation_rate
        
        Parameters:
        -----------
        individual : str
            String yang akan dimutasi
            
        Returns:
        --------
        mutated : str
            String setelah mutasi
        """
        individual_list = list(individual)
        
        for i in range(self.target_length):
            # Mutasi dengan probabilitas mutation_rate
            if random.random() < self.mutation_rate:
                individual_list[i] = random.choice(self.genes)
        
        return ''.join(individual_list)
    
    def evolve(self):
        """Evolusi satu generasi"""
        
        # Hitung fitness semua individu
        fitness_scores = [self.calculate_fitness(ind) for ind in self.population]
        
        # Track statistics
        best_fitness = max(fitness_scores)
        avg_fitness = np.mean(fitness_scores)
        
        self.best_fitness_history.append(best_fitness)
        self.avg_fitness_history.append(avg_fitness)
        
        # Buat generasi baru
        new_population = []
        
        # Elitism: Keep best 2 individuals
        best_individuals = sorted(
            zip(self.population, fitness_scores), 
            key=lambda x: x[1], 
            reverse=True
        )[:2]
        new_population.extend([ind[0] for ind in best_individuals])
        
        # Buat offspring sampai populasi penuh
        while len(new_population) < self.population_size:
            # Selection
            parent1, parent2 = self.selection()
            
            # Crossover
            child = self.crossover(parent1, parent2)
            
            # Mutation
            child = self.mutate(child)
            
            new_population.append(child)
        
        self.population = new_population
        self.generation_count += 1
        
        return best_fitness, avg_fitness
    
    def get_best_individual(self):
        """Dapatkan individu terbaik"""
        fitness_scores = [self.calculate_fitness(ind) for ind in self.population]
        best_index = fitness_scores.index(max(fitness_scores))
        return self.population[best_index], fitness_scores[best_index]
    
    def run(self, max_generations=1000, print_every=50):
        """
        Jalankan GA sampai menemukan solusi atau max generations
        
        Parameters:
        -----------
        max_generations : int
            Maksimal generasi
        print_every : int
            Print progress setiap N generasi
        """
        
        print("=" * 70)
        print("🧬 GENETIC ALGORITHM: WORD GUESSING")
        print("=" * 70)
        print(f"Target: {self.target}")
        print(f"Population Size: {self.population_size}")
        print(f"Mutation Rate: {self.mutation_rate}")
        print(f"Max Generations: {max_generations}")
        print("=" * 70)
        print()
        
        print(f"{'Gen':<8} {'Best':<20} {'Fitness':<12} {'Avg Fitness':<15}")
        print("-" * 70)
        
        for generation in range(max_generations):
            # Evolusi
            best_fitness, avg_fitness = self.evolve()
            best_individual, _ = self.get_best_individual()
            
            # Print progress
            if (generation + 1) % print_every == 0 or best_fitness == self.target_length:
                print(f"{generation + 1:<8} {best_individual:<20} "
                      f"{best_fitness}/{self.target_length:<12} {avg_fitness:.2f}")
            
            # Check if solved
            if best_fitness == self.target_length:
                print("-" * 70)
                print(f"\n🎉 BERHASIL! Kata ditemukan di generasi {generation + 1}")
                print(f"   Solusi: {best_individual}")
                print(f"   Target: {self.target}")
                break
        else:
            print("\n⚠️ Mencapai maksimal generasi tanpa menemukan solusi sempurna")
            best_individual, best_fitness = self.get_best_individual()
            print(f"   Best solution: {best_individual} (fitness: {best_fitness}/{self.target_length})")
        
        print("\n" + "=" * 70)
        
        return best_individual
    
    def plot_evolution(self):
        """Plot progress evolusi"""
        
        fig, axes = plt.subplots(1, 2, figsize=(15, 5))
        
        generations = range(1, len(self.best_fitness_history) + 1)
        
        # Plot 1: Best Fitness
        axes[0].plot(generations, self.best_fitness_history, 
                    linewidth=2, color='#27ae60', label='Best Fitness')
        axes[0].axhline(y=self.target_length, color='r', linestyle='--', 
                       label='Target', linewidth=2)
        axes[0].set_xlabel('Generasi', fontsize=12)
        axes[0].set_ylabel('Fitness Score', fontsize=12)
        axes[0].set_title('Evolution Progress: Best Fitness', 
                         fontsize=14, fontweight='bold')
        axes[0].legend()
        axes[0].grid(True, alpha=0.3)
        
        # Plot 2: Average Fitness
        axes[1].plot(generations, self.avg_fitness_history, 
                    linewidth=2, color='#3498db', label='Average Fitness')
        axes[1].set_xlabel('Generasi', fontsize=12)
        axes[1].set_ylabel('Average Fitness Score', fontsize=12)
        axes[1].set_title('Evolution Progress: Average Fitness', 
                         fontsize=14, fontweight='bold')
        axes[1].legend()
        axes[1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('results/evolution_progress.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        print("✅ Visualisasi evolusi berhasil disimpan!")


def main():
    """Fungsi utama"""
    
    # Test 1: Kata pendek
    print("\n🧪 TEST 1: Kata Pendek\n")
    ga1 = GeneticWordGuesser(
        target="HELLO",
        population_size=100,
        mutation_rate=0.01
    )
    solution1 = ga1.run(max_generations=500, print_every=25)
    ga1.plot_evolution()
    
    # Test 2: Kata lebih panjang
    print("\n\n🧪 TEST 2: Kata Lebih Panjang\n")
    ga2 = GeneticWordGuesser(
        target="SOFT COMPUTING",
        population_size=200,
        mutation_rate=0.01
    )
    solution2 = ga2.run(max_generations=1000, print_every=50)
    ga2.plot_evolution()
    
    # Test 3: Custom target
    print("\n\n🧪 TEST 3: Custom Target\n")
    custom_target = input("Masukkan kata target (huruf kapital + spasi): ").upper()
    
    if custom_target:
        ga3 = GeneticWordGuesser(
            target=custom_target,
            population_size=150,
            mutation_rate=0.01
        )
        solution3 = ga3.run(max_generations=1500, print_every=100)
        ga3.plot_evolution()
    
    print("\n✅ Semua test selesai!")


if __name__ == "__main__":
    main()
