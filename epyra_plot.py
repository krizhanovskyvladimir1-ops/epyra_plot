import matplotlib.pyplot as plt
import numpy as np

# Данные для эпюр
sections = [0, 1, 2]  # Номера участков
N_values = [80, 120, 110]  # Продольные силы, кН
sigma_values = [113.17, 244.46, 114.33]  # Напряжения, МПа

# Масштабирование (10 кН = 1 клетка, 10 МПа = 1 клетка)
N_scaled = [n / 10 for n in N_values]
sigma_scaled = [s / 10 for s in sigma_values]

# Создание фигуры с двумя подграфиками
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Эпюра продольных сил (N)
ax1.bar(sections, N_scaled, width=0.5, align='center', color='blue', alpha=0.7)
ax1.set_ylabel('Продольная сила N (в клетках)', fontsize=12)
ax1.set_title('Эпюра продольных сил', fontsize=14, fontweight='bold')
ax1.set_xticks(sections)
ax1.set_xticklabels([f'Участок {i+1}' for i in sections])
ax1.axhline(0, color='k', lw=0.5)
ax1.grid(axis='y', linestyle='--', alpha=0.7)
for i, n in enumerate(N_scaled):
    ax1.text(i, n + 0.2, f'{N_values[i]}', ha='center', fontsize=10)

# Эпюра нормальных напряжений (σ)
ax2.bar(sections, sigma_scaled, width=0.5, align='center', color='red', alpha=0.7)
ax2.set_xlabel('Участки', fontsize=12)
ax2.set_ylabel('Нормальное напряжение σ (в клетках)', fontsize=12)
ax2.set_title('Эпюра нормальных напряжений', fontsize=14, fontweight='bold')
ax2.set_xticks(sections)
ax2.set_xticklabels([f'Участок {i+1}' for i in sections])
ax2.axhline(0, color='k', lw=0.5)
ax2.grid(axis='y', linestyle='--', alpha=0.7)
for i, s in enumerate(sigma_scaled):
    ax2.text(i, s + 0.2, f'{sigma_values[i]:.2f}', ha='center', fontsize=10)

# Настройка внешнего вида
plt.tight_layout()
plt.show()
