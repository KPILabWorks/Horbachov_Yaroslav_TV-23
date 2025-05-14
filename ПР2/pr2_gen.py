import pandas as pd
import numpy as np


num_rows = 20_000_000
num_cols = 10

data = {f'col_{i}': np.random.rand(num_rows) for i in range(num_cols)}

df = pd.DataFrame(data)

# === Збереження у CSV ===
df.to_csv("data.csv", index=False)
print("✔ CSV-файл створено.")
