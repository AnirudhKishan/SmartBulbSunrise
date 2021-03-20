import getopt, sys

from time import sleep

from tuyaha import TuyaApi

from ConfigurationReader import ConfigurationReader


DEBUG = False
confFile = "conf.json"
opts, args = getopt.getopt(sys.argv[1:], "c:d")
for opt, arg in opts:
    if opt == '-d':
        DEBUG = True
    elif opt == '-c':
        confFile = arg
        
conf = ConfigurationReader.Read(confFile)

username = conf["username"]
password = conf["password"]
countryCode = conf["country_code"]
deviceId = conf["device_id"]

api = TuyaApi()

api.init(username, password, countryCode)

device = api.get_device_by_id(deviceId)

device.set_brightness(10)
device.set_color_temp(2700)

delay = 5
step = 1

if DEBUG == True:
    delay = 1
    step = 20

for brightness in range(11, 255, step):
    device.set_brightness(brightness)
    sleep(delay)
    

device.set_brightness(255)
device.set_color_temp(10000)

