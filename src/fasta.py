import requests
import os

# Send the FASTA sequences to JPred
jpred = 'http://www.compbio.dundee.ac.uk/jpred4'

# mode : seq for single FASTA file, batch for multiple sequences in FASTA
req = {
    'file': './sequences/benign/A174S.fasta',
    'mode': 'seq',
    'format': 'fasta',
    'email': 'fpreim@cs.utexas.edu',
    'name': 'test_job',
    'skipPDB': 'on'
}

# try:
#     resp = requests.post(jpred, json=req)
#     print(resp.text)
# except requests.exceptions.HTTPError as err:
#     print("Request failed")
#     print(err)
    
# if resp.status_code != 201:
#     print('Request failed')
#     raise ApiError('POST error'.format(resp.status_code()))

all_benign = open('../sequences/benign/ALL_BENIGN.fasta', 'w')
counter = 0
for file in os.listdir('../sequences/benign/'):
    print(file)
    with open('../sequences/benign/'+file, 'r') as f:
        for line in f:
            if line[0] == ">":
                all_benign.write(">" + str(counter) + '\n')
                counter += 1
            else:
                all_benign.write(line.strip('\n') + '\n')
all_benign.close()

all_pathogenic = open('../sequences/pathogenic/ALL_PATHOGENIC.fasta', 'w')
counter = 0
for file in os.listdir('../sequences/pathogenic/'):
    print(file)
    with open('../sequences/pathogenic/'+file, 'r', encoding='utf-8') as f:
        for line in f:
            if line[0] == ">":
                all_pathogenic.write(">" + str(counter) + '\n')
                counter += 1
            else:
                all_pathogenic.write(line.strip('\n') + '\n')
all_benign.close()
all_pathogenic.close()
