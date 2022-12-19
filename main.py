from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

PROMISED_DOWN = 15
PROMISED_UP = 2
EMAIL = ""
PASSWORD = ""
URL_SPEEDTEST = "https://www.speedtest.net"
URL_TWITTER = "https://www.twitter.com"
DRIVER_PATH = "/Users/jano/chromedriver"
down_speed = 0
up_speed = 0


class InternetSpeedBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(driver_path)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        global down_speed, up_speed
        self.driver.get(URL_SPEEDTEST)
        popup_cookies = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
        popup_cookies.click()
        sleep(2)
        go_button = self.driver.find_element(By.CLASS_NAME, "start-text")
        go_button.click()
        sleep(50)
        down_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        up_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.driver.quit()
        print(f"down: {down_speed}\nup: {up_speed}")

    def tweet_at_provider(self):
        self.driver.get(URL_TWITTER)
        login = self.driver.find_element(By.ID, )
        login.click()
        sleep(2)
        email_field = self.driver.find_element(By.ID, )
        email_field.send_keys(EMAIL)
        pass_field = self.driver.find_element(By.ID, )
        pass_field.send_keys(PASSWORD)
        pass_field.send_keys(Keys.ENTER)
        sleep(2)
        input_field = self.driver.find_element(By.ID, )
        input_field.send_keys(f"Hey Internet Provider, why is my internet speed {down_speed}down/{up_speed}up when I pay for 30down/5up?")



bot = InternetSpeedBot(DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()


#news_tags = soup.findAll("a", href=True)
#news = [tag.getText() for tag in news_tags]

#article_upvotes = [int(score.getText().split()[0]) for score in soup.findAll("span", class_="score")]

# with open("website.html") as file:
#     contents = file.read()
# soup = BeautifulSoup(contents, "html.parser")
# all_anchors = soup.findAll(name="a")
# print(all_anchors)
# for anchor in all_anchors:
#     print(anchor.get("href"))
