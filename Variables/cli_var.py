
import    random 
import    string 
def generate_random_string(length):
    letters = string.ascii_letters  # Contains both uppercase and lowercase letters
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string

# String variables
G1_MICRO_TYPE =             "g1.micro"
UBUNTU_IMG =                "Ubuntu_20.04_LTS"   
LOGIN =                     "digicloud account login --email newsha.amiri@digikala.com --password Newsh@@4560 --debug"
LOGOUT =                    "digicloud account logout"
INS_NAME =                  generate_random_string(6).lower()
NET_NAME =                  generate_random_string(3).lower()
ROUTER_NAME =               generate_random_string(4).lower()
G1_M_TYPE =                 "g1.medium"
CREATE_INSTANCE =           f"digicloud instance create {INS_NAME} --simple --instance-type {G1_M_TYPE} --image {UBUNTU_IMG}"
SHOW_INSTANCE =             f"digicloud instance show {INS_NAME}"
DELETE_INSTANCE =           f"digicloud instance delete {INS_NAME} --i-am-sure --delete-root-volume"
INSTANCE_LIST =             "digicloud instance list "   
CREATE_NETWORK =            f"digicloud network create {NET_NAME}"
NET_LIST =                  "digicloud network list"
NET_DETAILS =               f"digicloud network show {NET_NAME}"
ADMIN_S_UP =                "UP"
ADMIN_S_DWN =               "DOWN"
NETWORK_NAME_UPDATE =       "new-name"
NET_UPDATE =                f"digicloud network update {NET_NAME} --name {NETWORK_NAME_UPDATE} --admin-state {ADMIN_S_UP}"
CREATE_ROUTER =             f"digicloud router create {ROUTER_NAME} --admin-state {ADMIN_S_UP}"



