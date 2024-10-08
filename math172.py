import matplotlib.pyplot as plt
import random

class Task172:
    def __init__(self, n, sequence):
        self.n = n
        self.sequence = sequence  

    def draw_circles(self):
        fig, ax = plt.subplots()
        ax.set_aspect('equal')  

        for i in range(0, 3 * self.n, 3):
            x = self.sequence[i]      
            y = self.sequence[i + 1]
            r = self.sequence[i + 2]   

            color = (random.random(), random.random(), random.random())

            circle = plt.Circle((x, y), r, color=color, fill=True, alpha=0.5)
            ax.add_patch(circle)

        ax.set_xlim(min(self.sequence) - max(self.sequence), max(self.sequence) + max(self.sequence))
        ax.set_ylim(min(self.sequence) - max(self.sequence), max(self.sequence) + max(self.sequence))

        plt.show()  

n = int(input("Введите количество кругов (n): "))
sequence = list(map(int, input(f"Введите последовательность {3 * n} чисел (координаты и радиусы): ").split()))

drawer = Task172(n, sequence)
drawer.draw_circles()