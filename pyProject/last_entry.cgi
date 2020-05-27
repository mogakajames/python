#! C:\Users\mogak\AppData\Local\Programs\Python\Python38\python.exe
#this code created the beeGenes table but is ommitted from the procee.py
print("Content-Type: text/html\n")


import cx_Oracle


#may vary from user to user depending on installation      
#create beegenes table
#please note credentials might be different for you and must be adjusted to run 
conn = cx_Oracle.connect('c##username/password@localhost:1521/orcl')
cursor = conn.cursor()

                  
if cursor:
    query ="select * from BEEGENES where GI_ID = 147907436"
    cursor.execute(query)
    results = cursor.fetchone()
    r = {
        "id": results[0],
        "nucleotide": results[1],
        "A": results[2],
        "C": results[3],
        "G": results[4],
        "T": results[5],
        "GC": results[6]
    }
    print(r)
    
else:
    print("an error occurred")
        #print("success")