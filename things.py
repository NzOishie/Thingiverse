import scrapy
import json


class ThingsSpider(scrapy.Spider):
    name = 'things'

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
        writefile = open('things/things.json', 'a')
        # json.dump("[]",writefile)
        # with open("things/things.json") as readfile:
        #     previous_data = json.load(readfile)
        # if (previous_data):
        #     hits = {**previous_data, **parsed_data}
        #     json.dump(hits, writefile)
        #     print("Boo!")
        # else:
        json.dump(parsed_data, writefile)
