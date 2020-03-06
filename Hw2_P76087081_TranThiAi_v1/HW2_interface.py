# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\HW2_interface.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget_HW2(object):
    def setupUi(self, Widget_HW2):
        Widget_HW2.setObjectName("Widget_HW2")
        Widget_HW2.resize(500, 360)
        Widget_HW2.setMinimumSize(QtCore.QSize(500, 360))
        Widget_HW2.setMaximumSize(QtCore.QSize(500, 360))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("cvHw1.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Widget_HW2.setWindowIcon(icon)
        self.groupCVDL = QtWidgets.QGroupBox(Widget_HW2)
        self.groupCVDL.setGeometry(QtCore.QRect(30, 30, 441, 291))
        self.groupCVDL.setObjectName("groupCVDL")
        self.group_stereo = QtWidgets.QGroupBox(self.groupCVDL)
        self.group_stereo.setGeometry(QtCore.QRect(20, 40, 201, 101))
        self.group_stereo.setObjectName("group_stereo")
        self.btn_disparity = QtWidgets.QPushButton(self.group_stereo)
        self.btn_disparity.setGeometry(QtCore.QRect(40, 30, 121, 41))
        self.btn_disparity.setObjectName("btn_disparity")
        self.group_NCC = QtWidgets.QGroupBox(self.groupCVDL)
        self.group_NCC.setGeometry(QtCore.QRect(20, 160, 201, 101))
        self.group_NCC.setObjectName("group_NCC")
        self.btn_ncc = QtWidgets.QPushButton(self.group_NCC)
        self.btn_ncc.setGeometry(QtCore.QRect(40, 30, 121, 41))
        self.btn_ncc.setObjectName("btn_ncc")
        self.group_sift = QtWidgets.QGroupBox(self.groupCVDL)
        self.group_sift.setGeometry(QtCore.QRect(250, 40, 171, 221))
        self.group_sift.setObjectName("group_sift")
        self.btn_keypoints = QtWidgets.QPushButton(self.group_sift)
        self.btn_keypoints.setGeometry(QtCore.QRect(20, 40, 131, 41))
        self.btn_keypoints.setObjectName("btn_keypoints")
        self.btn_MK = QtWidgets.QPushButton(self.group_sift)
        self.btn_MK.setGeometry(QtCore.QRect(20, 130, 131, 41))
        self.btn_MK.setObjectName("btn_MK")
        self.label_myname = QtWidgets.QLabel(Widget_HW2)
        self.label_myname.setGeometry(QtCore.QRect(30, 330, 151, 21))
        self.label_myname.setObjectName("label_myname")

        self.retranslateUi(Widget_HW2)
        QtCore.QMetaObject.connectSlotsByName(Widget_HW2)

    def retranslateUi(self, Widget_HW2):
        _translate = QtCore.QCoreApplication.translate
        Widget_HW2.setWindowTitle(_translate("Widget_HW2", "HW2_P76087081_TranThiAi"))
        self.groupCVDL.setTitle(_translate("Widget_HW2", "CDVL"))
        self.group_stereo.setTitle(_translate("Widget_HW2", "1. Stereo"))
        self.btn_disparity.setText(_translate("Widget_HW2", "1.1 Disparity"))
        self.group_NCC.setTitle(_translate("Widget_HW2", "2. Normalized Cross Correlation"))
        self.btn_ncc.setText(_translate("Widget_HW2", "2.1 NCC"))
        self.group_sift.setTitle(_translate("Widget_HW2", "3. SIFT"))
        self.btn_keypoints.setText(_translate("Widget_HW2", "3.1 Keypoints"))
        self.btn_MK.setText(_translate("Widget_HW2", "3.2 Matched Keypoints"))
        self.label_myname.setText(_translate("Widget_HW2", "HW2_P76087081_TranThiAi"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget_HW2 = QtWidgets.QWidget()
    ui = Ui_Widget_HW2()
    ui.setupUi(Widget_HW2)
    Widget_HW2.show()
    sys.exit(app.exec_())
