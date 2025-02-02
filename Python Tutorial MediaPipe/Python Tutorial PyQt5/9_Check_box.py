# Create by Packetsss
# Personal use is allowed
# Commercial use is prohibited

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 600)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.roots = QtWidgets.QCheckBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.roots.setFont(font)
        self.roots.setObjectName("roots")
        self.verticalLayout_2.addWidget(self.roots)
        self.dirt = QtWidgets.QCheckBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dirt.setFont(font)
        self.dirt.setObjectName("dirt")
        self.verticalLayout_2.addWidget(self.dirt)
        self.rawPotato = QtWidgets.QCheckBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rawPotato.setFont(font)
        self.rawPotato.setObjectName("rawPotato")
        self.verticalLayout_2.addWidget(self.rawPotato)

        self.roots.stateChanged.connect(self.checked_item)
        self.dirt.stateChanged.connect(self.checked_item)
        self.rawPotato.stateChanged.connect(self.checked_item)


        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_rst = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_rst.setFont(font)
        self.label_rst.setObjectName("label_rst")
        self.verticalLayout.addWidget(self.label_rst)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_3.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Jeffson\'s"))
        self.label.setText(_translate("Dialog", "Regular Jeffs' Price: 20"))
        self.label_2.setText(_translate("Dialog", "Select Extra Toppings"))
        self.roots.setText(_translate("Dialog", "Roots"))
        self.dirt.setText(_translate("Dialog", "Dirt"))
        self.rawPotato.setText(_translate("Dialog", "Potato_raw"))
        self.label_rst.setText(_translate("Dialog", "Rst"))

    def checked_item(self):
        price = 20
        # resets every time check/uncheck item

        if self.roots.isChecked():
            price += 3
        if self.dirt.isChecked():
            price += 50
        if self.rawPotato.isChecked():
            price += 2

        self.label_rst.setText(f"Total price is {price}")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())