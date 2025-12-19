import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# 1. Визначення функції та меж інтегрування
def f(x):
    return x**2

a = 0  # Нижня межа
b = 2  # Верхня межа
f_max = f(b)  # Максимальне значення функції на відрізку [0, 2] (оскільки x^2 зростає)

# 2. Обчислення інтеграла методом Монте-Карло
num_samples = 100000  # Кількість випадкових точок
x_rand = np.random.uniform(a, b, num_samples)
y_rand = np.random.uniform(0, f_max, num_samples)

# Точки, що знаходяться під кривою
under_curve = y_rand <= f(x_rand)
mc_result = (b - a) * f_max * np.sum(under_curve) / num_samples

# 3. Перевірка за допомогою quad (аналітичне значення)
quad_result, error = spi.quad(f, a, b)

# Вивід результатів
print(f"Інтеграл: {quad_result}, {error}")
print(f"Площа сірої зони: ~{mc_result}")
print(f"Результат методом Монте-Карло ({num_samples} точок): {mc_result}")
print(f"Результат функції quad: {quad_result}")
print(f"Абсолютна помилка методу Монте-Карло: {abs(mc_result - quad_result)}")

# 4. Побудова графіка
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots(figsize=(10, 6))

# Малювання функції та заповнення області
ax.plot(x, y, 'r', linewidth=2, label='$f(x) = x^2$')
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3, label='Область інтегрування')

# Візуалізація точок Монте-Карло
viz_points = 2000
ax.scatter(x_rand[:viz_points], y_rand[:viz_points], 
           c=under_curve[:viz_points], cmap='coolwarm', s=1, alpha=0.5)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.5])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title(f'Обчислення інтеграла методом Монте-Карло\nРезультат: {mc_result:.4f} (Quad: {quad_result:.4f})')
ax.legend()
plt.grid(True)
plt.show()