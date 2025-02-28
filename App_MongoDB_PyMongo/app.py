import insert
import read
import update
import delete


class Programa:
    def __init__(self):
        self.dato = 1

    def menu(self):

        while self.dato:
            #chossing option to do CRUD operations
            selection = input("\nSelect: \n1 to INSERT \n2 to UPDATE \n3 to READ \n4 to DELETE\n Enter an option: ")

            if selection =='1':
                insert.insert()
            elif selection =='2':
                update.update()
            elif selection =='3':
                read.read()
            elif selection =='4':
                delete.delete()
            else:
                print("\n INVALID SELECTION \n")


persona1 = Programa()
persona1.menu()
