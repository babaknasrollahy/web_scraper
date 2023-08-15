
#### this file was created for get all links of one specific tag(title) ####

from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
from flask import Flask
import requests

app = Flask(__name__)
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


@app.route('/title/<title>')
def get_title(title):
    print(title)
    today = str(date.today()).split('-')
    driver = connect_to_chrome()
    for year in range(int(today[0]),2022,-1):

        for month in range(int(today[1]),0,-1):
            if len(str(month)) < 2 :
                month = "0" + str(month)

            for day in range(int(today[2]),0,-1):
                if len(str(day)) < 2 :
                    day = "0" + str(day)

            ######################### get all links  ######################################
                try:
                    driver.set_page_load_timeout(15)
                    print(f"########  {year} - {month} - {day}  ########")
                    driver.get(f"https://medium.com/tag/{title}/archive/{year}/{month}/{day}")
                
                    main = driver.find_element(By.TAG_NAME, "body")

                    articles = main.find_elements(By.CLASS_NAME, "streamItem--postPreview")

                    for article in articles:
                        titles = article.find_element(By.TAG_NAME, "h3")
                        print(titles.text)
                        link = article.find_elements(By.TAG_NAME, 'a')[3]
                        link_url = link.get_attribute("href")  
                        with open(f"../shared_files/{title}_links.txt" , 'a') as file :
                            file.write(f"{titles.text}==={link_url}==={year}-{month}-{day}\n")
                except: 
                    print("error through find element !!!")
            #######################################################################
            today[2] = "30"
        today[1] = "12"
        
    requests.get('http://sign_in:5000/sign_in')
    return f"request for sing_in send"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

