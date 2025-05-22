import pandas as pd
import matplotlib.pyplot as plt

# === 1. Завантаження файлів ===
files = {
    "PC": "PC.csv",
    "Microwave ON": "MicrOn.csv",
    "Microwave OFF": "MicrOFF.csv",
    "Room Center": "Room.csv"
}

datasets = {}
for label, path in files.items():
    datasets[label] = pd.read_csv(path, delimiter=';', decimal=',')

# === 2. Аналіз і повідомлення ===
print("=== АНАЛІЗ МАГНІТНОГО ПОЛЯ ===")
overall_means = []

for label, df in datasets.items():
    abs_field = df["Absolute field (µT)"]
    mean_val = abs_field.mean()
    min_val = abs_field.min()
    max_val = abs_field.max()
    std_val = abs_field.std()

    overall_means.append(mean_val)

    print(f"\n[{label}]")
    print(f"  Середнє: {mean_val:.2f} µT")
    print(f"  Мінімум: {min_val:.2f} µT")
    print(f"  Максимум: {max_val:.2f} µT")
    print(f"  Ст. відхилення: {std_val:.2f} µT")

    # Повідомлення за рівнем
    if mean_val < 50:
        print("  ✅ Низький рівень магнітного поля (норма)")
    elif mean_val <= 70:
        print("  ⚠️ Помірний рівень (з обережністю)")
    else:
        print("  🔴 Високий рівень! (небажане тривале перебування)")

# === 3. Побудова графіка з загальним середнім ===
overall_avg = sum(overall_means) / len(overall_means)

plt.figure(figsize=(14, 7))
for label, df in datasets.items():
    plt.plot(df["Time (s)"], df["Absolute field (µT)"], label=label)

plt.axhline(overall_avg, color='black', linestyle='--', linewidth=1.5,
            label=f"Загальне середнє: {overall_avg:.2f} µT")

plt.title("Порівняння абсолютного магнітного поля у різних зонах")
plt.xlabel("Час (с)")
plt.ylabel("Магнітне поле (µT)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
