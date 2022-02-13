import requests
import gzip
import json
import logging
import csv 


#exercise 01
def send_post_request():
    params = {"isadmin":"1"}
    url = "https://httpbin.org/anything"
    page = requests.post(url,params=params)
    return page.text

def send_post_request_headers():
    params = {"isadmin":"1"}
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
    url = "https://httpbin.org/anything"
    page = requests.post(url,params=params,headers = headers)
    return page.text
    
# exercice 02:
class product(object):
    # FYI there is an error in json file key 'Product'  the correct key sholud be "Products"
    def read_json_file(self,json_file=None):
        if not json_file:
            json_file = './data/data.json.gz'
        a_file = gzip.open(json_file, "rb")
        contents = a_file.read()
        data =  json.loads(contents)
        items = data['Bundles']
        return items

    def print_and_write(self,items):
        csvfile = open('./product.csv', 'w')
        writer = csv.writer(csvfile)
        writer.writerow(['name','price'])
        for row in items:
            for key,products in row.items():
                if key in ['Product','Products']:
                    for product in products:
                        try:
                            name= product['Name']
                            name = name[:30]
                            price = product['Price']
                            if price == None:
                                price = 0
                            price = '%.1f'%(price)
                            is_available = product['IsAvailable']
                            if not is_available:
                                logging.warning("this product id :{id}, name:{name} unavailable".format(id=product['Barcode'],name=product['Name']))
                            else:
                                writer.writerow([name,price])


                        except Exception as e:
                            if '{}'.format(e)=="'IsAvailable'":
                                logging.error("ERROR: product’s availability can’t be found   {}".format(e))
                            elif '{}'.format(e)=="'Name'":
                                logging.error("ERROR: product’s Name can’t be found   {}".format(e))


if __name__ == __main__:
    #
    """third_part/from src import product 
    p= product()
    items = p.read_json_file()    
    p.print_and_write(items)"""                
                            
                        

