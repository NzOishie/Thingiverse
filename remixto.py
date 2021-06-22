import scrapy
import json
stop = {}


class RemixtoPySpider(scrapy.Spider):
    name = 'remixto.py'
    all_remixto = []
    allowed_domains = ['https://api.thingiverse.com/things/62510/derivatives?page=1&per_page=9']
    start_urls = ['http://https://api.thingiverse.com/things/62510/derivatives?page=1&per_page=9/']

    def start_requests(self):
        global stop
        headers = {"Authorization": "Bearer 56edfc79ecf25922b98202dd79a291aa"}

        with open('designs.json') as f:
            designs = json.load(f)
        for design in designs:
            i = 1
            stop[design["id"]] = False
            print("**************************************" + str(design["id"]))
            while True:
                if stop[design["id"]] == True:
                    break;
                url = 'https://api.thingiverse.com/things/' + str(design["id"]) + '/derivatives?page=' + str(
                    i) + '&per_page=9'
                yield scrapy.http.Request(url, headers=headers, cb_kwargs={"page": i, "design_id": design["id"]})
                i = i + 1

    def parse(self, response, page, design_id):
        print(page, design_id)
        parsed_data = json.loads(response.text)

        if len(parsed_data) == 0:
            stop[design_id] = True
        else:

            for remix in parsed_data:
                remix["design_id"] = design_id
                self.all_remixto.append(remix)
            writefile = open('remixto.json', 'w')

            json.dump(self.all_remixto, writefile)
            writefile.close()
