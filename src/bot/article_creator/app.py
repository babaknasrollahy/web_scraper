
#### this file was created for creating all artifact files ####
from selenium import webdriver
from selenium.webdriver.common.by import By
from flask import Flask , request
import requests
import json
from time import sleep

app = Flask(__name__)

###############  Conecting to the ChromeDriver Function  ######################
def connect_to_chrome():
    chrome_server_url = "http://chrome:4444"

    # Configure Chrome options with desired capabilities
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-dev-shm-usage')
    options.page_load_strategy = 'eager'
    

    # Connect to the Chrome server using Selenium WebDriver
    return webdriver.Remote(command_executor=chrome_server_url, options=options)
##################################################################################


@app.route('/creating_articles', methods=['GET','POST'])
def creating_files():
    link = request.data.decode('utf-8')
    print(f'signIn link created.')
    driver = connect_to_chrome()
    driver.get(link)
    print("login was successful")

    with open('../shared_files/New_links.txt' , 'r') as file:
            all_text = file.readlines()
            for text in all_text:
                val = text.split("===")    
                        
                url = val[1]
                file_name = val[0]
                try:
                    driver.set_page_load_timeout(15)
                    driver.get(url)
                    ###########################  Achieve all of Information  ##############################
                    # Find the element and get its text content
                    element = driver.find_element(By.TAG_NAME , "article")
                    cont_en = element.text
                    ######################
                    # Achieve header of an article
                    header = file_name
                    ######################
                    # Achieve Writer's name
                    writer_name = element.find_element(By.CSS_SELECTOR ,"a[data-testid='authorName']")
                    writer = writer_name.text
                    ######################
                    # Achieve likes count
                    like_count = element.find_element(By.CLASS_NAME, "pw-multi-vote-count")
                    like = like_count.text
                    ######################
                    # Achieve date
                    date = val[2]
                    #######################
                    # Achieve tag_id
                    tag_id = requests.get('http://tag_checker:5000/show_active')
                    tag_id = int(tag_id.text)
                    #######################
                    # Achieve all tags and send tags to tag_checher .
                    # tags = driver.find_elements(By.CLASS_NAME , "oa")
                    # tags_list = tags[0].text.split("\n")
                    # for item in tags_list:
                    #     requests.get(f"http://tag_checker:5000/add_tag_bot/{item}")
                    #     sleep(1)
                    # tags = tags[0].text.replace("\n",",")
                    ########################
                    #########################################################################################
                    
                    ###################    create json file    #########################
                    article_json = {
                        "tag_id" : tag_id ,
                        "cont_en" : cont_en,
                        "cont_fa" : "this is content farsi",
                        "header" : header,
                        "date" : date,
                        "like" : like, 
                        "writer" : writer,
                        "other_tags" : "tags"
                    }
                    headers = {'Content-Type': 'application/json'}
                    receiver = "http://content_writer:5000/receive_json/" 
                    response = requests.post(receiver, data=json.dumps(article_json), headers=headers)
                    # Process the response if needed
                    if response.status_code == 200:
                        print('Text sent successfully')
                    else:
                        print('Error sending text')
                        
                except: 
                    print("there are some errors, while writing articles!!!")

    requests.get("http://tag_checker:5000/complete/")
    return "all files were created."




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
