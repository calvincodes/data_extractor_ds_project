import sys
import csv

csv.field_size_limit(sys.maxsize)

with open('raw_dataset.csv') as sample_csv:
    csv_reader = csv.reader(sample_csv)
    line_count = 0
    for row in csv_reader:
        if line_count == 350:
            break
        if line_count == 0:
            line_count += 1
        else:
            line_count += 1
            f = open("dataset_output/" + str(row[0]) + ".txt", "w")
            f.write(row[9])
            f.close()
            print('\tArticle ' + str(row[0]) + ' written to '  + str(row[0]) + '.txt')