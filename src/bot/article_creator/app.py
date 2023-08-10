
#### this file was created for creating all artifact files ####
from selenium import webdriver
from selenium.webdriver.common.by import By
from flask import Flask , request

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

    # Connect to the Chrome server using Selenium WebDriver
    return webdriver.Remote(command_executor=chrome_server_url, options=options)
##################################################################################

##########  Achieve information of an Article    #############

    

#############################################################
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
                        print(writer_name.text)


                        #########################################################################################
                        with open(f'../articles/{file_name}.txt' , 'a') as f :
                            f.write(cont_en)
                        print(f"file {file_name} was created.")
                    except: "there are some errors, while writing articles!!!"
    return "all files were created."




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
