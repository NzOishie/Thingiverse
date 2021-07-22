import scrapy
import json
stop = {}

class FollowersSpider(scrapy.Spider):
    name = 'followers'


    def start_requests(self):
        global stop
        headers = {"Authorization": "Bearer 56edfc79ecf25922b98202dd79a291aa"}

        with open('../users.json') as f:
            users = json.load(f)

        for user in users["hits"]:
            i = 1
            print(user["id"])
            stop[user["id"]] = False
            while True:
                if stop[user["id"]]:
                    break;
                url = "https://www.thingiverse.com/"+user["name"]+"/followers?page=1&per_page=20"
                yield scrapy.http.Request(url, headers=headers, cb_kwargs={"page":i,"user_id":user["id"]})
                i = i + 1

    def parse(self, response, page, user_id):
        parsed_data = json.loads(response.text)

        if len(parsed_data) == 0:
            stop[user_id] = True
        else:
            followers = response.css('a.user-header::attr(href)')
            for follower in followers:
                follower = follower.strip("/")
                print(follower)
                print("---------------------------")

