from careerjet_api_client import CareerjetAPIClient

class CareerJet:

    def __init__(self, secret, ip_addr, user_agent, locale_code):
        self.affid = secret
        self.ip = ip_addr
        self.agent = user_agent
        self.cj  =  CareerjetAPIClient(locale_code);

    # search the available jobs that fit the criteria
    # returns a list of jobs or -1 if search fails
    # each job is a dict with the following keys of interest:
    #      salary_min, title, description, url, company, location, date
    def search(self, location, keywords, url):
        # returns a dict with keys:
        #      type, hits, jobs, pages, response_time
        result_json = self.cj.search({
                                'location'    : location,
                                'keywords'    : keywords,
                                'affid'       : self.affid,
                                'user_ip'     : self.ip,
                                'url'         : url,
                                'user_agent'  : self.agent
                              });
        # we're interested chiefly in the jobs field
        # does not exist if we didn't find any jobs
        try:
            return result_json['jobs']
        except KeyError:
            return -1

    # change the domain being searched
    def change_locale(self, new_locale):
        self.cj = CareerjetAPIClient(new_locale)
