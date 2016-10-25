# class for containing jobs descriptions
class Job:  # no, not the former Apple CEO

    # the core properties of a job are:
    #      title, description, salary, currency, company, location, url
    # the properties to be given the job are:
    #      value

    def __init__(self, title, description, salary_min,
                 currency, company, location, url):
        self.title = title
        self.description = description
        self.salary = salary_min
        self.currency = currency
        self.company = company
        self.location = location
        self.url = url

    # compute the value of the job to the potential employee
    # (should involve much machine learning, but this is hacking)
    #      first component of value is keywords in the title/description
    #      second component of value is the compensation received
    #      third component of value is the company
    #      fourth component of value is the locations
    #      fifth component of value is the quality of the url
    def compute_value(self, params):
        self.value = 0
        # determine first component
        words = self.title + ' ' + self.description
        num_words = len(words.split(' '))
        for keyword in params['keywords']['pos'].split(';'):
            self.value += 1
        for keyword in params['keywords']['neg'].split(';'):
            self.value -= 1
        # to be continues
