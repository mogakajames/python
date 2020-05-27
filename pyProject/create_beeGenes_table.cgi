#! C:\Users\mogak\AppData\Local\Programs\Python\Python38\python.exe
#this code created the beeGenes table but is ommitted from the procee.py
print("Content-Type: text/html\n")


import cx_Oracle


#may vary from user to user depending on installation      
#create beegenes table
#please note credentials might be different for you and must be adjusted to run 
conn = cx_Oracle.connect('c##username/password@localhost:1521/orcl')
cursor = conn.cursor()
#create beegenes table
cursor.execute("CREATE TABLE beeGenes(\
    gi_id VARCHAR (150),\
    nucleotide_seq VARCHAR(250),\
    A NUMBER,\
    C NUMBER,\
    G NUMBER,\
    T NUMBER,\
    GC NUMBER\
        )")
if cursor:
    print("table created")
     
else:
    print("error creating table")