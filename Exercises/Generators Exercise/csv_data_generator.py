'''
CSV Data Generator
'''
import csv

def read_csv(filename):
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            yield tuple(row)

for row in read_csv('heart_failure_clinical_records.csv'):
    print(row)
