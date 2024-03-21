import csv

def read_csv_faile(filename):
    with open(filename, 'r', newline='') as faile:
        reader = csv.reader(faile)
        for rrr in reader:
            print(rrr)

def main():
    filename = input("Ievadiet teksta faila nosaukumu (ar paplašinājumu .csv): ")
    try:
        read_csv_faile(filename)
    except FileNotFoundError:
        print("Fails nav atrasts")
    except Exception as ee:
        print(f"Kļūda: {ee}")

if __name__ == "__main__":
    main()