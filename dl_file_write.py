import requests

## requests.get() used for getting the file for download
## raise_for_status to check the status code

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()

## Open a file call rj.txt in write binary format

playFile = open('rj.txt', 'wb')

## iter_content() used for writing the res content in the file call rj.txt


for chunk in res.iter_content(1000000):

    playFile.write(chunk)
    
playFile.close()

