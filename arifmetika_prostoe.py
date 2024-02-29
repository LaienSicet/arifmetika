from PyQt5 import QtCore, QtGui, QtWidgets
from random import randint, choice


diapazon = [0, 0] # [0, 100]
diapazon_1 = [0, 0] # [1, 10]
diapazon_2 = [0, 0] #[1, 50]

# ["сложение", "вычитание", "умножение", "деление", "скобки"]
#statistika = {"сложение": [0, 0], "вычитание": [0, 0], "умножение": [0, 0], "деление": [0, 0], "скобки": [0, 0]}

mir = 0

doska_1 = ["", "", "", "", ""]
doska_2 = ["", "", "", "", ""]

blok_1 = []
blok_2 = []

def vvod(tek, ot=-1000000, do=1000000):
    "отсев ошибок ввода"
    q = 0
    while q != -1:
        try:
            a = int(input(tek))
            if not(ot <= a <= do):
                g = 1 / 0

            q = -1
        except:
            print("увы... что-то нето. повтори.")
            q += 1
    return a


def kilroi(fraza):
    "заголовок"
    ui.label_5.setText(fraza)

class Primer:

    def __init__(self, k=2):
        if self.dei == " + " or self.dei == " - ":
            self.a = []
            for i in range(k):
                self.a.append(randint(diapazon[0], diapazon[1]))
        elif self.dei == " x ":
            self.a = [randint(diapazon_1[0], diapazon_1[1]), randint(diapazon_1[0], diapazon_1[1])]
        elif self.dei == " : ":
            d2 = randint(diapazon_2[0]+1, diapazon_2[1])
            d1 = d2 * randint(diapazon_2[0]+1, diapazon_2[1])
            self.a = [d1, d2]

        self.a.sort(reverse=True)


    def prin_te(self):
        tek = "     "
        for i, n in enumerate(self.a):
            tek += str(n)
            if i != len(self.a) - 1:
                tek += self.dei
            else:
                tek += " = "
        return tek


class Slo(Primer):
    "сложение"

    dei = " + "

    def rez(self):
        self.re = 0
        for i in self.a:
            self.re += i
        return self.re


class Vih(Primer):
    "вычитание"

    dei = " - "

    def rez(self):
        self.re = self.a[0]
        for i in self.a[1::]:
            self.re -= i
        return self.re


class Ymno(Primer):
    "умножение"
    dei = " x "

    def rez(self):
        return self.a[0] * self.a[1]


class Dile(Primer):
    "деление"
    dei = " : "

    def rez(self):
        return int(self.a[0] / self.a[1])


class Skobki:
    "скобки"

    def slo(self, a = randint(diapazon[0], diapazon[1]), b = randint(diapazon[0], diapazon[1])):
        global t
        t.append([str(a), " + ", str(b)])
        #print("сложение", str(a), "+", str(b), "=", a+b)#
        return a+b

    def vih(self, a = randint(diapazon[0], diapazon[1]), b = randint(diapazon[0], diapazon[1])):
        global t
        t.append([ str(a), " - ", str(b)])
        #print("вычитание", str(a), "-", str(b), "=", a - b)#
        return a-b

    def ymno(self, a = randint(diapazon_1[0], diapazon_1[1]), b = randint(diapazon_1[0], diapazon_1[1])):
        global t
        t.append([str(a), " x ", str(b)])
        #print("умножение", str(a), "x", str(b), "=", a * b)#
        return a * b

    def dile(self, a = randint(diapazon_2[0], diapazon_2[1]), b = randint(diapazon_1[0], diapazon_1[1])):
        global t
        t.append([str(a), " : ", str(b)])
        #print("деление", str(a), ":", str(b), "=", a / b)#
        return a / b

    def prin_te(self):
        return self.tek

    def rez(self):
        return int(self.re)

    def __init__(self):
        global t
        vi = randint(1, 9)
        self.re = - 2.6
        v1 = 3
        v2 = 2
        v3 = 1
        v4 = 10
        v5 = 11
        if vi == 1:  # ((  x  ) - ) +  :  =
            while self.re < 0 or v3 * v4 - v5 < 0:  #v1 / v2 != int(v1 / v2) or
                t = []
                v2 = randint(diapazon_1[0]+1, diapazon_1[1])
                v1 = v2 * randint(diapazon_2[0], diapazon_2[1])
                v3 = randint(diapazon_1[0], diapazon_1[1])
                v4 = randint(diapazon_1[0], diapazon_1[1])
                v5 = randint(diapazon[0], diapazon[1])
                self.re = self.slo(self.vih(self.ymno(v3, v4), v5), self.dile(v1, v2))
                self.tek = "((" + t[0][0] + t[0][1] + t[0][2] + ")" + t[1][1] + t[1][2] + ") + "\
                           + t[2][0] + t[2][1] + t[2][2] + " = "
        elif vi == 2: # ( + ) x ( + ) =

            t = []
            v1 = randint(diapazon_1[0], diapazon_1[1])
            v2 = randint(diapazon_1[0], diapazon_1[1])
            v3 = randint(diapazon_1[0], diapazon_1[1])
            v4 = randint(diapazon_1[0], diapazon_1[1])
            self.re = self.ymno(self.slo(v1, v2), self.slo(v3, v4))
            self.tek = "(" + t[0][0] + t[0][1] + t[0][2] + ")" + " x " + "(" + t[1][0] + t[1][1] + t[1][2] + ") = "
        elif vi == 3:#  +  x ( - )  +  =

            while self.re < 0 or v1 < v2:
                t = []
                v1 = randint(diapazon[0], diapazon[1])
                v2 = randint(diapazon[0], diapazon[1])
                v3 = randint(diapazon_1[0], diapazon_1[1])
                v4 = randint(diapazon[0], diapazon[1])
                v5 = randint(diapazon[0], diapazon[1])
                self.re = self.slo(v5, self.slo(self.ymno(v3, self.vih(v1, v2)), v4))
                self.tek = t[3][0] + t[3][1]+ t[1][0] + t[1][1] + "(" + t[0][0] + t[0][1] + t[0][2] + ")" + \
                           t[2][1] + t[2][2] + " = "
        elif vi == 4: # ( : ) -  =

            while self.re < 0:  # or v1 / v2 != int(v1 / v2)
                t = []
                v2 = randint(diapazon_1[0]+1, diapazon_1[1])
                v1 = v2 * randint(diapazon_2[0], diapazon_2[1])
                v3 = randint(diapazon[0], diapazon[1])
                self.re = self.vih(self.dile(v1, v2), v3)
                print(t)
                self.tek = "(" + t[0][0] + t[0][1] + t[0][2] + ")" + t[1][1] + t[1][2] + " = "
        elif vi == 5:  #  (  +  ) x (  -  ) =
            while self.re < 0 or v3 < v4:
                t = []
                v1 = randint(diapazon_1[0], diapazon_1[1])
                v2 = randint(diapazon_1[0], diapazon_1[1])
                v3 = randint(diapazon_1[0], diapazon_1[1])
                v4 = randint(diapazon_1[0], diapazon_1[1])
                self.re = self.ymno(self.slo(v1, v2), self.vih(v3, v4))
                self.tek = "(" + t[0][0] + t[0][1] + t[0][2] + ")" + " x " + "(" + t[1][0] + t[1][1] + t[1][2] + ") = "
        elif vi == 6:  #   x ((  + ) x  ) =
            t = []
            v1 = randint(diapazon_1[0], diapazon_1[1])
            v2 = randint(diapazon_1[0], diapazon_1[1])
            v3 = randint(diapazon[0], diapazon[1])
            v4 = randint(diapazon[0], diapazon[1])
            self.re = self.ymno(v1, self.ymno(self.slo(v3, v4), v2))
            self.tek = t[2][0] + t[2][1] + "((" + t[0][0] + t[0][1] + t[0][2] + ")" + t[1][1] + t [1][2] + ") = "
        elif vi == 7:  #    (((  + )- )+ )+  =
            while self.re < 0 or v1 + v2 < v3:
                t = []
                v1 = randint(diapazon[0], diapazon[1])
                v2 = randint(diapazon[0], diapazon[1])
                v3 = randint(diapazon[0], diapazon[1])
                v4 = randint(diapazon[0], diapazon[1])
                v5 = randint(diapazon[0], diapazon[1])
                self.re = self.slo(self.slo(self.vih(self.slo(v1, v2), v3), v4), v5)
                self.tek = "(((" + t[0][0] + t[0][1] + t[0][2] + ")" + t[1][1] + t[1][2] + ")" +\
                           t[2][1] + t[2][2] + ")" + t[3][1] + t[3][2] + " = "

        elif vi == 8:  #  (  -  ) x (  -  ) =
            while self.re < 0 or v3 < v4 or v1 < v2:
                t = []
                v1 = randint(diapazon_1[0], diapazon_1[1])
                v2 = randint(diapazon_1[0], diapazon_1[1])
                v3 = randint(diapazon_1[0], diapazon_1[1])
                v4 = randint(diapazon_1[0], diapazon_1[1])
                self.re = self.ymno(self.vih(v1, v2), self.vih(v3, v4))
                self.tek = "(" + t[0][0] + t[0][1] + t[0][2] + ")" + " x " + "(" + t[1][0] + t[1][1] + t[1][2] + ") = "
        elif vi == 9: #     x( + )  =
            t = []
            v1 = randint(diapazon_1[0], diapazon_1[1])
            v2 = randint(diapazon_1[0], diapazon_1[1])
            v3 = randint(diapazon_1[0], diapazon_1[1])
            self.re = self.ymno(v3, self.slo(v1, v2))
            self.tek = t[1][0] + t[1][1] + "(" + t[0][0] + t[0][1] + t[0][2] + ")" + " = "


def primer(p, bonus=0):
    if p == "сложение":
        a = Slo(2+bonus)
    elif p == "вычитание":
        a = Vih(2+bonus)
    elif p == "умножение":
        a = Ymno()
    elif p == "деление":
        a = Dile()
    elif p == "скобки":
        try:
            a = Skobki()
        except:
            a = Skobki()
    global verno, ne_ve, REZ
    st = a.prin_te()
    ui.label_20.setText(" " * (50-len(st))+st)
    REZ = a.rez()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1015, 725)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        font_1, font_2, font_3, font_4, font_5, font_6 = QtGui.QFont(), QtGui.QFont(), QtGui.QFont(), QtGui.QFont(),\
            QtGui.QFont(), QtGui.QFont()
        self.spisok_f = [[font_1, 7, True, 75], [font_2, 12, False, 50], [font_3, 12, True, 75], [font_4, 14, True, 75],
                         [font_5, 16, True, 75], [font_6, 18, True, 75]]
        for i in self.spisok_f:
            i[0].setFamily("Segoe Script")
            i[0].setPointSize(i[1])
            i[0].setBold(i[2])
            i[0].setWeight(i[3])

        self.label_5, self.label_20, self.label_21 = QtWidgets.QLabel(self.centralwidget),\
            QtWidgets.QLabel(self.centralwidget), QtWidgets.QLabel(self.centralwidget)
        self.spisok_l_1 = [[self.label_5, 50, 25, 700, 35, font_5], [self.label_20, 40, 530, 600, 35, font_6],
                           [self.label_21, 30, 600, 560, 35, font_5]]
        for i in self.spisok_l_1:
            i[0].setGeometry(QtCore.QRect(i[1], i[2], i[3], i[4]))
            i[0].setFont(i[5])

        self.baza_l_2 = [[850, 50, 80, 35, font_5, 'темы:'], [850, 315, 150, 60, font_5, 'уровень \nсложности:'],
                         [850, 455, 150, 60, font_5, 'количество \nблоков*:'],
                         [860, 10, 140, 25, font_1, 'разработчик: Тарасов Д.Л.'],
                         [855, 555, 140, 25, font_3, '* по 5 примеров.']]
        self.spisok_l_2 = []
        for i in self.baza_l_2:
            self.l = QtWidgets.QLabel(self.centralwidget)
            self.l.setGeometry(QtCore.QRect(i[0], i[1], i[2], i[3]))
            self.l.setFont(i[4])
            self.spisok_l_2.append([self.l, i[5]])

        self.baza_l_3 = [[70, 70, 600, 35, False], [70, 150, 600, 35, False], [70, 240, 600, 35, False],
                         [70, 330, 600, 35, False], [70, 420, 600, 35, False], [110, 110, 300, 35, True],
                         [110, 190, 300, 35, True], [110, 280, 300, 35, True], [110, 370, 300, 35, True],
                         [110, 460, 300, 35, True]]
        self.sp_st, self.sp_ot = [], []
        for i in self.baza_l_3:
            self.l_2 = QtWidgets.QLabel(self.centralwidget)
            self.l_2.setGeometry(QtCore.QRect(i[0], i[1], i[2], i[3]))
            self.l_2.setFont(font_2)
            if i[4] == False:
                self.sp_st.append(self.l_2)
            else:
                self.sp_ot.append(self.l_2)

        self.baza_cb = ['сложение', 'вычитание', 'умножение', 'деление', 'скобки']
        self.galki = []
        h = 0
        for i in self.baza_cb:
            self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
            self.checkBox.setGeometry(QtCore.QRect(850, 90 + h*40, 150, 30))
            self.checkBox.setFont(font_3)
            self.galki.append(self.checkBox)
            h += 1

        self.pushButton, self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget), QtWidgets.QPushButton(self.centralwidget)
        self.spinBox, self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget), QtWidgets.QSpinBox(self.centralwidget)
        self.spisok_p_s = [[self.pushButton, 850, 590, 140, 70], [self.pushButton_2, 630, 590, 140, 70],
                           [self.spinBox, 890, 380, 60, 35], [self.spinBox_2, 890, 520, 60, 35]]
        for i in self.spisok_p_s:
            i[0].setGeometry(QtCore.QRect(i[1], i[2], i[3], i[4]))
            i[0].setFont(font_5)

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(670, 520, 140, 50))
        self.textEdit.setFont(font_4)

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
        MainWindow.setWindowTitle(_translate("MainWindow", "арифметика"))
        for i in self.spisok_l_2:
            i[0].setText(_translate("MainWindow", i[1]))
        for i, l in enumerate(self.galki):
            l.setText(_translate("MainWindow", self.baza_cb[i]))
        self.pushButton.setText(_translate("MainWindow", "начать! "))
        self.pushButton_2.setText(_translate("MainWindow", "ввод"))


def N():
    'кнопка "НАЧАЛИ!".'
    ui.textEdit.clear()
    ui.label_21.setText(" ")
    global mir, vibor, KOL_BLO, yr_slohn, diapazon, diapazon_1, diapazon_2, REZ, tema, statistika, blok_1, blok_2, \
        doska_1, doska_2

    if mir == True:
        ui.label_21.setText("     Уже начали.")
        return False
    vibor = []
    spisok_g = ["сложение", "вычитание", "умножение", "деление", "скобки"]
    for j, i in enumerate(ui.galki):
        if i.isChecked() == True:
            vibor.append(spisok_g[j])
    if len(vibor) == 0:
        ui.label_21.setText("    А какие темы?")
        return False
    statistika = {i: [0, 0] for i in vibor}

    KOL_BLO = ui.spinBox_2.value()

    yr_slohn = ui.spinBox.value()
    diapazon = [0, 10 + 10 * yr_slohn]
    diapazon_1 = [0, 5 + 5 * yr_slohn]
    diapazon_2 = [0, 10 + 5 * yr_slohn]

    tema = [choice(vibor), 1]
    primer(tema[0])
    kilroi(tema[0])

    blok_1 = []
    blok_2 = []

    doska_1 = ["", "", "", "", ""]
    doska_2 = ["", "", "", "", ""]
    melom_po_doske()

    if KOL_BLO != 0:
        mir = 1
    else:
        mir = 2
        ui.label_21.setText("  Одиночный пример.")

def V():
    'кнопка "ввод"'
    ui.label_21.setText(" ")
    global doska_1, doska_2, blok_1, blok_2, mir, tema, KOL_BLO

    if mir == 0:
        ui.label_21.setText("    Нет задания.")
        return False

    if tema[1] == 1:
        blok_1 = []
        blok_2 = []
        doska_1 = ["", "", "", "", ""]
        doska_2 = ["", "", "", "", ""]
        melom_po_doske()

    if len(ui.textEdit.toPlainText()) == 0:
        ui.label_21.setText("    Введите ответ.")
        return False
    try:
        otvet = int(ui.textEdit.toPlainText())
    except:
        ui.label_21.setText("  Некорректный ответ. Повторите.")
        return False

    if otvet == REZ:
        ui.label_21.setText(" "*40 + "Верно!")
        statistika[tema[0]][0] += 1
        blok_2.append("Верно!")
    else:
        ui.label_21.setText(" "*25 + "Неверно.")
        statistika[tema[0]][1] += 1
        blok_2.append(f"неа...  Oтвет: {REZ}")

    if mir == 2:
        mir = 0
        return True

    blok_1.append(ui.label_20.text().strip() + " " + str(otvet))
    j = 0
    for i in blok_1[::-1]:
        doska_1[j] = i
        j += 1
    j = 0
    for i in blok_2[::-1]:
        doska_2[j] = i
        j += 1
    melom_po_doske()
    ui.textEdit.clear()
    tema[1] += 1
    if tema[1] == 6:
        tema = [choice(vibor), 1]
        KOL_BLO -= 1
        if KOL_BLO == 0:
            itog()
            return True
    if (tema[0] == "сложение" or tema[0] == "вычитание") and tema[1] == 5:
        primer(tema[0], 2)
    else:
        primer(tema[0])
    kilroi(tema[0])

def itog():
    'подведение итогов'
    global mir, doska_1, doska_2
    verno = 0
    ne_ve = 0
    doska_1 = ["", "", "", "", ""]
    doska_2 = ["", "", "", "", ""]
    j = 4
    for i in statistika:
        verno += statistika[i][0]
        ne_ve += statistika[i][1]
        if statistika[i][0] != 0 or statistika[i][1] != 0:
            doska_1[j] = i
            doska_2[j] = f"верно {statistika[i][0]}    |     неверно {statistika[i][1]}"
            j -= 1
        melom_po_doske()
    ui.textEdit.clear()
    ui.label_20.setText(" ")
    ui.label_21.setText(" ")
    kilroi(f"ИТОГ: верно   {verno}   из   {verno + ne_ve} .         при сложности {yr_slohn}")
    mir = 0

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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    melom_po_doske()
    ui.label_5.setText("")
    ui.label_20.setText("")
    ui.label_21.setText("")
    ui.pushButton.clicked.connect(N)
    ui.pushButton_2.clicked.connect(V)
    sys.exit(app.exec_())
