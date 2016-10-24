from careerjet_api_client import CareerjetAPIClient

class CareerJet:

    def __init__(self, secret, ip_addr, user_agent, locale_code):
        self.affid = secret
        self.ip = ip_addr
        self.agent = user_agent
        self.cj  =  CareerjetAPIClient(locale_code);

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
        return result_json['jobs']
