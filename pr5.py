import pandas as pd
from faker import Faker
import uuid

# Створення генератора фейкових даних
faker_gen = Faker()

# Кількість необхідних рядків
records_count = 20

# Формування списку записів
entries = []

for _ in range(records_count):
    person = {
        'ID': uuid.uuid4().hex,
        'FullName': faker_gen.name(),
        'Email': faker_gen.email(),
        'PhoneNumber': faker_gen.phone_number(),
        'Country': faker_gen.country(),
        'FullAddress': faker_gen.address().replace('\n', ', '),
        'DOB': faker_gen.date_of_birth(minimum_age=18, maximum_age=80).isoformat()
    }
    entries.append(person)

# Створення DataFrame з отриманих даних
df_synthetic = pd.DataFrame(entries)

# Вивід згенерованих даних у консоль
print("📋 Згенеровані синтетичні дані:")
print(df_synthetic.to_string(index=False))

# Експорт у CSV-файл
output_file = 'synthetic_data.csv'
df_synthetic.to_csv(output_file, index=False)
print(f"\n✅ Дані успішно збережено у файл: {output_file}")
