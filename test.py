import glob
import os
import shutil
import time
import logging
from shutil import copytree, rmtree

url='C:/python_work/FETCH_LOG/ips.txt'

try:
    with open(url, 'r') as file_object:
        urls=file_object.read()
        #print(lines)
        logging.basicConfig(filename='log.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)
        logging.warning(f'name \n{urls}, exist in {url}') 
except:
    print(f"The file does not exist in the location")
    logging.basicConfig(filename='log.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)
    logging.warning(f'The files named -para.txt does not exist in the location:') 
    

else:
    ips=urls.split('\n')
    print(ips)
    for ip in ips[:]:
        print(ip)
        
