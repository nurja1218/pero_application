import subprocess
from os import getpid

import psutil
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon, QMovie

# background process kill(keyConverter and pero_ui)
def kill_process():
    for proc in psutil.process_iter():
        if any(procstr in proc.name() for procstr in ['Palmcat', 'palmcat', 'python', 'Python']):
            print(f'Killing {proc.name()}')
            proc.kill()


subprocess_list = []


class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(1330, 810)
        Form.setFixedSize(1330, 810)
        Form.setFocusPolicy(QtCore.Qt.NoFocus)
        Form.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        Form.setWindowOpacity(3.0)
        Form.setStyleSheet("background-color: rgb(255, 255, 255)")

        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 1311, 791))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_255 = QtWidgets.QGridLayout()
        self.gridLayout_255.setObjectName("gridLayout_255")
        self.gesture_function_set = QtWidgets.QLabel(self.gridLayoutWidget)
        self.gesture_function_set.setObjectName("gesture_function_set")
        self.gridLayout_255.addWidget(self.gesture_function_set, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_255, 2, 7, 1, 4)
        self.gridLayout_263 = QtWidgets.QGridLayout()
        self.gridLayout_263.setObjectName("gridLayout_263")
        self.gest_func_comment = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoUL00")
        font.setPointSize(8)
        self.gest_func_comment.setFont(font)
        self.gest_func_comment.setObjectName("gest_func_comment")
        self.gridLayout_263.addWidget(self.gest_func_comment, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_263, 2, 11, 1, 8)
        self.gridLayout_110 = QtWidgets.QGridLayout()
        self.gridLayout_110.setObjectName("gridLayout_110")
        self.gridLayout.addLayout(self.gridLayout_110, 2, 6, 1, 1)
        self.gridLayout_445 = QtWidgets.QGridLayout()
        self.gridLayout_445.setObjectName("gridLayout_445")
        self.gridLayout.addLayout(self.gridLayout_445, 6, 0, 1, 1)
        self.gridLayout_82 = QtWidgets.QGridLayout()
        self.gridLayout_82.setObjectName("gridLayout_82")
        self.gridLayout.addLayout(self.gridLayout_82, 11, 6, 1, 1)
        self.gridLayout_98 = QtWidgets.QGridLayout()
        self.gridLayout_98.setObjectName("gridLayout_98")
        self.gridLayout.addLayout(self.gridLayout_98, 25, 16, 1, 1)
        self.gridLayout_15 = QtWidgets.QGridLayout()
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.gridLayout.addLayout(self.gridLayout_15, 25, 19, 1, 1)
        self.gridLayout_79 = QtWidgets.QGridLayout()
        self.gridLayout_79.setObjectName("gridLayout_79")
        self.gridLayout.addLayout(self.gridLayout_79, 14, 6, 1, 1)
        self.gridLayout_103 = QtWidgets.QGridLayout()
        self.gridLayout_103.setObjectName("gridLayout_103")
        self.gridLayout.addLayout(self.gridLayout_103, 22, 6, 1, 1)
        self.gridLayout_18 = QtWidgets.QGridLayout()
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.gridLayout.addLayout(self.gridLayout_18, 8, 6, 1, 1)
        self.gridLayout_20 = QtWidgets.QGridLayout()
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.gridLayout.addLayout(self.gridLayout_20, 25, 11, 1, 1)
        self.gridLayout_13 = QtWidgets.QGridLayout()
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.gridLayout.addLayout(self.gridLayout_13, 4, 6, 1, 1)
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.gridLayout.addLayout(self.gridLayout_10, 6, 6, 1, 1)
        self.gridLayout_78 = QtWidgets.QGridLayout()
        self.gridLayout_78.setObjectName("gridLayout_78")
        self.gridLayout.addLayout(self.gridLayout_78, 15, 6, 1, 1)
        self.gridLayout_101 = QtWidgets.QGridLayout()
        self.gridLayout_101.setObjectName("gridLayout_101")
        self.gridLayout.addLayout(self.gridLayout_101, 25, 18, 1, 1)
        self.gridLayout_36 = QtWidgets.QGridLayout()
        self.gridLayout_36.setObjectName("gridLayout_36")
        self.gridLayout.addLayout(self.gridLayout_36, 19, 6, 1, 1)
        self.gridLayout_80 = QtWidgets.QGridLayout()
        self.gridLayout_80.setObjectName("gridLayout_80")
        self.gridLayout.addLayout(self.gridLayout_80, 13, 6, 1, 1)
        self.gridLayout_54 = QtWidgets.QGridLayout()
        self.gridLayout_54.setObjectName("gridLayout_54")
        self.gridLayout.addLayout(self.gridLayout_54, 16, 6, 1, 1)
        self.gridLayout_446 = QtWidgets.QGridLayout()
        self.gridLayout_446.setObjectName("gridLayout_446")
        self.gridLayout.addLayout(self.gridLayout_446, 5, 0, 1, 1)
        self.gridLayout_22 = QtWidgets.QGridLayout()
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.gridLayout.addLayout(self.gridLayout_22, 25, 13, 1, 1)
        self.gridLayout_19 = QtWidgets.QGridLayout()
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.gridLayout.addLayout(self.gridLayout_19, 3, 6, 1, 1)
        self.gridLayout_96 = QtWidgets.QGridLayout()
        self.gridLayout_96.setObjectName("gridLayout_96")
        self.gridLayout.addLayout(self.gridLayout_96, 25, 14, 1, 1)
        self.gridLayout_108 = QtWidgets.QGridLayout()
        self.gridLayout_108.setObjectName("gridLayout_108")
        self.gridLayout.addLayout(self.gridLayout_108, 23, 6, 1, 1)
        self.gridLayout_93 = QtWidgets.QGridLayout()
        self.gridLayout_93.setObjectName("gridLayout_93")
        self.gridLayout.addLayout(self.gridLayout_93, 25, 23, 1, 1)
        self.gridLayout_44 = QtWidgets.QGridLayout()
        self.gridLayout_44.setObjectName("gridLayout_44")
        self.gridLayout.addLayout(self.gridLayout_44, 17, 6, 1, 1)
        self.gridLayout_102 = QtWidgets.QGridLayout()
        self.gridLayout_102.setObjectName("gridLayout_102")
        self.gridLayout.addLayout(self.gridLayout_102, 21, 6, 1, 1)
        self.gridLayout_91 = QtWidgets.QGridLayout()
        self.gridLayout_91.setObjectName("gridLayout_91")
        self.gridLayout.addLayout(self.gridLayout_91, 25, 21, 1, 1)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.gridLayout.addLayout(self.gridLayout_9, 7, 6, 1, 1)
        self.gridLayout_100 = QtWidgets.QGridLayout()
        self.gridLayout_100.setObjectName("gridLayout_100")
        self.gridLayout.addLayout(self.gridLayout_100, 25, 17, 1, 1)
        self.gridLayout_37 = QtWidgets.QGridLayout()
        self.gridLayout_37.setObjectName("gridLayout_37")
        self.gridLayout.addLayout(self.gridLayout_37, 18, 6, 1, 1)
        self.gridLayout_90 = QtWidgets.QGridLayout()
        self.gridLayout_90.setObjectName("gridLayout_90")
        self.gridLayout.addLayout(self.gridLayout_90, 25, 20, 1, 1)
        self.gridLayout_92 = QtWidgets.QGridLayout()
        self.gridLayout_92.setObjectName("gridLayout_92")
        self.gridLayout.addLayout(self.gridLayout_92, 25, 22, 1, 1)
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.gridLayout.addLayout(self.gridLayout_11, 5, 6, 1, 1)
        self.gridLayout_107 = QtWidgets.QGridLayout()
        self.gridLayout_107.setObjectName("gridLayout_107")
        self.gridLayout.addLayout(self.gridLayout_107, 25, 24, 1, 1)
        self.gridLayout_83 = QtWidgets.QGridLayout()
        self.gridLayout_83.setObjectName("gridLayout_83")
        self.gridLayout.addLayout(self.gridLayout_83, 10, 6, 1, 1)
        self.gridLayout_21 = QtWidgets.QGridLayout()
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.gridLayout.addLayout(self.gridLayout_21, 25, 12, 1, 1)
        self.gridLayout_81 = QtWidgets.QGridLayout()
        self.gridLayout_81.setObjectName("gridLayout_81")
        self.gridLayout.addLayout(self.gridLayout_81, 12, 6, 1, 1)
        self.gridLayout_97 = QtWidgets.QGridLayout()
        self.gridLayout_97.setObjectName("gridLayout_97")
        self.gridLayout.addLayout(self.gridLayout_97, 25, 15, 1, 1)
        self.gridLayout_17 = QtWidgets.QGridLayout()
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.gridLayout.addLayout(self.gridLayout_17, 9, 6, 1, 1)
        self.gridLayout_71 = QtWidgets.QGridLayout()
        self.gridLayout_71.setObjectName("gridLayout_71")
        self.gridLayout.addLayout(self.gridLayout_71, 0, 8, 1, 1)
        self.gridLayout_74 = QtWidgets.QGridLayout()
        self.gridLayout_74.setObjectName("gridLayout_74")
        self.gridLayout.addLayout(self.gridLayout_74, 0, 21, 1, 1)
        self.gridLayout_87 = QtWidgets.QGridLayout()
        self.gridLayout_87.setObjectName("gridLayout_87")
        self.gridLayout.addLayout(self.gridLayout_87, 25, 8, 1, 1)
        self.gridLayout_88 = QtWidgets.QGridLayout()
        self.gridLayout_88.setObjectName("gridLayout_88")
        self.gridLayout.addLayout(self.gridLayout_88, 25, 9, 1, 1)
        self.gridLayout_266 = QtWidgets.QGridLayout()
        self.gridLayout_266.setObjectName("gridLayout_266")
        self.gridLayout.addLayout(self.gridLayout_266, 0, 12, 1, 1)
        self.gridLayout_260 = QtWidgets.QGridLayout()
        self.gridLayout_260.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_260.setObjectName("gridLayout_260")
        self.gridLayout.addLayout(self.gridLayout_260, 1, 8, 1, 1)
        self.gridLayout_256 = QtWidgets.QGridLayout()
        self.gridLayout_256.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_256.setObjectName("gridLayout_256")
        self.gridLayout.addLayout(self.gridLayout_256, 1, 6, 1, 1)
        self.gridLayout_280 = QtWidgets.QGridLayout()
        self.gridLayout_280.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_280.setObjectName("gridLayout_280")
        self.gridLayout.addLayout(self.gridLayout_280, 1, 13, 1, 1)
        self.gridLayout_322 = QtWidgets.QGridLayout()
        self.gridLayout_322.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_322.setObjectName("gridLayout_322")
        self.gridLayout.addLayout(self.gridLayout_322, 1, 19, 1, 1)
        self.gridLayout_73 = QtWidgets.QGridLayout()
        self.gridLayout_73.setObjectName("gridLayout_73")
        self.gridLayout.addLayout(self.gridLayout_73, 0, 10, 1, 1)
        self.gridLayout_258 = QtWidgets.QGridLayout()
        self.gridLayout_258.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_258.setObjectName("gridLayout_258")
        self.gridLayout.addLayout(self.gridLayout_258, 1, 7, 1, 1)
        self.gridLayout_267 = QtWidgets.QGridLayout()
        self.gridLayout_267.setObjectName("gridLayout_267")
        self.gridLayout.addLayout(self.gridLayout_267, 0, 13, 1, 1)
        self.gridLayout_269 = QtWidgets.QGridLayout()
        self.gridLayout_269.setObjectName("gridLayout_269")
        self.gridLayout.addLayout(self.gridLayout_269, 0, 15, 1, 1)
        self.gridLayout_86 = QtWidgets.QGridLayout()
        self.gridLayout_86.setObjectName("gridLayout_86")
        self.gridLayout.addLayout(self.gridLayout_86, 25, 7, 1, 1)
        self.gridLayout_72 = QtWidgets.QGridLayout()
        self.gridLayout_72.setObjectName("gridLayout_72")
        self.gridLayout.addLayout(self.gridLayout_72, 0, 9, 1, 1)
        self.gridLayout_264 = QtWidgets.QGridLayout()
        self.gridLayout_264.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_264.setObjectName("gridLayout_264")
        self.gridLayout.addLayout(self.gridLayout_264, 1, 10, 1, 1)
        self.gridLayout_265 = QtWidgets.QGridLayout()
        self.gridLayout_265.setObjectName("gridLayout_265")
        self.gridLayout.addLayout(self.gridLayout_265, 0, 11, 1, 1)
        self.gridLayout_89 = QtWidgets.QGridLayout()
        self.gridLayout_89.setObjectName("gridLayout_89")
        self.gridLayout.addLayout(self.gridLayout_89, 25, 10, 1, 1)
        self.gridLayout_85 = QtWidgets.QGridLayout()
        self.gridLayout_85.setObjectName("gridLayout_85")
        self.gridLayout.addLayout(self.gridLayout_85, 25, 6, 1, 1)
        self.gridLayout_262 = QtWidgets.QGridLayout()
        self.gridLayout_262.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_262.setObjectName("gridLayout_262")
        self.gridLayout.addLayout(self.gridLayout_262, 1, 9, 1, 1)
        self.gridLayout_69 = QtWidgets.QGridLayout()
        self.gridLayout_69.setObjectName("gridLayout_69")
        self.gridLayout.addLayout(self.gridLayout_69, 0, 6, 1, 1)
        self.gridLayout_70 = QtWidgets.QGridLayout()
        self.gridLayout_70.setObjectName("gridLayout_70")
        self.gridLayout.addLayout(self.gridLayout_70, 0, 7, 1, 1)
        self.gridLayout_332 = QtWidgets.QGridLayout()
        self.gridLayout_332.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_332.setObjectName("gridLayout_332")
        self.gridLayout.addLayout(self.gridLayout_332, 2, 22, 1, 1)
        self.gridLayout_447 = QtWidgets.QGridLayout()
        self.gridLayout_447.setObjectName("gridLayout_447")
        self.gridLayout.addLayout(self.gridLayout_447, 4, 0, 1, 1)
        self.gridLayout_25 = QtWidgets.QGridLayout()
        self.gridLayout_25.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_25.setObjectName("gridLayout_25")
        self.gridLayout.addLayout(self.gridLayout_25, 2, 4, 1, 1)
        self.gridLayout_437 = QtWidgets.QGridLayout()
        self.gridLayout_437.setObjectName("gridLayout_437")
        self.gridLayout.addLayout(self.gridLayout_437, 24, 6, 1, 1)
        self.gridLayout_438 = QtWidgets.QGridLayout()
        self.gridLayout_438.setObjectName("gridLayout_438")
        self.gridLayout.addLayout(self.gridLayout_438, 20, 6, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.PERO = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoUL00")
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.PERO.setFont(font)
        self.PERO.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.PERO.setObjectName("PERO")
        self.gridLayout_2.addWidget(self.PERO, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 2, 2)
        self.gridLayout_443 = QtWidgets.QGridLayout()
        self.gridLayout_443.setObjectName("gridLayout_443")
        self.gridLayout.addLayout(self.gridLayout_443, 8, 0, 1, 1)
        self.gridLayout_14 = QtWidgets.QGridLayout()
        self.gridLayout_14.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.applications = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoUL00")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.applications.setFont(font)
        self.applications.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.applications.setObjectName("applications")
        self.gridLayout_14.addWidget(self.applications, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_14, 2, 0, 1, 2)
        self.gridLayout_336 = QtWidgets.QGridLayout()
        self.gridLayout_336.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_336.setObjectName("gridLayout_336")
        self.gridLayout.addLayout(self.gridLayout_336, 2, 19, 1, 1)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.palmcat_logo = QtWidgets.QLabel(self.gridLayoutWidget)
        self.palmcat_logo.setObjectName("palmcat_logo")
        self.gridLayout_8.addWidget(self.palmcat_logo, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_8, 0, 22, 2, 4)
        self.gridLayout_24 = QtWidgets.QGridLayout()
        self.gridLayout_24.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.gridLayout.addLayout(self.gridLayout_24, 2, 3, 1, 1)
        self.gridLayout_23 = QtWidgets.QGridLayout()
        self.gridLayout_23.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.gridLayout.addLayout(self.gridLayout_23, 2, 2, 1, 1)
        self.gridLayout_331 = QtWidgets.QGridLayout()
        self.gridLayout_331.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_331.setObjectName("gridLayout_331")
        self.gridLayout.addLayout(self.gridLayout_331, 2, 23, 1, 3)

        self.reset_btn = QtWidgets.QPushButton()
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoM00")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.reset_btn.setFont(font)
        self.reset_btn.setObjectName("reset_btn")
        self.reset_btn.setFixedSize(90, 27)
        self.reset_btn.setStyleSheet(
            "background: #CBC7B8;  border: 2px solid #A8A69E; border-radius: 10px; text-align: center;")

        self.gridLayout_331.addWidget(self.reset_btn, 1, 1, 1, 1)
        # self.gridLayout_174.addLayout(self.gridLayout_179, 2, 2, 1, 1)

        self.reset_btn.setIcon(QtGui.QIcon("reset_icon.png"))
        self.reset_btn.setIconSize(QtCore.QSize(16, 16))
        self.reset_btn.setText(" Reset!")
        self.reset_btn.pressed.connect(self.press_reset_btn)
        self.reset_btn.released.connect(self.release_reset_btn)

        self.quit_btn = QtWidgets.QPushButton()
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoM00")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.quit_btn.setFont(font)
        self.quit_btn.setObjectName("quit_btn")
        self.quit_btn.setFixedSize(90, 27)
        self.quit_btn.setStyleSheet(
            "background: #CBC7B8;  border: 2px solid #A8A69E; border-radius: 10px; text-align: center;")

        self.gridLayout_331.addWidget(self.quit_btn, 1, 2, 1, 1)
        # self.gridLayout_174.addLayout(self.gridLayout_179, 2, 2, 1, 1)
        self.quit_btn.setText("Quit")
        self.quit_btn.pressed.connect(self.press_quit_btn)
        self.quit_btn.released.connect(self.release_quit_btn)

        self.gridLayout_270 = QtWidgets.QGridLayout()
        self.gridLayout_270.setObjectName("gridLayout_270")
        self.gridLayout.addLayout(self.gridLayout_270, 0, 16, 1, 1)
        self.gridLayout_278 = QtWidgets.QGridLayout()
        self.gridLayout_278.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_278.setObjectName("gridLayout_278")
        self.gridLayout.addLayout(self.gridLayout_278, 1, 12, 1, 1)
        self.gridLayout_272 = QtWidgets.QGridLayout()
        self.gridLayout_272.setObjectName("gridLayout_272")
        self.gridLayout.addLayout(self.gridLayout_272, 0, 18, 1, 1)
        self.gridLayout_337 = QtWidgets.QGridLayout()
        self.gridLayout_337.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_337.setObjectName("gridLayout_337")
        self.gridLayout.addLayout(self.gridLayout_337, 2, 20, 1, 1)
        self.gridLayout_273 = QtWidgets.QGridLayout()
        self.gridLayout_273.setObjectName("gridLayout_273")
        self.gridLayout.addLayout(self.gridLayout_273, 0, 19, 1, 1)
        self.gridLayout_333 = QtWidgets.QGridLayout()
        self.gridLayout_333.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_333.setObjectName("gridLayout_333")
        self.gridLayout.addLayout(self.gridLayout_333, 2, 21, 1, 1)
        self.gridLayout_323 = QtWidgets.QGridLayout()
        self.gridLayout_323.setObjectName("gridLayout_323")
        self.gridLayout.addLayout(self.gridLayout_323, 1, 20, 1, 1)
        self.gridLayout_319 = QtWidgets.QGridLayout()
        self.gridLayout_319.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_319.setObjectName("gridLayout_319")
        self.gridLayout.addLayout(self.gridLayout_319, 1, 16, 1, 1)
        self.gridLayout_275 = QtWidgets.QGridLayout()
        self.gridLayout_275.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_275.setObjectName("gridLayout_275")
        self.gridLayout.addLayout(self.gridLayout_275, 1, 11, 1, 1)
        self.gridLayout_312 = QtWidgets.QGridLayout()
        self.gridLayout_312.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_312.setObjectName("gridLayout_312")
        self.gridLayout.addLayout(self.gridLayout_312, 1, 15, 1, 1)
        self.gridLayout_321 = QtWidgets.QGridLayout()
        self.gridLayout_321.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_321.setObjectName("gridLayout_321")
        self.gridLayout.addLayout(self.gridLayout_321, 1, 18, 1, 1)
        self.gridLayout_324 = QtWidgets.QGridLayout()
        self.gridLayout_324.setObjectName("gridLayout_324")
        self.gridLayout.addLayout(self.gridLayout_324, 1, 21, 1, 1)
        self.gridLayout_320 = QtWidgets.QGridLayout()
        self.gridLayout_320.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_320.setObjectName("gridLayout_320")
        self.gridLayout.addLayout(self.gridLayout_320, 1, 17, 1, 1)
        self.gridLayout_271 = QtWidgets.QGridLayout()
        self.gridLayout_271.setObjectName("gridLayout_271")
        self.gridLayout.addLayout(self.gridLayout_271, 0, 17, 1, 1)
        # self.gridLayout_330 = QtWidgets.QGridLayout()
        # self.gridLayout_330.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        # self.gridLayout_330.setObjectName("gridLayout_330")
        # self.gridLayout.addLayout(self.gridLayout_330, 2, 24, 1, 1)
        self.gridLayout_274 = QtWidgets.QGridLayout()
        self.gridLayout_274.setObjectName("gridLayout_274")
        self.gridLayout.addLayout(self.gridLayout_274, 0, 20, 1, 1)
        self.gridLayout_305 = QtWidgets.QGridLayout()
        self.gridLayout_305.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_305.setObjectName("gridLayout_305")
        self.gridLayout.addLayout(self.gridLayout_305, 1, 14, 1, 1)
        self.gridLayout_268 = QtWidgets.QGridLayout()
        self.gridLayout_268.setObjectName("gridLayout_268")
        self.gridLayout.addLayout(self.gridLayout_268, 0, 14, 1, 1)
        # self.gridLayout_329 = QtWidgets.QGridLayout()
        # self.gridLayout_329.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        # self.gridLayout_329.setObjectName("gridLayout_329")
        # self.gridLayout.addLayout(self.gridLayout_329, 2, 25, 1, 1)
        self.gridGroupBox_80 = QtWidgets.QGroupBox(self.gridLayoutWidget)
        self.gridGroupBox_80.setObjectName("gridGroupBox_80")
        self.gridLayout_95 = QtWidgets.QGridLayout(self.gridGroupBox_80)
        self.gridLayout_95.setObjectName("gridLayout_95")
        self.gridLayout_137 = QtWidgets.QGridLayout()
        self.gridLayout_137.setObjectName("gridLayout_137")
        self.gridLayout_95.addLayout(self.gridLayout_137, 13, 11, 1, 1)
        self.gridLayout_138 = QtWidgets.QGridLayout()
        self.gridLayout_138.setObjectName("gridLayout_138")
        self.gridLayout_95.addLayout(self.gridLayout_138, 14, 11, 1, 1)
        self.gridLayout_127 = QtWidgets.QGridLayout()
        self.gridLayout_127.setObjectName("gridLayout_127")
        self.gridLayout_95.addLayout(self.gridLayout_127, 3, 11, 1, 1)
        self.gridLayout_128 = QtWidgets.QGridLayout()
        self.gridLayout_128.setObjectName("gridLayout_128")
        self.gridLayout_95.addLayout(self.gridLayout_128, 4, 11, 1, 1)
        self.gridLayout_139 = QtWidgets.QGridLayout()
        self.gridLayout_139.setObjectName("gridLayout_139")
        self.gridLayout_95.addLayout(self.gridLayout_139, 15, 11, 1, 1)
        self.gridGroupBox_78 = QtWidgets.QGroupBox(self.gridGroupBox_80)
        self.gridGroupBox_78.setStyleSheet("background-color: rgb(204, 204, 204); border-radius: 10px;")
        self.gridGroupBox_78.setObjectName("gridGroupBox_78")
        self.gridLayout_173 = QtWidgets.QGridLayout(self.gridGroupBox_78)
        self.gridLayout_173.setObjectName("gridLayout_173")
        self.gridLayout_174 = QtWidgets.QGridLayout()
        self.gridLayout_174.setObjectName("gridLayout_174")
        self.gridLayout_176 = QtWidgets.QGridLayout()
        self.gridLayout_176.setObjectName("gridLayout_176")
        self.touch4 = QtWidgets.QLabel(self.gridGroupBox_78)
        self.touch4.setObjectName("touch4")
        self.gridLayout_176.addWidget(self.touch4, 0, 0, 1, 1)
        self.gridLayout_174.addLayout(self.gridLayout_176, 6, 0, 1, 1)
        self.gridLayout_185 = QtWidgets.QGridLayout()
        self.gridLayout_185.setObjectName("gridLayout_185")
        self.commends = QtWidgets.QLabel(self.gridGroupBox_78)
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoM00")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.commends.setFont(font)
        self.commends.setObjectName("commends")
        self.gridLayout_185.addWidget(self.commends, 0, 0, 1, 1)
        self.gridLayout_174.addLayout(self.gridLayout_185, 2, 1, 1, 1)
        self.gridLayout_186 = QtWidgets.QGridLayout()
        self.gridLayout_186.setObjectName("gridLayout_186")
        self.label_31 = QtWidgets.QLabel(self.gridGroupBox_78)
        self.label_31.setText("")
        self.label_31.setObjectName("label_31")
        self.gridLayout_186.addWidget(self.label_31, 0, 0, 1, 1)
        self.gridLayout_174.addLayout(self.gridLayout_186, 1, 1, 1, 1)
        self.gridLayout_187 = QtWidgets.QGridLayout()
        self.gridLayout_187.setObjectName("gridLayout_187")
        self.touch3 = QtWidgets.QLabel(self.gridGroupBox_78)
        self.touch3.setObjectName("touch3")
        self.gridLayout_187.addWidget(self.touch3, 0, 0, 1, 1)
        self.gridLayout_174.addLayout(self.gridLayout_187, 5, 0, 1, 1)
        self.gridLayout_188 = QtWidgets.QGridLayout()
        self.gridLayout_188.setObjectName("gridLayout_188")
        self.touch2 = QtWidgets.QLabel(self.gridGroupBox_78)
        self.touch2.setObjectName("touch2")
        self.gridLayout_188.addWidget(self.touch2, 0, 0, 1, 1)
        self.gridLayout_174.addLayout(self.gridLayout_188, 4, 0, 1, 1)
        self.gridLayout_190 = QtWidgets.QGridLayout()
        self.gridLayout_190.setObjectName("gridLayout_190")
        self.finger = QtWidgets.QLabel(self.gridGroupBox_78)
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoM00")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.finger.setFont(font)
        self.finger.setObjectName("finger")
        self.gridLayout_190.addWidget(self.finger, 0, 0, 1, 1)
        self.gridLayout_174.addLayout(self.gridLayout_190, 2, 0, 1, 1)
        self.gridLayout_191 = QtWidgets.QGridLayout()
        self.gridLayout_191.setObjectName("gridLayout_191")
        self.label_30 = QtWidgets.QLabel(self.gridGroupBox_78)
        self.label_30.setText("")
        self.label_30.setObjectName("label_30")
        self.gridLayout_191.addWidget(self.label_30, 0, 0, 1, 1)
        self.gridLayout_174.addLayout(self.gridLayout_191, 1, 0, 1, 1)
        self.gridLayout_192 = QtWidgets.QGridLayout()
        self.gridLayout_192.setObjectName("gridLayout_192")
        self.label_32 = QtWidgets.QLabel(self.gridGroupBox_78)
        self.label_32.setText("")
        self.label_32.setObjectName("label_32")
        self.gridLayout_192.addWidget(self.label_32, 0, 0, 1, 1)
        self.gridLayout_174.addLayout(self.gridLayout_192, 1, 2, 1, 1)
        self.gridLayout_177 = QtWidgets.QGridLayout()
        self.gridLayout_177.setObjectName("gridLayout_177")
        self.video_comment = QtWidgets.QLabel(self.gridGroupBox_78)
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoM00")
        font.setPointSize(8)
        self.video_comment.setFont(font)
        self.video_comment.setObjectName("video_comment")
        self.gridLayout_177.addWidget(self.video_comment, 0, 0, 1, 1)
        self.gridLayout_174.addLayout(self.gridLayout_177, 0, 0, 1, 3)

        self.gridLayout_179 = QtWidgets.QGridLayout()
        self.gridLayout_179.setObjectName("gridLayout_179")

        # self.submit_btn = QtWidgets.QPushButton(self.gridGroupBox_78)
        # font = QtGui.QFont()
        # font.setFamily("AppleSDGothicNeoM00")
        # font.setPointSize(9)
        # font.setBold(True)
        # font.setWeight(75)
        # self.submit_btn.setFont(font)
        # self.submit_btn.setObjectName("submit_btn")
        # self.submit_btn.setFixedSize(100, 27)
        # self.submit_btn.setStyleSheet("background: #CBC7B8;  border: 2px solid #A8A69E;")
        #
        # self.gridLayout_179.addWidget(self.submit_btn, 1, 0, 1, 1)
        # self.gridLayout_174.addLayout(self.gridLayout_179, 2, 2, 1, 1)
        #
        # self.submit_btn.setText("Use it!")
        # self.submit_btn.pressed.connect(self.press_submit_btn)
        # self.submit_btn.released.connect(self.release_submit_btn)

        self.save_btn = QtWidgets.QPushButton(self.gridGroupBox_78)
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoM00")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.save_btn.setFont(font)
        self.save_btn.setObjectName("save_btn")
        self.save_btn.setFixedSize(80, 27)
        self.save_btn.setStyleSheet("background: #CBC7B8;  border: 2px solid #A8A69E;")

        self.gridLayout_179.addWidget(self.save_btn, 1, 1, 1, 1)
        self.gridLayout_174.addLayout(self.gridLayout_179, 2, 2, 1, 1)

        self.save_btn.setText("save!")
        self.save_btn.pressed.connect(self.press_save_btn)
        self.save_btn.released.connect(self.release_save_btn)

        self.gridLayout_189 = QtWidgets.QGridLayout()
        self.gridLayout_189.setObjectName("gridLayout_189")
        self.fi_com_des = QtWidgets.QLabel(self.gridGroupBox_78)
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoM00")
        font.setPointSize(8)
        self.fi_com_des.setFont(font)
        self.fi_com_des.setObjectName("fi_com_des")
        self.gridLayout_189.addWidget(self.fi_com_des, 0, 0, 1, 1)
        self.gridLayout_174.addLayout(self.gridLayout_189, 3, 0, 1, 3)
        self.gridLayout_183 = QtWidgets.QGridLayout()
        self.gridLayout_183.setObjectName("gridLayout_183")
        self.touch_des1 = QtWidgets.QComboBox(self.gridGroupBox_78)
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoM00")
        self.touch_des1.setFont(font)
        self.touch_des1.setStyleSheet("background-color: rgb(102, 102, 102); color: gray;")
        self.touch_des1.setObjectName("touch_des1")
        self.gridLayout_183.addWidget(self.touch_des1, 0, 0, 1, 1)
        self.gridLayout_174.addLayout(self.gridLayout_183, 4, 1, 1, 2)
        self.gridLayout_182 = QtWidgets.QGridLayout()
        self.gridLayout_182.setObjectName("gridLayout_182")
        self.touch_des2 = QtWidgets.QComboBox(self.gridGroupBox_78)
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoM00")
        self.touch_des2.setFont(font)
        self.touch_des2.setStyleSheet("background-color: rgb(102, 102, 102); color: gray;")
        self.touch_des2.setObjectName("touch_des2")
        self.gridLayout_182.addWidget(self.touch_des2, 0, 0, 1, 1)
        self.gridLayout_174.addLayout(self.gridLayout_182, 5, 1, 1, 2)
        self.gridLayout_181 = QtWidgets.QGridLayout()
        self.gridLayout_181.setObjectName("gridLayout_181")
        self.touch_des3 = QtWidgets.QComboBox(self.gridGroupBox_78)
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoM00")
        self.touch_des3.setFont(font)
        self.touch_des3.setStyleSheet("background-color: rgb(102, 102, 102); color: white;")
        self.touch_des3.setObjectName("touch_des3")
        self.gridLayout_181.addWidget(self.touch_des3, 0, 0, 1, 1)
        self.gridLayout_174.addLayout(self.gridLayout_181, 6, 1, 1, 2)
        self.gridLayout_173.addLayout(self.gridLayout_174, 1, 0, 1, 1)
        self.gridLayout_175 = QtWidgets.QGridLayout()
        self.gridLayout_175.setObjectName("gridLayout_175")
        self.video = QtWidgets.QLabel(self.gridGroupBox_78)
        self.video.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.video.setObjectName("video")
        self.video.setFixedSize(546, 260)
        self.gridLayout_175.addWidget(self.video, 0, 0, 1, 1)
        self.gridLayout_173.addLayout(self.gridLayout_175, 0, 0, 1, 1)
        self.gridLayout_95.addWidget(self.gridGroupBox_78, 2, 12, 16, 14)
        self.gridLayout_126 = QtWidgets.QGridLayout()
        self.gridLayout_126.setObjectName("gridLayout_126")
        self.gridLayout_95.addLayout(self.gridLayout_126, 2, 11, 1, 1)
        self.gridLayout_129 = QtWidgets.QGridLayout()
        self.gridLayout_129.setObjectName("gridLayout_129")
        self.gridLayout_95.addLayout(self.gridLayout_129, 5, 11, 1, 1)
        self.gridLayout_172 = QtWidgets.QGridLayout()
        self.gridLayout_172.setObjectName("gridLayout_172")
        self.finger_touch_des = QtWidgets.QLabel(self.gridGroupBox_80)
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoM00")
        font.setPointSize(10)
        self.finger_touch_des.setFont(font)
        self.finger_touch_des.setObjectName("finger_touch_des")
        self.gridLayout_172.addWidget(self.finger_touch_des, 0, 0, 1, 1)
        self.gridLayout_95.addLayout(self.gridLayout_172, 1, 12, 1, 14)
        self.gridLayout_47 = QtWidgets.QGridLayout()
        self.gridLayout_47.setObjectName("gridLayout_47")
        self.gridLayout_95.addLayout(self.gridLayout_47, 18, 5, 1, 1)
        self.gridLayout_99 = QtWidgets.QGridLayout()
        self.gridLayout_99.setObjectName("gridLayout_99")
        self.gridLayout_95.addLayout(self.gridLayout_99, 18, 7, 1, 1)
        self.gridLayout_106 = QtWidgets.QGridLayout()
        self.gridLayout_106.setObjectName("gridLayout_106")
        self.gridLayout_95.addLayout(self.gridLayout_106, 18, 6, 1, 1)
        self.gridLayout_109 = QtWidgets.QGridLayout()
        self.gridLayout_109.setObjectName("gridLayout_109")
        self.gridLayout_95.addLayout(self.gridLayout_109, 18, 14, 1, 1)
        self.gridLayout_111 = QtWidgets.QGridLayout()
        self.gridLayout_111.setObjectName("gridLayout_111")
        self.gridLayout_95.addLayout(self.gridLayout_111, 18, 20, 1, 1)
        self.gridLayout_45 = QtWidgets.QGridLayout()
        self.gridLayout_45.setObjectName("gridLayout_45")
        self.gridLayout_95.addLayout(self.gridLayout_45, 18, 1, 1, 1)
        self.gridLayout_32 = QtWidgets.QGridLayout()
        self.gridLayout_32.setObjectName("gridLayout_32")
        self.gridLayout_95.addLayout(self.gridLayout_32, 18, 0, 1, 1)
        self.gridLayout_112 = QtWidgets.QGridLayout()
        self.gridLayout_112.setObjectName("gridLayout_112")
        self.gridLayout_95.addLayout(self.gridLayout_112, 18, 18, 1, 1)
        self.gridLayout_16 = QtWidgets.QGridLayout()
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.gridLayout_95.addLayout(self.gridLayout_16, 18, 24, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout_149 = QtWidgets.QGridLayout()
        self.gridLayout_149.setObjectName("gridLayout_149")
        self.linear1 = QtWidgets.QLabel(self.gridGroupBox_80)
        self.linear1.setMaximumSize(QtCore.QSize(55, 55))
        self.linear1.setObjectName("linear1")
        self.gridLayout_149.addWidget(self.linear1, 0, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_149)
        self.gridLayout_147 = QtWidgets.QGridLayout()
        self.gridLayout_147.setObjectName("gridLayout_147")
        self.linear2 = QtWidgets.QLabel(self.gridGroupBox_80)
        self.linear2.setMaximumSize(QtCore.QSize(55, 55))
        self.linear2.setObjectName("linear2")
        self.gridLayout_147.addWidget(self.linear2, 0, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_147)
        self.gridLayout_148 = QtWidgets.QGridLayout()
        self.gridLayout_148.setObjectName("gridLayout_148")
        self.linear3 = QtWidgets.QLabel(self.gridGroupBox_80)
        self.linear3.setMaximumSize(QtCore.QSize(55, 55))
        self.linear3.setObjectName("linear3")
        self.gridLayout_148.addWidget(self.linear3, 0, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_148)
        self.gridLayout_146 = QtWidgets.QGridLayout()
        self.gridLayout_146.setObjectName("gridLayout_146")
        self.linear4 = QtWidgets.QLabel(self.gridGroupBox_80)
        self.linear4.setMaximumSize(QtCore.QSize(55, 55))
        self.linear4.setObjectName("linear4")
        self.gridLayout_146.addWidget(self.linear4, 0, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_146)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_153 = QtWidgets.QGridLayout()
        self.gridLayout_153.setObjectName("gridLayout_153")
        self.linear5 = QtWidgets.QLabel(self.gridGroupBox_80)
        self.linear5.setMaximumSize(QtCore.QSize(55, 55))
        self.linear5.setObjectName("linear5")
        self.gridLayout_153.addWidget(self.linear5, 0, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_153)
        self.gridLayout_152 = QtWidgets.QGridLayout()
        self.gridLayout_152.setObjectName("gridLayout_152")
        self.linear6 = QtWidgets.QLabel(self.gridGroupBox_80)
        self.linear6.setMaximumSize(QtCore.QSize(55, 55))
        self.linear6.setObjectName("linear6")
        self.gridLayout_152.addWidget(self.linear6, 0, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_152)
        self.gridLayout_154 = QtWidgets.QGridLayout()
        self.gridLayout_154.setObjectName("gridLayout_154")
        self.linear7 = QtWidgets.QLabel(self.gridGroupBox_80)
        self.linear7.setMaximumSize(QtCore.QSize(55, 55))
        self.linear7.setObjectName("linear7")
        self.gridLayout_154.addWidget(self.linear7, 0, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_154)
        self.gridLayout_150 = QtWidgets.QGridLayout()
        self.gridLayout_150.setObjectName("gridLayout_150")
        self.linear8 = QtWidgets.QLabel(self.gridGroupBox_80)
        self.linear8.setMaximumSize(QtCore.QSize(55, 55))
        self.linear8.setObjectName("linear8")
        self.gridLayout_150.addWidget(self.linear8, 0, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_150)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout_95.addLayout(self.verticalLayout, 4, 0, 4, 11)
        self.gridLayout_144 = QtWidgets.QGridLayout()
        self.gridLayout_144.setObjectName("gridLayout_144")
        self.curve_action = QtWidgets.QLabel(self.gridGroupBox_80)
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoM00")
        font.setPointSize(10)
        self.curve_action.setFont(font)
        self.curve_action.setObjectName("curve_action")
        self.gridLayout_144.addWidget(self.curve_action, 0, 0, 1, 1)
        self.gridLayout_95.addLayout(self.gridLayout_144, 8, 0, 1, 11)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gridLayout_156 = QtWidgets.QGridLayout()
        self.gridLayout_156.setObjectName("gridLayout_156")
        self.curve1 = QtWidgets.QLabel(self.gridGroupBox_80)
        self.curve1.setMaximumSize(QtCore.QSize(55, 55))
        self.curve1.setObjectName("curve1")
        self.gridLayout_156.addWidget(self.curve1, 0, 0, 1, 1)
        self.horizontalLayout_4.addLayout(self.gridLayout_156)
        self.gridLayout_158 = QtWidgets.QGridLayout()
        self.gridLayout_158.setObjectName("gridLayout_158")
        self.curve2 = QtWidgets.QLabel(self.gridGroupBox_80)
        self.curve2.setMaximumSize(QtCore.QSize(55, 55))
        self.curve2.setObjectName("curve2")
        self.gridLayout_158.addWidget(self.curve2, 0, 0, 1, 1)
        self.horizontalLayout_4.addLayout(self.gridLayout_158)
        self.gridLayout_157 = QtWidgets.QGridLayout()
        self.gridLayout_157.setObjectName("gridLayout_157")
        self.curve3 = QtWidgets.QLabel(self.gridGroupBox_80)
        self.curve3.setMaximumSize(QtCore.QSize(55, 55))
        self.curve3.setObjectName("curve3")
        self.gridLayout_157.addWidget(self.curve3, 0, 0, 1, 1)
        self.horizontalLayout_4.addLayout(self.gridLayout_157)
        self.gridLayout_155 = QtWidgets.QGridLayout()
        self.gridLayout_155.setObjectName("gridLayout_155")
        self.curve4 = QtWidgets.QLabel(self.gridGroupBox_80)
        self.curve4.setMaximumSize(QtCore.QSize(55, 55))
        self.curve4.setObjectName("curve4")
        self.gridLayout_155.addWidget(self.curve4, 0, 0, 1, 1)
        self.horizontalLayout_4.addLayout(self.gridLayout_155)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout_160 = QtWidgets.QGridLayout()
        self.gridLayout_160.setObjectName("gridLayout_160")
        self.curve5 = QtWidgets.QLabel(self.gridGroupBox_80)
        self.curve5.setMaximumSize(QtCore.QSize(55, 55))
        self.curve5.setObjectName("curve5")
        self.gridLayout_160.addWidget(self.curve5, 0, 0, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_160)
        self.gridLayout_161 = QtWidgets.QGridLayout()
        self.gridLayout_161.setObjectName("gridLayout_161")
        self.curve6 = QtWidgets.QLabel(self.gridGroupBox_80)
        self.curve6.setMaximumSize(QtCore.QSize(55, 55))
        self.curve6.setObjectName("curve6")
        self.gridLayout_161.addWidget(self.curve6, 0, 0, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_161)
        self.gridLayout_162 = QtWidgets.QGridLayout()
        self.gridLayout_162.setObjectName("gridLayout_162")
        self.curve7 = QtWidgets.QLabel(self.gridGroupBox_80)
        self.curve7.setMaximumSize(QtCore.QSize(55, 55))
        self.curve7.setObjectName("curve7")
        self.gridLayout_162.addWidget(self.curve7, 0, 0, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_162)
        self.gridLayout_159 = QtWidgets.QGridLayout()
        self.gridLayout_159.setObjectName("gridLayout_159")
        self.curve8 = QtWidgets.QLabel(self.gridGroupBox_80)
        self.curve8.setMaximumSize(QtCore.QSize(55, 55))
        self.curve8.setObjectName("curve8")
        self.gridLayout_159.addWidget(self.curve8, 0, 0, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_159)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.gridLayout_95.addLayout(self.verticalLayout_2, 9, 0, 4, 11)
        self.gridLayout_143 = QtWidgets.QGridLayout()
        self.gridLayout_143.setObjectName("gridLayout_143")
        self.linear_action = QtWidgets.QLabel(self.gridGroupBox_80)
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoM00")
        font.setPointSize(10)
        self.linear_action.setFont(font)
        self.linear_action.setObjectName("linear_action")
        self.gridLayout_143.addWidget(self.linear_action, 0, 0, 1, 1)
        self.gridLayout_95.addLayout(self.gridLayout_143, 3, 0, 1, 11)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_95.addLayout(self.gridLayout_4, 18, 13, 1, 1)
        self.gridLayout_48 = QtWidgets.QGridLayout()
        self.gridLayout_48.setObjectName("gridLayout_48")
        self.gridLayout_95.addLayout(self.gridLayout_48, 18, 2, 1, 1)
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.gridLayout_95.addLayout(self.gridLayout_12, 18, 25, 1, 1)
        self.gridLayout_49 = QtWidgets.QGridLayout()
        self.gridLayout_49.setObjectName("gridLayout_49")
        self.gridLayout_95.addLayout(self.gridLayout_49, 18, 3, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_95.addLayout(self.gridLayout_5, 18, 11, 1, 1)
        self.gridLayout_50 = QtWidgets.QGridLayout()
        self.gridLayout_50.setObjectName("gridLayout_50")
        self.gridLayout_95.addLayout(self.gridLayout_50, 18, 12, 1, 1)
        self.gridLayout_145 = QtWidgets.QGridLayout()
        self.gridLayout_145.setObjectName("gridLayout_145")
        self.overlap_action = QtWidgets.QLabel(self.gridGroupBox_80)
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoM00")
        font.setPointSize(10)
        self.overlap_action.setFont(font)
        self.overlap_action.setObjectName("overlap_action")
        self.gridLayout_145.addWidget(self.overlap_action, 0, 0, 1, 1)
        self.gridLayout_95.addLayout(self.gridLayout_145, 13, 0, 1, 11)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.gridLayout_166 = QtWidgets.QGridLayout()
        self.gridLayout_166.setObjectName("gridLayout_166")
        self.overlap1 = QtWidgets.QLabel(self.gridGroupBox_80)
        self.overlap1.setMaximumSize(QtCore.QSize(55, 55))
        self.overlap1.setObjectName("overlap1")
        self.gridLayout_166.addWidget(self.overlap1, 0, 0, 1, 1)
        self.horizontalLayout_6.addLayout(self.gridLayout_166)
        self.gridLayout_164 = QtWidgets.QGridLayout()
        self.gridLayout_164.setObjectName("gridLayout_164")
        self.overlap2 = QtWidgets.QLabel(self.gridGroupBox_80)
        self.overlap2.setMaximumSize(QtCore.QSize(55, 55))
        self.overlap2.setObjectName("overlap2")
        self.gridLayout_164.addWidget(self.overlap2, 0, 0, 1, 1)
        self.horizontalLayout_6.addLayout(self.gridLayout_164)
        self.gridLayout_167 = QtWidgets.QGridLayout()
        self.gridLayout_167.setObjectName("gridLayout_167")
        self.overlap3 = QtWidgets.QLabel(self.gridGroupBox_80)
        self.overlap3.setMaximumSize(QtCore.QSize(55, 55))
        self.overlap3.setObjectName("overlap3")
        self.gridLayout_167.addWidget(self.overlap3, 0, 0, 1, 1)
        self.horizontalLayout_6.addLayout(self.gridLayout_167)
        self.gridLayout_163 = QtWidgets.QGridLayout()
        self.gridLayout_163.setObjectName("gridLayout_163")
        self.overlap4 = QtWidgets.QLabel(self.gridGroupBox_80)
        self.overlap4.setMaximumSize(QtCore.QSize(55, 55))
        self.overlap4.setObjectName("overlap4")
        self.gridLayout_163.addWidget(self.overlap4, 0, 0, 1, 1)
        self.horizontalLayout_6.addLayout(self.gridLayout_163)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.gridLayout_171 = QtWidgets.QGridLayout()
        self.gridLayout_171.setObjectName("gridLayout_171")
        self.overlap5 = QtWidgets.QLabel(self.gridGroupBox_80)
        self.overlap5.setMaximumSize(QtCore.QSize(55, 55))
        self.overlap5.setObjectName("overlap5")
        self.gridLayout_171.addWidget(self.overlap5, 0, 0, 1, 1)
        self.horizontalLayout_5.addLayout(self.gridLayout_171)
        self.gridLayout_169 = QtWidgets.QGridLayout()
        self.gridLayout_169.setObjectName("gridLayout_169")
        self.overlap6 = QtWidgets.QLabel(self.gridGroupBox_80)
        self.overlap6.setMaximumSize(QtCore.QSize(55, 55))
        self.overlap6.setObjectName("overlap6")
        self.gridLayout_169.addWidget(self.overlap6, 0, 0, 1, 1)
        self.horizontalLayout_5.addLayout(self.gridLayout_169)
        self.gridLayout_170 = QtWidgets.QGridLayout()
        self.gridLayout_170.setObjectName("gridLayout_170")
        self.overlap7 = QtWidgets.QLabel(self.gridGroupBox_80)
        self.overlap7.setMaximumSize(QtCore.QSize(55, 55))
        self.overlap7.setObjectName("overlap7")
        self.gridLayout_170.addWidget(self.overlap7, 0, 0, 1, 1)
        self.horizontalLayout_5.addLayout(self.gridLayout_170)
        self.gridLayout_168 = QtWidgets.QGridLayout()
        self.gridLayout_168.setObjectName("gridLayout_168")
        self.overlap8 = QtWidgets.QLabel(self.gridGroupBox_80)
        self.overlap8.setMaximumSize(QtCore.QSize(55, 55))
        self.overlap8.setObjectName("overlap8")
        self.gridLayout_168.addWidget(self.overlap8, 0, 0, 1, 1)
        self.horizontalLayout_5.addLayout(self.gridLayout_168)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.gridLayout_95.addLayout(self.verticalLayout_3, 14, 0, 4, 11)
        self.gridLayout_130 = QtWidgets.QGridLayout()
        self.gridLayout_130.setObjectName("gridLayout_130")
        self.gridLayout_95.addLayout(self.gridLayout_130, 6, 11, 1, 1)
        self.gridLayout_132 = QtWidgets.QGridLayout()
        self.gridLayout_132.setObjectName("gridLayout_132")
        self.gridLayout_95.addLayout(self.gridLayout_132, 8, 11, 1, 1)
        self.gridLayout_131 = QtWidgets.QGridLayout()
        self.gridLayout_131.setObjectName("gridLayout_131")
        self.gridLayout_95.addLayout(self.gridLayout_131, 7, 11, 1, 1)
        self.gridLayout_51 = QtWidgets.QGridLayout()
        self.gridLayout_51.setObjectName("gridLayout_51")
        self.gridLayout_95.addLayout(self.gridLayout_51, 18, 22, 1, 1)
        self.gridLayout_64 = QtWidgets.QGridLayout()
        self.gridLayout_64.setObjectName("gridLayout_64")
        self.gridLayout_95.addLayout(self.gridLayout_64, 18, 19, 1, 1)
        self.gridLayout_115 = QtWidgets.QGridLayout()
        self.gridLayout_115.setObjectName("gridLayout_115")
        self.gridLayout_95.addLayout(self.gridLayout_115, 18, 17, 1, 1)
        self.gridLayout_134 = QtWidgets.QGridLayout()
        self.gridLayout_134.setObjectName("gridLayout_134")
        self.gridLayout_95.addLayout(self.gridLayout_134, 10, 11, 1, 1)
        self.gridLayout_124 = QtWidgets.QGridLayout()
        self.gridLayout_124.setObjectName("gridLayout_124")
        self.gridLayout_95.addLayout(self.gridLayout_124, 1, 11, 1, 1)
        self.gridLayout_84 = QtWidgets.QGridLayout()
        self.gridLayout_84.setObjectName("gridLayout_84")
        self.gridLayout_95.addLayout(self.gridLayout_84, 18, 4, 1, 1)
        self.gridLayout_136 = QtWidgets.QGridLayout()
        self.gridLayout_136.setObjectName("gridLayout_136")
        self.gridLayout_95.addLayout(self.gridLayout_136, 12, 11, 1, 1)
        self.gridLayout_133 = QtWidgets.QGridLayout()
        self.gridLayout_133.setObjectName("gridLayout_133")
        self.gridLayout_95.addLayout(self.gridLayout_133, 9, 11, 1, 1)
        self.gridLayout_135 = QtWidgets.QGridLayout()
        self.gridLayout_135.setObjectName("gridLayout_135")
        self.gridLayout_95.addLayout(self.gridLayout_135, 11, 11, 1, 1)
        self.gridLayout_140 = QtWidgets.QGridLayout()
        self.gridLayout_140.setObjectName("gridLayout_140")
        self.gridLayout_95.addLayout(self.gridLayout_140, 16, 11, 1, 1)
        self.gridLayout_116 = QtWidgets.QGridLayout()
        self.gridLayout_116.setObjectName("gridLayout_116")
        self.gridLayout_95.addLayout(self.gridLayout_116, 18, 9, 1, 1)
        self.gridLayout_53 = QtWidgets.QGridLayout()
        self.gridLayout_53.setObjectName("gridLayout_53")
        self.gridLayout_95.addLayout(self.gridLayout_53, 18, 21, 1, 1)
        self.gridLayout_113 = QtWidgets.QGridLayout()
        self.gridLayout_113.setObjectName("gridLayout_113")
        self.gridLayout_95.addLayout(self.gridLayout_113, 18, 8, 1, 1)
        self.gridLayout_117 = QtWidgets.QGridLayout()
        self.gridLayout_117.setObjectName("gridLayout_117")
        self.gridLayout_95.addLayout(self.gridLayout_117, 18, 15, 1, 1)
        self.gridLayout_52 = QtWidgets.QGridLayout()
        self.gridLayout_52.setObjectName("gridLayout_52")
        self.gridLayout_95.addLayout(self.gridLayout_52, 18, 23, 1, 1)
        self.gridLayout_122 = QtWidgets.QGridLayout()
        self.gridLayout_122.setObjectName("gridLayout_122")
        self.gridLayout_95.addLayout(self.gridLayout_122, 17, 11, 1, 1)
        self.gridLayout_119 = QtWidgets.QGridLayout()
        self.gridLayout_119.setObjectName("gridLayout_119")
        self.gridLayout_95.addLayout(self.gridLayout_119, 18, 10, 1, 1)
        self.gridLayout_123 = QtWidgets.QGridLayout()
        self.gridLayout_123.setObjectName("gridLayout_123")
        self.gridLayout_95.addLayout(self.gridLayout_123, 0, 11, 1, 1)
        self.gridLayout_120 = QtWidgets.QGridLayout()
        self.gridLayout_120.setObjectName("gridLayout_120")
        self.gridLayout_95.addLayout(self.gridLayout_120, 18, 16, 1, 1)
        self.gridLayout_141 = QtWidgets.QGridLayout()
        self.gridLayout_141.setObjectName("gridLayout_141")
        self.active_app = QtWidgets.QLabel(self.gridGroupBox_80)
        self.active_app.setObjectName("active_app")
        self.active_app.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.gridLayout_141.addWidget(self.active_app, 0, 0, 1, 1)
        self.gridLayout_95.addLayout(self.gridLayout_141, 0, 0, 1, 11)
        self.gridLayout_142 = QtWidgets.QGridLayout()
        self.gridLayout_142.setObjectName("gridLayout_142")
        self.movement = QtWidgets.QLabel(self.gridGroupBox_80)
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoM00")
        self.movement.setFont(font)
        self.movement.setObjectName("movement")
        self.gridLayout_142.addWidget(self.movement, 0, 0, 1, 1)
        self.gridLayout_95.addLayout(self.gridLayout_142, 1, 0, 1, 11)
        self.gridLayout.addWidget(self.gridGroupBox_80, 3, 7, 23, 19)
        self.gridLayout_26 = QtWidgets.QGridLayout()
        self.gridLayout_26.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_26.setObjectName("gridLayout_26")
        self.gridLayout.addLayout(self.gridLayout_26, 2, 5, 1, 1)
        self.gridLayout_40 = QtWidgets.QGridLayout()
        self.gridLayout_40.setObjectName("gridLayout_40")
        self.user_set = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoM00")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.user_set.setFont(font)
        self.user_set.setObjectName("user_set")
        self.gridLayout_40.addWidget(self.user_set, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_40, 0, 2, 2, 4)
        self.groupBox = QtWidgets.QGroupBox(self.gridLayoutWidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_34 = QtWidgets.QGridLayout()
        self.gridLayout_34.setObjectName("gridLayout_34")
        self.gridLayout_3.addLayout(self.gridLayout_34, 7, 2, 1, 1)
        self.gridLayout_55 = QtWidgets.QGridLayout()
        self.gridLayout_55.setObjectName("gridLayout_55")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout_55.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_55, 6, 0, 1, 1)
        self.gridLayout_46 = QtWidgets.QGridLayout()
        self.gridLayout_46.setObjectName("gridLayout_46")
        self.gridLayout_3.addLayout(self.gridLayout_46, 8, 1, 1, 1)
        self.gridLayout_42 = QtWidgets.QGridLayout()
        self.gridLayout_42.setObjectName("gridLayout_42")
        self.gridLayout_3.addLayout(self.gridLayout_42, 6, 2, 1, 1)
        self.gridLayout_35 = QtWidgets.QGridLayout()
        self.gridLayout_35.setObjectName("gridLayout_35")
        self.windows = QtWidgets.QLabel(self.groupBox)
        self.windows.setObjectName("windows")
        self.gridLayout_35.addWidget(self.windows, 0, 0, 3, 1)
        self.gridLayout_3.addLayout(self.gridLayout_35, 3, 0, 1, 6)
        self.gridLayout_56 = QtWidgets.QGridLayout()
        self.gridLayout_56.setObjectName("gridLayout_56")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout_56.addWidget(self.label_2, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_56, 7, 0, 1, 1)
        self.gridLayout_31 = QtWidgets.QGridLayout()
        self.gridLayout_31.setObjectName("gridLayout_31")
        self.gridLayout_3.addLayout(self.gridLayout_31, 9, 3, 1, 1)
        self.gridLayout_58 = QtWidgets.QGridLayout()
        self.gridLayout_58.setObjectName("gridLayout_58")
        self.gridLayout_3.addLayout(self.gridLayout_58, 7, 1, 1, 1)
        self.gridLayout_57 = QtWidgets.QGridLayout()
        self.gridLayout_57.setObjectName("gridLayout_57")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout_57.addWidget(self.label_3, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_57, 8, 0, 1, 1)
        self.gridLayout_67 = QtWidgets.QGridLayout()
        self.gridLayout_67.setObjectName("gridLayout_67")
        self.gridLayout_3.addLayout(self.gridLayout_67, 10, 5, 1, 1)
        self.gridLayout_63 = QtWidgets.QGridLayout()
        self.gridLayout_63.setObjectName("gridLayout_63")
        self.gridLayout_3.addLayout(self.gridLayout_63, 10, 2, 1, 1)
        self.gridLayout_65 = QtWidgets.QGridLayout()
        self.gridLayout_65.setObjectName("gridLayout_65")
        self.gridLayout_3.addLayout(self.gridLayout_65, 10, 3, 1, 1)
        self.gridLayout_66 = QtWidgets.QGridLayout()
        self.gridLayout_66.setObjectName("gridLayout_66")
        self.gridLayout_3.addLayout(self.gridLayout_66, 10, 4, 1, 1)
        self.gridLayout_76 = QtWidgets.QGridLayout()
        self.gridLayout_76.setObjectName("gridLayout_76")
        self.gridLayout_3.addLayout(self.gridLayout_76, 8, 3, 1, 1)
        self.gridLayout_94 = QtWidgets.QGridLayout()
        self.gridLayout_94.setObjectName("gridLayout_94")
        self.gridLayout_3.addLayout(self.gridLayout_94, 8, 5, 1, 1)
        self.gridLayout_75 = QtWidgets.QGridLayout()
        self.gridLayout_75.setObjectName("gridLayout_75")
        self.gridLayout_3.addLayout(self.gridLayout_75, 7, 3, 1, 1)
        self.gridLayout_125 = QtWidgets.QGridLayout()
        self.gridLayout_125.setObjectName("gridLayout_125")
        self.gridLayout_3.addLayout(self.gridLayout_125, 6, 4, 1, 1)
        self.gridLayout_105 = QtWidgets.QGridLayout()
        self.gridLayout_105.setObjectName("gridLayout_105")
        self.gridLayout_3.addLayout(self.gridLayout_105, 7, 5, 1, 1)
        self.gridLayout_114 = QtWidgets.QGridLayout()
        self.gridLayout_114.setObjectName("gridLayout_114")
        self.gridLayout_3.addLayout(self.gridLayout_114, 6, 3, 1, 1)
        self.gridLayout_151 = QtWidgets.QGridLayout()
        self.gridLayout_151.setObjectName("gridLayout_151")
        self.gridLayout_3.addLayout(self.gridLayout_151, 6, 5, 1, 1)
        self.gridLayout_104 = QtWidgets.QGridLayout()
        self.gridLayout_104.setObjectName("gridLayout_104")
        self.gridLayout_3.addLayout(self.gridLayout_104, 7, 4, 1, 1)
        self.gridLayout_77 = QtWidgets.QGridLayout()
        self.gridLayout_77.setObjectName("gridLayout_77")
        self.gridLayout_3.addLayout(self.gridLayout_77, 8, 4, 1, 1)
        self.gridLayout_68 = QtWidgets.QGridLayout()
        self.gridLayout_68.setObjectName("gridLayout_68")
        self.gridLayout_3.addLayout(self.gridLayout_68, 8, 2, 1, 1)
        self.gridLayout_38 = QtWidgets.QGridLayout()
        self.gridLayout_38.setObjectName("gridLayout_38")
        self.mac_os = QtWidgets.QLabel(self.groupBox)
        self.mac_os.setObjectName("mac_os")
        self.gridLayout_38.addWidget(self.mac_os, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_38, 2, 0, 1, 6)
        self.gridLayout_27 = QtWidgets.QGridLayout()
        self.gridLayout_27.setObjectName("gridLayout_27")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout_27.addWidget(self.label_4, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_27, 9, 0, 1, 1)
        self.gridLayout_41 = QtWidgets.QGridLayout()
        self.gridLayout_41.setObjectName("gridLayout_41")
        self.gridLayout_3.addLayout(self.gridLayout_41, 10, 1, 1, 1)
        self.gridLayout_39 = QtWidgets.QGridLayout()
        self.gridLayout_39.setObjectName("gridLayout_39")
        self.excel = QtWidgets.QLabel(self.groupBox)
        self.excel.setObjectName("excel")
        self.gridLayout_39.addWidget(self.excel, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_39, 1, 0, 1, 6)
        self.gridLayout_59 = QtWidgets.QGridLayout()
        self.gridLayout_59.setObjectName("gridLayout_59")
        self.gridLayout_3.addLayout(self.gridLayout_59, 6, 1, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.gridLayout_6.addWidget(self.label_5, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_6, 10, 0, 1, 1)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.ppt = QtWidgets.QLabel(self.groupBox)
        self.ppt.setObjectName("ppt")
        self.gridLayout_7.addWidget(self.ppt, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_7, 0, 0, 1, 6)
        self.gridLayout_29 = QtWidgets.QGridLayout()
        self.gridLayout_29.setObjectName("gridLayout_29")
        self.gridLayout_3.addLayout(self.gridLayout_29, 9, 4, 1, 1)
        self.gridLayout_30 = QtWidgets.QGridLayout()
        self.gridLayout_30.setObjectName("gridLayout_30")
        self.gridLayout_3.addLayout(self.gridLayout_30, 9, 1, 1, 1)
        self.gridLayout_28 = QtWidgets.QGridLayout()
        self.gridLayout_28.setObjectName("gridLayout_28")
        self.gridLayout_3.addLayout(self.gridLayout_28, 9, 5, 1, 1)
        self.gridLayout_33 = QtWidgets.QGridLayout()
        self.gridLayout_33.setObjectName("gridLayout_33")
        self.gridLayout_3.addLayout(self.gridLayout_33, 9, 2, 1, 1)
        self.gridLayout_165 = QtWidgets.QGridLayout()
        self.gridLayout_165.setObjectName("gridLayout_165")
        self.gridLayout_3.addLayout(self.gridLayout_165, 5, 5, 1, 1)
        self.gridLayout_43 = QtWidgets.QGridLayout()
        self.gridLayout_43.setObjectName("gridLayout_43")
        self.gridLayout_62 = QtWidgets.QGridLayout()
        self.gridLayout_62.setObjectName("gridLayout_62")
        self.notice2 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoUL00")
        font.setPointSize(8)
        self.notice2.setFont(font)
        self.notice2.setObjectName("notice2")
        self.gridLayout_62.addWidget(self.notice2, 0, 0, 1, 1)
        self.gridLayout_43.addLayout(self.gridLayout_62, 1, 0, 1, 1)
        self.gridLayout_61 = QtWidgets.QGridLayout()
        self.gridLayout_61.setObjectName("gridLayout_61")
        self.notice3 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoUL00")
        font.setPointSize(8)
        self.notice3.setFont(font)
        self.notice3.setObjectName("notice3")
        self.gridLayout_61.addWidget(self.notice3, 0, 0, 1, 1)
        self.gridLayout_43.addLayout(self.gridLayout_61, 2, 0, 1, 1)
        self.gridLayout_60 = QtWidgets.QGridLayout()
        self.gridLayout_60.setObjectName("gridLayout_60")
        self.notice1 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("AppleSDGothicNeoUL00")
        font.setPointSize(8)
        self.notice1.setFont(font)
        self.notice1.setObjectName("notice1")
        self.gridLayout_60.addWidget(self.notice1, 0, 0, 1, 1)
        self.gridLayout_43.addLayout(self.gridLayout_60, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_43, 4, 0, 2, 6)
        self.gridLayout.addWidget(self.groupBox, 3, 0, 23, 6)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    #####################################################################################################

    def retranslateUi(self, Form):

        subprocess_list.append(subprocess.Popen('python keyConverterPERO.py', shell=True))

        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Palmcat", "Palmcat"))
        Form.setWindowIcon(QIcon('palmcat_title.png'))

        pixmap_ges_func = QPixmap("./mainFrame/gesture_function.png")
        pixmap_ges_func = pixmap_ges_func.scaled(200, 19)
        self.gesture_function_set.setText(_translate("Form", "제스처,기능별설정"))
        self.gesture_function_set.setPixmap(QPixmap(pixmap_ges_func))

        self.gest_func_comment.setText(_translate("Form", "제스처에 기능을 설정하거나, 기능에 제스처를 설정할 수 있습니다."))
        self.PERO.setText(_translate("Form", "PERO"))
        self.applications.setText(_translate("Form", "Applications"))

        palm_logo = QPixmap("./mainFrame/palmcat_logo.png")
        palm_logo = palm_logo.scaled(145, 43)
        self.palmcat_logo.setText(_translate("Form", "팜켓"))
        self.palmcat_logo.setPixmap(QPixmap(palm_logo))

        touch_4 = QPixmap("./setting/move_video/touch_4.png")
        self.touch4.setText(_translate("Form", "터치4개"))
        self.touch4.setPixmap(QPixmap(touch_4))

        self.commends.setText(_translate("Form", "Commends"))

        touch_3 = QPixmap("./setting/move_video/touch_3.png")
        self.touch3.setText(_translate("Form", "터치3개"))
        self.touch3.setPixmap(QPixmap(touch_3))

        touch_2 = QPixmap("./setting/move_video/touch_2.png")
        self.touch2.setText(_translate("Form", "터치2개"))
        self.touch2.setPixmap(QPixmap(touch_2))

        self.finger.setText(_translate("Form", "Finger touch"))
        self.video_comment.setText(_translate("Form", "아래에서 결정한 손가락을 갯수로 터치한 상태에서 손을 왼쪽으로 당기는 제스처입니다."))
        self.fi_com_des.setText(_translate("Form", "손바닥 터치센서에 입력할 갯수에 따른 명령을 결정합니다."))
        self.touch_des1.addItem("---명령선택---")
        self.touch_des1.addItem("윈도우 오른쪽 이동")
        self.touch_des1.addItem("윈도우 왼쪽 이동")
        self.touch_des1.addItem("전체 선택")
        self.touch_des1.addItem("사용 안함")
        self.touch_des1.model().item(0).setEnabled(False)
        # self.touch_des1.currentIndexChanged.connect(self.select_combobox1)
        self.touch_des1.setDisabled(True)
        self.touch_des2.addItem("---명령선택---")
        self.touch_des2.addItem("윈도우 오른쪽 이동")
        self.touch_des2.addItem("윈도우 왼쪽 이동")
        self.touch_des2.addItem("전체 선택")
        self.touch_des2.addItem("사용 안함")
        self.touch_des2.model().item(0).setEnabled(False)
        # self.touch_des2.currentIndexChanged.connect(self.select_combobox2)
        self.touch_des2.setDisabled(True)
        self.touch_des3.addItem("---명령선택---")
        self.touch_des3.model().item(0).setEnabled(False)
        self.touch_des3.currentIndexChanged.connect(self.select_combobox3)

        movie = QMovie("./setting/move_video/loading.gif")
        self.video.setText(_translate("Form", "video or gif"))
        self.video.setMovie(movie)
        movie.start()
        self.finger_touch_des.setText(_translate("Form", "Description & Finger touch"))

        linear_img1 = QPixmap("./mainFrame/linear1.png")
        linear_img1 = linear_img1.scaled(45, 45)
        self.linear1.setText(_translate("Form", "linear1"))
        self.linear1.setAlignment(Qt.AlignCenter)
        self.linear1.setPixmap(QPixmap(linear_img1))
        self.linear1.mousePressEvent = self.select_linear1

        linear_img2 = QPixmap("./mainFrame/linear2.png")
        linear_img2 = linear_img2.scaled(45, 45)
        self.linear2.setText(_translate("Form", "linear2"))
        self.linear2.setAlignment(Qt.AlignCenter)
        self.linear2.setPixmap(QPixmap(linear_img2))
        self.linear2.mousePressEvent = self.select_linear2

        linear_img3 = QPixmap("./mainFrame/linear3.png")
        linear_img3 = linear_img3.scaled(45, 45)
        self.linear3.setText(_translate("Form", "linear3"))
        self.linear3.setAlignment(Qt.AlignCenter)
        self.linear3.setPixmap(QPixmap(linear_img3))
        self.linear3.mousePressEvent = self.select_linear3

        linear_img4 = QPixmap("./mainFrame/linear4.png")
        linear_img4 = linear_img4.scaled(45, 45)
        self.linear4.setText(_translate("Form", "linear4"))
        self.linear4.setAlignment(Qt.AlignCenter)
        self.linear4.setPixmap(QPixmap(linear_img4))
        self.linear4.mousePressEvent = self.select_linear4

        linear_img5 = QPixmap("./mainFrame/linear5.png")
        linear_img5 = linear_img5.scaled(45, 45)
        self.linear5.setText(_translate("Form", "linear5"))
        self.linear5.setAlignment(Qt.AlignCenter)
        self.linear5.setPixmap(QPixmap(linear_img5))
        self.linear5.mousePressEvent = self.select_linear5

        linear_img6 = QPixmap("./mainFrame/linear6.png")
        linear_img6 = linear_img6.scaled(45, 45)
        self.linear6.setText(_translate("Form", "linear6"))
        self.linear6.setAlignment(Qt.AlignCenter)
        self.linear6.setPixmap(QPixmap(linear_img6))
        self.linear6.mousePressEvent = self.select_linear6

        linear_img7 = QPixmap("./mainFrame/linear7.png")
        linear_img7 = linear_img7.scaled(45, 45)
        self.linear7.setText(_translate("Form", "linear7"))
        self.linear7.setAlignment(Qt.AlignCenter)
        self.linear7.setPixmap(QPixmap(linear_img7))
        self.linear7.mousePressEvent = self.select_linear7

        linear_img8 = QPixmap("./mainFrame/linear8.png")
        linear_img8 = linear_img8.scaled(45, 45)
        self.linear8.setText(_translate("Form", "linear8"))
        self.linear8.setAlignment(Qt.AlignCenter)
        self.linear8.setPixmap(QPixmap(linear_img8))
        self.linear8.mousePressEvent = self.select_linear8

        self.curve_action.setText(_translate("Form", "곡선운동"))

        curve_img1 = QPixmap("./mainFrame/curve1.png")
        curve_img1 = curve_img1.scaled(45, 45)
        self.curve1.setText(_translate("Form", "curve1"))
        self.curve1.setAlignment(Qt.AlignCenter)
        self.curve1.setPixmap(QPixmap(curve_img1))
        self.curve1.mousePressEvent = self.select_curve1

        curve_img2 = QPixmap("./mainFrame/curve2.png")
        curve_img2 = curve_img2.scaled(45, 45)
        self.curve2.setText(_translate("Form", "curve2"))
        self.curve2.setAlignment(Qt.AlignCenter)
        self.curve2.setPixmap(QPixmap(curve_img2))
        self.curve2.mousePressEvent = self.select_curve2

        curve_img3 = QPixmap("./mainFrame/curve3.png")
        curve_img3 = curve_img3.scaled(45, 45)
        self.curve3.setText(_translate("Form", "curve3"))
        self.curve3.setAlignment(Qt.AlignCenter)
        self.curve3.setPixmap(QPixmap(curve_img3))
        self.curve3.mousePressEvent = self.select_curve3

        curve_img4 = QPixmap("./mainFrame/curve4.png")
        curve_img4 = curve_img4.scaled(45, 45)
        self.curve4.setText(_translate("Form", "curve4"))
        self.curve4.setAlignment(Qt.AlignCenter)
        self.curve4.setPixmap(QPixmap(curve_img4))
        self.curve4.mousePressEvent = self.select_curve4

        self.curve5.setText(_translate("Form", ""))
        self.curve5.setAlignment(Qt.AlignCenter)

        self.curve6.setText(_translate("Form", ""))
        self.curve6.setAlignment(Qt.AlignCenter)

        self.curve7.setText(_translate("Form", ""))
        self.curve7.setAlignment(Qt.AlignCenter)

        self.curve8.setText(_translate("Form", ""))
        self.curve8.setAlignment(Qt.AlignCenter)

        self.linear_action.setText(_translate("Form", "직선운동"))

        self.overlap_action.setText(_translate("Form", "중첩운동"))

        overlap_img1 = QPixmap("./mainFrame/overlap1.png")
        overlap_img1 = overlap_img1.scaled(45, 45)
        self.overlap1.setText(_translate("Form", "overlap1"))
        self.overlap1.setAlignment(Qt.AlignCenter)
        self.overlap1.setPixmap(QPixmap(overlap_img1))
        self.overlap1.mousePressEvent = self.select_overlap1

        overlap_img2 = QPixmap("./mainFrame/overlap2.png")
        overlap_img2 = overlap_img2.scaled(45, 45)
        self.overlap2.setText(_translate("Form", "overlap2"))
        self.overlap2.setAlignment(Qt.AlignCenter)
        self.overlap2.setPixmap(QPixmap(overlap_img2))
        self.overlap2.mousePressEvent = self.select_overlap2

        overlap_img3 = QPixmap("./mainFrame/overlap3.png")
        overlap_img3 = overlap_img3.scaled(45, 45)
        self.overlap3.setText(_translate("Form", "overlap3"))
        self.overlap3.setAlignment(Qt.AlignCenter)
        self.overlap3.setPixmap(QPixmap(overlap_img3))
        self.overlap3.mousePressEvent = self.select_overlap3

        overlap_img4 = QPixmap("./mainFrame/overlap4.png")
        overlap_img4 = overlap_img4.scaled(45, 45)
        self.overlap4.setText(_translate("Form", "overlap4"))
        self.overlap4.setAlignment(Qt.AlignCenter)
        self.overlap4.setPixmap(QPixmap(overlap_img4))
        self.overlap4.mousePressEvent = self.select_overlap4

        self.overlap5.setText(_translate("Form", ""))
        self.overlap5.setAlignment(Qt.AlignCenter)

        self.overlap6.setText(_translate("Form", ""))
        self.overlap6.setAlignment(Qt.AlignCenter)

        self.overlap7.setText(_translate("Form", ""))
        self.overlap7.setAlignment(Qt.AlignCenter)

        self.overlap8.setText(_translate("Form", ""))
        self.overlap8.setAlignment(Qt.AlignCenter)

        self.movement.setText(_translate("Form", "Movement"))
        self.user_set.setText(_translate("Form", "사용자 설정"))

        windows_img = QPixmap("./mainFrame/windows.png")
        windows_tag = windows_img.scaled(167, 37)
        self.windows.setText(_translate("Form", "windows"))
        self.windows.setPixmap(QPixmap(windows_tag))
        self.windows.mousePressEvent = self.select_windows
        self.windows_current = "click_no"

        mac_img = QPixmap("./mainFrame/macOS.png")
        mac_tag = mac_img.scaled(161, 37)
        self.mac_os.setText(_translate("Form", "masOS"))
        self.mac_os.setPixmap(QPixmap(mac_tag))
        self.mac_os.mousePressEvent = self.select_mac_os
        self.mac_os_current = "click_no"
        self.mac_os.setDisabled(True)

        excel_img = QPixmap("./mainFrame/excel.png")
        excel_tag = excel_img.scaled(85, 37)
        self.excel.setText(_translate("Form", "excel"))
        self.excel.setPixmap(QPixmap(excel_tag))
        self.excel.mousePressEvent = self.select_excel
        self.excel_current = "click_no"
        self.excel.setDisabled(True)

        ppt_img = QPixmap("./mainFrame/ppt.png")
        ppt_tag = ppt_img.scaled(141, 37)
        self.ppt.setText(_translate("Form", "ppt"))
        self.ppt.setPixmap(QPixmap(ppt_tag))
        self.ppt.mousePressEvent = self.select_ppt
        self.ppt_current = "click_no"
        self.ppt.setDisabled(True)

        self.active_ppt = QPixmap("./mainFrame/active_ppt.png")
        self.active_ppt = self.active_ppt.scaled(127, 24)
        self.active_excel = QPixmap("./mainFrame/active_excel.png")
        self.active_excel = self.active_excel.scaled(75, 23)
        self.active_mac_os = QPixmap("./mainFrame/active_macOS.png")
        self.active_mac_os = self.active_mac_os.scaled(140, 22)
        self.active_windows = QPixmap("./mainFrame/active_windows.png")
        self.active_windows = self.active_windows.scaled(174, 26)

        self.active_app.setText(_translate("Form", "-----"))

        self.notice2.setText(_translate("Form", "비 활성화된 적용된 아이콘들은 추후 제공될 예정입니다."))
        self.notice3.setText(_translate("Form", "2020년 봄 업데이트 예정"))
        self.notice1.setText(_translate("Form", "...."))

        self.gesture_dic = {self.linear1: "click_no"}
        self.gesture_dic[self.linear2] = "click_no"
        self.gesture_dic[self.linear3] = "click_no"
        self.gesture_dic[self.linear4] = "click_no"
        self.gesture_dic[self.linear5] = "click_no"
        self.gesture_dic[self.linear6] = "click_no"
        self.gesture_dic[self.linear7] = "click_no"
        self.gesture_dic[self.linear8] = "click_no"
        self.gesture_dic[self.curve1] = "click_no"
        self.gesture_dic[self.curve2] = "click_no"
        self.gesture_dic[self.curve3] = "click_no"
        self.gesture_dic[self.curve4] = "click_no"
        self.gesture_dic[self.overlap1] = "click_no"
        self.gesture_dic[self.overlap2] = "click_no"
        self.gesture_dic[self.overlap3] = "click_no"
        self.gesture_dic[self.overlap4] = "click_no"

    def select_ppt(self, event):
        self.excel_current = "click_no"
        self.excel.setStyleSheet("background-color: white")
        self.windows_current = "click_no"
        self.windows.setStyleSheet("background-color: white")
        # self.mac_os_current = "click_no"
        # self.mac_os.setStyleSheet("background-color: white")

        if self.ppt_current == "click_no":
            self.ppt.setStyleSheet("background-color: '#fe9801'")
            self.ppt_current = "click_yes"
            self.active_app.setPixmap(QPixmap(self.active_ppt))
        elif self.ppt_current == "click_yes":
            self.ppt.setStyleSheet("background-color: white")
            self.ppt_current = "click_no"
            self.active_app.clear()

    def select_excel(self, event):
        self.ppt_current = "click_no"
        self.ppt.setStyleSheet("background-color: white")
        self.windows_current = "click_no"
        self.windows.setStyleSheet("background-color: white")
        # self.mac_os_current = "click_no"
        # self.mac_os.setStyleSheet("background-color: white")

        if self.excel_current == "click_no":
            self.excel.setStyleSheet("background-color: '#fe9801'")
            self.excel_current = "click_yes"
            self.active_app.setPixmap(QPixmap(self.active_excel))
        elif self.excel_current == "click_yes":
            self.excel.setStyleSheet("background-color: white")
            self.excel_current = "click_no"
            self.active_app.clear()

    def select_mac_os(self, event):
        self.excel_current = "click_no"
        self.excel.setStyleSheet("background-color: white")
        self.windows_current = "click_no"
        self.windows.setStyleSheet("background-color: white")
        self.ppt_current = "click_no"
        self.ppt.setStyleSheet("background-color: white")

        if self.mac_os_current == "click_no":
            self.mac_os.setStyleSheet("background-color: '#fe9801'")
            self.mac_os_current = "click_yes"
            self.active_app.setPixmap(QPixmap(self.active_mac_os))
        elif self.mac_os_current == "click_yes":
            self.mac_os.setStyleSheet("background-color: white")
            self.mac_os_current = "click_no"
            self.active_app.clear()

    def select_windows(self, event):
        self.excel_current = "click_no"
        self.excel.setStyleSheet("background-color: white")
        self.ppt_current = "click_no"
        self.ppt.setStyleSheet("background-color: white")
        # self.mac_os_current = "click_no"
        # self.mac_os.setStyleSheet("background-color: white")
        i = 0
        while True:
            list(self.gesture_dic.items())[i][0].setStyleSheet("background-color: white")
            self.gesture_dic[list(self.gesture_dic.items())[i][0]] = "click_no"
            i = i + 1
            if i == 16: break

        if self.windows_current == "click_no":
            self.windows.setStyleSheet("background-color: '#fe9801'")
            self.windows_current = "click_yes"
            self.active_app.setPixmap(QPixmap(self.active_windows))
        elif self.windows_current == "click_yes":
            self.windows.setStyleSheet("background-color: white")
            self.windows_current = "click_no"
            self.active_app.clear()

            self.touch_des3.clear()
            self.touch_des3.addItem("---명령선택---")
            self.touch_des3.model().item(0).setEnabled(False)

    def select_linear1(self, event):
        i = 0
        while True:
            if i == 0:
                if list(self.gesture_dic.items())[i][1] == "click_no":
                    list(self.gesture_dic.items())[i][0].setStyleSheet(
                        "background-color: '#fe9801'; border-radius: 10px;")
                    self.gesture_dic[list(self.gesture_dic.items())[i][0]] = "click_yes"
                elif list(self.gesture_dic.items())[i][1] == "click_yes":
                    list(self.gesture_dic.items())[i][0].setStyleSheet("background-color: white")
                    self.gesture_dic[list(self.gesture_dic.items())[i][0]] = "click_no"
            else:
                list(self.gesture_dic.items())[i][0].setStyleSheet("background-color: white")
                self.gesture_dic[list(self.gesture_dic.items())[i][0]] = "click_no"
            i = i + 1

            if i == 16:
                break

        self.touch_des3.clear()
        self.touch_des3.addItem("---명령선택---")
        self.touch_des3.model().item(0).setEnabled(False)

        movie = QMovie("./setting/move_video/linear1.gif")
        self.video.setMovie(movie)
        movie.start()

    def select_linear2(self, event):
        i = 0
        while True:
            if i == 1:
                if list(self.gesture_dic.items())[i][1] == "click_no":
                    list(self.gesture_dic.items())[i][0].setStyleSheet(
                        "background-color: '#fe9801'; border-radius: 10px;")
                    self.gesture_dic[list(self.gesture_dic.items())[i][0]] = "click_yes"
                elif list(self.gesture_dic.items())[i][1] == "click_yes":
                    list(self.gesture_dic.items())[i][0].setStyleSheet("background-color: white")
                    self.gesture_dic[list(self.gesture_dic.items())[i][0]] = "click_no"
            else:
                list(self.gesture_dic.items())[i][0].setStyleSheet("background-color: white")
                self.gesture_dic[list(self.gesture_dic.items())[i][0]] = "click_no"
            i = i + 1

            if i == 16:
                break

        self.touch_des3.clear()
        self.touch_des3.addItem("---명령선택---")
        self.touch_des3.model().item(0).setEnabled(False)

        movie = QMovie("./setting/move_video/linear2.gif")
        self.video.setMovie(movie)
        movie.start()

    def select_linear3(self, event):
        i = 0
        while True:
            if i == 2:
                if list(self.gesture_dic.items())[i][1] == "click_no":
                    list(self.gesture_dic.items())[i][0].setStyleSheet(
                        "background-color: '#fe9801'; border-radius: 10px;")
                    self.gesture_dic[list(self.gesture_dic.items())[i][0]] = "click_yes"
                elif list(self.gesture_dic.items())[i][1] == "click_yes":
                    list(self.gesture_dic.items())[i][0].setStyleSheet("background-color: white")
                    self.gesture_dic[list(self.gesture_dic.items())[i][0]] = "click_no"
            else:
                list(self.gesture_dic.items())[i][0].setStyleSheet("background-color: white")
                self.gesture_dic[list(self.gesture_dic.items())[i][0]] = "click_no"
            i = i + 1

            if i == 16:
                break

        if self.windows_current == "click_yes" and list(self.gesture_dic.items())[2][1] == "click_yes":
            self.touch_des3.clear()
            self.touch_des3.addItem("---명령선택---")
            self.touch_des3.addItem("시작화면 열기(Default)")
            self.touch_des3.addItem("윈도우 작업 보기")
            self.touch_des3.addItem("윈도우 검색 창 실행")
            self.touch_des3.model().item(0).setEnabled(False)
        else:
            self.touch_des3.clear()
            self.touch_des3.addItem("---명령선택---")
            self.touch_des3.model().item(0).setEnabled(False)

        movie = QMovie("./setting/move_video/linear3.gif")
        self.video.setMovie(movie)
        movie.start()

    def select_linear4(self, event):
        i = 0
        while True:
            if i == 3:
                if list(self.gesture_dic.items())[i][1] == "click_no":
                    list(self.gesture_dic.items())[i][0].setStyleSheet(
                        "background-color: '#fe9801'; border-radius: 10px;")
                    self.gesture_dic[list(self.gesture_dic.items())[i][0]] = "click_yes"
                elif list(self.gesture_dic.items())[i][1] == "click_yes":
                    list(self.gesture_dic.items())[i][0].setStyleSheet("background-color: white")
                    self.gesture_dic[list(self.gesture_dic.items())[i][0]] = "click_no"
            else:
                list(self.gesture_dic.items())[i][0].setStyleSheet("background-color: white")
                self.gesture_dic[list(self.gesture_dic.items())[i][0]] = "click_no"
            i = i + 1

            if i == 16:
                break

        if self.windows_current == "click_yes" and list(self.gesture_dic.items())[3][1] == "click_yes":
            self.touch_des3.clear()
            self.touch_des3.addItem("---명령선택---")
            self.touch_des3.addItem("모든창 최소화(Default)")
            self.touch_des3.addItem("돋보기 실행")
            self.touch_des3.addItem("탐색기 실행")
            self.touch_des3.model().item(0).setEnabled(False)
        else:
            self.touch_des3.clear()
            self.touch_des3.addItem("---명령선택---")
            self.touch_des3.model().item(0).setEnabled(False)

        movie = QMovie("./setting/move_video/linear4.gif")
        self.video.setMovie(movie)
        movie.start()

    def select_linear5(self, event):
        i = 0
        while True:
            if i == 4:
                if list(self.gesture_dic.items())[i][1] == "click_no":
                    list(self.gesture_dic.items())[i][0].setStyleSheet(
                        "background-color: '#fe9801'; border-radius: 10px;")
                    self.gesture_dic[list(self.gesture_dic.items())[i][0]] = "click_yes"
                elif list(self.gesture_dic.items())[i][1] == "click_yes":
                    list(self.gesture_dic.items())[i][0].setStyleSheet("background-color: white")
                    self.gesture_dic[list(self.gesture_dic.items())[i][0]] = "click_no"
            else:
                list(self.gesture_dic.items())[i][0].setStyleSheet("background-color: white")
                self.gesture_dic[list(self.gesture_dic.items())[i][0]] = "click_no"
            i = i + 1

            if i == 16:
                break

        self.touch_des3.clear()
        self.touch_des3.addItem("---명령선택---")
        self.touch_des3.model().item(0).setEnabled(False)

        movie = QMovie("./setting/move_video/linear5.gif")
        self.video.setMovie(movie)
        movie.start()

    def select_linear6(self, event):
        i = 0
        while True:
            if i == 5:
                if list(self.gesture_dic.items())[i][1] == "click_no":
                    list(self.gesture_dic.items())[i][0].setStyleSheet(
                        "background-color: '#fe9801'; border-radius: 10px;")
                    self.gesture_dic[list(self.gesture_dic.items())[i][0]] = "click_yes"
                elif list(self.gesture_dic.items())[i][1] == "click_yes":
                    list(self.gesture_dic.items())[i][0].setStyleSheet("background-color: white")
                    self.gesture_dic[list(self.gesture_dic.items())[i][0]] = "click_no"
            else:
                list(self.gesture_dic.items())[i][0].setStyleSheet("background-color: white")
                self.gesture_dic[list(self.gesture_dic.items())[i][0]] = "click_no"
            i = i + 1

            if i == 16:
                break

        self.touch_des3.clear()
        self.touch_des3.addItem("---명령선택---")
        self.touch_des3.model().item(0).setEnabled(False)

        movie = QMovie("./setting/move_video/linear6.gif")
        self.video.setMovie(movie)
        movie.start()

    def select_linear7(self, event):
        i = 0
        while True:
            if i == 6:
                if list(self.gesture_dic.items())[i][1] == "click_no":
                    list(self.gesture_dic.items())[i][0].setStyleSheet(
                        "background-color: '#fe9801'; border-radius: 10px;")
                    self.gesture_dic[list(self.gesture_dic.items())[i][0]] = "click_yes"
                elif list(self.gesture_dic.items())[i][1] == "click_yes":
                    list(self.gesture_dic.items())[i][0].setStyleSheet("background-color: white")
                    self.gesture_dic[list(self.gesture_dic.items())[i][0]] = "click_no"
            else:
                list(self.gesture_dic.items())[i][0].setStyleSheet("background-color: white")
                self.gesture_dic[list(self.gesture_dic.items())[i][0]] = "click_no"
            i = i + 1

            if i == 16:
                break

        self.touch_des3.clear()
        self.touch_des3.addItem("---명령선택---")
        self.touch_des3.model().item(0).setEnabled(False)

        movie = QMovie("./setting/move_video/loading.gif")
        self.video.setMovie(movie)
        movie.start()

    def select_linear8(self, event):
        i = 0
        while True:
            if i == 7:
                if list(self.gesture_dic.items())[i][1] == "click_no":
                    list(self.gesture_dic.items())[i][0].setStyleSheet(
                        "background-color: '#fe9801'; border-radius: 10px;")
                    self.gesture_dic[list(self.gesture_dic.items())[i][0]] = "click_yes"
                elif list(self.gesture_dic.items())[i][1] == "click_yes":
                    list(self.gesture_dic.items())[i][0].setStyleSheet("background-color: white")
                    self.gesture_dic[list(self.gesture_dic.items())[i][0]] = "click_no"
            else:
                list(self.gesture_dic.items())[i][0].setStyleSheet("background-color: white")
                self.gesture_dic[list(self.gesture_dic.items())[i][0]] = "click_no"
            i = i + 1

            if i == 16:
                break

        self.touch_des3.clear()
        self.touch_des3.addItem("---명령선택---")
        self.touch_des3.model().item(0).setEnabled(False)

        movie = QMovie("./setting/move_video/loading.gif")
        self.video.setMovie(movie)
        movie.start()

    def select_curve1(self, event):
        i = 0
        while True:
            if i == 8:
                if list(self.gesture_dic.items())[i][1] == "click_no":
                    list(self.gesture_dic.items())[i][0].setStyleSheet(
                        "background-color: '#fe9801'; border-radius: 10px;")
                    self.gesture_dic[list(self.gesture_dic.items())[i][0]] = "click_yes"
                elif list(self.gesture_dic.items())[i][1] == "click_yes":
                    list(self.gesture_dic.items())[i][0].setStyleSheet("background-color: white")
                    self.gesture_dic[list(self.gesture_dic.items())[i][0]] = "click_no"
            else:
                list(self.gesture_dic.items())[i][0].setStyleSheet("background-color: white")
                self.gesture_dic[list(self.gesture_dic.items())[i][0]] = "click_no"
            i = i + 1

            if i == 16:
                break

        self.touch_des3.clear()
        self.touch_des3.addItem("---명령선택---")
        self.touch_des3.model().item(0).setEnabled(False)

        movie = QMovie("./setting/move_video/curve1.gif")
        self.video.setMovie(movie)
        movie.start()

    def select_curve2(self, event):
        i = 0
        while True:
            if i == 9:
                if list(self.gesture_dic.items())[i][1] == "click_no":
                    list(self.gesture_dic.items())[i][0].setStyleSheet(
                        "background-color: '#fe9801'; border-radius: 10px;")
                    self.gesture_dic[list(self.gesture_dic.items())[i][0]] = "click_yes"
                elif list(self.gesture_dic.items())[i][1] == "click_yes":
                    list(self.gesture_dic.items())[i][0].setStyleSheet("background-color: white")
                    self.gesture_dic[list(self.gesture_dic.items())[i][0]] = "click_no"
            else:
                list(self.gesture_dic.items())[i][0].setStyleSheet("background-color: white")
                self.gesture_dic[list(self.gesture_dic.items())[i][0]] = "click_no"
            i = i + 1

            if i == 16:
                break

        self.touch_des3.clear()
        self.touch_des3.addItem("---명령선택---")
        self.touch_des3.model().item(0).setEnabled(False)

        movie = QMovie("./setting/move_video/curve2.gif")
        self.video.setMovie(movie)
        movie.start()

    def select_curve3(self, event):
        i = 0
        while True:
            if i == 10:
                if list(self.gesture_dic.items())[i][1] == "click_no":
                    list(self.gesture_dic.items())[i][0].setStyleSheet(
                        "background-color: '#fe9801'; border-radius: 10px;")
                    self.gesture_dic[list(self.gesture_dic.items())[i][0]] = "click_yes"
                elif list(self.gesture_dic.items())[i][1] == "click_yes":
                    list(self.gesture_dic.items())[i][0].setStyleSheet("background-color: white")
                    self.gesture_dic[list(self.gesture_dic.items())[i][0]] = "click_no"
            else:
                list(self.gesture_dic.items())[i][0].setStyleSheet("background-color: white")
                self.gesture_dic[list(self.gesture_dic.items())[i][0]] = "click_no"
            i = i + 1

            if i == 16:
                break

        self.touch_des3.clear()
        self.touch_des3.addItem("---명령선택---")
        self.touch_des3.model().item(0).setEnabled(False)

        movie = QMovie("./setting/move_video/loading.gif")
        self.video.setMovie(movie)
        movie.start()

    def select_curve4(self, event):
        i = 0
        while True:
            if i == 11:
                if list(self.gesture_dic.items())[i][1] == "click_no":
                    list(self.gesture_dic.items())[i][0].setStyleSheet(
                        "background-color: '#fe9801'; border-radius: 10px;")
                    self.gesture_dic[list(self.gesture_dic.items())[i][0]] = "click_yes"
                elif list(self.gesture_dic.items())[i][1] == "click_yes":
                    list(self.gesture_dic.items())[i][0].setStyleSheet("background-color: white")
                    self.gesture_dic[list(self.gesture_dic.items())[i][0]] = "click_no"
            else:
                list(self.gesture_dic.items())[i][0].setStyleSheet("background-color: white")
                self.gesture_dic[list(self.gesture_dic.items())[i][0]] = "click_no"
            i = i + 1

            if i == 16:
                break

        self.touch_des3.clear()
        self.touch_des3.addItem("---명령선택---")
        self.touch_des3.model().item(0).setEnabled(False)

        movie = QMovie("./setting/move_video/loading.gif")
        self.video.setMovie(movie)
        movie.start()

    def select_overlap1(self, event):
        i = 0
        while True:
            if i == 12:
                if list(self.gesture_dic.items())[i][1] == "click_no":
                    list(self.gesture_dic.items())[i][0].setStyleSheet(
                        "background-color: '#fe9801'; border-radius: 10px;")
                    self.gesture_dic[list(self.gesture_dic.items())[i][0]] = "click_yes"
                elif list(self.gesture_dic.items())[i][1] == "click_yes":
                    list(self.gesture_dic.items())[i][0].setStyleSheet("background-color: white")
                    self.gesture_dic[list(self.gesture_dic.items())[i][0]] = "click_no"
            else:
                list(self.gesture_dic.items())[i][0].setStyleSheet("background-color: white")
                self.gesture_dic[list(self.gesture_dic.items())[i][0]] = "click_no"
            i = i + 1

            if i == 16:
                break

        self.touch_des3.clear()
        self.touch_des3.addItem("---명령선택---")
        self.touch_des3.model().item(0).setEnabled(False)

        movie = QMovie("./setting/move_video/overlap1.gif")
        self.video.setMovie(movie)
        movie.start()

    def select_overlap2(self, event):
        i = 0
        while True:
            if i == 13:
                if list(self.gesture_dic.items())[i][1] == "click_no":
                    list(self.gesture_dic.items())[i][0].setStyleSheet(
                        "background-color: '#fe9801'; border-radius: 10px;")
                    self.gesture_dic[list(self.gesture_dic.items())[i][0]] = "click_yes"
                elif list(self.gesture_dic.items())[i][1] == "click_yes":
                    list(self.gesture_dic.items())[i][0].setStyleSheet("background-color: white")
                    self.gesture_dic[list(self.gesture_dic.items())[i][0]] = "click_no"
            else:
                list(self.gesture_dic.items())[i][0].setStyleSheet("background-color: white")
                self.gesture_dic[list(self.gesture_dic.items())[i][0]] = "click_no"
            i = i + 1

            if i == 16:
                break

        self.touch_des3.clear()
        self.touch_des3.addItem("---명령선택---")
        self.touch_des3.model().item(0).setEnabled(False)

        movie = QMovie("./setting/move_video/overlap2.gif")
        self.video.setMovie(movie)
        movie.start()

    def select_overlap3(self, event):
        i = 0
        while True:
            if i == 14:
                if list(self.gesture_dic.items())[i][1] == "click_no":
                    list(self.gesture_dic.items())[i][0].setStyleSheet(
                        "background-color: '#fe9801'; border-radius: 10px;")
                    self.gesture_dic[list(self.gesture_dic.items())[i][0]] = "click_yes"
                elif list(self.gesture_dic.items())[i][1] == "click_yes":
                    list(self.gesture_dic.items())[i][0].setStyleSheet("background-color: white")
                    self.gesture_dic[list(self.gesture_dic.items())[i][0]] = "click_no"
            else:
                list(self.gesture_dic.items())[i][0].setStyleSheet("background-color: white")
                self.gesture_dic[list(self.gesture_dic.items())[i][0]] = "click_no"
            i = i + 1

            if i == 16:
                break

        self.touch_des3.clear()
        self.touch_des3.addItem("---명령선택---")
        self.touch_des3.model().item(0).setEnabled(False)

        movie = QMovie("./setting/move_video/loading.gif")
        self.video.setMovie(movie)
        movie.start()

    def select_overlap4(self, event):
        i = 0
        while True:
            if i == 15:
                if list(self.gesture_dic.items())[i][1] == "click_no":
                    list(self.gesture_dic.items())[i][0].setStyleSheet(
                        "background-color: '#fe9801'; border-radius: 10px;")
                    self.gesture_dic[list(self.gesture_dic.items())[i][0]] = "click_yes"
                elif list(self.gesture_dic.items())[i][1] == "click_yes":
                    list(self.gesture_dic.items())[i][0].setStyleSheet("background-color: white")
                    self.gesture_dic[list(self.gesture_dic.items())[i][0]] = "click_no"
            else:
                list(self.gesture_dic.items())[i][0].setStyleSheet("background-color: white")
                self.gesture_dic[list(self.gesture_dic.items())[i][0]] = "click_no"
            i = i + 1

            if i == 16:
                break

        self.touch_des3.clear()
        self.touch_des3.addItem("---명령선택---")
        self.touch_des3.model().item(0).setEnabled(False)

        movie = QMovie("./setting/move_video/loading.gif")
        self.video.setMovie(movie)
        movie.start()

    # def select_combobox1(self):
    #     for i in range(4):
    #         self.touch_des1.model().item(i + 1).setEnabled(True)
    #         self.touch_des2.model().item(i + 1).setEnabled(True)
    #         self.touch_des3.model().item(i + 1).setEnabled(True)
    #
    #         td_index1 = self.touch_des1.currentIndex()
    #         td_index2 = self.touch_des2.currentIndex()
    #         td_index3 = self.touch_des3.currentIndex()
    #         if td_index1 == 4 and td_index2 != 4 and td_index3 != 4:
    #             self.touch_des1.model().item(td_index2).setEnabled(False)
    #             self.touch_des1.model().item(td_index3).setEnabled(False)
    #             self.touch_des2.model().item(td_index3).setEnabled(False)
    #             self.touch_des3.model().item(td_index2).setEnabled(False)
    #         elif td_index2 == 4 and td_index1 != 4 and td_index3 != 4:
    #             self.touch_des1.model().item(td_index3).setEnabled(False)
    #             self.touch_des2.model().item(td_index1).setEnabled(False)
    #             self.touch_des2.model().item(td_index3).setEnabled(False)
    #             self.touch_des3.model().item(td_index1).setEnabled(False)
    #         elif td_index3 == 4 and td_index1 != 4 and td_index2 != 4:
    #             self.touch_des1.model().item(td_index2).setEnabled(False)
    #             self.touch_des2.model().item(td_index1).setEnabled(False)
    #             self.touch_des3.model().item(td_index1).setEnabled(False)
    #             self.touch_des3.model().item(td_index2).setEnabled(False)
    #         elif td_index1 == 4 and td_index2 == 4 and td_index3 != 4:
    #             self.touch_des1.model().item(td_index3).setEnabled(False)
    #             self.touch_des2.model().item(td_index3).setEnabled(False)
    #         elif td_index1 == 4 and td_index3 == 4 and td_index2 != 4:
    #             self.touch_des1.model().item(td_index2).setEnabled(False)
    #             self.touch_des3.model().item(td_index2).setEnabled(False)
    #         elif td_index2 == 4 and td_index3 == 4 and td_index1 != 4:
    #             self.touch_des2.model().item(td_index1).setEnabled(False)
    #             self.touch_des3.model().item(td_index1).setEnabled(False)
    #         else:
    #             self.touch_des1.model().item(td_index2).setEnabled(False)
    #             self.touch_des1.model().item(td_index3).setEnabled(False)
    #             self.touch_des2.model().item(td_index1).setEnabled(False)
    #             self.touch_des2.model().item(td_index3).setEnabled(False)
    #             self.touch_des3.model().item(td_index1).setEnabled(False)
    #             self.touch_des3.model().item(td_index2).setEnabled(False)
    #
    # def select_combobox2(self):
    #     for i in range(4):
    #         self.touch_des1.model().item(i + 1).setEnabled(True)
    #         self.touch_des2.model().item(i + 1).setEnabled(True)
    #         self.touch_des3.model().item(i + 1).setEnabled(True)
    #
    #     td_index1 = self.touch_des1.currentIndex()
    #     td_index2 = self.touch_des2.currentIndex()
    #     td_index3 = self.touch_des3.currentIndex()
    #     if td_index1 == 4 and td_index2 != 4 and td_index3 != 4:
    #         self.touch_des1.model().item(td_index2).setEnabled(False)
    #         self.touch_des1.model().item(td_index3).setEnabled(False)
    #         self.touch_des2.model().item(td_index3).setEnabled(False)
    #         self.touch_des3.model().item(td_index2).setEnabled(False)
    #     elif td_index2 == 4 and td_index1 != 4 and td_index3 != 4:
    #         self.touch_des1.model().item(td_index3).setEnabled(False)
    #         self.touch_des2.model().item(td_index1).setEnabled(False)
    #         self.touch_des2.model().item(td_index3).setEnabled(False)
    #         self.touch_des3.model().item(td_index1).setEnabled(False)
    #     elif td_index3 == 4 and td_index1 != 4 and td_index2 != 4:
    #         self.touch_des1.model().item(td_index2).setEnabled(False)
    #         self.touch_des2.model().item(td_index1).setEnabled(False)
    #         self.touch_des3.model().item(td_index1).setEnabled(False)
    #         self.touch_des3.model().item(td_index2).setEnabled(False)
    #     elif td_index1 == 4 and td_index2 == 4 and td_index3 != 4:
    #         self.touch_des1.model().item(td_index3).setEnabled(False)
    #         self.touch_des2.model().item(td_index3).setEnabled(False)
    #     elif td_index1 == 4 and td_index3 == 4 and td_index2 != 4:
    #         self.touch_des1.model().item(td_index2).setEnabled(False)
    #         self.touch_des3.model().item(td_index2).setEnabled(False)
    #     elif td_index2 == 4 and td_index3 == 4 and td_index1 != 4:
    #         self.touch_des2.model().item(td_index1).setEnabled(False)
    #         self.touch_des3.model().item(td_index1).setEnabled(False)
    #     else:
    #         self.touch_des1.model().item(td_index2).setEnabled(False)
    #         self.touch_des1.model().item(td_index3).setEnabled(False)
    #         self.touch_des2.model().item(td_index1).setEnabled(False)
    #         self.touch_des2.model().item(td_index3).setEnabled(False)
    #         self.touch_des3.model().item(td_index1).setEnabled(False)
    #         self.touch_des3.model().item(td_index2).setEnabled(False)
    #
    # def select_combobox3(self):
    #     for i in range(4):
    #         self.touch_des1.model().item(i + 1).setEnabled(True)
    #         self.touch_des2.model().item(i + 1).setEnabled(True)
    #         self.touch_des3.model().item(i + 1).setEnabled(True)
    #
    #     td_index1 = self.touch_des1.currentIndex()
    #     td_index2 = self.touch_des2.currentIndex()
    #     td_index3 = self.touch_des3.currentIndex()
    #     if td_index1 == 4 and td_index2 != 4 and td_index3 != 4:
    #         self.touch_des1.model().item(td_index2).setEnabled(False)
    #         self.touch_des1.model().item(td_index3).setEnabled(False)
    #         self.touch_des2.model().item(td_index3).setEnabled(False)
    #         self.touch_des3.model().item(td_index2).setEnabled(False)
    #     elif td_index2 == 4 and td_index1 != 4 and td_index3 != 4:
    #         self.touch_des1.model().item(td_index3).setEnabled(False)
    #         self.touch_des2.model().item(td_index1).setEnabled(False)
    #         self.touch_des2.model().item(td_index3).setEnabled(False)
    #         self.touch_des3.model().item(td_index1).setEnabled(False)
    #     elif td_index3 == 4 and td_index1 != 4 and td_index2 != 4:
    #         self.touch_des1.model().item(td_index2).setEnabled(False)
    #         self.touch_des2.model().item(td_index1).setEnabled(False)
    #         self.touch_des3.model().item(td_index1).setEnabled(False)
    #         self.touch_des3.model().item(td_index2).setEnabled(False)
    #     elif td_index1 == 4 and td_index2 == 4 and td_index3 != 4:
    #         self.touch_des1.model().item(td_index3).setEnabled(False)
    #         self.touch_des2.model().item(td_index3).setEnabled(False)
    #     elif td_index1 == 4 and td_index3 == 4 and td_index2 != 4:
    #         self.touch_des1.model().item(td_index2).setEnabled(False)
    #         self.touch_des3.model().item(td_index2).setEnabled(False)
    #     elif td_index2 == 4 and td_index3 == 4 and td_index1 != 4:
    #         self.touch_des2.model().item(td_index1).setEnabled(False)
    #         self.touch_des3.model().item(td_index1).setEnabled(False)
    #     else:
    #         self.touch_des1.model().item(td_index2).setEnabled(False)
    #         self.touch_des1.model().item(td_index3).setEnabled(False)
    #         self.touch_des2.model().item(td_index1).setEnabled(False)
    #         self.touch_des2.model().item(td_index3).setEnabled(False)
    #         self.touch_des3.model().item(td_index1).setEnabled(False)
    #         self.touch_des3.model().item(td_index2).setEnabled(False)

    # def select_combobox3(self):
    #     touch_des1_index = self.touch_des3.findText(self.touch_des3.currentText())
    #     touch_des2_index = self.touch_des3.findText(self.touch_des3.currentText())
    #     self.touch_des1.model().item(touch_des1_index).setEnabled(False)
    #     self.touch_des2.model().item(touch_des2_index).setEnabled(False)

    # def press_submit_btn(self):
    #     self.submit_btn.setStyleSheet("background: #ABA79B;  border: 3px solid #A8A69E;")
    #
    # def release_submit_btn(self):
    #     if self.touch_des1.currentIndex() == 0 or self.touch_des2.currentIndex() == 0 or self.touch_des3.currentIndex() == 0:
    #         reply = QtWidgets.QMessageBox.question(Form, 'Please check', '제스처를 선택하세요!', QtWidgets.QMessageBox.Ok)
    #         self.submit_btn.setStyleSheet("background: #CBC7B8;  border: 2px solid #A8A69E;")
    #     else:
    #         reply = QtWidgets.QMessageBox.question(Form, 'Please check', '사용할 준비가 되었습니까?', QtWidgets.QMessageBox.Ok)
    #
    #         self.submit_btn.setStyleSheet("background: #CBC7B8;  border: 2px solid #A8A69E;")
    #
    #         self.touch_des1.setDisabled(True)
    #         self.touch_des2.setDisabled(True)
    #         self.touch_des3.setDisabled(True)
    #
    #         self.submit_btn.setStyleSheet("background: #CBC7B8;  border: 2px solid #A8A69E;")
    #
    #         i = 0
    #         while True:
    #             # print(list(self.gesture_dic.items())[i][1])
    #             # i = i + 1
    #             if list(self.gesture_dic.items())[i][1] == "click_yes":
    #                 print(list(self.gesture_dic.items())[i][0].objectName())
    #                 break
    #             i = i + 1

    # def press_end_btn(self):
    #     self.end_btn.setStyleSheet("background: #ABA79B;  border: 3px solid #A8A69E;")
    #
    # def release_end_btn(self):
    #     self.end_btn.setStyleSheet("background: #CBC7B8;  border: 2px solid #A8A69E;")
    #
    #
    #     self.touch_des1.setEnabled(True)
    #     self.touch_des2.setEnabled(True)
    #     self.touch_des3.setEnabled(True)
    #
    #     self.touch_des1.setCurrentIndex(0)
    #     self.touch_des2.setCurrentIndex(0)
    #     self.touch_des3.setCurrentIndex(0)

    def select_combobox3(self):
        # print(self.touch_des3.currentText())
        pass

    def press_save_btn(self):
        self.save_btn.setStyleSheet("background: #ABA79B;  border: 3px solid #A8A69E;")

    def release_save_btn(self):
        self.save_btn.setStyleSheet("background: #CBC7B8;  border: 2px solid #A8A69E;")

        self.touch_des3.setEnabled(True)

        if self.touch_des3.currentIndex() == 0:
            reply = QtWidgets.QMessageBox.question(Form, 'Please check', '제스처와 명령을 선택하세요', QtWidgets.QMessageBox.Ok)
            self.save_btn.setStyleSheet("background: #CBC7B8;  border: 2px solid #A8A69E;")
        else:
            for i in range(0, 16):
                if list(self.gesture_dic.items())[i][1] == "click_yes":
                    gesture_name = list(self.gesture_dic.items())[i][0].objectName()
                    command = self.touch_des3.currentText()

                    f = open("./setting/pero_setting_data/gesture" + str(i + 1) + ".txt", "w")
                    f.write('%s:%s' % (gesture_name, command))
                    f.close()

                    f = open("./setting/pero_setting_data/pero_state.txt", "w")
                    f.write("user")
                    f.close()
                    # current_process.kill()
                    # current_process = subprocess.Popen('python keyConverterPERO.py', shell=True))

                    list(self.gesture_dic.items())[i][0].setStyleSheet("background-color: white")
                    self.gesture_dic[list(self.gesture_dic.items())[i][0]] = "click_no"

                    self.touch_des3.clear()
                    self.touch_des3.addItem("---명령선택---")
                    self.touch_des3.model().item(0).setEnabled(False)
                    break

            self.touch_des1.setCurrentIndex(0)
            self.touch_des2.setCurrentIndex(0)
            self.touch_des3.setCurrentIndex(0)

            gesture_type = ""
            if gesture_name == "linear3":
                gesture_type = "↑"
            elif gesture_name == "linear4":
                gesture_type = "↓"

            reply = QtWidgets.QMessageBox.question(Form,
                                                   'Please check', gesture_type + ' : ' + command + "\n(으)로 설정되었습니다.",
                                                   QtWidgets.QMessageBox.Ok)

    def press_reset_btn(self):
        self.reset_btn.setStyleSheet(
            "background: #ABA79B;  border: 3px solid #A8A69E; border-radius: 10px; text-align: center;")

    def release_reset_btn(self):
        self.reset_btn.setStyleSheet(
            "background: #CBC7B8;  border: 2px solid #A8A69E; border-radius: 10px; text-align: center;")

        self.touch_des3.setEnabled(True)

        reply = QtWidgets.QMessageBox.question(Form, 'Reset', "초기화되었습니다.", QtWidgets.QMessageBox.Ok)

        self.touch_des1.setCurrentIndex(0)
        self.touch_des2.setCurrentIndex(0)
        self.touch_des3.setCurrentIndex(0)

        self.touch_des3.clear()
        self.touch_des3.addItem("---명령선택---")
        self.touch_des3.model().item(0).setEnabled(False)

        for i in range(0, 16):
            list(self.gesture_dic.items())[i][0].setStyleSheet("background-color: white")
            self.gesture_dic[list(self.gesture_dic.items())[i][0]] = "click_no"

        f = open("./setting/pero_setting_data/pero_state.txt", "w")
        f.write("default")
        f.close()

    def press_quit_btn(self):
        self.quit_btn.setStyleSheet(
            "background: #ABA79B;  border: 3px solid #A8A69E; border-radius: 10px; text-align: center;")

    def release_quit_btn(self):
        self.quit_btn.setStyleSheet(
            "background: #CBC7B8;  border: 2px solid #A8A69E; border-radius: 10px; text-align: center;")

        reply = QtWidgets.QMessageBox.question(Form, 'Quit', "프로그램을 종료하시겠습니까?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:

            f = open("./setting/pero_setting_data/pero_state.txt", "w")
            f.write("default")
            f.close()

            kill_process()
            # print("why?")
        else:
            pass


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
