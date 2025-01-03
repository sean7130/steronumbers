# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'save_image_preview.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(407, 170)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.vframe_preview = QFrame(Form)
        self.vframe_preview.setObjectName(u"vframe_preview")
        self.vframe_preview.setFrameShape(QFrame.StyledPanel)
        self.vframe_preview.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.vframe_preview)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 242, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.hframe_preview = QFrame(self.vframe_preview)
        self.hframe_preview.setObjectName(u"hframe_preview")
        self.hframe_preview.setFrameShape(QFrame.StyledPanel)
        self.hframe_preview.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.hframe_preview)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.img_preview_label = QLabel(self.hframe_preview)
        self.img_preview_label.setObjectName(u"img_preview_label")
        self.img_preview_label.setFrameShape(QFrame.NoFrame)
        self.img_preview_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.img_preview_label)

        self.horizontalSpacer_4 = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addWidget(self.hframe_preview)

        self.verticalSpacer_2 = QSpacerItem(20, 242, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.verticalLayout_3.addWidget(self.vframe_preview)

        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.radio_white = QRadioButton(self.groupBox)
        self.radio_white.setObjectName(u"radio_white")

        self.horizontalLayout_2.addWidget(self.radio_white)

        self.radio_black = QRadioButton(self.groupBox)
        self.radio_black.setObjectName(u"radio_black")

        self.horizontalLayout_2.addWidget(self.radio_black)

        self.radio_default = QRadioButton(self.groupBox)
        self.radio_default.setObjectName(u"radio_default")

        self.horizontalLayout_2.addWidget(self.radio_default)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.custom_color_button = QPushButton(self.groupBox)
        self.custom_color_button.setObjectName(u"custom_color_button")

        self.horizontalLayout_2.addWidget(self.custom_color_button)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.save_button = QPushButton(Form)
        self.save_button.setObjectName(u"save_button")

        self.horizontalLayout.addWidget(self.save_button)

        self.close_button = QPushButton(Form)
        self.close_button.setObjectName(u"close_button")

        self.horizontalLayout.addWidget(self.close_button)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.img_preview_label.setText(QCoreApplication.translate("Form", u"image_displays_here", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Background Color", None))
        self.radio_white.setText(QCoreApplication.translate("Form", u"White", None))
        self.radio_black.setText(QCoreApplication.translate("Form", u"Black", None))
        self.radio_default.setText(QCoreApplication.translate("Form", u"Windows UI Default (240)", None))
        self.custom_color_button.setText(QCoreApplication.translate("Form", u"Custom...", None))
        self.save_button.setText(QCoreApplication.translate("Form", u"Save", None))
        self.close_button.setText(QCoreApplication.translate("Form", u"Cancel", None))
    # retranslateUi

