import matplotlib.pyplot as plt
import numpy as np

# Данные для эпюр
sections = [0, 1, 2, 3, 4]  # Номера участков
N_values = [80, 10, -20, -30, 0]  # Продольные силы, кН
sigma_values = [83.2, 14.1, -40.7, -42.4, 0]  # Напряжения, МПа

# Создание фигуры с двумя подграфиками
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Эпюра продольных сил (N)
ax1.plot(sections, N_values, drawstyle='steps-post', color='blue', linewidth=2, label='N, кН')
ax1.fill_between(sections, 0, N_values, alpha=0.3, color='blue')
ax1.set_ylabel('Продольная сила N, кН', fontsize=12)
ax1.set_title('Эпюра продольных сил', fontsize=14, fontweight='bold')
ax1.set_xticks(sections)
ax1.set_xticklabels([f'Уч. {i+1}' for i in sections])
ax1.axhline(0, color='k', linestyle='-', linewidth=0.5)
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.legend()

# Добавление значений на эпюру N
for i, n in enumerate(N_values):
    ax1.annotate(f'{n}', (sections[i], n), textcoords="offset points", xytext=(0,10), ha='center')

# Эпюра нормальных напряжений (σ)
ax2.plot(sections, sigma_values, drawstyle='steps-post', color='red', linewidth=2, label='σ, МПа')
ax2.fill_between(sections, 0, sigma_values, alpha=0.3, color='red')
ax2.set_xlabel('Участки стержня', fontsize=12)
ax2.set_ylabel('Нормальное напряжение σ, МПа', fontsize=12)
ax2.set_title('Эпюра нормальных напряжений', fontsize=14, fontweight='bold')
ax2.set_xticks(sections)
ax2.set_xticklabels([f'Уч. {i+1}' for i in sections])
ax2.axhline(0, color='k', linestyle='-', linewidth=0.5)
ax2.grid(True, linestyle='--', alpha=0.7)
ax2.legend()

# Добавление значений на эпюру σ
for i, s in enumerate(sigma_values):
    ax2.annotate(f'{s:.1f}', (sections[i], s), textcoords="offset points", xytext=(0,10), ha='center')

# Настройка внешнего вида
plt.tight_layout()
plt.show()
