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
            print(copy["id"])
            url = "https://www.thingiverse.com/make:" + str(copy["id"])
            yield scrapy.http.Request(url, headers=headers, cb_kwargs={"make_id":copy["id"]})

    def parse(self, response, make_id):
        shares = response.xpath('//*[@id="main"]/div/div[2]/div[2]/div[1]/div/span[3]/a/text()').get()
        views =  response.xpath('//*[@id="main"]/div/div[3]/div[1]/div[3]/div/text()').get()
        views = int ( "".join(filter(str.isdigit, views)))
        catagory = response.xpath('//*[@id="main"]/div/div[3]/div[1]/div[3]/a/text()').get()
        if catagory:
            catagory = catagory.strip("'\n                            Found in ")
        printerBrand = response.xpath('//*[@id="main"]/div/div[3]/div[2]/div[1]/div[2]/p/a/text()').get()
        printer_a = response.xpath('//*[@id="main"]/div/div[3]/div[2]/div[1]/div[3]/p/a/text()').get()
        printer_b = response.xpath('//*[@id="main"]/div/div[3]/div[2]/div[1]/div[3]/p/text()').get()
        if printer_a and printer_b:
            printer = printer_a + printer_b
        else:
            printer = None
        rafts = response.xpath('//*[@id="main"]/div/div[3]/div[2]/div[1]/div[4]/p/text()').get()
        supports = response.xpath('//*[@id="main"]/div/div[3]/div[2]/div[1]/div[5]/p/text()').get()
        resoulution = response.xpath('//*[@id="main"]/div/div[3]/div[2]/div[1]/div[6]/p/text()').get()
        infill = response.xpath('//*[@id="main"]/div/div[3]/div[2]/div[1]/div[7]/p/text()').get()
        filament = response.xpath('//*[@id="main"]/div/div[3]/div[2]/div[1]/a/text()').get()
        if filament:
            filament = filament.strip("\n                        ")
        sourceLikes = int(response.xpath('//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/span[1]/span/a/span/text()').get())
        sourceCollects = int(response.xpath('//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/span[2]/span/a/span/text()').get())
        sourceComments = int(response.xpath('//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/span[3]/span/a/span/text()').get())
        print(sourceComments,sourceLikes,shares)
        with open('make_details.csv', 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ['make_id','shares', 'views', 'category', 'printerBrand','printer', 'rafts', 'support', 'resoulution', 'infill',
                          'filament', 'sourceLikes', 'sourceCollects', 'sourceComments']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if self.count == 0:
                writer.writeheader()
            writer.writerow({'make_id':make_id,'shares':shares,'views':views,'category':catagory, 'printerBrand': printerBrand,
                             'printer':printer, 'rafts':rafts, 'support':supports,
                             'resoulution': resoulution,'infill': infill,'filament': filament,
                             'sourceLikes': sourceLikes,'sourceCollects': sourceCollects,'sourceComments': sourceComments})
        self.count = self.count + 1






