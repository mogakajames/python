#! C:\Users\mogak\AppData\Local\Programs\Python\Python38\python.exe
#this code created the beeGenes table but is ommitted from the procee.py
print("Content-Type: text/html\n")


import cx_Oracle


#may vary from user to user depending on installation      
#create beegenes table
#please note credentials might be different for you and must be adjusted to run 
conn = cx_Oracle.connect('c##username/password@localhost:1521/orcl')
cursor = conn.cursor()

#find maximum nucleotides

#since the file has been read and the data is available in the database, 
#this is why we are using the query database appoach

#the maximum number of nucleotides A, C, G, T is the sum of all the apperances ***[FREQUENCIES]**** for every gene 
#Which means sum of all respective frequencies
#See code:

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
        print(r)#The query provides respective results of A, C, G, T [RESPECTIVELY]Can be formatted further but this answers the question
        
        
        
        



    