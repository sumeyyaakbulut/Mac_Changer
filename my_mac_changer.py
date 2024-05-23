import subprocess
import optparse
import re

def get_user_input():

    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--interface", dest ="interface", help= "interface to changer")
    parse_object.add_option("-m", "--mac", dest="mac_address", help ="new mac address")

    return parse_object.parse_args()


def mac_changer_address(user_interface, user_mac_addres):

    subprocess.call(["ifconfig", user_interface, "down"])
    subprocess.call(["ifconfig",user_interface,"hw","ether",user_mac_addres])
    subprocess.call(["ifconfig",user_interface,"up"])

def control_new_mac(interface):
    ifconfig = subprocess.check_output(["ifconfig",interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig.decode("utf-8"))

    if new_mac:
        return new_mac.group(0)
    else:
        return None

print("my mac changer started")
(user_input,arguments) = get_user_input()
mac_changer_address(user_input.interface, user_input.mac_address)
finalized_mac = control_new_mac(user_input.interface)

if finalized_mac == user_input.mac_address:
    print("Success")
else:
    print("Error")