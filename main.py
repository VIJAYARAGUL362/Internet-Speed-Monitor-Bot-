from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os,time

load_dotenv()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")

chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
PROMISED_UP = 150
PROMISED_DOWN = 30
URL = "https://www.speedtest.net/"

CHROME_DRIVER_PATH = "C:/Users/Hi/Downloads/chromedriver-win64/chromedriver-win64"
MASTERDON_EMAIL = os.environ.get('MASTERDON_ACCOUNT_EMAIL')
MASTERDON_API_KEY = os.environ.get('MASTERDON_ACCOUNT_PASSWORD')


class InternetSpeedTwitterBot:
    def __init__(self,up_speed:int,down_speed:int):
        self.driver  = webdriver.Chrome(options = chrome_options)
        self.promised_up_speed = up_speed
        self.promised_down_speed = down_speed
        self.real_up_speed = 0
        self.real_down_speed = 0
        self.wait = WebDriverWait(self.driver,10)


    def get_internet_speed(self):
        """
        clicks the go button in the browser and get the upload and
        :return:
        None
        """
        try:
            go_button = self.driver.find_element(By.CLASS_NAME,"js-start-test")
            go_button.click()
            print("button is clicked")
        except NoSuchElementException:
            print("Go button not found")
            return

        # GETTING UPLOAD SPEED
        try:
            up_speed_element = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"upload-speed")))
            while True:
                up_speed_status = up_speed_element.get_attribute('data-upload-status-value')
                print(up_speed_status)
                if up_speed_status != "NaN":
                    self.real_up_speed = up_speed_element.text
                    break
            print(up_speed_element.text)
        except NoSuchElementException:
            print("No upload speed")

        time.sleep(1)
        # GETTING DOWNLOAD SPEED
        try:
            download_speed_element = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'download-speed')))
            while True:
                download_status = download_speed_element.get_attribute('data-download-status-value')
                if download_status != "NaN":
                    self.real_down_speed = download_speed_element.text
                    break
        except NoSuchElementException:
            print('Download speed not found')


    def post_on_masterdon(self):
        """
        posts the upload and download speed of the internet on the masterdon
        :return:
        """
        # POST IN MASTERDON
        post = (f"Hey airtel internet provider, why is my network speed is {self.real_up_speed} Mbps and"
                f" download speed is {self.real_down_speed} Mbps. But i pay for 40 Mbps for upload and 40 Mbps for download speed.")

        # OPENING THE masterdon PAGE
        self.driver.get("https://mastodon.social/explore")

        # LOGIN BUTTON
        try:
            login_button = self.driver.find_element(By.CLASS_NAME,"button-secondary")
            login_button.click()

        # ENTERING EMAIL ADDRESS

            email_input_box = self.driver.find_element(By.ID,"user_email")
            email_input_box.send_keys(MASTERDON_EMAIL)

        # ENTERING EMAIL PASSWORD
            email_password_input_box = self.driver.find_element(By.ID,"user_password")
            email_password_input_box.send_keys(MASTERDON_API_KEY)

        # LOGIN BUTTON
            logging_button = self.driver.find_element(By.CLASS_NAME,'btn')
            logging_button.click()

        except NoSuchElementException:
            print('already logged in')

        # INSERTING THE TEXT
        text_area = self.driver.find_element(By.CLASS_NAME,'autosuggest-textarea__textarea')
        text_area.send_keys(post)

        # POSTING THE POST
        post_button  = self.driver.find_element(By.CLASS_NAME,'button--compact')
        post_button.click()

internet_speed_test = InternetSpeedTwitterBot(PROMISED_UP,PROMISED_DOWN)

# OPENING THE WEBPAGE
internet_speed_test.driver.get(URL)

# CHECKING FOR THE COOKIES IN THE WEB PAGE
try:
    cookie_button = internet_speed_test.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Continue')]")))
    cookie_button.click()
    print("button is clicked")
except:
    print("cookie button is not found")

# GETTING THE INTERNET SPEED
internet_speed_test.get_internet_speed()

print(f"upload speed: {internet_speed_test.real_up_speed}")
print(f"download speed: {internet_speed_test.real_down_speed}")

# POSTING THE SPEED ON MASTERDON
internet_speed_test.post_on_masterdon()
