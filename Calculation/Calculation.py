import sys
import main
# now we must take height in inches instead of string

class Calculation:
    def __init__(self, 
        # User attributes
        sex, oppositeSex, looks, height, ethnicity,
        # Target attributes
        targetEthnicity, targetLooksMin, targetLooksMax,
        # CSV Dictionaries
        heightTab, ethnicityTabW, ethnicityTabM, looksTargetMen, looksTargetWomen):

        # User Attributes
        self.sex = sex
        self.oppositeSex = oppositeSex
        self.looks = int(looks)
        self.height = int(height)
        self.ethnicity = ethnicity
        # Target attributes
        self.targetEthnicity = targetEthnicity
        self.targetLooksMin = targetLooksMin
        self.targetLooksMax = targetLooksMax
        # Dictionaries
        self.heightTab = heightTab
        self.looksTargetMen = looksTargetMen
        self.looksTargetWomen = looksTargetWomen

        if self.sex.lower() == "m" or self.sex.lower() == "man":
            self.ethnicityTab = ethnicityTabW
            self.looksTab = looksTargetWomen
            self.baseline = main.BASELINE_MEN
        elif self.sex.lower() == "f" or self.sex.lower() == "woman":
            self.ethnicityTab = ethnicityTabM
            self.looksTab = looksTargetMen
            self.baseline = main.BASELINE_WOMEN
        else:
            print("The sex entered is wrong. Must be m/f or man/woman")
            sys.exit()

    def Calculate(self):
        mySexStr = self.sex.replace("a", "e").capitalize()
        oppositeSexStr = self.oppositeSex.replace("a", "e").capitalize()

        # looksAdj = self.looksTab["Additional Income Needed by " + mySexStr][self.looks]
        looksAdjMin = self.looksTab["Additional Income Needed by " + mySexStr + " " + str(self.looks)][oppositeSexStr + ' ' + str(self.targetLooksMin)]
        looksAdjMax = self.looksTab["Additional Income Needed by " + mySexStr + " " + str(self.looks)][oppositeSexStr + ' ' + str(self.targetLooksMax)]

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

        return [self.baseline + looksAdjMin + heightAdj + ethnicityAdj, self.baseline + looksAdjMax + heightAdj + ethnicityAdj]
