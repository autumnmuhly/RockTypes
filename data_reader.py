import csv

def read_csv_file(filename):
    x = []
    y = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            x.append(float(row['SiO2']))
            y.append(float(row['Na2O + K2O']))
    return x, y

# x, y = read_csv_file('c:/Users/saand/Documents/Geology-818/data/Voyager samples.csv')
    
# print(x, y)
