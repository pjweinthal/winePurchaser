# Wine Purchase Receipt Program

## Description
This program is designed to take wine purchase orders, calculate the total cost of the wine, and provide a receipt for the customer. It includes an interactive interface for input and an object-oriented approach to calculate wine costs based on predefined prices.

## Features
- Allows users to input multiple types of wine and the number of bottles (up to 3 per type).
- Provides detailed receipts including the wine name, number of bottles, price per bottle, and total price for each wine type.
- Calculates the overall total cost for all wine purchases.

## Program Structure
The program is composed of two parts:
1. **Interactive Driver (`DriverPW`)**: 
   - This part collects user input and displays the receipt.
   - It includes methods to:
     - `createWineListPW`: Prompt the user to enter wine types and quantities.
     - `dispWineListPW`: Display a summary of the ordered wines and their prices.
     - `finalWineCostPW`: Calculate and return the total cost of the wine order.
  
2. **Wine Purchase Object (`wineBuyPW`)**: 
   - This part handles the price calculations for each wine.
   - It includes methods to:
     - `costCalcPW`: Calculate the total price based on the number of bottles and wine type.
     - `getNamePW`, `getNumBottlesPW`, `getPricePW`: Accessor methods for the wine name, quantity, and price.

## How to Run
1. Ensure that `wineBuyPW` class is implemented in the `wineBuyPW.py` file.
2. Run the `DriverPW` class to start the interactive wine purchase process.
   - The program will prompt for the number of different wine types, the names of the wines, and the quantity (1-3) for each.
3. Once the input is completed, a detailed receipt of the purchased wines and the total cost will be displayed.

### Example Output:
```bash
How many different types of wine will you order today? 2

Wine Type #1-	
Enter the wine name: Screaming Eagle Cabernet Sauvignon
Enter the number of bottles of this wine (limit 3): 2

Wine Type #2-	
Enter the wine name: DLM Grand Cru
Enter the number of bottles of this wine (limit 3): 1


Here's a summary of the items purchased:
------------------------------------------
Wine:	Screaming Eagle Cabernet Sauvignon
Amount ordered:	2 bottle(s)
Price per bottle:	$4,518.00
Subtotal:	$9,036.00

Wine:	DLM Grand Cru
Amount ordered:	1 bottle(s)
Price per bottle:	$39,605.00
Subtotal:	$39,605.00


Total cost:	$48,641.00
