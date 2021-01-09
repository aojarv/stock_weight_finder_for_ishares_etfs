import csv

listOfNames = [
  {
    "name": 'CSSPX_holdings.csv',
    "weight": 0.5
  },
  {
    "name": "DGTL_holdings.csv",
    "weight": 0.5
  }
]

def main():
  for etf in listOfNames:
    with open(etf["name"], mode="w") as file:
      csv_reader = csv.reader(file, delimiter=",")
      for row in csv_reader:
