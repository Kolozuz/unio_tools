from selenium import webdriver
from selenium.webdriver.common.by import By

class webPage(object):
    """
    Instantiates a new webpage, with a given url parameter
    """
    browser = webdriver.Chrome()

    def __init__(self, url):
        self.url = url
        self.browser.get(url)
        self.browser.implicitly_wait(3)
        
    def login(self, user_name = "", user_password = ""):
        """
        Takes username and password parameters to sign in and returns a success message,
        if no parameters are given it asks for them in console

        Args:
            user_name (str): user name.
            user_password (str): password.

        Returns:
            str: result message.
        """

        print("Signing In...")

        #form = self.browser.find_element(By.XPATH,"/html[1]/body[1]/form[1]")
        user_name_input = self.browser.find_element(By.XPATH,"//input[@id='j_idt7:usuario']")
        user_password_input = self.browser.find_element(By.XPATH, "//input[@id='j_idt7:password']")
        submit_btn = self.browser.find_element(By.XPATH,"//button[@id='j_idt7:btnIngresar']")

        def checkCredentials(user_name = "", user_password = "") :

            while not user_name or not user_password : 
                user_name = input("Type your Username \n")
                user_password = input("Type your Password \n")
                user_name_input.clear()
                user_password_input.clear()
                user_name_input.send_keys(user_name)
                user_password_input.send_keys(user_password)
                submit_btn.click()
                #form.submit()
                
                homePage = self.browser.find_elements(By.XPATH, "//div[@class='landing']")

                if len(homePage) == 0 : # While error message is present
                    errorMessage = self.browser.find_element(By.CLASS_NAME, "ui-growl-message").text
                    #errorMsg = 
                    print(errorMessage)
                    print("Wrong Username or Password! Try Again")
                    user_name = ""
                    user_password = ""
                else:
                    print("si")

        print("Success!")

        checkCredentials(user_name, user_password)