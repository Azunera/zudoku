import sqlite3

try:
    con = sqlite3.connect("sudoku_database.db")
    # IP, USuario y contrsaensa para una base de datos online
except:
    pass

cur = con.cursor()
cur.execute("PRAGMA foreign_keys = ON")

try:
    cur.execute("DROP TABLE movies")
    cur.execute("DROP TABLE users")
except:
    pass


try:
    cur.execute("CREATE TABLE users(id INT PRIMARY KEY, name TEXT NOT NULL) strict")
except Exception as Ex:
    print(Ex) 
    
try:
    cur.execute("""CREATE TABLE zudoku(
        id INT PRIMARY KEY AUTOINCREMENT
        sudoku , 
        score REAL NOT NULL, 
        rented_by INT,
        FOREIGN KEY(rented_by) REFERENCES users(id)) strict
""")
except Exception as Ex:
    print(Ex) 

try:
    cur.execute("""
        INSERT INTO movies VALUES
            ('Monty Python and the Holy Grail', 1975, 8.2, null),
            ('And Now for Something Completely Different', 1971, 7.5, null)
    """)
except:
    pass

cur.execute("""
    INSERT INTO movies VALUES
        ('Random Film', 2024, 8.2, null),
        ('Random Film2', 1076, 5.6, null)
""")

cur.execute("""
    INSERT INTO users VALUES
        (1, "Enmanuel"),
        (2, "Jose")
""")

cur.execute("""
            UPDATE movies SET rented_by = 1
            where title = 'Random Film'
            """)

con.commit()

res = cur.execute("""
            SELECT * from users""")
print(res.fetchall())

res = cur.execute("""
            SELECT * from movies""")
print(res.fetchall())

res = cur.execute("""
            SELECT users.name, movies.title from users left join movies on users.id = movies.rented_by""")
print(res.fetchall())

# Se puede conseguir bucleando,
# Create, crear ,Select, recibir datos,  Insert, insertar rows/columsn, Delete borrar filas, Drop borrar tabla entera,
# Unique 
# ESTUDIAR JOINS

# Primary Key (ID) : Todas las tables (no necesariamente). deberian tener una primary key (ID). 
# ^ Se necesitan para los joins, ya que al relacionar ablas con Join usas la Primary Key para relacionarlas.add()

# Esta base de datos es Ralacionales
# Mantener la consistencia entr elos datos

# Documento databasa (para grandes)