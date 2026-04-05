import csv

# with open('9-my-csv.txt', 'r') as FH:
#     my_reader = csv.reader(FH)
#     for i in my_reader:
#         print(i)
        
data = [["name","age"], ["Alice", 25], ["Bob", 30]]        
with open('9-my-csv-write.csv', 'w') as FHW:
    my_writer = csv.writer(FHW)
    my_writer.writerows(data)