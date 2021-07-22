import scrapy
import json

count = 1
stop = {}



class DesignsSpider(scrapy.Spider):
    name = 'designs'

    def start_requests(self):
        global stop

        headers = {"Authorization": "Bearer 56edfc79ecf25922b98202dd79a291aa"}
        with open('users.json') as f:
            users = json.load(f)
        for user in users:
            i = 1
            stop[user["name"]] = False
            print("**************************************"+user["name"])
            while True:
                if stop[user["name"]] == True:
                    break;
                url = 'https://api.thingiverse.com/users/'+user["name"]+'/search/?page='+str(i)+'&per_page=20&type=things&sort=newest&t=1624203762938'
                yield scrapy.http.Request(url, headers=headers, cb_kwargs={"page":i,"username":user["name"]})
                i = i + 1

    def parse(self,response,page,username):
        global count,stop
        # page = response.request.cb_kwargs["i"]
        # username = response.request.cb_kwargs["username"]
        print(page,username)
        parsed_data = json.loads(response.text)
        print(count, len(parsed_data["hits"]))

        if len(parsed_data["hits"]) == 0:
            stop[username] = True
        else:
            writefile = open(f'designs/designs-{username}-{page}.json', 'w')
            # readfile = open('designs.json','r')
            # content = readfile.read()
            # hits = parsed_data["hits"]
            # if content:
            #     previous_data = json.loads(content)
            #     hits = [*previous_data, *hits]
            json.dump(parsed_data["hits"], writefile)
            writefile.close()
        count = count + 1







