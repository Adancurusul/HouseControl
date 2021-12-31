import machine, neopixel
import time
import dht
from machine import Timer
from machine import I2C, Pin
from ssd1306 import SSD1306_I2C
from machine import Pin
from machine import I2C, Pin, Timer, UART, PWM
import time
import machine
import network
from umqtt.simple import MQTTClient
import ujson
import machine
import webrepl
import random

SERVER = '192.168.43.227'
CLIENT_ID = b"esp32" + str(random.randint(0, 300))
USER = b'21' + str(random.randint(0, 300))
PWD = b'oxudFWl71'
TOPIC = b'test_topic'
TOPIC_DATA = b'data'
client = MQTTClient(CLIENT_ID, SERVER, 1883, USER, PWD)
globalDataDoor = "close"
sensor = dht.DHT11(Pin(13))
tim13 = Timer(13)
tim2 = Timer(2)


def disconnect():
    '''
    断开网络连接
    :return:  None
    '''
    sta_if = network.WLAN(network.STA_IF)
    if sta_if.isconnected():
        sta_if.disconnect()
        print('the network had been disconnect')


def do_connect(essid, password):
    '''
    根据给定的eddid和password连接wifi
    :param essid:  wifi essid
    :param password:  password
    :return:  None
    '''
    if essid == None or essid == '':
        raise BaseException('essid can not be null')
    if password == None or password == '':
        raise BaseException('password can not be null')
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.active():
        print("set sta active")
        sta_if.active(True)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.connect(essid, password)
        retry_times = 30
        while not sta_if.isconnected() and retry_times > 0:
            print(" wait a moment i will try %s items,please" % retry_times)
            time.sleep(2)
            retry_times -= 1
    print('network config:', sta_if.ifconfig())
    IP_ADRESS = sta_if.ifconfig()
    print(IP_ADRESS)
    print(type(IP_ADRESS))


def mqtt_upload(t):
    hum_ = (sensor.humidity())  # ????????????
    temp_ = (sensor.temperature())
    sendSTR = str(hum_) + str(temp_) + str(pinIN.value())
    client.publish(TOPIC, sendSTR)

    # global startState


stepTimeList = [0, 0, 0]


def sub_(topic, message):
    global globalDataDoor
    st = message.decode('utf-8')
    # print(st)
    if (st == "open"):
        globalDataDoor = st
    elif st == "close":
        globalDataDoor = st


def init_first():
    do_connect("nova 7 Pro 5G", "313115249")

    client.connect()
    client.set_callback(sub_)
    client.subscribe(TOPIC_DATA)

    # client.publish(TOPIC, "WATTCH1 connected")
    timer = Timer(1)
    timer.init(period=2000, mode=Timer.PERIODIC, callback=mqtt_upload)

    print("finish init")


def timer13_tick(_):
    # try:
    # sensor.measure()
    # time.sleep(0.5)
    pass
    # except:
    # print("e")


counterTimer = 0


def timer2_tick(_):
    global counterTimer
    hum_ = (sensor.humidity())  # ????????????
    temp_ = (sensor.temperature())
    if pinIN.value() == 1:
        # print("l0")
        strT = "on "
    else:
        strT = "off"
    # print(hum_)
    oled.fill(0)
    counterTimer = 1
    oled.text("temp:", 0, 0)
    oled.text("hum:", 0, 10)
    oled.text("light:", 0, 20)
    oled.text(str(hum_), 50, 10)
    oled.text(str(temp_), 50, 0)
    oled.text(strT, 50, 20)
    oled.text("doorState:", 0, 40)
    oled.text(globalDataDoor, 80, 50)
    oled.show()


try:
    sensor.measure()
    time.sleep(2.5)
    temp_ = (sensor.temperature())  # ??????measure()????????????????????????
    hum_ = (sensor.humidity())  # ????????????
except:
    hum_ = 50
    temp_ = 50


# print("temp now is : "+str(temp_)+" degree")
# print("humidity now is: "+str(hum_)+" %")
def ledON():
    for eachLed in range(0, n):
        np[eachLed] = (254, 254, 50)
        np.write()


def ledOFF():
    for eachLed in range(0, n):
        np[eachLed] = (0, 0, 0)
        np.write()


if __name__ == '__main__':
    n = 8
    # strip control gpio
    p = 14
    pinWater = Pin(14, Pin.OUT)
    pinWater.value(1)

    i2c = I2C(scl=Pin(4), sda=Pin(5), freq=10000)  # ??????I2C
    oled = SSD1306_I2C(128, 64, i2c)  # ??????oled??????
    oled.text("temp:", 0, 0)
    oled.text("hum:", 0, 10)
    oled.text("light:", 0, 20)
    oled.show()

    np = neopixel.NeoPixel(machine.Pin(p), n)
    pinIN = machine.Pin(27, machine.Pin.IN)

    tim13.init(period=1000, mode=Timer.PERIODIC, callback=timer13_tick)
    tim2.init(period=1500, mode=Timer.PERIODIC, callback=timer2_tick)

    waterStateNow = 0

    init_first()
    while True:
        sensor.measure()
        time.sleep(0.5)
        client.check_msg()
# client.wait_msg()
'''
while 1:
    try:
        sensor.measure()
        time.sleep(1)
        hum_ = (sensor.humidity())# ????????????
        temp_ = (sensor.temperature())
    except:
        pass

    #print("h"+str(hum_))
    #print("t "+str(temp_))
    if pinIN.value() ==1:
        #print("l0")
        pass
    else:
        pass
        #print("l1")
'''