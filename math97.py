class TaskCalculation:
    def __init__(self, steps):
        self.steps = steps  
    def calc(self):
        x = 1  
        y = 1  
        
        for i in range(2, self.steps + 1):
            x_new = 0.3 * x   
            y_new = x + y    
            
            x = x_new
            y = y_new
        
        n = x / (1 + y)
        return n

steps = int(input("Введите количество шагов: "))

calculator = TaskCalculation(steps)

result = calculator.calc()
print(f"Результат для {steps} шагов: n = {result}")
