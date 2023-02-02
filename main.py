import readCSV
import Calculation

BASELINE_MEN = 62500
BASELINE_WOMEN = 42500
DEBUG_MODE = True


def displayDicts(dictDict):
    for d in dictDict:
        print(d)
        print(dictDict[d])


if __name__ == '__main__':
    looksTab = readCSV.readCSVtoDict("looks")
    heightTab = readCSV.readCSVtoDict("height")
    ethnicityWomen = readCSV.readCSVtoDict("ethnicityTargetWomen")
    ethnicityMen = readCSV.readCSVtoDict("ethnicityTargetMen")

    if DEBUG_MODE:
        print("Looks:")
        displayDicts(looksTab)
        print("Height:")
        displayDicts(heightTab)
        print("Ethnicity when men looking for women:")
        displayDicts(ethnicityWomen)
        print("Ethnicity when women looking for men:")
        displayDicts(ethnicityMen)

    c1 = Calculation("m", 7.0, '5\'10"', "asian", "white", looksTab, heightTab, ethnicityWomen, ethnicityMen)
    print(c1.Calculate())

    print("Program finished")
