import scrapy
from ..items import AmazonTutItem

class AmazonSpider(scrapy.Spider):
    name = "amazon"
    start_urls = [
        "https://www.amazon.in/s?i=stripbooks&bbn=976389031&rh=n%3A976389031%2Cp_n_publication_date%3A2684819031%2Cp_n_feature_three_browse-bin%3A9141482031&dc&ds=v1%3AVIOuxxmQSAAD%2BXd582rjlRV84bvj5Cr2o8iRRoVOtUU&qid=1701948496&rnid=9141481031&ref=sr_nr_p_n_feature_three_browse-bin_1"
        ]

    def parse(self, response):
        items = AmazonTutItem()

        product_name = response.css('h2 a span::text').extract()
        product_author = response.css(".a-color-secondary .a-size-base:nth-child(2)").css("::text").extract()
        product_price = response.css(".puis-price-instructions-style .a-price-whole").css("::text").extract()
        product_link = response.css(" div > h2> a::attr(href)").extract()

        items["product_name"] = product_name
        items["product_author"] = product_author
        items["product_price"] = product_price
        items["product_link"] = product_link

        yield items

       # yield{
           # "product_name":product_name,
            #"product_author":product_author,
            #"product_price":product_price,
            #"product_link":product_link
        #}


