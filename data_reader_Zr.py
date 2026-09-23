import csv

def read_csv_file(filename):
    x = []
    y = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            x.append(float(row['Zr/Ti']))
            y.append(float(row['Nb/Y']))
    return x, y

# x, y = read_csv_file('c:/Users/saand/Documents/Geology-818/data/Voyager_samples_Zr.csv')
    
# print(x, y)