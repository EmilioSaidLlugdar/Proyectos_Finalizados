import mysql.connector

personas_db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='personas_db'
)

cursor = personas_db.cursor()
sentencia_sql = ('INSERT INTO personas (nombre, apellido, edad) VALUES (%s, %s, %s)')
valores=('Victor', 'Ramos', 46)
cursor.execute(sentencia_sql,valores)
personas_db.commit() #guardar cambios en la db
personas_db.close()