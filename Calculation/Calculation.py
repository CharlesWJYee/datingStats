import sys

import main


# now we must take height in inches instead of string
def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)


HEIGHT_MAX = 82
HEIGHT_MIN = 60


class Calculation:
    def __init__(self,
                 # User attributes
                 sex, oppositeSex, looks, height, ethnicity,
                 # Target attributes
                 targetLooksMin, targetLooksMax, targetHeightMin, targetHeightMax, targetEthnicity,
                 # CSV Dictionaries
                 looksTargetMen, looksTargetWomen, heightTargetMen, heightTargetWomen, ethnicityTabM, ethnicityTabW):

        # User Attributes
        self.sex = sex
        self.oppositeSex = oppositeSex
        self.looks = int(looks)
        self.height = clamp(int(height), HEIGHT_MIN, HEIGHT_MAX)
        self.ethnicity = ethnicity
        # Target attributes
        self.targetEthnicity = targetEthnicity
        self.targetLooksMin = clamp(targetLooksMin, 0, 10)
        self.targetLooksMax = clamp(targetLooksMax, 0, 10)
        self.targetHeightMin = clamp(targetHeightMin, HEIGHT_MIN, HEIGHT_MAX)
        self.targetHeightMax = clamp(targetHeightMax, HEIGHT_MIN, HEIGHT_MAX)
        # Dictionaries
        self.heightTargetMen = heightTargetMen
        self.heightTargetWomen = heightTargetWomen
        self.looksTargetMen = looksTargetMen
        self.looksTargetWomen = looksTargetWomen

        if self.sex.lower() == "m" or self.sex.lower() == "man":
            self.ethnicityTab = ethnicityTabW
            self.looksTab = looksTargetWomen
            self.heightTab = heightTargetWomen
            self.baseline = main.BASELINE_MEN
        elif self.sex.lower() == "f" or self.sex.lower() == "woman":
            self.ethnicityTab = ethnicityTabM
            self.looksTab = looksTargetMen
            self.heightTab = heightTargetMen
            self.baseline = main.BASELINE_WOMEN
        else:
            print("The sex entered is wrong. Must be m/f or man/woman")
            sys.exit()

    def Calculate(self, api_mode):
        mySexStr = self.sex.replace("a", "e").capitalize()
        oppositeSexStr = self.oppositeSex.replace("a", "e").capitalize()

        looksAdjMin = self.looksTab["Additional Income Needed by " + mySexStr + " " + str(self.looks)][
            oppositeSexStr + ' ' + str(self.targetLooksMin)]
        looksAdjMax = self.looksTab["Additional Income Needed by " + mySexStr + " " + str(self.looks)][
            oppositeSexStr + ' ' + str(self.targetLooksMax)]

        heightAdjMin = self.heightTab["Additional Income Needed by " + mySexStr + " " + str(self.height)][
            oppositeSexStr + ' ' + str(self.targetHeightMin)]
        heightAdjMax = self.heightTab["Additional Income Needed by " + mySexStr + " " + str(self.height)][
            oppositeSexStr + ' ' + str(self.targetHeightMax)]

        if self.ethnicity.lower() == "white":
            myRaceStr = "White " + mySexStr
        elif self.ethnicity.lower() == "black":
            myRaceStr = "Black " + mySexStr
        elif self.ethnicity.lower() == "hispanic":
            myRaceStr = "Hispanic " + mySexStr
        elif self.ethnicity.lower() == "asian":
            myRaceStr = "Asian " + mySexStr
        else:
            print("Error in user ethnicity")
            sys.exit()

        if self.targetEthnicity.lower() == "white":
            targetRaceStr = "White " + oppositeSexStr
        elif self.targetEthnicity.lower() == "black":
            targetRaceStr = "Black " + oppositeSexStr
        elif self.targetEthnicity.lower() == "hispanic":
            targetRaceStr = "Hispanic " + oppositeSexStr
        elif self.targetEthnicity.lower() == "asian":
            targetRaceStr = "Asian " + oppositeSexStr
        else:
            print("Error in target ethnicity")
            sys.exit()

        ethnicityAdj = self.ethnicityTab["Additional Income Needed by " + myRaceStr][targetRaceStr]

        maxAdj = findMaxAdj(looksAdjMax, heightAdjMax, ethnicityAdj, api_mode)

        return [self.baseline + looksAdjMin + heightAdjMin + ethnicityAdj,
                self.baseline + looksAdjMax + heightAdjMax + ethnicityAdj, maxAdj]


def findMaxAdj(looks, height, ethnicity, api_mode):
    """
    Finds the maximum adjustment amongst all parameters and prompt on what is the biggest influence on income needed to
    be as desirable
    :param api_mode: prevents printing messages to console
    :param looks: looksAdjMax
    :param height: heightAdjMax
    :param ethnicity: ethnicityAdj
    :return: prompts only, but may also return the amount if needed (currently not used)
    """
    if looks > height and looks > ethnicity:
        if not api_mode:
            print("$" + str(looks)
                  + " of the increase in income are compensating for your lack of looks compared to your target")
        return "looks", looks
    elif height > looks and height > ethnicity:
        if not api_mode:
            print("$" + str(height) + " of the increase in income are compensating for your lack of height")
        return "height", height
    elif ethnicity > looks and ethnicity > height:
        if not api_mode:
            print("Unfortunately, your race is less desired by members of your target's race and you must make $"
                + ethnicity + " more per year to be desirable.")
        return "ethnicity", ethnicity
    else:
        if not api_mode:
            print("All attributes are equal")
        return "equal", 0
