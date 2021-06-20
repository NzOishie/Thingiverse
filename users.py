import scrapy
from scrapy import Request
import json

class UsersSpider(scrapy.Spider):
    name = 'users'

    def start_requests(self):
        headers = {"Authorization": "Bearer 56edfc79ecf25922b98202dd79a291aa"}
        for i in range(1,3):

            url = "https://api.thingiverse.com/search/?page="+str(i)+"&per_page=20&sort=followers&type=users"
            yield scrapy.http.Request(url, headers=headers)

    def parse(self, response):

        #
        # print(parsed_data["hits"])
        print(response.body)
        print("--------------")
        f = open('users.json', 'w')
        parsed_data = json.loads(response.text)
        json.dump(parsed_data, f)


