import json  # for the json
from datetime import datetime  # for the dates and times
import pickle  # for the pickling
from careerjet_search import CareerJet  # for the jobs
from job import Job  # for representing the jobs

# get the secret keys for using the api
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
for domain in where_what.keys():
    for location in where_what[domain].keys():
        # search careerjet using their api
        careerjet = CareerJet(
            ids['careerjet'],
            'ip_goes_here',
            'Mozilla',
            domain
        )
        search = careerjet.search(location,
                                  where_what[domain][location],
                                  'http://www.example.com/')

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
                    job['url'],
                    datetime.now()
                ))
        else:
            pass  # should probably notify user

# now we need to evaluate all the jobs based on the users interest
for job in jobs:
    job.compute_value(interests)

# order the jobs by their computed value
jobs.sort(key=lambda x: x.value, reverse=True)

# pickle the list so we can read it back later to compare and track jobs
with open('save.sv', 'w+') as f:
    pickle.dump(jobs, f)

# get the job values for display
vals = [x.value for x in jobs]
print(vals)
