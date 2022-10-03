import csv
import os
import numpy as np

def readcsv(ID):
    dev1 = pergunta2(0, ID)
    dev2 = pergunta2(1, ID)
    dev3 = pergunta2(2, ID)
    dev4 = pergunta2(3, ID)
    dev5 = pergunta2(4, ID)

    #print(dataID)



def pergunta2(i, ID):
    file = "part" + str(ID) + "dev" + str(i+1) + ".csv"
    pasta = "dataset/part" + str(ID)
    dir = os.path.join(pasta, file)
    dev = []
    with open(dir) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            linha = [np.float64(n) for n in row]
            dev.append(linha)

    return np.array(dev)


if __name__ == "__main__":
    readcsv(0)
    


    

