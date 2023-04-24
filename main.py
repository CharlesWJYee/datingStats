import readCSV
from Calculation import Calculation
import locale
import argparse
import json

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

BASELINE_MEN = 62500
BASELINE_WOMEN = 42500
EDUCATION_OPTIONS = ['high-school', 'some-college', 'college-bachlors', 'college-masters', 'college-phd',
                     'professional']
ETHNICITY_OPTIOONS = ['white', 'black', 'asian', 'hispanic']
DEBUG_MODE = False
API_MODE = False


def displayDicts(dictDict):
    for d in dictDict:
        print(d)
        print(dictDict[d])


def buildParser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--sex", default='man', choices=['man', 'woman'], type=str, help="sex of the person")
    parser.add_argument("-l", "--looks", default=5, type=int, help="looks of the person on a scale of 1 to 10")
    parser.add_argument("-height", "--height", default=69, type=int, help="height of the person")
    parser.add_argument("-e", "--ethnicity", default='white', choices=ETHNICITY_OPTIOONS, type=str,
                        help="ethnicity of the person")
    parser.add_argument("-w", "--weight", default=190, type=int, help="weight in lbs")
    parser.add_argument("-a", "--age", default=21, type=int, help="age")
    parser.add_argument("-edu", "--education", default='high-school', choices=EDUCATION_OPTIONS, type=str,
                        help="Education attained")

    parser.add_argument("-te", "--target-ethnicity", default='white', choices=ETHNICITY_OPTIOONS, type=str,
                        help="target ethnicity of the person")
    parser.add_argument("-thmin", "--target-height-min", default=48, type=int, help="target height min in inches")
    parser.add_argument("-thmax", "--target-height-max", default=72, type=int, help="target height max in inches")
    parser.add_argument("-twmin", "--target-weight-min", default=70, type=int, help="target weight min in lbs")
    parser.add_argument("-twmax", "--target-weight-max", default=150, type=int, help="target weight max in lbs")
    parser.add_argument("-tamin", "--target-age-min", default=18, type=int, help="target Age min")
    parser.add_argument("-tamax", "--target-age-max", default=35, type=int, help="target Age max")
    parser.add_argument("-tedu", "--target-education", default='high-school', choices=EDUCATION_OPTIONS, type=str,
                        help="target education attained")
    parser.add_argument("-tlmin", "--target-looks-min", default=5, type=int, help="target Looks min")
    parser.add_argument("-tlmax", "--target-looks-max", default=10, type=int, help="target Looks max")

    parser.add_argument("--api", default=False, help="output just the values", action='store_true')
    parser.add_argument("--debug", default=False, help="enable debug mode", action='store_true')

    return parser


# python main.py -s man -l 7 -height 74 -e white -te white -tlmin 6 -tlmax 10 -thmin 66 -thmax 74
if __name__ == '__main__':
    args = buildParser().parse_args()

    DEBUG_MODE = args.debug
    API_MODE = args.api

    if DEBUG_MODE and not API_MODE:
        print("arguments:")
        print(args)

    sex = args.sex
    oppositeSex = 'woman' if sex == 'man' else 'man'
    looks = args.looks
    height = args.height
    ethnicity = args.ethnicity

    targetEthnicity = args.target_ethnicity
    targetLooksMin = args.target_looks_min
    targetLooksMax = args.target_looks_max
    targetHeightMin = args.target_height_min
    targetHeightMax = args.target_height_max

    # looksTab = readCSV.readCSVtoDict("looks")
    # heightTab = readCSV.readCSVtoDict("height")
    ethnicityTargetWomenTab = readCSV.readCSVtoDict("ethnicityTargetWomen")
    ethnicityTargetMenTab = readCSV.readCSVtoDict("ethnicityTargetMen")
    looksTargetWomenTab = readCSV.readCSVtoDict("looksTargetWomen")
    looksTargetMenTab = readCSV.readCSVtoDict("looksTargetMen")
    heightTargetWomenTab = readCSV.readCSVtoDict("heightTargetWomen")
    heightTargetMenTab = readCSV.readCSVtoDict("heightTargetMen")

    if DEBUG_MODE and not API_MODE:
        print("Height when men looking for women:")
        displayDicts(heightTargetWomenTab)
        print("Height when women looking for men:")
        displayDicts(heightTargetMenTab)
        print("Looks when men looking for women:")
        displayDicts(looksTargetWomenTab)
        print("Looks when women looking for men:")
        displayDicts(looksTargetMenTab)
        print("Ethnicity when men looking for women:")
        displayDicts(ethnicityTargetWomenTab)
        print("Ethnicity when women looking for men:")
        displayDicts(ethnicityTargetMenTab)

    c1 = Calculation.Calculation(
        sex, oppositeSex, looks, height, ethnicity,
        # target
        targetLooksMin, targetLooksMax, targetHeightMin, targetHeightMax, targetEthnicity,
        # csv dicts
        looksTargetMenTab, looksTargetWomenTab, heightTargetMenTab, heightTargetWomenTab, ethnicityTargetMenTab, ethnicityTargetWomenTab)
    output = c1.Calculate()

    if API_MODE:
        output = {
            "result": output
        }
        print(json.dumps(output))

    else:
        print("For a " + str(height) + " inches tall " + sex + " who is " + ethnicity + " and a " + str(
            looks) + "/10, looking for a "
              + targetEthnicity + " " + oppositeSex + ", you must be earning $" + f'{output[0]:n} - {output[1]:n}' + " a year")

    # print("Program finished")
