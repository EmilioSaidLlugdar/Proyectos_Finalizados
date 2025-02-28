from pymongo import MongoClient
# creating conections for comunicating with MongoDB

client= MongoClient('localhost',27017)
db = client['EmployeeData']

#Function to update record to mongo db
def update():
    try:
        criteria = input('Enter id to update: ')
        name = input('Enter name to update: ')
        age = input('Enter age to update: ')
        country = input('Enter Country to update: ')

        db.Employees.update_one( #consultamos a la DB
            {"id": criteria}, #busamos el id a modificar si existe modificamos, sino da error
            {
                "$set":{ #nos permite modificar
                    "name":name,
                    "age": age,
                    "country":country
                        }
            })
        print('Records Update Successfully')
    except ImportError:
        platform_specific_module = None
        #print str(e)
