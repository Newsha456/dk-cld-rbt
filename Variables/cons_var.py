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
GOT_IT_BTN =                " Got it "
HOME_PAGE =                 "//*[@id='app']/div[2]/main/div[2]/div[1]"
SERVICE_DROPDOWN =          "//*[@id='app']/div[2]/header/nav/div/div[2]/div[1]/div[1]"
REGION_SELECTOR =           "class=dropdown__toggle region-selection__toggle"
REGION_NAME =               " ir-vanak-plaza "
DROPDOWN_DESCRIPTION =      "class='header__services-dropdown-menu-intro text-center'"
CLOUD_COMPUTING =           "//*[@id='app]/div[2]/header/nav/div/div[2]/div[1]/div[2]/ul/li[1]/span[1]"
INS_LIST_PG =               "class=instances-list"
ADD_INS =                   "Add Instance" 
CREATE_STEP_ONE =           "Server Specifications"
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