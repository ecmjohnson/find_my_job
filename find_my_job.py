import json
from careerjet_search import CareerJet
from job import Job

# get the secret keys for using the apis
with open('secrets.ids') as f:
    ids = json.loads(f.read())

# get the list of locations and keywords to search
with open('where_what.json') as f:
    where_what = json.loads(f.read())

# get the definitions for the assignment of value for jobs
with open('interests.json') as f:
    interests = json.loads(f.read())

# for every user desired location, keyword pair
jobs = []
for location in where_what.keys():
    # search careerjet using their api
    careerjet = CareerJet(
        ids['careerjet'],
        'ip_goes_here',
        'Mozilla',
        'en_GB'
    )
    search = careerjet.search(location, where_what[location], 'http://www.example.com/')

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

# now we need to evaluate all the jobs based on the users interest
for job in jobs:
    job.compute_value(interests)

# order the jobs by their computed value
jobs.sort(key=lambda x: x.value, reverse=True)
import ipdb; ipdb.set_trace()
