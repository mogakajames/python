#! C:\Users\mogak\AppData\Local\Programs\Python\Python38\python.exe
#this code created the beeGenes table but is ommitted from the procee.py
print("Content-Type: text/html\n")


import cx_Oracle


#may vary from user to user depending on installation      
#create beegenes table
#please note credentials might be different for you and must be adjusted to run 
conn = cx_Oracle.connect('c##username/password@localhost:1521/orcl')
cursor = conn.cursor()
#connection established
#following code for jupyter frequency test
                  
if cursor:
    queries = ["select SUM(A) from BEEGENES",
               "select SUM(C) from BEEGENES",
               "select SUM(G) from BEEGENES",
               "select SUM(T) from BEEGENES"
               ]
    for query in queries:
        cursor.execute(query)
        results = cursor.fetchone()
        r = {
            "maximum number": results
        }
        print(r)
    #for row in results:
        #print(row)
    
else:
    print("an error occurred")
        #print("success")