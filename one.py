
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

#element = WebDriverWait(driver, 10).until
#EC.presence_of_element_located((By.ID, "myDynamicElement"))

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
        time.sleep(2)

        
        message_button = driver.find_element(By.XPATH, "//button[text()='Message']")
        message_button.click()
        time.sleep(2)

        message_input = driver.find_element(By.XPATH, "//textarea")
        message_input.send_keys("Texxttt") # message here
        message_input.send_keys(Keys.RETURN)
        time.sleep(2)

def logout_instagram(driver):
    driver.get('https://www.instagram.com/accounts/logout/')
    time.sleep(2)

def main():
    usernames = read_usernames('usernames.txt')
    user_groups = chunk_users(usernames, 2)

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