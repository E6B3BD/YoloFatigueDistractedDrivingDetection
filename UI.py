
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QGroupBox, QGridLayout, QCheckBox, QLabel, QPushButton, QComboBox, QListWidget, QTextEdit, QWidget,QTextBrowser
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtCore import QSize
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from qfluentwidgets import PushButton
from qfluentwidgets import PillPushButton
from qfluentwidgets import SwitchButton
from qfluentwidgets import SplashScreen
from qframelesswindow import FramelessWindow, StandardTitleBar
from qframelesswindow import StandardTitleBar
import sys


# 设置图标路径，这里暂时未使用
COVER = 'images/i.jpg'


        


class FatigueDetecting(object):
    def setupUi(self, parent):
        
        # 设置窗口标题
        parent.setWindowTitle("检测系统  (基于python人脸识别行为检测提醒系统)")
        # 设置窗口的位置和大小，(100, 100) 是窗口左上角的坐标，873 是宽度，535 是高度
        parent.setGeometry(100, 100, 1000, 535)
        # 创建一个 QWidget 作为主窗口的中心部件
        parent.centralWidget = QWidget()
        # 将创建的 QWidget 设置为主窗口的中心部件
        parent.setCentralWidget(parent.centralWidget)
        # 创建一个垂直布局，用于放置视频显示和控制部分
        mainLayout = QVBoxLayout(parent.centralWidget)
        # 创建一个水平布局，用于放置视频显示部分
        videoLayout = QHBoxLayout()
        # 将视频显示布局添加到主布局中
        mainLayout.addLayout(videoLayout)

        # 创建一个 QLabel 用于显示视频
        parent.videoLabel = QLabel()
        # 设置 QLabel 的初始图片
        #parent.videoLabel.setPixmap(QPixmap(COVER))
        # 将视频显示标签添加到视频布局中，并设置其占用比例为 9
        videoLayout.addWidget(parent.videoLabel, 9)

        # 创建一个垂直布局，用于放置控制按钮等
        controlsLayout = QVBoxLayout()
        # 将控制布局添加到视频布局中，并设置其占用比例为 3
        videoLayout.addLayout(controlsLayout, 3)

        # 创建一个参数设置组
        paramGroup = QGroupBox("参数设置")
        # 将参数设置组添加到控制布局中
        controlsLayout.addWidget(paramGroup)
        # 为参数设置组创建一个垂直布局
        paramLayout = QVBoxLayout(paramGroup)

        # 创建一个视频源设置组
        videoSourceGroup = QGroupBox("视频源")
        # 将视频源设置组添加到参数布局中
        paramLayout.addWidget(videoSourceGroup)
        # 为视频源设置组创建一个网格布局
        videoSourceLayout = QGridLayout(videoSourceGroup)
        # 创建一个下拉框，用于选择摄像头
        parent.cameraChoice = QComboBox()
        # 添加摄像头选项
        parent.cameraChoice = PillPushButton("打开摄像头")
        parent.cameraChoice.setIcon(QIcon("images/to/shexiangtou.png"))
        # 创建三个按钮，用于控制视频的开始、打开文件和暂停
        parent.Turn_on_alerts = PillPushButton("对称占位")
        parent.openVideoButton = PillPushButton("对称占位")
        parent.pauseButton = PillPushButton("对称占位")
        # 将下拉框和按钮添加到视频源设置布局中
        videoSourceLayout.addWidget(parent.cameraChoice, 0, 0)
        videoSourceLayout.addWidget(parent.pauseButton, 0, 1)
        videoSourceLayout.addWidget(parent.openVideoButton, 1, 0)
        videoSourceLayout.addWidget(parent.Turn_on_alerts, 1, 1)
        #设置图标
        parent.pauseButton.setIcon(QIcon("images/to/shezhi.png"))
        parent.Turn_on_alerts.setIcon(QIcon("images/to/shezhi.png"))
        parent.openVideoButton.setIcon(QIcon("images/to/shezhi.png"))
        
        
       
        # 创建一个疲劳检测设置组
        fatigueGroup = QGroupBox("疲劳检测")
        # 将疲劳检测设置组添加到参数布局中
        paramLayout.addWidget(fatigueGroup)
        # 为疲劳检测设置组创建一个垂直布局
        
        fatigueLayout = QVBoxLayout(fatigueGroup)
        # 创建三个复选框，用于选择是否检测打哈欠、闭眼
        #parent.yawnCheckBox = QCheckBox("行为检测")
        #parent.yawnCheckBox.setChecked(True)
        #parent.blinkCheckBox = QCheckBox("疲劳检测")
        #parent.blinkCheckBox.setChecked(True)
        # 将复选框添加到疲劳检测布局中
        #fatigueLayout.addWidget(parent.yawnCheckBox)
        #fatigueLayout.addWidget(parent.blinkCheckBox)
        # 创建一个水平布局，用于设置疲劳时间
        
        fatigueTimeLayout = QHBoxLayout()
        fatigueTimeLayout.addWidget(QLabel("闭眼次数:"))
         #创建一个记录闭眼次数的文本控件
        parent.Close_your_eyes = QTextEdit()
        parent.Close_your_eyes.setMaximumSize(40,25)
        fatigueTimeLayout.addWidget(parent.Close_your_eyes)
        fatigueLayout.addLayout(fatigueTimeLayout)

        # 添加一个弹簧控件
        fatigueTimeLayout.addStretch()

        fatigueTimeLayout.addWidget(QLabel("哈欠次数:"))
         #创建一个记录哈欠次数的文本控件
        parent.yawn = QTextEdit()
        parent.yawn.setMaximumSize(40,25)
        fatigueTimeLayout.addWidget(parent.yawn)
        fatigueLayout.addLayout(fatigueTimeLayout)
       

        # 创建一个行为检测设置组
        absenceGroup = QGroupBox("行为检测")
        # 行为检测设置组添加到参数布局中
        paramLayout.addWidget(absenceGroup)

         # 为行为检测设置组创建一个网格布局
        Behavioral_grids = QGridLayout()
        absenceGroup.setLayout(Behavioral_grids)

        #设置一组水平布局
        Mobile_phone_level=QHBoxLayout()
        #将手机控件添加到水平控件中
        Mobile_phone_level.addWidget(QLabel("手机："))
        parent.cell_phone = QTextEdit()
        parent.cell_phone.setReadOnly(True)
        parent.cell_phone.setMinimumSize(70,25)
        parent.cell_phone.setMaximumSize(70,25)
        Mobile_phone_level.addWidget(parent.cell_phone)
        # 创建一个包含水平布局的小部件
        cell_phone_widget = QWidget()
        cell_phone_widget.setLayout(Mobile_phone_level)
        #将手机组放在网格布局中
        Behavioral_grids.addWidget(cell_phone_widget, 0, 0)

        #设置二组水平布局
        Drink_water_levels=QHBoxLayout()
         #将喝水控件添加到水平控件中
        Drink_water_levels.addWidget(QLabel("喝水："))
        parent.Drink = QTextEdit()
        parent.Drink.setReadOnly(True)
        parent.Drink.setMinimumSize(70,25)
        parent.Drink.setMaximumSize(70,25)
        Drink_water_levels.addWidget(parent.Drink)
        # 创建一个包含水平布局的小部件
        Drink_widget = QWidget()
        Drink_widget.setLayout(Drink_water_levels)
        #将二组放在网格布局中
        Behavioral_grids.addWidget(Drink_widget, 0, 1)

        #设置三组抽烟水平
        Smoking_level=QHBoxLayout()
         #将抽烟控件添加到水平控件中
        Smoking_level.addWidget(QLabel("抽烟："))
        parent.smoke = QTextEdit()
        parent.smoke.setReadOnly(True)
        parent.smoke.setMinimumSize(70,25)
        parent.smoke.setMaximumSize(70,25)
        Smoking_level.addWidget(parent.smoke)
        # 创建一个包含水平布局的小部件
        smoke_widget = QWidget()
        smoke_widget.setLayout(Smoking_level)
        #将三组放在网格布局中
        Behavioral_grids.addWidget(smoke_widget, 1, 0)

        #设置四组零食水平
        Snack_levels=QHBoxLayout()
         #将零食控件添加到水平控件中
        Snack_levels.addWidget(QLabel("对称占位"))
        parent.snacks = QTextEdit()
        parent.snacks.setText("")
        parent.snacks.setReadOnly(True)
        parent.snacks.setMinimumSize(70,25)
        parent.snacks.setMaximumSize(70,25)
        Snack_levels.addWidget(parent.snacks)
        # 创建一个包含水平布局的小部件
        snacks_widget = QWidget()
        snacks_widget.setLayout(Snack_levels)
        #将四组放在网格布局中
        Behavioral_grids.addWidget(snacks_widget, 1, 1)
        # 创建一个分析区域设置组
        analysisGroup = QGroupBox("分析区域")
        # 将分析区域设置组添加到参数布局中
        paramLayout.addWidget(analysisGroup)
        # 为分析区域设置组创建一个水平布局
        analysisLayout = QHBoxLayout(analysisGroup)
        analysisLayout.addWidget(QLabel("人员状态："))
        # 创建一个下拉框，用于选择检测区域
        parent.analysisChoice = QTextEdit()
        parent.analysisChoice.setReadOnly(True)
        parent.analysisChoice.setMinimumSize(180,25)
        parent.analysisChoice.setMaximumSize(180,25)
        analysisLayout.addWidget(parent.analysisChoice)
        #添加了一个弹簧
        analysisLayout.addStretch()

        # 创建一个状态输出组
        statusGroup = QGroupBox("状态输出")
        # 将状态输出组添加到参数布局中
        paramLayout.addWidget(statusGroup)
        # 为状态输出组创建一个垂直布局
        statusLayout = QVBoxLayout(statusGroup)
        # 创建一个文本编辑框，用于输出状态信息
        parent.statusText = QTextBrowser()
        parent.statusText.setReadOnly(True)
        parent.statusText.setMinimumSize(180,200)
        statusLayout.addWidget(parent.statusText)

        # 设置窗口图标
        parent.setWindowIcon(QIcon('images/icon.ico'))
        # 输出初始化完成的信息
        print("PySide2界面初始化加载完成！")

        # 消息框显示函数
        # 定义一个名为 'printf' 的方法，用于在文本浏览器中显示消息。
    def printf(parent, mes):
        current_text = parent.statusText.toPlainText()  # 使用 toPlainText() 获取文本
        new_text = current_text + "\n" + mes  # 使用换行符 \n 来追加消息
        parent.statusText.setPlainText(new_text)  # 更新 QTextBrowser 的文本
        parent.cursot = parent.statusText.textCursor()  # 获取文本浏览器的文本光标。
        parent.statusText.moveCursor(parent.cursot.End)  # 将光标移动到文本浏览器中文本的末尾。



class MainWindow(QMainWindow, FatigueDetecting):
    def __init__(self):
        super().__init__()
        # 调用 setupUi 方法初始化界面
        self.setupUi(self)


if __name__ == "__main__":
    # 创建一个 QApplication 实例
    app = QApplication([])
    # 创建一个 MainWindow 实例
    window = MainWindow()
    # 显示主窗口
    window.show()
    # 运行应用程序
    app.exec_()
    
    