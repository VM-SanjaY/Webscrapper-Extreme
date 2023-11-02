   # for mainlink in mainlinks:       
    #     nam = mainlink.find_element(By.XPATH, './/div[@class="_4rR01T"]').text
    #     print("product -",product)
    #     if product in nam:
    #         print("name is -", nam)
    #         imgedata = mainlink.find_element(By.XPATH, './/img[@class="_396cs4"]').get_attribute('src')
    #         actimga = imgedata.replace("312", "416")
    #         print("actimga-",actimga)
    #         time.sleep(1)
    #         rating = mainlink.find_element(By.XPATH, './/div[@class="_3LWZlK"]').text
    #         print("rating is -", rating)
    #         time.sleep(1)
    #         sellprice = mainlink.find_element(By.XPATH, './/div[@class="_30jeq3 _1_WHN1"]').text
    #         print("sellprice -", sellprice)
    #         time.sleep(1)
    #     else:
    #         print("No product available in that name")
    #     time.sleep(1)
    #     break
    
    
 # ------------------------------------------------------------------------------------------------------------------------
 
 
    # for mainlink in mainlinks:
    #     imgedata = mainlink.find_element(By.XPATH, './/img[@class="_396cs4"]').get_attribute('src')
    #     actimga = imgedata.replace("312", "416")
    #     print("actimga-",actimga)
    #     time.sleep(1)
        
    #     nam = mainlink.find_element(By.XPATH, './/div[@class="_4rR01T"]').text
    #     print("product -",product)
    #     if product in nam:
    #         print("name is -", nam)
    #     else:
    #         print("No product available in that name")
    #     time.sleep(1)

    #     rating = mainlink.find_element(By.XPATH, './/div[@class="_3LWZlK"]').text
    #     print("rating is -", rating)
    #     time.sleep(1)

    #     sellprice = mainlink.find_element(By.XPATH, './/div[@class="_30jeq3 _1_WHN1"]').text
    #     print("sellprice -", sellprice)
    #     time.sleep(1)
    #     break


# thumb image - https://rukminim2.flixcart.com/image/312/312/ktketu80/mobile/2/y/o/iphone-13-mlpk3hn-a-apple-original-imag6vpyur6hjngg.jpeg?q=70
# main image - https://rukminim2.flixcart.com/image/416/416/ktketu80/mobile/2/y/o/iphone-13-mlpk3hn-a-apple-original-imag6vpyur6hjngg.jpeg?q=70
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------

   
    
    # for mainlink in mainlinks:
    #     nam = mainlink.find_element(By.XPATH, './/div[@class="_4rR01T"]').text
    #     similarity = fuzz.partial_ratio(product.lower(), nam.lower())
    #     if similarity >= similarity_threshold:
    #         if sitename:
    #             Brand(name=sitename[0]).save()
    #         print("name is -", nam)
    #         try:
    #             imgedata = mainlink.find_element(By.XPATH, './/img[@class="_396cs4"]').get_attribute('src')
    #             actimga = imgedata.replace("312", "416")
    #             print("actimga-", actimga)
    #         except:
    #             continue
    #         time.sleep(1)
    #         try:
    #             rating = mainlink.find_element(By.XPATH, './/div[@class="_3LWZlK"]').text
    #             print("rating is -", rating)
    #         except:
    #             continue
    #         time.sleep(1)
    #         try:
    #             sellprice = mainlink.find_element(By.XPATH, './/div[@class="_30jeq3 _1_WHN1"]').text
    #             print("sellprice -", sellprice)
    #         except:
    #             continue
    #         time.sleep(1)
    #         file_count+=1
    #         brname = Brand.objects.get(name=sitename[0])
    #         datain_bd = Electronicinfo(
    #             brandname=brname,
    #             rating=rating,
    #             image=actimga,
    #             price=sellprice,
    #             site="Flipkart"
    #             )
    #         datain_bd.save()                 
    #     else:
    #         print("No product available with a similar name")
    #     time.sleep(1)
    #     break
    # return HttpResponse("Data runned completely.")
    
    
# --------------------------------------------------------------------------------------------------------------

# for mainlink in mainlinks:
#         if file_count >= 5:
#             break
#         else:
#             nam = mainlink.find_element(By.XPATH, './/div[@class="_4rR01T"]').text
#             similarity = fuzz.partial_ratio(product.lower(), nam.lower())
#             if similarity >= similarity_threshold:
#                 if sitename:
#                     Brand(name=sitename[0]).save()
#                 print("name is -", nam)
#                 try:
#                     imgedata = mainlink.find_element(By.XPATH, './/img[@class="_396cs4"]').get_attribute('src')
#                     actimga = imgedata.replace("312", "416")
#                     print("actimga-", actimga)
#                 except:
#                     continue
#                 time.sleep(1)
#                 try:
#                     rating = mainlink.find_element(By.XPATH, './/div[@class="_3LWZlK"]').text
#                     print("rating is -", rating)
#                 except:
#                     continue
#                 time.sleep(1)
#                 try:
#                     sellprice = mainlink.find_element(By.XPATH, './/div[@class="_30jeq3 _1_WHN1"]').text
#                     print("sellprice -", sellprice)
#                 except:
#                     continue
#                 time.sleep(1)
#                 file_count+=1
#                 brname = Brand.objects.get(name=sitename[0])
#                 datain_bd = Electronicinfo(
#                     brandname=brname,
#                     rating=rating,
#                     image=actimga,
#                     price=sellprice,
#                     site="Flipkart"
#                     )
#                 datain_bd.save()
#             else:
#                 print("No product available with a similar name")
#             time.sleep(1)
    
    
# -----------------------------------------------------------------------------------------------------------------------------

# -------------------------------  Flipkart --------------------------------------------------

#     driver.get("https://www.flipkart.com/")
#     driver.find_element(By.XPATH,'//div[@class="JFPqaw"]/span').click()
#     time.sleep(2)
#     parent_dir = 'media\\Flipkart\\'
#     driver.find_element(By.XPATH, "//input[@name='q']").send_keys(product,Keys.ENTER)
#     name_site = product.split()
#     if len(name_site) >= 1:
#         sitename = name_site
#         print(sitename[0])
#     mainlinks = driver.find_elements(By.XPATH, '//div[@class="_13oc-S"]//a')
#     similarity_threshold = 50
#     file_count = 0
    
#     for mainlink in mainlinks:
#         flipurl = mainlink.get_attribute('href')
#         flipsiteurl = "https://www.flipkart.com"+flipurl
#         if file_count >= 5:
#             break
#         else:
#             nam = mainlink.find_element(By.XPATH, './/div[@class="_4rR01T"]').text
#             similarity = fuzz.partial_ratio(product.lower(), nam.lower())
#             if similarity >= similarity_threshold:
#                 if sitename:
#                     if not Brand.objects.filter(name=sitename[0]).exists():
#                         Brand(name=sitename[0],modelname=product).save()
#                 print("name is -", nam)
#                 try:
#                     imgedata = mainlink.find_element(By.XPATH, './/img[@class="_396cs4"]').get_attribute('src')
#                     actimga = imgedata.replace("312", "416")
#                     print("actimga-", actimga)
#                     try:
#                         file_path = os.path.join(parent_dir, nam + '.jpeg')
#                         if not os.path.exists(file_path):
#                             with urlopen(actimga) as response:
#                                 img_data = response.read()
#                             with open(file_path, 'wb') as img_file:
#                                 img_file.write(img_data)
#                             print("Image is downloaded and saved.")
#                         else:
#                             print("Image already exists.")
#                     except Exception as e:
#                         print("Error while downloading image:", str(e))
#                 except:
#                     continue
#                 time.sleep(1)
#                 try:
#                     rating = mainlink.find_element(By.XPATH, './/div[@class="_3LWZlK"]').text
#                     print("rating is -", rating)
#                 except:
#                     continue
#                 time.sleep(1)
#                 try:
#                     sellprice = mainlink.find_element(By.XPATH, './/div[@class="_30jeq3 _1_WHN1"]').text
#                     print("sellprice -", sellprice)
#                 except:
#                     continue
#                 time.sleep(1)
#                 file_count+=1
#                 brname = Brand.objects.get(name=sitename[0])
#                 if not Electronicinfo.objects.filter(Q(image=file_path)&Q(price=sellprice)&Q(productname=nam)).exists():
#                     datain_bd = Electronicinfo(
#                         brandname=brname,
#                         productname=nam,
#                         rating=rating,
#                         image=file_path, # actimga
#                         price=sellprice,
#                         site="Flipkart",
#                         siteurl=flipsiteurl,
#                         )
#                     datain_bd.save()
#             else:
#                 print("No product available with a similar name")
#             time.sleep(1)

# ----------------------------------------------------------------------------------------------------------

# ---------------------------------- Amazon -------------------------------------------------

# driver.get("https://www.amazon.in/")
#     time.sleep(2)
#     main_dir = 'media\\Amazon\\'
#     driver.find_element(By.XPATH, '//input[@id="twotabsearchtextbox"]').send_keys(product,Keys.ENTER)
#     name_site = product.split()
#     if len(name_site) >= 1:
#         sitename = name_site
#         print(sitename[0])
    
#     amalink = driver.find_elements(By.XPATH,'//div[@class="a-section"]//span[@class="a-size-medium a-color-base a-text-normal"]')
#     namecount = 0
#     for namedata in amalink:
#         nadata = namedata.text
#         similarity_threshold = 50
#         similarity = fuzz.partial_ratio(product.lower(), nadata.lower())
#         print("Similarity Score:", similarity)
#         if similarity >= similarity_threshold:
#             nameofproduct = namedata.text
#             urlofproduct = namedata.get_attribute('href')
#             print("urlofproduct- ",urlofproduct)
#             print("nameofproduct -",nameofproduct)
#             namedata.click()
#             p= driver.window_handles[0]         
#             c = driver.window_handles[1]
#             driver.switch_to.window(c)        

#             get_url = driver.current_url
#             print("The current url is:"+str(get_url))
#             imageroute = driver.find_element(By.XPATH,'//img[@alt='+nameofproduct+']').get_attribute('src')
#             print("imageroute-", imageroute)
#             if not ".jpg" in imageroute:
#                 imageroute = imageroute+".jpg"
#             prodprice = driver.find_element(By.XPATH,"(//span[@class='a-price-whole'])[1]").text
#             print("prodprice- ",prodprice)
#             namecount +=1
#             if namecount == 1:
#                 break
#             time.sleep(2)
# 


# ------------------------------------------------------------------------------------------------------------

# -------------Flipkart 2 -------------------------------


#     driver.get("https://www.flipkart.com/")
#     driver.find_element(By.XPATH,'//div[@class="JFPqaw"]/span').click()
#     time.sleep(2)
#     parent_dir = 'media\\Flipkart\\'
#     driver.find_element(By.XPATH, "//input[@name='q']").send_keys(product,Keys.ENTER)
#     name_site = product.split()
#     if len(name_site) >= 1:
#         sitename = name_site
#         print(sitename[0])
#     mainlinks = driver.find_elements(By.XPATH, '//div[@class="_13oc-S"]//a')
#     similarity_threshold = 50
#     file_count = 0
    
#     for mainlink in mainlinks:
#         flipurl = mainlink.get_attribute('href')
#         if file_count >= 5:
#             break
#         else:
#             nam = mainlink.find_element(By.XPATH, './/div[@class="_4rR01T"]').text
#             similarity = fuzz.partial_ratio(product.lower(), nam.lower())
#             if similarity >= similarity_threshold:
#                 if sitename:
#                     if not Brand.objects.filter(name=sitename[0]).exists():
#                         Brand(name=sitename[0],modelname=product).save()
#                 print("name is -", nam)
#                 try:
#                     imgedata = mainlink.find_element(By.XPATH, './/img[@class="_396cs4"]').get_attribute('src')
#                     actimga = imgedata.replace("312", "416")
#                     print("actimga-", actimga)
#                     try:
#                         file_path = os.path.join(parent_dir, nam + '.jpeg')
#                         img_path = os.path.join("Flipkart", nam + '.jpeg')
#                         if not os.path.exists(file_path):
#                             with urlopen(actimga) as response:
#                                 img_data = response.read()
#                             with open(file_path, 'wb') as img_file:
#                                 img_file.write(img_data)
#                             print("Image is downloaded and saved.")
#                         else:
#                             print("Image already exists.")
#                     except Exception as e:
#                         print("Error while downloading image:", str(e))
#                 except:
#                     continue
#                 time.sleep(1)
#                 try:
#                     rating = mainlink.find_element(By.XPATH, './/div[@class="_3LWZlK"]').text
#                     print("rating is -", rating)
#                 except:
#                     continue
#                 time.sleep(1)
#                 try:
#                     sellprice = mainlink.find_element(By.XPATH, './/div[@class="_30jeq3 _1_WHN1"]').text
#                     print("sellprice -", sellprice)
#                 except:
#                     continue
#                 time.sleep(1)
#                 file_count+=1
#                 brname = Brand.objects.get(name=sitename[0])
#                 if not Electronicinfo.objects.filter(Q(image=file_path)&Q(price=sellprice)&Q(productname=nam)).exists():
#                     datain_bd = Electronicinfo(
#                         brandname=brname,
#                         usersearch=product,
#                         productname=nam,
#                         rating=rating,
#                         image=img_path, # actimga
#                         price=sellprice,
#                         site="Flipkart",
#                         siteurl=flipurl,
#                         imageurl= actimga,
#                         )
#                     datain_bd.save()
#             else:
#                 print("No product available with a similar name")
#             time.sleep(1)





    #     <h1>WebScarpper Extreme</h1>
    #   <div class="preloader">
    #     <div class="p">Loading....</div>
    #   </div>