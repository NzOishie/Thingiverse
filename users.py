import scrapy
from scrapy import Request
import json

class UsersSpider(scrapy.Spider):
    name = 'users'
    all_user = []

    def start_requests(self):
        headers = {"Authorization": "Bearer 56edfc79ecf25922b98202dd79a291aa"}
        for i in range(1,501):

            url = "https://api.thingiverse.com/search/?page="+str(i)+"&per_page=20&sort=followers&type=users"
            yield scrapy.http.Request(url, headers=headers)

    def parse(self, response):

        #
        # print(parsed_data["hits"])
        parsed_data = json.loads(response.text)
        for user in parsed_data["hits"]:
            self.all_user.append(user)
        writefile = open('users.json', 'w')
        json.dump(self.all_user,writefile)
        writefile.close()



