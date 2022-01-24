import glob
import os
import shutil
import time
import logging
from shutil import copytree, rmtree
import ip
#get the unique variable to defferentiate date
date=input("enter date: yyyymmdd: ")
token=input("enter Search token: Token: ")
hr=input("enter Hr: HH: ")
#store the IPs$path in this location in this format "//127.0.0.1/c$/python_work/FETCH_LOG/wrapper"
url='C:/python_work/FETCH_LOG/ips.txt'
#read the the file-ips.txt
try:
    with open(url, 'r') as file_object:
        urls=file_object.read()
        
except:
    print(f"The file does not exist in the location")
    
else:
    #convert it to a list(ips)
    ips=urls.split('\n')
    #loop through the list 1 at a time
    for ip in ips[:]:
        #store the common name structure of the logs here
        path='C:/python_work/FETCH_LOG/para.txt'

        try:
            #read the name structure stored in above
            with open(path, 'r') as file_object:
                liness=file_object.read()
                #print(lines)
                logging.basicConfig(filename='log.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)
                logging.warning(f'name \n{liness}, exist in {path}') 
        except:
            print(f"The file does not exist in the location")
            logging.basicConfig(filename='log.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)
            logging.warning(f'The files named -para.txt does not exist in the location:') 
            

        else:
            #make a list of the names
            contents1=liness.split('\n')
            print(contents1)
            
            #loop through the names 1 at a time
            for name in contents1[:]:
                print(name)
                destination=str("C:/python_work/FETCH_LOG/content")
                print(ip)
                #pass the stored  IPs$path to an os list
                for file in os.listdir(str(ip)):
                    print(file)
                    names=name+date+'T'+hr
                    #search for files that start with the above naming convention
                    if file.startswith((names)):
                        #print(name+date)
                        path2=f'{ip}/{str(file)}'
                        #print(path2)
                        #read the file that start with the define naming convention
                        with open(path2, 'r') as file_object:
                            lines=file_object.read()
                            #print(lines)
                            #convert to list
                            contents2=lines.split('\n')
                             
                            count=0
                            #loop through the list of the content of the file and search for the token supllied
                            for line in contents2[:]:
                                #print(contents2)
                                search=token
                                if search in line:
                                    count+=1
                                    #print(search)
                                    print(f'{search} can be found {count} times in {file} and have been copied to "content"')



                                    src = f'C:/python_work/FETCH_LOG/wrapper/{str(file)}'
                                    destination=str(f"C:/python_work/FETCH_LOG/content/{str(file)}")
                                    dst = destination
                                    #print(dst)
                                    #if token is found in the log, the log is moved to a location called content in destination
                                    shutil.copy2(src, dst)
                                    #os.rename("C://python_work//folder_zip//output//"+ name,"C://python_work//folder_zip//output//"+ name+date)
                                    logging.basicConfig(filename='log.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)
                                    logging.warning(f'The files patterns: Zipped soruce files is being moved to their individual Folders {dst}')
                                    #r"C://python_work//folder_zip//output//"
                                    #dst=str(os.makedirs("C://python_work//folder_zip//output//"+ name))
                                        
