
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

def wait_for_object(self , type, string):
        return WebDriverWait(self.browser, 3).until(EC.presence_of_element_located((type,string)))

def wait_for_objects(self , type, string):
        return WebDriverWait(self.browser, 15).until(EC.presence_of_all_elements_located((type,string)))


def read_usernames(filename):
    with open(filename, 'r') as file:
        usernames = [line.strip() for line in file]
    return usernames

def chunk_users(usernames, chunk_size):
    return [usernames[i:i + chunk_size] for i in range(0, len(usernames), chunk_size)]

def login_instagram(driver, username, password):
    driver.get('https://www.instagram.com/accounts/login/')
    time.sleep(2)

    username_input = driver.find_element(By.NAME ,  'username')
    password_input = driver.find_element(By.NAME ,  'password')

    username_input.send_keys(username)
    time.sleep(2)
    password_input.send_keys(password)
    time.sleep(2)
    password_input.send_keys(Keys.RETURN)
    time.sleep(4)

def send_messages(driver, users):
    for user in users:
        driver.get(f'https://www.instagram.com/{user}/')
        time.sleep(4)

        
        #message_button = WebDriverWait.until(EC.presence_of_element_located(By.XPATH, "//button[text()='Message']"))
        message_button = driver.find_element(By.XPATH, "(//div[@role='button'][normalize-space()='Message'])[1]")
        #message_button = driver.find_element(By.XPATH, "//button[text()='Message']")
        message_button.click()
        time.sleep(8)

        message_input = driver.find_element(By.XPATH, "(//p[@class='xat24cr xdj266r'])[1]")
        message_input.send_keys("Testing....") # message here
        message_input.send_keys(Keys.RETURN)
        time.sleep(2)

def logout_instagram(driver):
    driver.get('https://www.instagram.com/accounts/logout/')
    time.sleep(2)

def main():
    usernames = read_usernames('usernames.txt')
    user_groups = chunk_users(usernames, 10)

    accounts = [
        {'username': 'ronak_boy_010', 'password': 'ronak@97852'},
        {'username': 'educationwave.in', 'password': 'name@97852'},
        # Add more accounts as needed
    ]

    driver = webdriver.Chrome()

    for i, users in enumerate(user_groups):
        account = accounts[i % len(accounts)]
        login_instagram(driver, account['username'], account['password'])
        send_messages(driver, users)
        logout_instagram(driver)

    driver.quit()

if __name__ == '__main__':
    main()