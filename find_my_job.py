import json
from careerjet_search import CareerJet

# get the secret keys for using the apis
with open('secrets.ids') as f:
    ids = json.loads(f.read())

careerjet = CareerJet(ids['careerjet'],
    'ip_goes_here',
    'Mozilla',
    'en_GB')
print(careerjet.search('zurich', 'robotics', 'http://www.example.com/jobsearch?q=python&l=london'))
