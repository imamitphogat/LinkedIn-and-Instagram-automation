
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
    time.sleep(4)

    username_input = driver.find_element(By.NAME ,  'username')
    password_input = driver.find_element(By.NAME ,  'password')

    username_input.send_keys(username)
    time.sleep(2)
    password_input.send_keys(password)
    time.sleep(2)
    password_input.send_keys(Keys.RETURN)
    time.sleep(4)
    try:         
        username_input = driver.find_element(By.NAME ,  'username')
        password_input = driver.find_element(By.NAME ,  'password')

        username_input.send_keys(username)
        time.sleep(4)
        password_input.send_keys(password)
        time.sleep(4)
        password_input.send_keys(Keys.RETURN)
        time.sleep(8)
    except:
         pass

def send_messages(driver, users):
    for user in users:

        driver.get('https://www.instagram.com/direct/inbox/')
        time.sleep(4)

        try:
            notnow_button = driver.find_element(By.CSS_SELECTOR, 'button._a9--._a9_1')
            notnow_button.click()
        except:
             pass
                    
        time.sleep(4)
        senduser = driver.find_element(By.CSS_SELECTOR, "svg[aria-label$='Search']")
        senduser.click()
        time.sleep(4)
        search_user = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
        search_user.click()
        search_user.send_keys(f"{user}")
        time.sleep(5)
        select_user = driver.find_element(By.XPATH, f"//a[@href='/{user}/']//div[@class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh xxbr6pl xbbxn1n xwib8y2 x1y1aw1k x1uhb9sk x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1']//div[@class='x9f619 x1n2onr6 x1ja2u2z x1qjc9v5 x78zum5 xdt5ytf x1iyjqo2 xl56j7k xeuugli']//div[@class='x9f619 x1n2onr6 x1ja2u2z x78zum5 x2lah0s x1qughib x6s0dn4 xozqiw3 x1q0g3np']//div[@class='x9f619 x1n2onr6 x1ja2u2z x78zum5 x1iyjqo2 xs83m0k xeuugli x1qughib x6s0dn4 x1a02dak x1q0g3np xdl72j9']//div[@class='x9f619 x1n2onr6 x1ja2u2z x78zum5 xdt5ytf x2lah0s x193iq5w xeuugli x1iyjqo2']//div[@class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1uhb9sk x1plvlek xryxfnj x1iyjqo2 x2lwn1j xeuugli xdt5ytf xqjyukv x1cy8zhl x1oa3qoh x1nhvcw1']")
        select_user.click()
        time.sleep(10)
        message_user = driver.find_element(By.XPATH, "//div[contains(text(),'Message')]")
        message_user.click()
        
        time.sleep(4)

        message_input = driver.find_element(By.XPATH, "(//p[@class='xat24cr xdj266r'])[1]")
        time.sleep(4)
        message_input.send_keys("BigFan....") # message here
        message_input.send_keys(Keys.RETURN)
        time.sleep(4)

def logout_instagram(driver):
    driver.get('https://www.instagram.com/accounts/logout/')
    time.sleep(2)

def main():
    usernames = read_usernames('usernames.txt')
    user_groups = chunk_users(usernames, 10)

    accounts = [
        {'username': '#id name', 'password': '#yopur password'},
        {'username': '#id name', 'password': '#your password'},
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
