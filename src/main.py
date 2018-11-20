import pandas as pd
import matplotlib as plt
import numpy as np
import requests
from bs4 import BeautifulSoup

from Bio import Medline
from Bio import Entrez
Entrez.email = "fpreimesberger@gmail.com"

# Scraping PubMed DBVar for pathogenic variants of SMARCB1
def getPathogenicUids():
    handle = Entrez.esearch(db="dbvar", term='(SMARCB1[Gene Name]) pathogenic')
    records = Entrez.read(handle)
    # uids stores the unique IDs for each of the variants
    pathogenic_uids = records['IdList']
    print(pathogenic_uids)

# Scraping PubMed DBVar for normal variants of SMARCB1
def getNormalUids():
    handle2 = Entrez.esearch(db="dbvar", term='(SMARCB1[Gene Name]) NOT pathogenic')
    records2 = Entrez.read(handle2)
    normal_uids = records['IdList']
    print(normal_uids)

# for uid in pathogenic_uids:
#     search = str(uid) + '[UID]'
#     print(search)
#     handle =  Entrez.esummary(db='dbvar', id=uid)
#     print(Entrez.read(handle))

# Save data sets into .txt files
