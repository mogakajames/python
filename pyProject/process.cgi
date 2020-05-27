#! C:\Users\mogak\AppData\Local\Programs\Python\Python38\python.exe
print("Content-Type: text/html\n")

# Import modules for CGI handling 
import cgi, cgitb
import re
#import Counter
import cx_Oracle
from collections import defaultdict
#may vary from user to user depending on installation            
#please note credentials might be different for you and must be adjusted to run 
conn = cx_Oracle.connect('c##username/password@localhost:1521/orcl')
cursor = conn.cursor()

#define main function to get input data from the form
def main():
    # instance of FieldStorage function for the form
    form = cgi.FieldStorage()
    # Get from form, title and path
    global title
    global path
    title = form.getvalue('title')
    path  = form.getvalue('path')
    
    #print(title)
    #print(path)
     
#processInput function to read, write the path file and insert into ORACLE
def processInput(file_path, c):
    #read file to read and write
    file = open(file_path, 'rt')
    #assign the read data to a variable
    file_data = file.read()
    #print(file_data)
    #text to search and append to
    text_to_search = 'mRNA'
    #text to append after search matches
    text_to_append = '_**gene_seq_starts_here**_mRNA'
    #searching and appending
    file_data = file_data.replace(text_to_search, text_to_append)
    #closing file after operation
    file.close()
    #opening file in write mode
    file = open(file_path, 'wt')
    #replacing the changes to the original file...this program should run once since not all
    #conditions are taken care of,,,refreshing will break the logic
    file.write(file_data)
    #if you need to run it twice, replace with the original source text
    #closing modified file
    file.close()
    #Reading the contents of the new file to loop for occurences of 
    #newfile = open(file_path, 'r')
    #new_data = newfile.read()
    #gi id and the gene sequence
    #extracting gene ID and sequence to ready them for db entry
    gi_ids = []
    gene_sequence = []
    #get gene ids----
    with open(file_path, 'r') as infile:
        for line in infile:
            #if gi is found
            if "gi" in line:
                if line.strip().split('|')[1].strip(" ") not in gi_ids:
                    gi_ids.append(line.strip().split('|')[1].strip(" "))
    #loop for each line of gene matching the main henes                
    with open(file_path, 'r') as infile:
        search_gene = ['A','C','G','T']
        for search_gene in infile:
            if search_gene.isupper(): 
                gene_sequence.append(search_gene.rstrip('\n')) 
    #genes and ids as they appear #might be used to structure all
    #------------  i=id, j = gene 
    #data before insertion have it mind                  
    genes = [i + j for i, j in zip(gi_ids, gene_sequence)] 
    #------------                      
    #print(gi_ids)
    #print(gene_sequence) 
    #print(genes)   
    for gene in genes:
        #print(gene)
        #genes_str = ''.join(map(str, gene))
        formarted_gene = re.match(r'([0-9]+)([A-Z]+)', gene, re.I)
        #if formarted_gene:#genes formated
        each_gene = formarted_gene.groups()#each gene has been arrived at
        #for nuc in each_gene:
        gi_id = each_gene[0]
        gene_seq = each_gene[1]
        substringA = 'A'#A
        substringC = 'C'#C
        substringG = 'G'#G
        substringT = 'T'#T
        
        countA = gene_seq.count(substringA)#FREQUENCY
        countC = gene_seq.count(substringC)#FREQUENCY
        countG = gene_seq.count(substringG)#FREQUENCY
        countT = gene_seq.count(substringT)#FREQUENCY
        freq_GC = countG + countC#FREQUENCY
        
        all_data =[gi_id,gene_seq,countA,countC,countG,countT,freq_GC]
        #print(all_data)
        #data = [1,6,4,5,6,7,8]
        #for row in all_data:
        #array size binding
        cursor.bindarraysize = 1000   
        #execute entries
        cursor.execute("""
            insert into beeGenes (gi_id, nucleotide_seq, A, C, G, T, GC)
            values (:1, :2, :3, :4, :5, :6, :7)""", all_data)
        conn.commit()
        
    

    
    
#def fileToStr():
    
    
#displayong the success message from the meesage template    
def makePage():
    message = """<html>
    <head>
    <title>Gene Processor</title>
    </head>
    <body>
    <h1>GENE PROCESSOR</h1><br/>
    <h4 style="color:green">Your gene file has been processed successfully</h4>
    <h4 style="color:green">Your data is now available in your database</h4>
    <button><a href="fetch.cgi">Click to See Some Results</a></button>
    </body>
    </html>"""
    
    print(message)
            
            
               
                              
main()                    
processInput(path, conn)
makePage()
#db(cursor,dba)

             
   




 
