#### this file was created for creating all artifact files ####
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from flask import Flask , request
import requests
from time import sleep
import json

def connect_to_chrome():
    chrome_server_url = "http://localhost:4444"

    # Configure Chrome options with desired capabilities
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--pageLoadStrategy=eager')
    options.page_load_strategy = 'eager'
    

    # Connect to the Chrome server using Selenium WebDriver
    return webdriver.Remote(command_executor=chrome_server_url, options=options)

app = Flask(__name__)
@app.route('/')
def test():
    # driver = webdriver.Chrome()
    # # driver = connect_to_chrome()
    # with open('./New_links.txt' , 'r') as file:
    #             all_text = file.readlines()
    #             for text in all_text:
    #                     val = text.split("===")    
                            
    #                     url = val[1]
    #                     file_name = val[0]
    #                     # try:
    #                     # driver.set_page_load_timeout(10)
    #                     driver.get(url)
    # #                     input()
    # #                     ###########################  Achieve all of Information  ##############################
    # #                     # Find the element and get its text content
    # #                     element = driver.find_element(By.TAG_NAME , "article")
    # #                     cont_en = element.text
    # #                     ######################
    # #                     # Achieve header of an article
    # #                     header = file_name
    # #                     ######################
    # #                     # Achieve Writer's name
    # #                     writer_name = element.find_element(By.CSS_SELECTOR ,"a[data-testid='authorName']")
    # #                     writer = writer_name.text
    # #                     ######################
    # #                     # Achieve likes count
    # #                     like_count = element.find_element(By.CLASS_NAME, "pw-multi-vote-count")
    # #                     like = int(like_count.text)
    # #                     ######################
    # #                     # Achieve date
    # #                     date = val[2]
    # #                     #######################
    # #                     # Achieve tag_id
    # #                     # tag_id = requests.get('http://tag_checker:5000/show_active')
    # #                     # tag_id = tag_id.text
    # #                     #######################
    # #                     # Achieve all tags and send tags to tag_checher .
    #                     tags = driver.find_elements(By.TAG_NAME , "a")
    #                     tags_list = []
    #                     other_tags = ""
    #                     for item in tags:
    #                         if "/tag" in item.get_attribute("href"):
    #                             tags_list.append(item.text)
    #                             other_tags += item.text + " "
    #                     print(tags_list)
    #                     print(other_tags)
    #                     for index in tags_list:
    #                         requests.get(f"http://tag_checker:5000/add_tag_bot/{index}")
    #                         sleep(0.5)
    # #                     ########################
    # #                     #########################################################################################
                        
    # #                     ###################    create json file    #########################
    # #                     article_json = {
    # #                         "tag_id" : 1 ,
    # #                         "cont_en" : cont_en,
    # #                         "cont_fa" : "this is content farsi",
    # #                         "header" : header,
    # #                         "date" : date,
    # #                         "like" : like, 
    # #                         "writer" : writer,
    # #                         "other_tags" : tags
    # #                     }
    # #                     # headers = {'Content-Type': 'application/json'}
    # #                     # receiver = "http://localhost:5005/receive_json/" 
    # #                     # response = requests.post(receiver, data=json.dumps(article_json), headers=headers)
    # #                     # # Process the response if needed
    # #                     # if response.status_code == 200:
    # #                     #     print('Text sent successfully')
    # #                     # else:
    # #                     #     print('Error sending text')
                        
                        
    # #                     # except: print("there are some errors, while writing articles!!!")
    # # print(f"this is like_count = {like} and  {type(like)}")
    # return "ok"
    active = requests.get('http://localhost:5000/show_active')
    active = active.text
    tag_id = active.split('---')[0]
    tag = active.split('---')[1]
    print(f"this is tag_id === {tag_id}")
    print(f"this is tag === {tag}")
    return "ok"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)
