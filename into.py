from forex_python.converter import CurrencyRates

print("..Currency Converter From Forex..")

forex_from = input("Write your suggestion from FOREX to convert => ")
forex_to = input("Write your suggestion to MONEY withdraw => ")

cash = CurrencyRates()  
case = cash.convert( forex_from , forex_to , 1 )

print("Convert result...! =======>",case)
