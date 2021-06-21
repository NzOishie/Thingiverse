import scrapy
import json


class RepliesSpider(scrapy.Spider):
    name = 'replies'
    all_replies = []


    def start_requests(self):
        headers = {"Authorization": "Bearer 56edfc79ecf25922b98202dd79a291aa"}
        with open('root_comment.json') as f:
            root_comments = json.load(f)
        for comment in root_comments:
            print(comment["id"])
            url = 'https://api.thingiverse.com/comments/'+str(comment["id"])+'/replies?t=1624297527420'
            yield scrapy.http.Request(url, headers=headers)

    def parse(self, response):

        parsed_data = json.loads(response.text)
        self.all_replies = [*self.all_replies, *parsed_data]
        writefile = open('replies.json', 'w')
        json.dump(self.all_replies, writefile)
