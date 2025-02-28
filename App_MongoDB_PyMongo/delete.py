from pymongo import MongoClient
# creating conections for comunicating with MongoDB

client= MongoClient('localhost',27017)
db = client['EmployeeData']

#Function to delete record form mondo db
def delete():
    try:
        criteria=input('\n Enter employee id to delete\n') #busamos el id a eliminar
        db.Employees.delete_many({"id":criteria}) #eliminamos el id
        print('\n Deletion Succcessful\n')
    except ImportError:
        platform_specific_module=None