from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot():
    def __init__(self, email, password):
        self.browser = webdriver.Chrome("./chromedriver")
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
        
        time.sleep(3)

        print("Logged In")
        
        notif = self.browser.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
        notif.send_keys(Keys.ENTER)

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

    def getUserFollowers(self, username, maximum):
        self.browser.get('https://www.instagram.com/' + username)
        followersLink = self.browser.find_element_by_css_selector('ul li a')
        followersLink.click()
        time.sleep(2)
        #element_inside_popup = self.browser.find_element_by_xpath('//div[@class="entity-list-wrapper ember-view"]//a')
        #followersLink.send_keys(Keys.SPACE)
        followersList = self.browser.find_element_by_css_selector('div[role=\'dialog\'] ul')
        numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
        lst = followersList.find_elements_by_css_selector('li')
        anchor = lst[len(lst)-1]
        lst.send_keys(Keys.END)
        
##        print(numberOfFollowersInList)
##        followersList.click()
##        actionChain = webdriver.ActionChains(self.browser)
##        while (numberOfFollowersInList < maximum):
##            actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
##            numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
##            #print(numberOfFollowersInList)
##        
##        followers = []
##        for user in followersList.find_elements_by_css_selector('li'):
##            userLink = user.find_element_by_css_selector('a').get_attribute('href')
##            print(userLink)
##            followers.append(userLink)
##            if (len(followers) == maximum):
##                break
##        return followers



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
    bot = InstagramBot("usernameOfBot","password")
    bot.signIn()
    #bot.Like()
    #bot.seeAll_follow()
    #bot.DMessage('sumitsaini_lc_928','using your bot')

    #public famous
    #bot.follow_by_name('therock')
    #bot.unfollow_by_name('therock')
    
    #public
    #bot.follow_by_name(user)
    #bot.unfollow_by_name('sumitsaini_lc_928')
    #bot.getUserFollowers('sumitsaini_lc_928',30)   
    print("done")

start = input()
main(start)
