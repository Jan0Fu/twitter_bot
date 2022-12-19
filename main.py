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
        print(f"down: {down_speed}\nup: {up_speed}")

    def tweet_at_provider(self):
        self.driver.get(URL_TWITTER)

        sleep(2)
        email_field = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input' )
        pass_field = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')
        email_field.send_keys(EMAIL)
        pass_field.send_keys(PASSWORD)
        sleep(2)
        pass_field.send_keys(Keys.ENTER)
        sleep(4)

        input_field = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        tweet = f"Hey Internet Provider, why is my internet speed {down_speed}down/{up_speed}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        input_field.send_keys(tweet)
        sleep(3)
        tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()
        sleep(2)
        self.driver.quit()


bot = InternetSpeedBot(DRIVER_PATH)
bot.get_internet_speed()
if float(down_speed) < (PROMISED_DOWN - 2) or float(up_speed) < (PROMISED_UP - 0.5):
    bot.tweet_at_provider()


# news_tags = soup.findAll("a", href=True)
# news = [tag.getText() for tag in news_tags]
# article_upvotes = [int(score.getText().split()[0]) for score in soup.findAll("span", class_="score")]

# with open("website.html") as file:
#     contents = file.read()
# soup = BeautifulSoup(contents, "html.parser")
# all_anchors = soup.findAll(name="a")
# print(all_anchors)
# for anchor in all_anchors:
#     print(anchor.get("href"))
