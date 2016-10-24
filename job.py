# class for containing jobs descriptions
class Job: # no, not the former Apple CEO

    # the core properties of a job are:
    #      title, description, salary, currency, company, url
    # the properties to be given the job are:
    #      value

    def __init__(self, title, description, salary_min,
                 currency, company, url):
        self.title = title
        self.description = description
        self.salary = salary_min
        self.currency = currency
        self.company = company
        self.url = url

    def compute_value(self):
        pass
