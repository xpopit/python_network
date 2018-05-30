import csv
import socket

with open('nrru.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        try:
            if socket.gethostbyname(row[0]) == row[1]:
                #print(row[0], "==", row[1])
                print('')
            else:
                print(row[0], "!=", socket.gethostbyname(row[0]))

        except:
            print("error->", row[0])
