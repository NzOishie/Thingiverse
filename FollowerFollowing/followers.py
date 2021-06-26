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
            followers =  response.css('div.user-about>div:not([class*="user-fullname"])')
            count = 0
            # username = username.strip("\n                ")
            follower = followers[0]
            for follower in followers:
                username = follower.css("div::text").extract_first()
                if count% 2 == 0:
                    print(count, username)
                count = count + 1
