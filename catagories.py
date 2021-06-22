import scrapy
import json


class CatagoriesSpider(scrapy.Spider):
    name = 'catagories'
    all_catagories = []

    def start_requests(self):

        headers = {"Authorization": "Bearer 56edfc79ecf25922b98202dd79a291aa"}

        with open('designs.json') as f:
            designs = json.load(f)
        for design in designs:
            print(design["id"])
            url = "https://api.thingiverse.com/things/"+str(design["id"])+"/categories"
            yield scrapy.http.Request(url, headers=headers, cb_kwargs={"design_id":design["id"]})

    def parse(self, response, design_id):
        parsed_data = json.loads(response.text)

        for comment in parsed_data:
            comment["design_id"] = design_id
            self.all_catagories.append(comment)
        writefile = open('catagories.json', 'w')

        json.dump(self.all_catagories, writefile)
        writefile.close()