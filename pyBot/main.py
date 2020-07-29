# need to work on liking the post
# need to figure out how to get the list of followers of users having followers in 'k' and 'm'.(thousands and millions)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot():
    def __init__(self, email, password):
        #self.browser = webdriver.Chrome("./chromedriver") #gettig list of followers not working with chrome
        self.browser = webdriver.Firefox() #for running geckodriver on linux, the geckodriver file should be placed in /usr/local/bin
        self.email = email
        self.password = password

    def signIn(self):
        self.browser.get('https://www.instagram.com/accounts/login/')

        time.sleep(3)

        #print(self.browser.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input'))
        #emailInput = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input')

        emailInput = self.browser.find_elements_by_css_selector('form input')[0]
        passwordInput = self.browser.find_elements_by_css_selector('form input')[1]

        emailInput.send_keys(self.email)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        
        time.sleep(5)

        saveinfo = self.browser.find_element_by_css_selector('button.sqdOP:nth-child(1)')
        #saveinfo = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button')
        saveinfo.send_keys(Keys.ENTER)

        time.sleep(5)

        
        notif = self.browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        notif.send_keys(Keys.ENTER)

        print("Logged In")

        time.sleep(4)

    def seeAll_follow(self):
        time.sleep(3)
        
        link = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/section/div[3]/div[2]/div[1]/a');
        link.send_keys(Keys.ENTER)

        time.sleep(4)

        followButton = self.browser.find_elements_by_css_selector('button');
        for bttn in followButton:
            if(bttn.text == 'Follow'):
                bttn.click()
                #print("Pressed Follow Button")
                #time.sleep(2)

        time.sleep(4)

    def follow_by_name(self,username):

        self.browser.get('https://www.instagram.com/' + username + '/')
        time.sleep(4)

        followButton = self.browser.find_element_by_css_selector('button')

        if followButton.text == '': #error handling (sort of) with private and pubic accounts 
            followButton = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/button')

        if (followButton.text == 'Follow'):
            followButton.send_keys(Keys.ENTER)
            print("Pressed Follow Button")
            time.sleep(2)
        else:
            print("You are already following this user")
        time.sleep(4)


    def Like(self):
        time.sleep(4)
        
        likeButton = self.browser.find_elements_by_xpath('/html/body/div[1]/section/main/section/div[1]/div[3]/div/article[1]/div[2]/section[1]/span[1]/button')
        for i in likeButton:
            i.send_keys(Keys.ENTER)

    def getUserFollowers(self, username):

        self.browser.get('https://www.instagram.com/' + username)
        followersLink = self.browser.find_element_by_css_selector('ul li a')

        link = self.browser.find_element_by_css_selector('li.Y8-fY:nth-child(2) > a:nth-child(1) > span:nth-child(1)')
        fllwno = int(link.get_attribute('title'))
        print(fllwno)

        followersLink.click()
        time.sleep(2)

        followersList = self.browser.find_element_by_css_selector('div[role=\'dialog\'] ul')
        followersList.click()
        numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))


        actionChain = webdriver.ActionChains(self.browser)
        while numberOfFollowersInList < fllwno:
            actionChain.key_down(Keys.END).key_up(Keys.END).perform()
            numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))

        time.sleep(2)

        final = followersList.find_elements_by_css_selector('li')
        for user in final:
            userLink = user.find_element_by_css_selector('a').get_attribute('href')
            print(userLink)


    def DMessage(self,To,message):
        time.sleep(2)
        self.browser.get('https://www.instagram.com/' + To + '/')
        time.sleep(2)
        ButtonList = self.browser.find_elements_by_css_selector('button')
        ButtonList[0].click()
        time.sleep(2)
        textArea = self.browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
        textArea.send_keys(message)
        time.sleep(1)
        textArea.send_keys(Keys.ENTER)
        
        #person = self.browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[3]/div/div/div/div')
        #for i in person:
        #    print(i)
    

    def unfollow_by_name(self,username):
        self.browser.get('https://www.instagram.com/' + username + '/')
        time.sleep(4)
        followButton = self.browser.find_elements_by_css_selector('button')

##        for i in followButton:
##            print(i.text)


        if followButton[1].text == 'Requested':
            print("req")
            followButton[1].send_keys(Keys.ENTER)
            unfollowButton = self.browser.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]')
            unfollowButton.send_keys(Keys.ENTER)
            print("Pressed Unfollow Button")
          

        if followButton[0].text == 'Message':
            followButton = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div[2]/span/span[1]/button')
            followButton.send_keys(Keys.ENTER)
            unfollowButton = self.browser.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]')
            unfollowButton.send_keys(Keys.ENTER)
            print("Pressed Unfollow Button")

        else:
            print("Not follwing")
            
        time.sleep(4)
            



def main(user):
    bot = InstagramBot("username","password")
    bot.signIn()
    #bot.Like() #still need to work on this
    #bot.seeAll_follow()
    #bot.DMessage('sumitsaini_lc_928','using your bot')

    #public famous
    #bot.follow_by_name('therock')
    #bot.unfollow_by_name('therock')
    
    #public
    #bot.follow_by_name(user)
    #bot.unfollow_by_name('sumitsaini_lc_928')
    #bot.getUserFollowers('sumitsaini_lc_928')
    print("done")

start = input()
main(start)

