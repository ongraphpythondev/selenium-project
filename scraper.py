from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def scraper(username, password):
    driver = webdriver.Firefox(executable_path='< driver's path >')
    # give here firefox path where it is installed
    driver.get("https://www.instagram.com")
    driver.implicitly_wait(30)
    driver.find_element_by_name("username").send_keys(username)
    driver.implicitly_wait(30)
    driver.find_element_by_name("password").send_keys(password)
    driver.implicitly_wait(30)
    driver.find_element_by_name('password').send_keys(Keys.ENTER)
    driver.implicitly_wait(30)
    driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()
    driver.implicitly_wait(30)
    driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()
    driver.save_screenshot("screenshot.png")


if __name__ == "__main__":
    username = input("Enter your instagram username :\n")
    password = input("Enter your instagram password:\n")
    scraper(username, password)
