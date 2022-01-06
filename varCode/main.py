'''
@Filename    :main.py
@Description :pyqt
@Author      :delay-n-days
@version     :1.0
@Date        :2022/01/04 15:13:47
'''

import sys
from PySide2.QtWidgets import QDial
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtSerialPort import QSerialPort, QSerialPortInfo
from PySide2.QtWidgets import QStyleFactory
# from PySide2.QtWidgets import QCheckBox
from Ui_main import Ui_MainWindow
import re
import baidu_fanyi_api
import json


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        # 初始化继承的父类（QMainWindow）
        super(Main, self).__init__(parent)
        self.ui = Ui_MainWindow()  # 创建UI对象
        self.setupUi(self)  # 构造UI
        # 设置信号与槽
        self.radioButton.setChecked(True)
        self.jsontoTextEdit()
        self.CreateSignalSlot()
        self.resize(1000, 700)

    # 设置信号与槽
    def CreateSignalSlot(self):
        self.pushButton_2.clicked.connect(self.transltor) 
        self.pushButton_3.clicked.connect(self.conversion)  
        self.pushButton_4.clicked.connect(self.TransltorAndConversion)  

    # 使用收费Api
    # def transltor(self):
    #     str2 = ""
    #     str1 = self.textEdit_3.toPlainText()
    #     Arr = baidu_fanyi_api.transUseMyapi(str1)
    #     for str in Arr:
    #         str2 += str['dst']+"\n"
    #     self.textEdit_4.setText(str2)

    # 使用免费费Api
    def transltor(self):
        str2 = ""
        str1 = self.textEdit_3.toPlainText()
        srcArrstr = str1.split("\n")
        for srcStr in srcArrstr:
            dst = baidu_fanyi_api.trans(srcStr)
            str2 += dst + "\n"
        self.textEdit_4.setText(str2)

    # 把输入框中的数据保存到配置文件中
    def textEdittoJson(self):
        conversion = []
        savedata = {"conversion": conversion}
        ArrEditText1 = self.textEdit_5.toPlainText().split("\n")
        ArrEditText2 = self.textEdit_6.toPlainText().split("\n")
        for i in range(len(ArrEditText1)):
            ll = {}
            ll['src'] = ArrEditText1[i]
            ll['dst'] = ArrEditText2[i]
            conversion.append(ll)
        savedata["conversion"] = conversion
        with open("./conf.json", "w") as f:
            json.dump(savedata, f, indent=4)

    # 驼峰命名法
    def tuofeng(self, str1):
        Arrstr = str1.split("\n")
        a = ""
        for str in Arrstr:
            ArrS = str.split(" ")
            for s in ArrS:
                s = s.capitalize()
                a += s
            a += "\n"
        return a

    # 通过替换规则替换后,并使用选定的命名方法命名
    def conversion(self):
        self.textEdittoJson()
        str1 = self.textEdit_4.toPlainText()
        with open("./conf.json", "r") as f:
            arr3 = json.load(f)
            for arr in arr3['conversion']:
                str1 = str1.replace(str(arr['src']), str(arr['dst']))
        if self.radioButton.isChecked() is True:  # 驼峰命名法
            str1 = self.tuofeng(str1)
        if self.radioButton_2.isChecked() is True:  # 下划线命名法
            while '  ' in str1:
                str1 = str1.replace('  ', ' ')
            str1 = str1.replace(" ", "_").casefold()
        self.textEdit_7.setText(str1)

    # 把配置文件里的json转移到输入框中
    def jsontoTextEdit(self):
        EditText1 = ""
        EditText2 = ""
        with open("./conf.json", "r") as f:
            arr3 = json.load(f)
            for arr in arr3['conversion']:
                EditText1 += str(arr['src']) + "\n"
                EditText2 += str(arr['dst']) + "\n"
        self.textEdit_5.setText(EditText1)
        self.textEdit_6.setText(EditText2)

    def TransltorAndConversion(self):
        self.transltor()
        self.conversion()


class HtextExec():
    def __init__(self, strr, parent=None):
        try:
            Arr = strr.split("//")
            Arr2 = Arr[0].split(" ")
            self.varName = Arr2[0]
            self.bitLength = Arr2[1]
            self.explain = Arr[1]
        except:
            self.varName = " "
            self.bitLength = "0"
            self.explain = " "

    def printt(self):
        return "unsigned " + self.varName + ": " + self.bitLength + "; " + "// " + self.explain + "\n"


if __name__ == '__main__':
    # 每一个pyside2程序中都需要有一个QApplication对象，sys.argv是一个命令行参数列表
    app = QApplication(sys.argv)
    # 设置主题
    app.setStyle(QStyleFactory.create('fusion'))
    # 实例化窗口
    window = Main()
    # 起名字
    window.setWindowTitle('varCode')
    # # 做图标
    # window.setWindowIcon(QIcon('logo.ico'))
    # 紧致拉伸窗口大小
    # window.setCentralWidget(window.centralwidget)
    # window.setFixedSize(window.width(), window.height())
    # 窗口显示
    window.show()
    # 进入程序的主循环，遇到退出情况，终止程序
    sys.exit(app.exec_())
