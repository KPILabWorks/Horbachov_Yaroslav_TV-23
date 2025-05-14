import pandas as pd
import dask.dataframe as dd
import time

file_path = "data.csv"

# === PANDAS ===
start_pandas = time.time()
pdf = pd.read_csv(file_path)
mean_pandas = pdf.mean()
end_pandas = time.time()
pandas_time = end_pandas - start_pandas
print("Pandas time:", pandas_time)


# === DASK ===
start_dask = time.time()
ddf = dd.read_csv(file_path)
mean_dask = ddf.mean().compute()
end_dask = time.time()
dask_time = end_dask - start_dask
print("Dask time:", dask_time)

# Висновок
print(f"Dask швидший у {pandas_time / dask_time:.2f} разів")
