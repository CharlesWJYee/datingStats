import os
import pandas as pd

def readCSVtoDict(csvFileName):
    """
    The input CSV fie column names are:
    attractiveness metric (looks, height, ethinicity), gender, gender (or sometimes ethinicity)
    And the contents are income in $1000 multiples
    We will read this template file and return a dictionary of dictionaries
    First layer of dictionary indicates which column of gender (or ethinicity). Second layer of dictionary
    contains key of metric, and value in income $ values
    :param csvFileName: input csv file
    :return: dictionary of dictionaries
    """
    dirname = os.path.dirname(__file__)
    csvFilePath = os.path.join(dirname, "Data")
    csvFilePath = os.path.join(csvFilePath, csvFileName + ".csv")

    readFile = pd.read_csv(csvFilePath)
    readFile.fillna(0,
                    inplace=True)  # unavailable information "-" and "Not Feasible" are empty in csv, and filled with 0

    fileColumns = list(readFile.columns)[1:]  # ignore first column as it's a type of index
    indexColumn = list(readFile.columns)[0]
    dictDict = dict()  # return dict of dictionaries (male/female, or different ethinicities as first layer keys)

    for d in fileColumns:
        newDict = dict()
        for i, row in readFile.iterrows():
            newDict[row[indexColumn]] = row[d] * 1000  # income per year is always scaled by $1000
        dictDict[d] = newDict
    return dictDict
