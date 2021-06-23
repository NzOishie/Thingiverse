import scrapy
import csv
import json


class MakeDetailsSpider(scrapy.Spider):
    name = 'make_details'
    count = 0
    def start_requests(self):
        headers = {"Authorization": "Bearer 56edfc79ecf25922b98202dd79a291aa"}
        with open('copies.json') as f:
            copies = json.load(f)
        for copy in copies:
            url = "https://www.thingiverse.com/make:" + str(copy["id"])
            yield scrapy.http.Request(url, headers=headers, cb_kwargs={"make_id":copy["id"]})

    def parse(self, response, make_id):

        for i in response.css('div.comment-5478347-wrapper'):
            yield {

            }

        # with open('make_comments.csv', 'a', newline='', encoding="utf-8") as csvfile:
        #     fieldnames = ['make_id','shares', 'views', 'category', 'printer', 'rafts', 'support', 'resoulution', 'infill',
        #                   'filament', 'sourceLikes', 'sourceCollects', 'sourceComments']
        #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #     if self.count == 0:
        #         writer.writeheader()
        #     writer.writerow({'make_id':make_id,'shares':shares,'views':views,'category':catagory,'printer':printer, 'rafts':rafts, 'support':supports,
        #                      'resoulution': resoulution,'infill': infill,'filament': filament,
        #                      'sourceLikes': sourceLikes,'sourceCollects': sourceCollects,'sourceComments': sourceComments})
        # self.count = self.count + 1






