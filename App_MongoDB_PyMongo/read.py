from pymongo import MongoClient
# creating conections for comunicating with MongoDB

client= MongoClient('localhost',27017)
db = client['EmployeeData']

# function to read records form mongo db
def read():
    try:
        empcol = db.Employees.find()
        print('\n All data from EmployeeData Database \n')
        for emp in empcol:
            print("\n")
            print(emp)

    except ImportError:
        platform_specific_module = None