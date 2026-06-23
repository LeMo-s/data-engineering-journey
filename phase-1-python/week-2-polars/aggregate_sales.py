from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
data_file = BASE_DIR / "data" / "raw" / "sales.txt"
processed_data_folder = BASE_DIR / "data" / "processed" 
processed_data_folder.mkdir(parents=True, exist_ok=True)
processed_data = processed_data_folder / "processed.txt"

products = {}

with open(data_file, 'r', encoding='utf-8') as sales:
    for line in sales:
        product, amount = line.strip().split(',')
        products[product] = products.get(product, 0) + int(amount)

with open(processed_data, 'w', encoding='utf-8') as processed:
    for product, amount in products.items():
        processed.write(f'{product},{amount}\n')

unique = set(products)
print(unique)