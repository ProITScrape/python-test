import scrapy
from woolworths.items import WoolworthsItem
import json 

class ShopSpider(scrapy.Spider):
    name = 'shop'
    
    start_urls = ['https://www.woolworths.com.au/shop/browse/drinks/cordials-juices-iced-teas/iced-teas']
    
    
    def parse(self, response):
        headers = {
                "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0",
                "Accept": "application/json, text/plain, */*",
                "Accept-Language": "en-US,en;q=0.5",
                "Content-Type": "application/json"
              
            }
        url = "https://www.woolworths.com.au/apis/ui/browse/category"
        body = "{\"categoryId\":\"1_9573995\",\"pageNumber\":1,\"pageSize\":36,\"sortType\":\"TraderRelevance\",\"url\":\"/shop/browse/drinks/cordials-juices-iced-teas/iced-teas\",\"location\":\"/shop/browse/drinks/cordials-juices-iced-teas/iced-teas\",\"formatObject\":\"{\\\"name\\\":\\\"Iced Teas\\\"}\",\"isSpecial\":false,\"isBundle\":false,\"isMobile\":false,\"filters\":[],\"token\":\"\"}"
        yield scrapy.Request(url, callback=self.parse_results, method="POST", body=body,headers = headers)

    def parse_results(self, response):
        item =  WoolworthsItem()
        data = json.loads(response.body)
        products = data['Bundles']
        for product in products:
            product_fields = product['Products']
            for row in product_fields:
                department_names = row['AdditionalAttributes']['piesdepartmentnamesjson'].replace('\"', '').replace('[', '').replace(']', '')
                category_names = row['AdditionalAttributes']['piescategorynamesjson'].replace('\"', '').replace('\"', '').replace('[', '').replace(']', '')
                subcategory_names = row['AdditionalAttributes']['piessubcategorynamesjson'].replace('\"', '').replace('\"', '').replace('[', '').replace(']', '')
                product_name = product['Name']
                item['Products'] = product_name
                item['Breadcrumb'] = ['Home', department_names, category_names, subcategory_names]
                yield item