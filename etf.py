import csv
import pandas as pd

# Function for getting isin-codes from a txt file named isincodes.txt. Returns an array of isin-codes
def getIsinCodesOrFileNames(whichOne):
  try:
    arr = []
    etfWeights = {}
    # open the file named filenames.txt or isincodes.txt
    with open(whichOne, 'r') as file:
      for line in file:
        filename = line.split(', ')[0]
        weight = float(line.split(', ')[1].replace(',', '.'))
        arr.append(filename)
        etfWeights[filename] = weight
  except:
    print(f'file named {whichOne} does not exist or something went wrong.')
    return []
  return arr, etfWeights

# Function for sorting the list of stocks
def stockSort(stock):
  return stock['weight']

# Function for returning an array with updated stocks and stock weights
def mergeDuplicates(arr, etf_count):
  names = []
  tickers = {}
  for i in range(len(arr)):
    names.append(arr[i]['name'])
    tickers[arr[i]['name']] = arr[i]['ticker']
  # Remove duplicates
  names = list(dict.fromkeys(names))
  newArr = []
  # combine same stocks
  for name in names:
    w = 0
    inHowManyEtfs = 0

    for i in range(len(arr)):
      if arr[i]['name'] == name:
        w += arr[i]['weight'] * arr[i]['etfWeight']
        inHowManyEtfs += 1
    newArr.append({ "name": name, "ticker": tickers[name], "weight": w })
  # make sure that all the values are rounded to 5 decimals
  #for i in range(len(newArr)):
    #newArr[i]["weight"] = round(float(newArr[i]["weight"]) / etf_count, 5)
  # sort array
  newArr.sort(reverse=True, key=stockSort)
  return newArr

# Requires implementation
# Function for returning array with stocks and stock weights
def isincodes():
  # Assign list of isin codes to variable codes
  etfs = getIsinCodesOrFileNames('isincodes.txt')
  if len(etfs) == 0:
    return

  # Loop etfs, this one needs implementation
  for etf in etfs:
    with open(etf, mode="r") as file:
      csv_reader = csv.reader(file, delimiter=",")
      for row in csv_reader:
        print(row)
  
  return []

# Function for returning array with stocks and stock weights
def filenames():
  # get filenames
  etfs, etfWeights = getIsinCodesOrFileNames('filenames.txt')
  arr = []
  etf_count = 0
  # Loop through the files
  for etf in etfs:
    try:
      # For every file, loop through rows and add stocks to list named arr
      with open(etf.replace('\n', ''), 'r') as file:
        etf_count += 1
        csv_reader = csv.reader(file, delimiter=",")
        row_count = 0
        # Loop, if row count or row length is bad, then do nothing but move to next row
        for row in csv_reader:
          if row_count > 2 and len(row) > 3:
            ticker = row[0]
            name = row[1]
            weight = round(float(row[3]) / 100, 5)
            arr.append({ "name": name, "ticker": ticker, "weight": weight, "etfWeight": etfWeights[etf] })
          row_count += 1
    except Exception as e:
      print(e)
      continue
  # Having all stocks with their weights from all the files, merge the duplicate stocks and calculate weights
  arr = mergeDuplicates(arr, etf_count)
  # Print the stocks (stock with the highest weight on top)
  for i in arr:
    print(i)
  return arr

def writeFile(etfs):
  print('job')

def main():
  answer = input('filenames or isincodes? Type help for more information. Only allowed inputs are "filenames", "isincodes" and "help".\n')
  stocks = []
  # when having only the isin-codes and having typed isincodes, use the isin-codes
  if answer == 'isincodes':
    print('\nisincodes selected\n')
    stocks = isincodes()
  # If files are in the folder and filenames given as input, use the csv files
  elif answer == 'filenames':
    print('\nfilenames selected\n')
    stocks = filenames()
  # Instructions for using the script
  elif answer == 'help':
    print('\nYou have two options:\n1. Write isin codes separated by line breaks in a file named isincodes.txt\n2. Download the csv files from website of ishares, add them to this folder\nand write the filenames separated by line breaks (for example "foo.csv") in a file named filenames.txt.\n')
  else:
    # Return when input is something else than one of the three
    print('incorrect input, try again')
    return
  # If something fails, the length of stocks is zero
  if len(stocks) == 0:
    print('Something failed, no stocks were found for the isin codes or csv files that you provided.')
  else:
    writeFile(stocks)
  return



main()