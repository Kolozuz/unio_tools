from selenium import webdriver
from selenium.webdriver.common.by import By

from sgps import webPage

def main():
    myPage = webPage("https://www.seti.co/gpsweb/")
    myPage.login("", "")

if __name__ == '__main__':
    print("Starting...")
    main()