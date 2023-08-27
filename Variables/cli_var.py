# from    robot   import run_cli
import      random
import      subprocess
import      string 
def generate_random_string(length):
    letters = string.ascii_letters  # Contains both uppercase and lowercase letters
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string




# String variables
#instance type variables
G1_MICRO =                  "g1.micro" 
G1_MEDIUM =                 "g1.medium"
C1_XLARGE =                 "c1.xlarge"
G1_LARGE =                  "g1.large"
G1_XLARGE =                 "g1.xlarge"
C1_SMALL =                  "c1.small"
INSTANCE_TYPES =            [G1_MICRO, G1_MEDIUM, C1_SMALL, C1_XLARGE, G1_LARGE ,G1_XLARGE]
random_index =              random.randint(0, 5)
chosen_instance_t =         INSTANCE_TYPES[random_index]

#image type variables
UBUNTU22_IMG =              "Ubuntu_22.04_LTS_LVM"   
FEDORA2 =                   "fedora-coreos-35-custom2"            
PFS26 =                     "pfSense-26"                          
ROCKY_LVM =                 "Rocky8_LVM"                         
CENTOS9_LVM =               "Centos9_stream_LVM"                  
DEBIAN11_LVM =              "Debian11_LVM"                                             
WINDOWS2022 =               "Windows_Server_2022_datacenter_core" 
CIROSS =                    "Cirros"                              
IMAGE_TYPES =               [UBUNTU22_IMG, FEDORA2, PFS26, ROCKY_LVM, CENTOS9_LVM ,DEBIAN11_LVM ,WINDOWS2022, CIROSS]
random_index =              random.randint(0, 7)
chosen_image =              IMAGE_TYPES[random_index]

LOGIN =                     "digicloud account login --email newsha.amiri@digikala.com --password Newsha1234! --debug"
LOGOUT =                    "digicloud account logout"
INS_NAME =                  generate_random_string(6).lower()
NET_NAME =                  generate_random_string(3).lower()
ROUTER_NAME =               generate_random_string(4).lower()
SG_NAME =                   generate_random_string(4).lower()
CREATE_INSTANCE =           f"digicloud instance create {INS_NAME} --network newsha --instance-type {chosen_instance_t} --image {chosen_image}"
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

# server group variables

def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def INS_CREATEs(chosen_sg_t):
    INS_NAME = generate_random_string(4)
    INS_CREATE = f"digicloud instance create {INS_NAME} --network newsha --instance-type {chosen_instance_t} --image {chosen_image}"
    return INS_CREATE , INS_NAME

def SG_CREATEs(chosen_sg_t):
    SG_NAME = generate_random_string(4)
    SG_CREATE = f"digicloud server group create {SG_NAME} --policy {chosen_sg_t}"
    return SG_CREATE , SG_NAME

def SG_DEL(SG_NAME):
    SG_DELETE= f"digicloud server group delete {SG_NAME} --i-am-sure"
    return SG_DELETE

AFFINITY =                  "AFFINITY"
ANTI_AFFINITY =             "ANTI_AFFINITY"
S_AFFINITY =                "SOFT_AFFINITY"
SOFT_ANTI_AFFINITY =        "SOFT_ANTI_AFFINITY"
SERVER_GROUPS_TYPE =        [AFFINITY, ANTI_AFFINITY, S_AFFINITY, SOFT_ANTI_AFFINITY]
random_index =              random.randint(0, 3)
chosen_sg_t =               SERVER_GROUPS_TYPE[random_index]
RULES_ANTI_A =              "--rules max_server_per_host=1"
SG_CREATE =                 SG_CREATEs(chosen_sg_t)
SG_SHOW =                   f"digicloud server group show {SG_NAME}"
SG_LIST =                   "digicloud sever group list"
CRT_INS_W_SG =              f"digicloud instance create {INS_NAME} --simple --instance-type {chosen_instance_t} --image {chosen_image} --server-group {chosen_sg_t}"
SG_QOUTA_ERROR =            "You don't have enough quota. number of server groups allowed per namespace is 10 but you used 11"
INS_SG_QOUTA_ERROR =            "You don't have enough quota. number of members allowed per server group is 5 but you used 6."
ANTI_A_CREATE_SG =          f"digicloud server group create {SG_NAME} --policy {ANTI_AFFINITY}"
