from pymongo import MongoClient
# creating conections for comunicating with MongoDB

client= MongoClient('localhost',27017)
db = client['EmployeeData']

#Function to insert data into mongo db
def insert():
    try:
        employeeid = input('Enter Employee id: ')
        employeename = input('Enter name: ')
        employeeage = input('Enter age: ')
        employeecountry = input('Enter Country: ')
        db.Employees.insert_one(
            {
                "id":employeeid,
                "name":employeename,
                "age":employeeage,
                "country": employeecountry
            })
        print('Inserted data successfully')
    except ImportError:
        platform_specific_module = None
        #print str(e)

