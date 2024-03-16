import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi


# Визначення функції та межі інтегрування
def f(x):
    return x ** 2


a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

points = 1_000_000
random_x = np.random.uniform(a, b, points)
random_y = np.random.uniform(a, f(b), points)

points_in_search_area = sum(random_y <= f(random_x))

# Monte-Carlo
monte_carlo_result = (points_in_search_area / points) * (b - a) * max(f(a), f(b))

print(f"Monte-Carlo Integral {monte_carlo_result}")

# Обчислення інтеграла
quad_result = spi.quad(f, a, b)

print(f"Quad Integral {quad_result}")
