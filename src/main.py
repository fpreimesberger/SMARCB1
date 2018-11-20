import pandas as pd
import matplotlib as plt
import numpy as np
import requests
from bs4 import BeautifulSoup

from Bio import Medline
from Bio import Entrez

# Scraping PubMed DBVar for pathogenic variants of SMARCB1
Entrez.email = "fpreimesberger@gmail.com"
handle = Entrez.esearch(db="dbvar", term='(SMARCB1[Gene Name]) pathogenic')
records = Entrez.read(handle)
# uids stores the unique IDs for each of the variants
uids = records['IdList']
print(uids)

for uid in uids:
    search = str(uid) + '[UID]'
    print(search)
    handle =  Entrez.esummary(db='dbvar', id=uid)
    print(Entrez.read(handle))

# Save data sets into .txt files
