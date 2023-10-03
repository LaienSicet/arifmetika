from PyQt5 import QtCore, QtGui, QtWidgets
from pickle import load

doska_1 = ["", "", "", "", ""]
doska_2 = ["", "", "", "", ""]

blok_1 = []
blok_2 = []

ohi = ""
dlina = 0

try:
    with open("stat.bin", "rb") as sta:
        S = load(sta)
        dlina = len(S)
except:
    S = []
    ohi = " "*40 + "нет статистики."

def melom_po_doske():
    'вывод "доски" на экран'
    j = 4
    for i in ui.sp_st:
        i.setText(doska_1[j])
        j -= 1
    j = 4
    for i in ui.sp_ot:
        i.setText(doska_2[j])
        j -= 1

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.sp_st = []
        self.sp_ot = []

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1015, 628)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(840, 40, 151, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(809, 375, 181, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(860, 440, 60, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox_2.setFont(font)
        self.spinBox_2.setObjectName("spinBox_2")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(820, 510, 150, 70))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.clicked.connect(smotret)
        self.pushButton.setObjectName("pushButton")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(860, 10, 140, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.label_2_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_2_5.setGeometry(QtCore.QRect(50, 25, 700, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2_5.setFont(font)
        self.label_2_5.setObjectName("label_2_5")

        self.label_2_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_2_6.setGeometry(QtCore.QRect(70, 70, 600, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2_6.setFont(font)
        self.label_2_6.setObjectName("label_2_6")
        self.sp_st.append(self.label_2_6)

        self.label_2_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_2_7.setGeometry(QtCore.QRect(110, 110, 300, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2_7.setFont(font)
        self.label_2_7.setObjectName("label_2_7")
        self.sp_ot.append(self.label_2_7)

        self.label_2_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_2_8.setGeometry(QtCore.QRect(70, 150, 600, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2_8.setFont(font)
        self.label_2_8.setObjectName("label_2_8")
        self.sp_st.append(self.label_2_8)

        self.label_2_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_2_9.setGeometry(QtCore.QRect(110, 190, 300, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2_9.setFont(font)
        self.label_2_9.setObjectName("label_2_9")
        self.sp_ot.append(self.label_2_9)

        self.label_2_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_2_11.setGeometry(QtCore.QRect(110, 280, 300, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2_11.setFont(font)
        self.label_2_11.setObjectName("label_2_11")
        self.sp_ot.append(self.label_2_11)

        self.label_2_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_2_10.setGeometry(QtCore.QRect(70, 240, 600, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2_10.setFont(font)
        self.label_2_10.setObjectName("label_2_10")
        self.sp_st.append(self.label_2_10)

        self.label_2_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_2_13.setGeometry(QtCore.QRect(110, 370, 300, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2_13.setFont(font)
        self.label_2_13.setObjectName("label_2_13")
        self.sp_ot.append(self.label_2_13)

        self.label_2_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_2_12.setGeometry(QtCore.QRect(70, 330, 600, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2_12.setFont(font)
        self.label_2_12.setObjectName("label_2_12")
        self.sp_st.append(self.label_2_12)

        self.label_2_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_2_14.setGeometry(QtCore.QRect(60, 440, 600, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2_14.setFont(font)
        self.label_2_14.setObjectName("label_2_14")
        self.sp_st.append(self.label_2_14)

        self.label_2_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_2_15.setGeometry(QtCore.QRect(110, 470, 300, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2_15.setFont(font)
        self.label_2_15.setObjectName("label_2_15")
        self.sp_ot.append(self.label_2_15)

        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(30, 550, 721, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")

        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(870, 90, 100, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1015, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "статистика"))
        self.label_2.setText(_translate("MainWindow", "всего уроков:"))
        self.label_3.setText(_translate("MainWindow", "выбрать урок:"))
        self.pushButton.setText(_translate("MainWindow", "смотреть"))
        self.label_4.setText(_translate("MainWindow", "разработчик: Тарасов Д.Л."))
        self.label_2_5.setText(_translate("MainWindow", "")) #"*тема*******или вывод*************************************"

        self.label_2_6.setText(_translate("MainWindow", "*5й пример*"))
        self.label_2_7.setText(_translate("MainWindow", "*5й ответ*"))
        self.label_2_8.setText(_translate("MainWindow", "*4й пример*"))
        self.label_2_9.setText(_translate("MainWindow", "*4й ответ*"))
        self.label_2_11.setText(_translate("MainWindow", "*3й ответ*"))
        self.label_2_10.setText(_translate("MainWindow", "*3й пример*"))
        self.label_2_13.setText(_translate("MainWindow", "*2й ответ*"))
        self.label_2_12.setText(_translate("MainWindow", "*2й пример*"))
        self.label_2_14.setText(_translate("MainWindow", "*1й пример*"))
        self.label_2_15.setText(_translate("MainWindow", "*1й ответ*"))

        self.label_21.setText(_translate("MainWindow", ohi)) #"*тех. строка*************************************************"
        self.label_16.setText(_translate("MainWindow", "  " + str(dlina)))#" *****"

        melom_po_doske()

def kilroi(fraza):
    "заголовок"
    ui.label_2_5.setText(fraza)

def smotret():
    'кнопка.'
    global doska_1, doska_2
    ui.label_21.setText(" ")
    a = ui.spinBox_2.value()-1
    if a < 0:
        ohi = " " * 30 + "введите номер урока. "
        ui.label_21.setText(ohi)
        return False
    elif a + 1 > dlina:
        ohi = " " * 30 + "ещё нет такого урока."
        ui.label_21.setText(ohi)
        return False
    if len(S) == 0:
        ohi = " " * 30 + "нет статистики.."
        ui.label_21.setText(ohi)
        return False
    verno = 0
    ne_ve = 0
    doska_1 = ["", "", "", "", ""]
    doska_2 = ["", "", "", "", ""]
    j = 4
    statistika = S[a]
    for i in statistika:
        if i != "сложность":

            verno += statistika[i][0]
            ne_ve += statistika[i][1]
            if statistika[i][0] != 0 or statistika[i][1] != 0:
                doska_1[j] = i
                doska_2[j] = f"верно {statistika[i][0]}    |     неверно {statistika[i][1]}"
                j -= 1
    melom_po_doske()
    kilroi(f'ИТОГ: верно   {verno}   из   {verno + ne_ve} .         при сложности {str(statistika["сложность"])}')



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
