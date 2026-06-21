with open("./data/raw/cities.txt", "r", encoding="utf-8") as f:
    cities = f.readlines()

cleaned = [f"{i}: {city.strip().upper()}" for i, city in enumerate(cities, start=1)]

for line in cleaned:
    print(line)

with open("./data/processed/cities_clean.txt", "w", encoding="utf-8") as out:
    out.write("\n".join(cleaned) + "\n")