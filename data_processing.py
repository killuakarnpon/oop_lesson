class TableDB:
    def __init__(self):
        self.tableData = []

    def insert(self, table):
        idx = self.search(table)
        if idx == -1:
            self.tableData.append(table)
        else:
            print(f"{table}: Duplicated account")

    def search(self, tableName):
        for acc in self.tableData:
            if acc == tableName:
                return acc
        return -1

class Table:
    def __init__(self, tableName, table):
        self.tableName = tableName
        self.table = table

    def filter(self, condition):
        filterList = []
        for it in self.table:
            if condition(it):
                filterList.append(it)
        return filterList

    def aggregate(self, aggregaKey, aggregaFunc):
        _list = []
        for item in self.table:
            value = float(item[aggregaKey])
            _list.append(value)

        return aggregaFunc(_list)

    def __str__(self):
        return f"Table: {self.tableName}, with {len(self.table)}"

import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

countries = []
with open(os.path.join(__location__, 'Countries.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        countries.append(dict(r))
# Let's write code to

citiesTable = Table("cities", cities)
countriesTable = Table("countries", countries)

db = TableDB()
db.insert(citiesTable)
db.insert(countriesTable)

citiesInItaly = citiesTable.filter(lambda x: x['country'] == 'Italy')
citiesInSweden = citiesTable.filter(lambda x: x["country"] == "Sweden")

citiesItaly = Table("italy_cities", citiesInItaly)
citiesSweden = Table("sweden_cities", citiesInSweden)

db.insert(citiesInItaly)
db.insert(citiesInSweden)


# - print the average temperature for all the cities in Italy
avgItaly = citiesItaly.aggregate("temperature", lambda x: sum(x)/len(x))
print(f"The average temperature of all the cities in Italy :\n{avgItaly}\n")
# - print the average temperature for all the cities in Sweden
avgSweden = citiesSweden.aggregate("temperature", lambda x: sum(x)/len(x))
print(f"The average temperature of all the cities in Sweden :\n{avgSweden}\n")
# - print the min temperature for all the cities in Italy
minItaly = citiesItaly.aggregate("temperature", lambda x: min(x))
print(f"The min temperature of all the cities in Italy :\n{minItaly}\n")
# - print the max temperature for all the cities in Sweden
maxSweden = citiesSweden.aggregate("temperature", lambda x: max(x))
print(f"The max temperature of all the cities in Sweden :\n{maxSweden}\n")

maxLatitude = citiesTable.aggregate("latitude", lambda x: max(x))
minLatitude = citiesTable.aggregate("latitude", lambda x: min(x))

print("Max latitude for the cities in every countries")
print(f"{maxLatitude}\n")
print("Min latitude for the cities in every countries")
print(f"{minLatitude}\n")
