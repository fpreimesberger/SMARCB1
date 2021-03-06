import pandas as pd
import matplotlib as plt
import numpy as np
import requests
from bs4 import BeautifulSoup
import tensorflow as tf

from Bio import Medline
from Bio import Entrez
Entrez.email = "fpreimesberger@gmail.com"

# Scraping PubMed DBVar for pathogenic variants of SMARCB1
def getPathogenicUids():
    handle = Entrez.esearch(db="dbvar", term='(SMARCB1[Gene Name]) pathogenic')
    records = Entrez.read(handle)
    # print(records)
    # uids stores the unique IDs for each of the variants
    pathogenic_uids = records['IdList']
    # print(str(pathogenic_uids))
    return(pathogenic_uids)

# Scraping PubMed DBVar for normal variants of SMARCB1
def getNormalUids():
    handle2 = Entrez.esearch(db="dbvar", term='(SMARCB1[Gene Name]) NOT pathogenic')
    records2 = Entrez.read(handle2)
    normal_uids = records['IdList']
    print(normal_uids)

# Get FASTA of sequence based on uid
def getSequence(uid):
    handle = Entrez.efetch(db="nucest", id=uid, rettype='fasta', retmode='xml')
    records = Entrez.read(handle)
    print(records[0])
    # return((records))
    use = ''
    counter = 0
    for key in records[0]:
        if counter == 7:
            use = key
        counter += 1
    return(records[0].get(use))
    # print(records[0].get('TSeq defline'))
    # print(records[0]['TSeq sequence'])
    

def main():
    pathogens = (getPathogenicUids())
    # getSequence(pathogens)
    path_output = open("path_output.txt", "w")
    path_output.write('pls')
    for path in pathogens:
        path_output.write(str(getSequence(path)) + '\n \n')
    path_output.close()

main()
