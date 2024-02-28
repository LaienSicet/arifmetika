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
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1015, 628)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        font_1, font_2, font_3, font_4 = QtGui.QFont(), QtGui.QFont(), QtGui.QFont(), QtGui.QFont()
        self.spisok_f = [[font_1, 7, True, 50], [font_2, 12, False, 50], [font_3, 16, True, 75], [font_4, 20, True, 75]]
        for i in self.spisok_f:
            i[0].setFamily("Segoe Script")
            i[0].setPointSize(i[1])
            i[0].setBold(i[2])
            i[0].setWeight(i[3])

        self.label_2, self.label_3, self.label_4, self.label_16, self.label_21, self.label_2_5, self.label_2_6,\
            self.label_2_7, self.label_2_8, self.label_2_9, self.label_2_10, self.label_2_11, self.label_2_12,\
            self.label_2_13, self.label_2_14, self.label_2_15 = QtWidgets.QLabel(self.centralwidget),\
            QtWidgets.QLabel(self.centralwidget), QtWidgets.QLabel(self.centralwidget),\
            QtWidgets.QLabel(self.centralwidget), QtWidgets.QLabel(self.centralwidget),\
            QtWidgets.QLabel(self.centralwidget), QtWidgets.QLabel(self.centralwidget),\
            QtWidgets.QLabel(self.centralwidget), QtWidgets.QLabel(self.centralwidget),\
            QtWidgets.QLabel(self.centralwidget), QtWidgets.QLabel(self.centralwidget),\
            QtWidgets.QLabel(self.centralwidget), QtWidgets.QLabel(self.centralwidget),\
            QtWidgets.QLabel(self.centralwidget), QtWidgets.QLabel(self.centralwidget),\
            QtWidgets.QLabel(self.centralwidget)

        self.spisok_l = [[self.label_2, 840, 40, 151, 60, font_3, 'всего уроков:'],
                         [self.label_3, 809, 375, 181, 60, font_3, 'выбрать урок:'],
                         [self.label_4, 860, 10, 140, 25, font_1, 'разработчик: Тарасов Д.Л.'],
                         [self.label_16, 870, 90, 100, 60, font_4, "  " + str(dlina)],
                         [self.label_21, 30, 550, 721, 35, font_3, ohi],
                         [self.label_2_5, 50, 25, 700, 35, font_3], [self.label_2_6, 70, 70, 600, 35, font_2],
                         [self.label_2_7, 110, 110, 300, 35, font_2], [self.label_2_8, 70, 150, 600, 35, font_2],
                         [self.label_2_9, 110, 190, 300, 35, font_2], [self.label_2_10, 70, 240, 600, 35, font_2],
                         [self.label_2_11, 110, 280, 300, 35, font_2], [self.label_2_12, 70, 330, 600, 35, font_2],
                         [self.label_2_13, 110, 370, 300, 35, font_2], [self.label_2_14, 60, 440, 600, 35, font_2],
                         [self.label_2_15, 110, 470, 300, 35, font_2]]
        for i in self.spisok_l:
            i[0].setGeometry(QtCore.QRect(i[1], i[2], i[3], i[4]))
            i[0].setFont(i[5])

        self.sp_st = [self.label_2_6, self.label_2_8, self.label_2_10, self.label_2_12, self.label_2_14]
        self.sp_ot = [self.label_2_7, self.label_2_9, self.label_2_11, self.label_2_13, self.label_2_15]


        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(860, 440, 60, 35))
        self.spinBox_2.setFont(font_3)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(820, 510, 150, 70))
        self.pushButton.setFont(font_3)
        self.pushButton.clicked.connect(smotret)

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
        for i in self.spisok_l[0:4:1]:
            i[0].setText(_translate("MainWindow", i[6]))
        self.pushButton.setText(_translate("MainWindow", "смотреть"))
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
