import scrapy
import json

count = 1
stop = False
i = 1



class DesignsSpider(scrapy.Spider):
    name = 'designs'

    def start_requests(self):
        global i, stop
        headers = {"Authorization": "Bearer 56edfc79ecf25922b98202dd79a291aa"}
        with open('users.json') as f:
            users = json.load(f)
        for user in users["hits"]:
            print(user["name"])
        while True:
            if stop == True:
                break;
            url = 'https://api.thingiverse.com/users/dutchmogul/search/?page='+str(i)+'&per_page=20&type=things&sort=newest&t=1624203762938'
            i = i +1
            yield scrapy.http.Request(url, headers=headers)

    def parse(self,response):
        global count,stop
        parsed_data = json.loads(response.text)
        print(count, len(parsed_data["hits"]))

        if len(parsed_data["hits"]) == 0:
            stop = True
        else:
            writefile = open('designs.json', 'w')
            readfile = open('designs.json','r')
            content = readfile.read()
            hits = parsed_data["hits"]
            if content:
                previous_data = json.loads(content)
                hits = [*previous_data, *hits]
            json.dump(hits, writefile)
            readfile.close()
            writefile.close()
        count = count + 1







