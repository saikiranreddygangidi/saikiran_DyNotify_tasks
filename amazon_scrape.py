import requests
from bs4 import BeautifulSoup
import json
import time


def get_data(next_page):
    all_product_details=[]
    try:
        while next_page != None:
            page=requests.get(next_page)
            #it wait for 2 second complete page is loaded 
            time.sleep(2)
            soup =BeautifulSoup(page.content,'html.parser')
            all_title=soup.find_all("span",{"class":"a-size-medium a-color-base a-text-normal"})
            all_price=soup.find_all("span",{"class":"a-price-whole"})
            all_stars=soup.find_all("span",{"class":"a-icon-alt"})
            all_img=soup.find_all("div",{"class":"a-section aok-relative s-image-fixed-height"})
            for a,b,c,d in zip(all_title,all_price,all_stars,all_img):
                all_product_details.append({'title':a.get_text(),'price':b.get_text(),'stars':c.get_text(),'img':d.find('img')["src"]})
            next_page=soup.find("li",{"class":"a-last"})
            if next_page is not None :
                next_page=next_page.find('a')
                if next_page is not None:
                    next_page="https://www.amazon.in"+next_page["href"]
            
    except Exception as e:
        print(e)
    return all_product_details

#start executing from here
if __name__ == "__main__": 
    PRODUCT=input("enter product name you want:- ")
    next_page="https://www.amazon.in/s?k="+PRODUCT   
    all_product_details=get_data(next_page)
    PRODUCT=PRODUCT.replace(" ","_")
    all_product_details=json.dumps(all_product_details)   
    file = open('data_'+PRODUCT+'.json', 'w') 
    file.write(all_product_details) 
    file.close()
    

