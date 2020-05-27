#! C:\Users\mogak\AppData\Local\Programs\Python\Python38\python.exe
print("Content-Type: text/html\n")

#import Counter
import cx_Oracle
#may vary from user to user depending on installation            
#please note credentials might be different for you and must be adjusted to run 
conn = cx_Oracle.connect('c##username/password@localhost:1521/orcl')
cursor = conn.cursor()

#querying the db for gene data 
#and returning sorted for user
    
    
def fetch_data(connection):
    queries = ["select GI_ID, A from BEEGENES where A = (select MAX(A) from BEEGENES)",
               "select GI_ID, C from BEEGENES where C = (select MAX(C) from BEEGENES)",
               "select GI_ID, G from BEEGENES where G = (select MAX(G) from BEEGENES)",
               "select GI_ID, T from BEEGENES where T = (select MAX(T) from BEEGENES)"
               ]
    for query in queries:
        cursor.execute(query)
        results = cursor.fetchone()
        r = {
            "id": results[0],
            "Highest Frequency": results[1]
        }
        print(r)
          
    
    
def result_template():
    display = """<html>
    <head>
    <title>Gene Processor</title>
    </head>
    <body>
        <h1>SOME GENE DATA FROM DB</h1>
    <table border="1">
    <tr>
    <td>NUCLEOTIDE</td>
    <td>CODE</td>
    <td>GI ID</td>
    <td>HIGHEST FREQUENCY</td>
    </tr>
    <tr>
    <td>ADENINE</td>
    <td>A</td>
    <td>118150503</td>
    <td>54</td>
    </tr>
    <tr>
    <td>CYTOSINE</td>
    <td>C</td>
    <td>299890787</td>
    <td>38</td>
    </tr>
    <tr>
    <td>GUANINE</td>
    <td>G</td>
    <td>62198228</td>
    <td>32</td>
    </tr>
    <tr>
    <td>THYMINE</td>
    <td>T</td>
    <td>402695572</td>
    <td>39</td>
    </tr>
    
    </table>
    </body>
    </html>"""
    
    print(display)
    
        
fetch_data(conn)  
result_template()  