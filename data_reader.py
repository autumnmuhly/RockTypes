import csv

def read_csv_file(filename):
    sample_list = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            sample = {}
            sample['SiO2']= float(row['SiO2'])
            sample['Na2O']=float(row['Na2O'])
            sample['K2O']=float(row['K2O'])
            sample_list.append(sample)
    return sample_list

# x, y = read_csv_file('c:/Users/saand/Documents/Geology-818/data/Voyager samples.csv')
    
# print(x, y)
