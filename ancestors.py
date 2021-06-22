import scrapy
import json

#not necessary

class AncestorsPySpider(scrapy.Spider):
    name = 'ancestors.py'
    all_ancestors = []


    def start_requests(self):
        headers = {"Authorization": "Bearer 56edfc79ecf25922b98202dd79a291aa"}
        with open('designs.json') as f:
            designs = json.load(f)
        for design in designs:
            print(design["id"])
            url = "http://api.thingiverse.com/things/"+str(design["id"])+"/ancestors/"
            yield scrapy.http.Request(url, headers=headers)

    def parse(self, response):

        parsed_data = json.loads(response.text)
        self.all_ancestors =[*self.all_ancestors, *parsed_data]
        writefile = open('ancestors.json', 'w')
        json.dump(self.all_ancestors, writefile)


