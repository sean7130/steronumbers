# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'custom_gradient_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(QDialog):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(390, 332)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_4 = QFrame(self.groupBox)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, -1)
        self.start_color_label = QLabel(self.frame_4)
        self.start_color_label.setObjectName(u"start_color_label")
        self.start_color_label.setMinimumSize(QSize(0, 0))
        self.start_color_label.setMaximumSize(QSize(16777215, 20))
        self.start_color_label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_4.addWidget(self.start_color_label)

        self.verticalSpacer_3 = QSpacerItem(20, 1, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, -1)
        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.btn_edit_start_color = QPushButton(self.frame_5)
        self.btn_edit_start_color.setObjectName(u"btn_edit_start_color")
        sizePolicy.setHeightForWidth(self.btn_edit_start_color.sizePolicy().hasHeightForWidth())
        self.btn_edit_start_color.setSizePolicy(sizePolicy)
        self.btn_edit_start_color.setMinimumSize(QSize(80, 80))
        self.btn_edit_start_color.setStyleSheet(u"QPushButton#btn_edit_start_color {\n"
"    background-color: rgb(170, 255, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: bold 14px;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton#btn_edit_start_color:pressed {\n"
"    background-color: rgb(240, 240, 240);\n"
"    border-style: inset;\n"
"}")

        self.horizontalLayout_4.addWidget(self.btn_edit_start_color)

        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout_4.addWidget(self.frame_5)

        self.verticalSpacer_4 = QSpacerItem(20, 1, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)


        self.horizontalLayout.addWidget(self.frame_4)

        self.line = QFrame(self.groupBox)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.frame_2 = QFrame(self.groupBox)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, -1)
        self.end_color_label = QLabel(self.frame_2)
        self.end_color_label.setObjectName(u"end_color_label")
        self.end_color_label.setMinimumSize(QSize(0, 0))
        self.end_color_label.setMaximumSize(QSize(16777215, 20))
        self.end_color_label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.end_color_label)

        self.verticalSpacer = QSpacerItem(20, 1, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, -1)
        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_edit_end_color = QPushButton(self.frame_3)
        self.btn_edit_end_color.setObjectName(u"btn_edit_end_color")
        sizePolicy.setHeightForWidth(self.btn_edit_end_color.sizePolicy().hasHeightForWidth())
        self.btn_edit_end_color.setSizePolicy(sizePolicy)
        self.btn_edit_end_color.setMinimumSize(QSize(80, 80))
        self.btn_edit_end_color.setStyleSheet(u"QPushButton#btn_edit_end_color {\n"
"    background-color: rgb(85, 170, 127);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: bold 14px;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton#btn_edit_end_color:pressed {\n"
"    background-color: rgb(240, 240, 240);\n"
"    border-style: inset;\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_edit_end_color)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.verticalSpacer_2 = QSpacerItem(20, 1, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.groupBox)

        self.line_preview = QLabel(Dialog)
        self.line_preview.setObjectName(u"line_preview")
        self.line_preview.setMaximumSize(QSize(16777215, 40))
        self.line_preview.setPixmap(QPixmap(u"gradient_preview.png"))
        self.line_preview.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.line_preview)

        self.line_edit_save_gradient = QLineEdit(Dialog)
        self.line_edit_save_gradient.setObjectName(u"line_edit_save_gradient")

        self.verticalLayout.addWidget(self.line_edit_save_gradient)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close|QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(False)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Custom Gradient", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Gradient Defintion", None))
        self.start_color_label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Start Color: <span style=\" font-weight:700;\">(170, 255, 0)</span></p></body></html>", None))
        self.btn_edit_start_color.setText("")
        self.end_color_label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>End Color: <span style=\" font-weight:700;\">(85, 170, 127)</span></p></body></html>", None))
        self.btn_edit_end_color.setText("")
        self.line_preview.setText("")
        self.line_edit_save_gradient.setPlaceholderText(QCoreApplication.translate("Dialog", u"Save as...", None))
    # retranslateUi

