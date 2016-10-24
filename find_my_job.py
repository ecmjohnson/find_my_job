import json
from careerjet_search import CareerJet
from job import Job

# get the secret keys for using the apis
with open('secrets.ids') as f:
    ids = json.loads(f.read())

# search careerjet using their api
jobs = []
careerjet = CareerJet(
    ids['careerjet'],
    'ip_goes_here',
    'Mozilla',
    'en_GB'
)
search = careerjet.search('zurich', 'robotics', 'http://www.example.com/')

# check success of search
if search != -1:
    # build a list of job objects for comparison
    for job in search:
        try:
            salary = int(job['salary_min'])
            currency = job['salary_currency_code']
        except KeyError, ValueError:
            salary = -1
            currency = 'None'
        jobs.append(Job(
            job['title'],
            job['description'],
            salary,
            currency,
            job['company'],
            'zurich',
            job['url']
        ))
else:
    pass  # should probably notify user
