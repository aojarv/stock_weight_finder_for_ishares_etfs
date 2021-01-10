import csv
import pandas as pd

# Function for getting isin-codes from a txt file named isincodes.txt. Returns an array of isin-codes
def getIsinCodesOrFileNames(whichOne):
  try:
    arr = []
    with open(whichOne, 'r') as file:
      for line in file:
        arr.append(line)
  except:
    print(f'file named {whichOne} does not exist.')
    return []
  return arr

# Function for returning an array with updated stocks and stock weights
def mergeDuplicates(arr, etf_count):
  stocks = []
  for i in range(len(arr)):
    stocks.append(arr[i]['stock'])
    # Remove duplicates
  stocks = list(dict.fromkeys(stocks))
  newArr = []
  for stock in stocks:
    w = 0
    for i in range(len(arr)):
      if arr[i]['stock'] == stock:
        w += arr[i]['weight']
    newArr.append({ "stock": stock, "weight": w })
  for i in range(len(newArr)):
    newArr[i]["weight"] = round(float(newArr[i]["weight"]) / etf_count, 5)

  return newArr

# Function for returning array with stocks and stock weights
def isincodes():
  # Assign list of isin codes to variable codes
  etfs = getIsinCodesOrFileNames('isincodes.txt')
  if len(etfs) == 0:
    return

  # Loop etfs, this one needs implementation
  for etf in etfs:
    with open(etf["name"], mode="r") as file:
      csv_reader = csv.reader(file, delimiter=",")
      for row in csv_reader:
        print(row)

  
  return []

# Function for returning array with stocks and stock weights
def filenames():
  etfs = getIsinCodesOrFileNames('filenames.txt')
  arr = []
  etf_count = 0
  for etf in etfs:
    try:
      with open(etf.replace('\n', ''), 'r') as file:
        etf_count += 1
        csv_reader = csv.reader(file, delimiter=",")
        row_count = 0
        for row in csv_reader:
          if row_count > 2 and len(row) > 3:
            stock = row[0]
            weight = round(float(row[3]) / 100, 5)
            arr.append({ "stock": stock, "weight": weight })
          row_count += 1
    except Exception as e:
      print(e)
      continue
  arr = mergeDuplicates(arr, etf_count)
  for i in arr:
    print(i)
  return arr

def writeFile(etfs):
  print('job')

def main():
  answer = input('filenames or isincodes? Type help for more information. Only allowed inputs are "filenames", "isincodes" and "help".\n')
  stocks = []
  if answer == 'isincodes':
    print('\nisincodes selected\n')
    stocks = isincodes()
  elif answer == 'filenames':
    print('\nfilenames selected\n')
    stocks = filenames()
  elif answer == 'help':
    print('\nYou have two options:\n1. Write isin codes separated by line breaks in a file named isincodes.txt\n2. Download the csv files from website of ishares, add them to this folder\nand write the filenames separated by line breaks (for example "foo.csv") in a file named filenames.txt.\n')
  else:
    print('incorrect input, try again')
    return
  if len(stocks) == 0:
    print('Something failed, no stocks were found for the isin codes or csv files that you provided.')
  else:
    writeFile(stocks)
  return



main()