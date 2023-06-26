from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-popup-blocking")
options.add_argument("--window-size=1920x1080")  # Adjust the window size as needed
options.add_argument("--disable-notifications")
options.add_argument("--headless")  # Run Chrome in headless mode for recording

# Enable video recording by providing a directory to save the video file
options.add_argument("--remote-debugging-port=9222")  # Make sure to have a free port available
options.add_argument("--remote-debugging-address=0.0.0.0")  # Allow remote debugging
options.add_argument("--autoplay-policy=no-user-gesture-required")  # Prevent Chrome from pausing the video

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

driver = webdriver.Chrome(options=options)



import    random 
import    string 
def generate_random_string(length):
    letters = string.ascii_letters  # Contains both uppercase and lowercase letters
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string

DIGI_CLOUD_URL  =           "https://console.digicloud.dev/"
CHROME =                    "Chrome"
LOGIN_PG =                  "class=auth"
MAIL_INPUT_BOX =            "id:email"
MAIL_VALUE =                "newsha.amiri@digikala.com"
PASS_INPUT_BOX =            "id:password"
PASS_VALUE =                "Newsh@@4560"
LOGIN_BUTTON =              "//*[@id='app']/div[2]/div/main/div[2]/form/button"
INCREASE_POPUP =            "Price update notice"
# GOT_IT_BTN =                Got it 
HOME_PAGE =                 "//*[@id='app']/div[2]/main/div[2]/div[1]"
SERVICE_DROPDOWN =          "//*[@id='app']/div[2]/header/nav/div/div[2]/div[1]/div[1]"
REGION_SELECTOR =           "css:[dropdown__toggle region-selection__toggle]"
REGION_NAME =               " ir-vanak-plaza "
DROPDOWN_DESCRIPTION =      "//*[@id='app']/div[2]/header/nav/div/div[2]/div[1]/div[2]/div[2]"
CLOUD_COMPUTING =           "//*[@id='app']/div[2]/header/nav/div/div[2]/div[1]/div[2]/ul/li[1]"
INS_LIST_PG =               "class=instances-list"
ADD_INS =                   "//*[@id='app']/div[2]/main/div[2]/div/div[1]/div[3]/a" 
CREATE_STEP_ONE =           "css:[value=ir-vanak-plaza]"
CONFIRM_BTN =               " Confirm and Continue  "
ADVANCE_STNG =              "class=h2_4de9b95f4acab1df1f60b1b927465bf4"
INS_NAME_INPUT =            "id:Servers Name"
INS_NAME =                  generate_random_string(6).lower()
IMAGE_TYPE_UBUNTU =         "Ubuntu"
INS_TYPE =                  " g1.medium "
CREATE_BTN =                "//*[@id='app']/div[2]/main/div[2]/div/div[2]/div/div[2]/div/div[3]/button"
CREATING_STATE =            "Creating"
INS_STNG =                  "//*[@id=app]/div[2]/main/div[2]/div/div[1]/div/div[2]/div/div[1]/div[1]/button"
DELETE_INS =                "Delete"
DELETE_INS_POPUP =          "//*[@id=app]/div[2]/main/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div[2]"      
ROOT_VOLUME_DELETE =        "class=deleteRootVolume"
DELETE_BTN =                "//*[@id=app]/div[2]/main/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/button[2]"
ACTIVE_STATUS =             "ACTIVE"
CREATE_SMP_INS =            "//*[@id='app']/div[2]/main/div[2]/div/div[2]/div/div[6]/div[5]/div[3]/div/button"