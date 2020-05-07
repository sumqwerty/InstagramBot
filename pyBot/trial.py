from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class InstagramBot():
    def __init__(self, search):
        self.browser = webdriver.Chrome("./chromedriver")
        self.search = search

    def signIn(self):
        print(self.browser.get('https://www.duckduckgo.com'))
        
        time.sleep(3)
        SearchInput = self.browser.find_elements_by_css_selector('form input')[0]

        SearchInput.send_keys(self.search)
        SearchInput.send_keys(Keys.ENTER)
        
        cross = self.browser.find_element_by_xpath('/html/body/div[2]/div[8]/a/span')
        if(cross != None):
            print('cross')
            cross.click()

        cross.execute_script("window.scrollTo(0,document.body.scrollHeight)")

##        body = self.browser.find_element_by_xpath('/html/body')
##        body.send_keys(Keys.SPACE)

        
        
        
def main(user):
    bot = InstagramBot("qwerty")
    bot.signIn()   
    print("done")



start = input()
main(start)

