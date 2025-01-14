# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'export_select.ui'
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
        Form.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_select_all = QPushButton(Form)
        self.btn_select_all.setObjectName(u"btn_select_all")
        self.btn_select_all.setFlat(True)

        self.horizontalLayout_2.addWidget(self.btn_select_all)

        self.btn_deselect_all = QPushButton(Form)
        self.btn_deselect_all.setObjectName(u"btn_deselect_all")
        self.btn_deselect_all.setFlat(True)

        self.horizontalLayout_2.addWidget(self.btn_deselect_all)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.gradient_list = QListWidget(Form)
        __qlistwidgetitem = QListWidgetItem(self.gradient_list)
        __qlistwidgetitem.setCheckState(Qt.PartiallyChecked);
        __qlistwidgetitem1 = QListWidgetItem(self.gradient_list)
        __qlistwidgetitem1.setCheckState(Qt.Checked);
        self.gradient_list.setObjectName(u"gradient_list")
        self.gradient_list.setViewMode(QListView.ListMode)

        self.verticalLayout.addWidget(self.gradient_list)

        self.save_button = QPushButton(Form)
        self.save_button.setObjectName(u"save_button")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_button.sizePolicy().hasHeightForWidth())
        self.save_button.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.save_button)


        self.retranslateUi(Form)

        self.gradient_list.setCurrentRow(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Select Gradent Export", None))
        self.btn_select_all.setText(QCoreApplication.translate("Form", u"Select All", None))
        self.btn_deselect_all.setText(QCoreApplication.translate("Form", u"Deselect All", None))

        __sortingEnabled = self.gradient_list.isSortingEnabled()
        self.gradient_list.setSortingEnabled(False)
        ___qlistwidgetitem = self.gradient_list.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Form", u"Item1", None));
        ___qlistwidgetitem1 = self.gradient_list.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Form", u"Item2", None));
        self.gradient_list.setSortingEnabled(__sortingEnabled)

        self.save_button.setText(QCoreApplication.translate("Form", u"Save Selected", None))
    # retranslateUi

