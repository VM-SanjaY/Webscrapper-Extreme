from django.shortcuts import render, redirect
from selenium import webdriver
from django.db.models import Q
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from fuzzywuzzy import fuzz
from django.http import JsonResponse
import os
from django.http import HttpResponse
from .models import *
import random
import string
from bs4 import BeautifulSoup
import urllib.request
from urllib.request import urlopen
import time
import re
# Create your views here.


options = webdriver.ChromeOptions()
options.add_argument('headless')
service_obj = Service('D:/UdemuSelenium/chromedriver.exe')
driver = webdriver.Chrome(service=service_obj,options=options) #,options=options
driver.maximize_window()
driver.implicitly_wait(25)



def findproduct(request):
    if request.method == "GET" and 'term' in request.GET:
        print("ghjhgf")
        product = request.GET.get('term').lower()
        print(product)
        datas = Electronicinfo.objects.filter(usersearch__startswith=product)
        print("sgsggg- ", datas)
        results = []
        countbreaker = 0
        for data in datas:
            results.append(data.usersearch)
            countbreaker += 1
            if countbreaker == 4:
                break
        return JsonResponse(results, safe=False)

        
    if request.method == "POST":
        product = request.POST.get('product')
        if product:
            print(product)
            if Electronicinfo.objects.filter(usersearch=product).exists():
                return redirect('showdata', product=product)
            else:
                return redirect('runingselenium', product=product)
            # return redirect('runingselenium', product=product)
    return render(request,"main.html")




def runingselenium(request,product):
    driver.get("https://www.flipkart.com/")
    driver.find_element(By.XPATH,'//div[@class="JFPqaw"]/span').click()
    time.sleep(2)
    parent_dir = 'media\\Flipkart\\'
    driver.find_element(By.XPATH, "//input[@name='q']").send_keys(product,Keys.ENTER)
    name_site = product.split()
    if len(name_site) >= 1:
        sitename = name_site
        print(sitename[0])
    mainlinks = driver.find_elements(By.XPATH, '//div[@class="_13oc-S"]//a')
    similarity_threshold = 80
    file_count = 0
    
    for mainlink in mainlinks:
        flipurl = mainlink.get_attribute('href')
        if file_count >= 5:
            break
        else:
            nam = mainlink.find_element(By.XPATH, './/div[@class="_4rR01T"]').text
            similarity = fuzz.partial_ratio(product.lower(), nam.lower())
            if similarity >= similarity_threshold:
                if sitename:
                    if not Brand.objects.filter(name=sitename[0]).exists():
                        Brand(name=sitename[0],modelname=product).save()
                print("name is -", nam)
                try:
                    imgedata = mainlink.find_element(By.XPATH, './/img[@class="_396cs4"]').get_attribute('src')
                    actimga = imgedata.replace("312", "416")
                    print("actimga-", actimga)
                    try:
                        file_path = os.path.join(parent_dir, nam + '.jpeg')
                        img_path = os.path.join("Flipkart", nam + '.jpeg')
                        if not os.path.exists(file_path):
                            with urlopen(actimga) as response:
                                img_data = response.read()
                            with open(file_path, 'wb') as img_file:
                                img_file.write(img_data)
                            print("Image is downloaded and saved.")
                        else:
                            print("Image already exists.")
                    except Exception as e:
                        print("Error while downloading image:", str(e))
                except:
                    continue
                time.sleep(1)
                try:
                    rating = mainlink.find_element(By.XPATH, './/div[@class="_3LWZlK"]').text
                    print("rating is -", rating)
                except:
                    continue
                time.sleep(1)
                try:
                    sellprice = mainlink.find_element(By.XPATH, './/div[@class="_30jeq3 _1_WHN1"]').text
                    print("sellprice -", sellprice)
                except:
                    continue
                time.sleep(1)
                file_count+=1
                brname = Brand.objects.get(modelname=product)
                if not Electronicinfo.objects.filter(Q(image=file_path)&Q(productname=nam)).exists():
                    datain_bd = Electronicinfo(
                        brandname=brname,
                        usersearch=product,
                        productname=nam,
                        rating=rating,
                        image=img_path, # actimga
                        price=sellprice,
                        site="Flipkart",
                        siteurl=flipurl,
                        imageurl= actimga,
                        )
                    datain_bd.save()
            else:
                print("No product available with a similar name")
            time.sleep(1)

    product_name ='' 
    product_url=''
    driver.get("https://www.amazon.in/")
    name_site = product.split()
    main_dir = 'media\\Amazon\\'
    if len(name_site) >= 1:
        sitename = name_site
        print(sitename[0])
    time.sleep(5)
    try:
        driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']").send_keys(product)
        driver.find_element(By.XPATH,"//input[@id='nav-search-submit-button']").click()
        time.sleep(5)
    except:
        print('Asking captcha')
        try:
            driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']").send_keys(product)
            driver.find_element(By.XPATH,"//input[@id='nav-search-submit-button']").click()
            time.sleep(5)
        except:
            print('Again Asking captcha')
    product_price =''
    product_rating=''
    main_divs = driver.find_elements(By.CLASS_NAME,"s-asin")
    amazon_count=0
    img_name = ''
    temp_img_url={}
    for main_div in main_divs:
        if amazon_count>=5:
            break
        product_name = main_div.find_element(By.CLASS_NAME,"a-text-normal").text
        
        if not Electronicinfo.objects.filter(productname = product_name,site='Amazon'): 
            try:
                product_price = main_div.find_element(By.CLASS_NAME,"a-price-whole").text
                a=product_price.split(',')
                price = ''
                for i in  range(len(a)):
                    price+=a[i]
            except:
                product_price=0
                price =0
                print('No value')
                
            if product in (product_name.lower()) and int(price) > 100:
                print('sellingprice- ',price)
                amazon_count+=1
                try:
                    product_rating = main_div.find_element(By.CLASS_NAME,"a-icon-alt").get_attribute('textContent')
                    rating = product_rating.split()
                    if len(rating) >= 1:
                        ratinge = rating[0]
                        print(ratinge)
                except:
                    print('No rating')  
                product_url = main_div.find_element(By.CLASS_NAME,"a-text-normal").get_attribute('href')
                image_name = ''.join(random.choices(string.ascii_lowercase, k=5))
                if product_name !='' and int(price) > 100 and product_rating !='' and product_url !='':
                    img_name = str(product.lower())+'_'+str(image_name)+'.jpeg'
                    
                    if not Brand.objects.filter(modelname=product):
                        Brand(name=sitename[0],modelname=product).save()
                        
                    brname = Brand.objects.get(modelname=product)
                    
                    data = Electronicinfo(
                        brandname=brname,
                        usersearch=product,
                        productname=product_name,
                        rating = ratinge, #product_rating
                        image='Amazon/'+img_name, # actimga
                        price=product_price,
                        site="Amazon",
                        siteurl=product_url,
                    )
                    data.save()
                    temp_img_url[img_name] = product_url
        else:
            print('Product already exist')        
    if temp_img_url:
        for image_name,product_url in temp_img_url.items():
            file_dir = os.path.dirname(__file__)
            driver.get(product_url)
            time.sleep(5)
            image = driver.find_element(By.XPATH,"//div[@id='imgTagWrapperId']/img").get_attribute('src')
            img_name = image_name
            img_file = open(os.path.dirname(file_dir)+"\\media\\Amazon\\"+img_name,'wb')
            img_file.write(urllib.request.urlopen(image).read())
            img_file.close()
            return redirect('showdata', product=product)
          
    return HttpResponse("Data runned completely.")
    


def showdata(request,product):
    imagedata = Electronicinfo.objects.filter(usersearch=product,site="Flipkart")
    if imagedata:
        imgdata = imagedata.last()
    amazon = Electronicinfo.objects.filter(usersearch__icontains=product,site="Amazon")
    flipkart = Electronicinfo.objects.filter(usersearch__icontains=product,site="Flipkart")
    if amazon:
        amazondata = amazon.first()
    if flipkart:
        flipkartdata = flipkart.first()
    context = {"amazondata":amazondata,"imgdata":imgdata,"flipkartdata":flipkartdata}
    return render(request,'datatoshow.html',context)

    
    
    
    
    
    # //div[@data-index="3"]//div//div//div//a   = href     
    # //div[@data-index="3"]//div//div//div//a//img  = img
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


    
    
    
    





        








