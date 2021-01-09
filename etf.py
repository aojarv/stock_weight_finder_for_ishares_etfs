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
def updateArr(arr, row):
  return []

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
  for etf in etfs:
    with open(etf, 'r') as file:
      csv_reader = csv.reader(file, delimiter=",")
      row_count = 0
      for row in csv_reader:
        if row_count > 0:
          arr = updateArr(arr, row)
        row_count += 1
  return arr

def writeFile(etfs):
  print('job')

def main():
  answer = input('filenames or isincodes? Type help for more information. Only allowed inputs are "filenames", "isincodes" and "help".\n')
  etfs = []
  if answer == 'isincodes':
    etfs = isincodes()
  elif answer == 'filenames':
    etfs = filenames()
  elif answer == 'help':
    print('\nYou have two options:\n1. Write isin codes separated by line breaks in a file named isincodes.txt\n2. Download the csv files from website of ishares, add them to this folder\nand write the filenames separated by line breaks (for example "foo.csv") in a file named filenames.txt.\n')
  else:
    print('incorrect input, try again')
    return
  writeFile(etfs)
  return



main()