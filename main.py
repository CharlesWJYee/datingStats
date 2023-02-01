import readCSV

def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]


def displayDicts(dictDict):
    for d in dictDict:
        print(d)
        print(dictDict[d])


if __name__ == '__main__':
    displayDicts(readCSV.readCSVtoDict("looks"))
    print("Program finished")

