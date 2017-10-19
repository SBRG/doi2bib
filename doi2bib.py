import requests
import sys

try:
    doi = sys.argv[1]
except IndexError:
    print('Usage:\n{} <doi>'.format(sys.argv[0]))
    sys.exit(1)

url = "http://dx.doi.org/" + doi

headers = {"accept": "application/x-bibtex"}
r = requests.get(url, headers=headers)

print r.text
