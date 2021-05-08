from forex_python.converter import CurrencyRates

def function():
  print("..Currency Converter From Forex..")

  value_from = input("Write your suggestion from FOREX to convert => ")
  value_to = input("Write your suggestion to MONEY withdraw => ")

  cash = CurrencyRates()  
  case = cash.convert( value_from , value_to , 1 )

  print("Convert result...! =======>",case)

def main():
    function()
main()