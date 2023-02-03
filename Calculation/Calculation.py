import sys
import main


class Calculation:
    def __init__(self, sex, looks, height, ethnicity, targetEthnicity, looksTab, heightTab, ethnicityTabW,
                 ethnicityTabM):
        self.sex = sex
        self.looks = looks
        self.height = height
        self.ethnicity = ethnicity
        self.targetEthnicity = targetEthnicity
        self.looksTab = looksTab
        self.heightTab = heightTab

        if self.sex.lower() == "m" or self.sex.lower() == "male":
            self.ethnicityTab = ethnicityTabW
            self.baseline = main.BASELINE_MEN
        elif self.sex.lower() == "f" or self.sex.lower() == "female":
            self.ethnicityTab = ethnicityTabM
            self.baseline = main.BASELINE_WOMEN
        else:
            print("The sex entered is wrong. Must be m/f/male/female")
            sys.exit()

    def Calculate(self):
        if self.sex.lower() == "m" or self.sex.lower() == "male":
            mySexStr = "Men"
            oppositeSexStr = "Women"
        elif self.sex.lower() == "f" or self.sex.lower() == "female":
            mySexStr = "Women"
            oppositeSexStr = "Men"

        looksAdj = self.looksTab["Additional Income Needed by " + mySexStr][self.looks]
        heightAdj = self.heightTab["Additional Income Needed by " + mySexStr][self.height]

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

        return self.baseline + looksAdj + heightAdj + ethnicityAdj
