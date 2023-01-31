from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from pw import user_name, passcode


class InstaBot:
    def __init__(self):
        chrome_driver_path = '../../../Downloads/chromedriver_win32/chromedriver.exe'
        self.driver = webdriver.Chrome(chrome_driver_path)
        self.driver.get("https://www.instagram.com/")

    def loging_in(self, username, password):
        sleep(3)
        username_field = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_field.send_keys(username)

        sleep(2)
        password_field = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_field.send_keys(password)

        sleep(2)
        login_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        login_button.click()

        sleep(15)
        not_now_button = self.driver.find_element(By.CSS_SELECTOR, "div ._ac8f button")
        not_now_button.click()

        sleep(3)
        not_now_button_two = self.driver.find_element(By.XPATH, '//button[text()="Not Now"]')
        not_now_button_two.click()

    def following_function(self):
        followers_buttons = self.driver.find_elements(By.CSS_SELECTOR,
                                                      "div ._ab8w ._ab94._ab97._ab9f._ab9k._ab9p ._ab9-._aba8._abcm button ._acan._acap._acas")
        for follower_button in followers_buttons:
            if follower_button.text == "Follow":
                follower_button.click()
                sleep(1)
            else:
                continue

    def followers_scrolling(self):
        all_a_tags = self.driver.find_elements(By.TAG_NAME, 'a')
        for a_tag in all_a_tags:
            print("s")
            if "/followers/" in a_tag.get_attribute('href'):
                a_tag.click()
                sleep(2)
                scroll = self.driver.find_element(By.XPATH,
                                                  '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
                for i in range(10):
                    self.following_function()
                    self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll)
                    sleep(2)

    def bot_action(self, number_of_accounts: int, searching_term: str):
        sleep(5)
        search_button = self.driver.find_element(By.CSS_SELECTOR, 'div ._aawf._aawg input ._aauy div ._aaw8')  # *****
        search_button.click()

        sleep(2)
        search_input = self.driver.find_element(By.XPATH, '//input[@placeholder="Search"]')
        search_input.send_keys(searching_term)

        index_no = 0
        while index_no < number_of_accounts:
            sleep(2)
            search_results = self.driver.find_elements(By.CSS_SELECTOR, "div ._aa61 div ._abm4")
            link = search_results[index_no].find_element(By.TAG_NAME, 'a')
            if "/tags/" in link.get_attribute('href'):
                index_no += 1
                continue
            else:
                sleep(2)
                link.click()
                sleep(2)
                self.followers_scrolling()
                sleep(2)
                self.driver.back()
                self.driver.back()
                sleep(2)
                search_button_two = self.driver.find_element(By.XPATH, '//span[text()="Books"]')
                search_button_two.click()
                index_no += 1
                sleep(2)


Bot = InstaBot()  # instance of Instabot
Bot.loging_in(username=user_name, password=passcode)  # loging in function
Bot.bot_action(number_of_accounts=5,
               searching_term="Books")  # this function does Searching, Switching accounts, following and Scrolling
