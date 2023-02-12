import readCSV
from Calculation import Calculation
import sys

BASELINE_MEN = 62500
BASELINE_WOMEN = 42500
DEBUG_MODE = True


def displayDicts(dictDict):
    for d in dictDict:
        print(d)
        print(dictDict[d])

# python main.py male 7 74.0 White White woman
if __name__ == '__main__':
    if len(sys.argv) != 7:
        print("Incorrect number of arguments. Usage: python main.py <sex> <looks> <height> <ethnicity> <targetEthnicity> <oppositeSex>")
        sys.exit(1)
    
    sex = sys.argv[1]
    looks = float(sys.argv[2])
    height = sys.argv[3]
    ethnicity = sys.argv[4]
    targetEthnicity = sys.argv[5]
    oppositeSex = sys.argv[6]

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

    c1 = Calculation.Calculation(sex, looks, height, ethnicity, targetEthnicity, looksTab, heightTab, ethnicityWomen, ethnicityMen)
    print("For a " + height + " inches tall " + sex + " who is " + ethnicity + " and a " + str(int(looks)) + "/10, looking for a "
          + targetEthnicity + " " + oppositeSex + ", you must be earning $" + str(c1.Calculate()) + " a year")

    #print("Program finished")
