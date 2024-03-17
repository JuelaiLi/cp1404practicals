def main():
    filename = "wimbledon_champions.txt"
    raw_data = read_champions_data(filename)
    champions, countries = process_data(raw_data)
    display_champions(champions)
    display_countries(countries)

def read_champions_data(filename):
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        data = in_file.readlines()
    return data

def process_data(data):
    champions = {}
    countries = set()
    for line in data:
        parts = line.strip().split(',')  # Assuming CSV format or similar
        name = parts[0].strip()
        country = parts[1].strip()
        countries.add(country)
        if name in champions:
            champions[name] += 1
        else:
            champions[name] = 1
    return champions, countries

def display_champions(champions):
    print("Wimbledon Champions:")
    for champion, wins in champions.items():
        print(f"{champion} {wins}")

def display_countries(countries):
    sorted_countries = sorted(list(countries))
    print(f"These {len(sorted_countries)} countries have won Wimbledon:")
    print(', '.join(sorted_countries))

if __name__ == "__main__":
    main()
