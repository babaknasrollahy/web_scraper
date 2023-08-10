#### this file was created for creating all artifact files ####
from selenium import webdriver
from selenium.webdriver.common.by import By
from flask import Flask , request

app = Flask(__name__)

@app.route('/')
def test():
    driver = webdriver.Chrome()
    with open('C:\\Users\\Home-PC\\Desktop\\stack_mag\\src\\bot\\article_creator\\New_links.txt' , 'r') as file:
                all_text = file.readlines()
                for text in all_text:
                        val = text.split("===")    
                            
                        url = val[1]
                        file_name = val[0]
                        print(f"########################    this is url === {url}   ################################")
                        try:
                            driver.set_page_load_timeout(20)
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
                            #



                            #########################################################################################
                        except: "there are some errors, while writing articles!!!"

    return "ok"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
