import matplotlib
import json
import pickle

from matplotlib import pyplot as plt
 

def parse(d):
    dictionary = dict()
    # Removes curly braces and splits the pairs into a list
    pairs = d.strip('{}').split(', ')
    for i in pairs:
        pair = i.split(': ')
        # Other symbols from the key-value pair should be stripped.
        dictionary[pair[0].strip('\'\'\"\"')] = pair[1].strip('\'\'\"\"')
    return dictionary

def read_log(filename):
    log = open(filename, 'rt')
    lines = log.read().split('\n')
    dictionaries = []
    for l in lines:
        if l != '':
            dictionaries.insert(len(dictionaries), json.loads(l))
    log.close()

    return dictionaries


def main():

    filename50 = "log50_3.txt"
    filename101 = "log101_3.txt"
    logs50 = read_log(filename50)
    logs101 = read_log(filename101)

    epocs50, ap50, epocs101, ap101 = [], [], [], []
    for i in range(100):
        epocs50.insert(len(epocs50), logs50[i]['epoch'] + 1)
        ap50.insert(len(ap50), logs50[i]["train_loss"])
        epocs101.insert(len(epocs101), logs101[i]['epoch'] + 1)
        ap101.insert(len(ap101), logs101[i]["train_loss"])
    

    plt.plot(epocs50, ap50, color="red", marker='.', label="rtdetr_r50vd_6x_coco")
    plt.plot(epocs101, ap101, color="purple", marker='.', label="rtdetr_r101vd_6x_coco")
    plt.legend(loc="upper right")
    plt.xlabel('Epochs')
    plt.ylabel('Total Loss')
    plt.grid()
    #plt.yticks([0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7]) 
    #plt.xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) 
    plt.savefig('epocsXloss_3.png')

if __name__ == "__main__":
    main()

