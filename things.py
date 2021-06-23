import scrapy
import json


class ThingsSpider(scrapy.Spider):
    name = 'things'
    all_things = []

    def start_requests(self):
        headers = {"Authorization": "Bearer 56edfc79ecf25922b98202dd79a291aa"}
        with open('designs.json') as f:
            designs = json.load(f)
        for design in designs:
            print(design["id"])
            url = "https://api.thingiverse.com/things/"+str(design["id"])
            yield scrapy.http.Request(url, headers=headers)

    def parse(self, response):

        # print(response.body)
        # print("--------------")
        parsed_data = json.loads(response.text)
        self.all_things.append(parsed_data)
        writefile = open('things/things.json', 'w')

        json.dump(self.all_things, writefile)
        writefile.close()
