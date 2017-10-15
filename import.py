import csv
data = []

def import_data():
    with open("Iris.csv","r") as f:
        reader = csv.reader(f)

        for row in reader:
            data.append(row)

    return data
