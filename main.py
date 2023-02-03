import readCSV
from Calculation import Calculation

BASELINE_MEN = 62500
BASELINE_WOMEN = 42500
DEBUG_MODE = False


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

    sex = "male"
    oppositeSex = "woman"
    looks = 10.0
    height = '5\'11"'
    ethnicity = "asian"
    targetEthnicity = "white"
    c1 = Calculation.Calculation(sex, looks, height, ethnicity, targetEthnicity, looksTab, heightTab, ethnicityWomen, ethnicityMen)
    print("For a " + height + " tall " + sex + " who is " + ethnicity + " and a " + str(int(looks)) + "/10, looking for a "
          + targetEthnicity + " " + oppositeSex + ", you must be earning $" + str(c1.Calculate()) + " a year")

    #print("Program finished")
