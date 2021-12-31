from untitled import Ui_MainWindow
from paho.mqtt import client as mqtt
import random
from PySide2 import QtWidgets
from PySide2.QtWidgets import QMainWindow
from PySide2.QtWidgets import *
from PySide2.QtCore import QTimer,QDateTime
import sys

MQTTHOST = "127.0.0.1"
MQTTPORT = 1883
mqttClient = mqtt.Client()
hum = ""
temp = ""
doorState  =""
lightState = ""
loginDataDict = {"test":"test"}
# 连接MQTT服务器
def on_mqtt_connect():
    mqttClient.connect(MQTTHOST, MQTTPORT, 60)
    mqttClient.loop_start()


# publish 消息
def on_publish(topic, payload, qos):
    mqttClient.publish(topic, payload, qos)

# 消息处理函数
def on_message_come(lient, userdata, msg):
    global hum, temp,lightState,doorState
    if msg.topic == "test_topic":
        msgNow = msg.payload.decode('utf-8')
        try:

            hum = msgNow[0:2]
            temp = msgNow[2:4]
            lightState = msgNow[4]
            #print(hum)
        except:
            pass
        #print(msgNow)
    elif msg.topic == "data":
        doorState = msg.payload.decode('utf-8')
        print(doorState)
    elif msg.topic =="login_topic":
        loginData = msg.payload.decode('utf-8')

        if ";" in loginData:
            listLogin = loginData.split(";")
            for key, value in loginDataDict.items():
                if listLogin[0]==key and listLogin[1]==value:
                    on_publish("loginPass","loginSuc",0)

                    print("login")
                    return
            print(listLogin)
            on_publish("loginPass", "loginFail", 0)
        if "," in loginData:
            listLogin = loginData.split(",")
            loginDataDict[listLogin[0]] = listLogin[1]
            print(loginDataDict)

    #print(msg.topic + " " + ":" + msg.payload.decode('utf-8'))


# subscribe 消息
def on_subscribe():
    mqttClient.subscribe("data", 0)
    mqttClient.subscribe("test_topic", 0)
    mqttClient.subscribe("login_topic", 0)
    mqttClient.on_message = on_message_come # 消息到来处理函数


def mainMQTT():
    on_mqtt_connect()
    on_publish("data", "qq", 0)
    on_subscribe()


class mainWinLogic(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(mainWinLogic, self).__init__()
        self.setupUi(self)
        self.initMQTT()
        self.initTimer()
    def showData(self):
        self.label_door.setText(doorState)
        self.label_hum.setText(hum)
        self.label_light.setText(lightState)
        self.label_temp.setText(temp)
    def initTimer(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showData)  # 这里调用不能有函数括号，不是单纯的运行函数

        # 设置时间间隔并启动定时器
        self.timer.start(1000)
    def initMQTT(self):
        mainMQTT()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = mainWinLogic()
    win.show()

    sys.exit(app.exec_())
