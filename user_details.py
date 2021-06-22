import scrapy
import json


class UserDetailsSpider(scrapy.Spider):
    name = 'user_details'
    all_user_details = []

    def start_requests(self):

        headers = {"Authorization": "Bearer 56edfc79ecf25922b98202dd79a291aa"}
        with open('users.json') as f:
            users = json.load(f)
        for user in users["hits"]:
            url = 'https://api.thingiverse.com/users/'+user["name"]+'?t=1624304270558&t=1624304270558/'
            yield scrapy.http.Request(url, headers=headers)


    def parse(self, response):

        parsed_data = json.loads(response.text)
        self.all_user_details.append(parsed_data)
        writefile = open('user_details.json', 'w')

        json.dump(self.all_user_details, writefile)
        writefile.close()
