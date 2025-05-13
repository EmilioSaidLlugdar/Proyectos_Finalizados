import mysql.connector

personas_db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='personas_db'
)

cursor = personas_db.cursor()
sentencia_sql = ('UPDATE personas SET nombre=%s, apellido=%s, edad=%s WHERE id=%s')
valores=('Lady', 'Ruiz',60, 5)
cursor.execute(sentencia_sql,valores)
personas_db.commit() #guardar cambios en la db
print('Se ha modificado la informacion...')
personas_db.close()