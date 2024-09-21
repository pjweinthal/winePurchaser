#Exam 3
#Philip Weinthal U71401206
#Description - This program can be used to give recipts for wine purchaces and is the object part.
class wineBuyPW:
    def __init__(self, namePW, numBottlesPW):
        self.__name = namePW
        self.__numBottles = numBottlesPW
        self.__priceListPW

    def __priceListPW(self, namePW):
        wineNameDictPW = {"DLM Grand Cru": 39605.00, "HJC Parantoux": 18364.00, "EMS Riesling": 16776.00, "HJE Grand Cru": 9120.00, "WJG Tawny Port": 8006.00, "JS Terrantez": 7514.00, "Screaming Eagle Sauvignon Blanc": 6373.00, "JJPW Riesling": 5280.00, "HMB 'T' Vintage": 4900.00, "Screaming Eagle Cabernet Sauvignon": 4518.00}
        return wineNameDictPW[namePW]
    def costCalcPW(self):
        indivCostPW = self.__priceListPW(self.__name)
        finalCostPW = float(indivCostPW) * float(self.__numBottles)
        return finalCostPW
    def getNamePW(self):
        return self.__name
    def getNumBottlesPW(self):
        return self.__numBottles
    def getPricePW(self):
        return self.__priceListPW(self.__name)
