import pandas as pd
import numpy as np
import time

np.random.seed(42)
data = {
    'date': pd.date_range(start='2025-01-01', periods=365, freq='D'),
    'group': np.random.choice(['A', 'B', 'C', 'D'], size=365),
    'consumption': np.abs(np.random.randn(365) * 100)
}
df = pd.DataFrame(data)

#'date' як індекс
df.set_index('date', inplace=True)


# за днями
start_time = time.time()
daily = df.groupby('group').resample('D').sum().drop(columns=['group'])
end_time = time.time()
daily_time = end_time - start_time

#  за місяцями
start_time = time.time()
monthly = df.groupby('group').resample('ME').sum().drop(columns=['group'])
end_time = time.time()
monthly_time = end_time - start_time

#  за роками
start_time = time.time()
yearly = df.groupby('group').resample('YE').sum().drop(columns=['group'])
end_time = time.time()
yearly_time = end_time - start_time

print("=== Денна агрегація ===\n", daily.head(), "\n")
print("=== Місячна агрегація ===\n", monthly.head(), "\n")
print("=== Річна агрегація ===\n", yearly.head(), "\n")

print(f"Час агрегації за днями: {daily_time:.6f} секунд")
print(f"Час агрегації за місяцями: {monthly_time:.6f} секунд")
print(f"Час агрегації за роками: {yearly_time:.6f} секунд")