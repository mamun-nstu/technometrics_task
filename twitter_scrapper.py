from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
from time import sleep

# PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome()

driver.get("https://twitter.com/bbcbangla")

###############################################################################################
def twitter_scrapper(number):
    for i in range(number):
        try:
            post_time = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, "//time"))
            ).get_attribute('datetime')
            post = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, ".//div[@data-testid='tweetText']"))
            ).text
            no_of_comments = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, ".//div[@data-testid='reply']"))
            ).text
            no_of_retweets = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, ".//div[@data-testid='retweet']"))
            ).text
            no_of_likes = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, ".//div[@data-testid='like']"))
            ).text
        except:
            driver.quit()

        tweets.append({
            "Post Time": post_time,
            "Post Text": post,
            "No. of Comments": no_of_comments,
            "No. of Retweets": no_of_retweets,
            "No. of Likes": no_of_likes
        })
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        sleep(1)
###############################################################################################


tweets = []
num_of_tweets = int(input("Number of Tweets required: "))

twitter_scrapper(num_of_tweets)

with open('DATA.json', 'w', encoding='utf8') as json_file:
    json.dump(tweets, json_file, ensure_ascii=False)


driver.quit()