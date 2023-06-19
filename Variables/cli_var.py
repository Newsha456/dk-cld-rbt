
import    random 
import    string 
def generate_random_string(length):
    letters = string.ascii_letters  # Contains both uppercase and lowercase letters
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string

# String variables
G1_TYPE =                   "g1.micro"
UBUNTU_IMG =                "Ubuntu_20.04_LTS"   
LOGIN =                     "digicloud account login --email newsha.amiri@digikala.com --password Newsh@@4560 --debug"
LOGOUT =                    "digicloud account logout "
INS_NAME =                  generate_random_string(6).lower()
CREATE_INSTANCE =           f"digicloud instance create {INS_NAME} --simple --instance-type {G1_TYPE} --image {UBUNTU_IMG}"
SHOW_INSTANCE =             f"digicloud instance show {INS_NAME}"
DELETE_INSTANCE =           f"digicloud instance delete {INS_NAME} --i-am-sure --delete-root-volume"
INSTANCE_LIST =             "digicloud instance list "   









