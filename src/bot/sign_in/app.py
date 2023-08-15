from flask import Flask 
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import imaplib
import re
import requests

app = Flask(__name__)


####################    Read Email and Regex Functions   ######################
def read_email_for_login():
    # IMAP server details for Outlook
    imap_server = 'outlook.office365.com'
    imap_port = 993

    # Your Outlook credentials
    username = 'mediumscraper@outlook.com'
    password = 'babak13830'

    # Connect to the IMAP server
    imap = imaplib.IMAP4_SSL(imap_server, imap_port)

    # Login to your Outlook account
    imap.login(username, password)

    # Select the mailbox (in this case, the 'INBOX' mailbox)
    imap.select('INBOX')

    # Search for all emails in the mailbox
    typ, message_numbers = imap.search(None, 'ALL')

    # Get a list of email IDs
    email_ids = message_numbers[0].split()

    # Retrieve the latest email (in this case, the last email)
    latest_email_id = email_ids[-1]

    # Fetch the email data
    typ, data  = imap.fetch(latest_email_id, '(RFC822)')

    # Logout from your Outlook account
    imap.logout()

    return data

def regex_and_find_link(link):
    file_content = str(link)
    # print(file_content)
    file_content_str = file_content.replace("\\n", "").replace("\\r", "").replace("3D", "")
    regex_pattern = "https://medium\.com/m/callback/email\?token=(\w+)=&operation=login&state=medium"

    result = re.search(regex_pattern, file_content_str)

    result = result.group()

    counter = 0
    result_str = ""
    for char in result:
        if char == "=":
            if counter == 1:
                counter += 1
                continue
            counter += 1
        result_str += char
        
    return result_str
##################################################################

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


@app.route('/sign_in')
def complete_sign_in():
    while True:
        try:
        ################    Send email   ######################
            driver = connect_to_chrome()
            driver.get("https://medium.com/tag/python/archive/")
            sign_in = driver.find_element(By.CLASS_NAME,"js-signInButton")
            sign_in.click()
            email = driver.find_element(By.CLASS_NAME,"js-emailButton")
            email.click()
            sleep(2)
            input_eamil = driver.find_element(By.ID,"email")
            input_eamil.send_keys("mediumscraper@outlook.com")
            sleep(2)
            click_on_continue = driver.find_element(By.CLASS_NAME , 'button--borderless')
            click_on_continue.click()
            sleep(10)
        ######################################################
        
        ################    Use Functins to Read and Regex   ######################

            email = read_email_for_login()
            link = regex_and_find_link(email)
            # url = "http://article_creator:5000/creating_articles"
            url = "http://article_creator:5000/creating_articles"
            print(f"######### Your Login Link is : {link} ############")
            driver.close()
            break
        except: 
            print("there is an error in your sign_in proccess !!!")
            continue
        
    requests.post( url , data=link)
    return "link sended. "

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)



    




# @app.route('/')
# def send_post():
#     url = "http://localhost:5000/get_post"
#     link = "https://babaknasrollahy.com/5454515121&stack/kdfjdkfj"
#     requests.post( url , data=link)
    
#     return redirect(url_for('get_post'))
    
# @app.route('/get_post' , methods=['GET','POST'])
# def get_post():
#     link = request.data.decode('utf-8')
#     print(f'this is link in get_post == {link}')
#     return "ok"
    



