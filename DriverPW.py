# Exam 3
# Philip Weinthal U71401206
# Description - This program can be used to give recipts for wine purchaces and is the interactive part.

from wineBuyPW import wineBuyPW


class DriverPW():
    def createWineListPW(self):
        wineListPW = []
        numTypesPW = input("How many different types of wine will you order today?")
        while int(numTypesPW) < 1:
            print("Number must be at least 1.")
            numTypesPW = input("How many different types of wine will you order today?")
        for i in range(int(numTypesPW)):
            print("Wine Type #{}-\t".format(i + 1))
            wineNamePW = input("Enter the wine name:\t")
            numBottlesPW = input("Enter the number of bottles of this wine (limit 3):\t")
            while int(numBottlesPW) < 1 or int(numBottlesPW) > 3:
                print("Amount of each type of wine must be between 1-3 bottles per order.")
                numBottlesPW = input("Enter the number of bottles of this wine (limit 3):\t")
            wineListPW.append([wineNamePW, numBottlesPW])
            print("\n\n")
        return wineListPW

    def dispWineListPW(wineListPW):
        print("Here's a summary of the items purchased:\n------------------------------------------")
        for i in wineListPW:
            tempPW = wineBuyPW(i[0],i[1])
            print("Wine:\t{}".format(i[0]))
            print("Amount ordered:\t{} bottle(s)".format(i[1]))
            print("Price per bottle:\t${:,.2f}".format((float(tempPW.costCalcPW())/float(i[1]))))
            print("Subtotal:\t${:,.2f}".format(tempPW.costCalcPW()))
            print("\n\n")

    def finalWineCostPW(wineListPW):
        pricePW = 0.00
        for i in wineListPW:
            tempPW = wineBuyPW(i[0], i[1])
            tempPricePW = tempPW.costCalcPW()
            pricePW += tempPricePW
        return pricePW
class mainPW():
        wineListPW = DriverPW.createWineListPW(wineBuyPW)
        DriverPW.dispWineListPW(wineListPW)
        pricePW = DriverPW.finalWineCostPW(wineListPW)
        print("Total cost:\t${:,.2f}".format(pricePW))