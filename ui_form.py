# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1068, 604)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.actionthis_also_does_something = QAction(MainWindow)
        self.actionthis_also_does_something.setObjectName(u"actionthis_also_does_something")
        self.actionthis_does_something = QAction(MainWindow)
        self.actionthis_does_something.setObjectName(u"actionthis_does_something")
        self.actionno_sep1 = QAction(MainWindow)
        self.actionno_sep1.setObjectName(u"actionno_sep1")
        self.actionno_sep2 = QAction(MainWindow)
        self.actionno_sep2.setObjectName(u"actionno_sep2")
        self.actionno_sep3 = QAction(MainWindow)
        self.actionno_sep3.setObjectName(u"actionno_sep3")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionImport_from_Text_File = QAction(MainWindow)
        self.actionImport_from_Text_File.setObjectName(u"actionImport_from_Text_File")
        self.actionLoad_Preset = QAction(MainWindow)
        self.actionLoad_Preset.setObjectName(u"actionLoad_Preset")
        self.actionAdd_Preset = QAction(MainWindow)
        self.actionAdd_Preset.setObjectName(u"actionAdd_Preset")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, 9, 9, 18)
        self.parameters = QFrame(self.centralwidget)
        self.parameters.setObjectName(u"parameters")
        self.parameters.setMinimumSize(QSize(200, 0))
        self.parameters.setMaximumSize(QSize(400, 16777215))
        self.parameters.setFrameShape(QFrame.StyledPanel)
        self.parameters.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.parameters)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 0, 0, 0)
        self.source_numbers_frame = QGroupBox(self.parameters)
        self.source_numbers_frame.setObjectName(u"source_numbers_frame")
        self.verticalLayout_3 = QVBoxLayout(self.source_numbers_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.source_numbers_text = QPlainTextEdit(self.source_numbers_frame)
        self.source_numbers_text.setObjectName(u"source_numbers_text")

        self.verticalLayout_3.addWidget(self.source_numbers_text)

        self.import_btn = QPushButton(self.source_numbers_frame)
        self.import_btn.setObjectName(u"import_btn")

        self.verticalLayout_3.addWidget(self.import_btn)


        self.verticalLayout_2.addWidget(self.source_numbers_frame)

        self.stereospacing = QGroupBox(self.parameters)
        self.stereospacing.setObjectName(u"stereospacing")
        self.verticalLayout_4 = QVBoxLayout(self.stereospacing)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 9)
        self.f_font_spacing = QFrame(self.stereospacing)
        self.f_font_spacing.setObjectName(u"f_font_spacing")
        self.f_font_spacing.setFrameShape(QFrame.StyledPanel)
        self.f_font_spacing.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.f_font_spacing)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.f_font_spacing)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_6.addWidget(self.label_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(12)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.slide_font_spacing = QSlider(self.f_font_spacing)
        self.slide_font_spacing.setObjectName(u"slide_font_spacing")
        self.slide_font_spacing.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.slide_font_spacing)

        self.spin_font_spacing = QDoubleSpinBox(self.f_font_spacing)
        self.spin_font_spacing.setObjectName(u"spin_font_spacing")
        self.spin_font_spacing.setMaximum(100.000000000000000)

        self.horizontalLayout_3.addWidget(self.spin_font_spacing)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)


        self.verticalLayout_4.addWidget(self.f_font_spacing)

        self.f_column_spacing = QFrame(self.stereospacing)
        self.f_column_spacing.setObjectName(u"f_column_spacing")
        self.f_column_spacing.setFrameShape(QFrame.StyledPanel)
        self.f_column_spacing.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.f_column_spacing)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_column_spacing = QLabel(self.f_column_spacing)
        self.label_column_spacing.setObjectName(u"label_column_spacing")

        self.verticalLayout_5.addWidget(self.label_column_spacing)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.slide_column_spacing = QSlider(self.f_column_spacing)
        self.slide_column_spacing.setObjectName(u"slide_column_spacing")
        self.slide_column_spacing.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.slide_column_spacing)

        self.spin_column_spacing = QDoubleSpinBox(self.f_column_spacing)
        self.spin_column_spacing.setObjectName(u"spin_column_spacing")
        self.spin_column_spacing.setMaximum(100.000000000000000)

        self.horizontalLayout.addWidget(self.spin_column_spacing)


        self.verticalLayout_5.addLayout(self.horizontalLayout)


        self.verticalLayout_4.addWidget(self.f_column_spacing)

        self.f_row_spacing = QFrame(self.stereospacing)
        self.f_row_spacing.setObjectName(u"f_row_spacing")
        self.f_row_spacing.setFrameShape(QFrame.StyledPanel)
        self.f_row_spacing.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.f_row_spacing)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.f_row_spacing)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_7.addWidget(self.label_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(12)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.slide_row_spacing = QSlider(self.f_row_spacing)
        self.slide_row_spacing.setObjectName(u"slide_row_spacing")
        self.slide_row_spacing.setOrientation(Qt.Horizontal)

        self.horizontalLayout_4.addWidget(self.slide_row_spacing)

        self.spin_row_spacing = QDoubleSpinBox(self.f_row_spacing)
        self.spin_row_spacing.setObjectName(u"spin_row_spacing")
        self.spin_row_spacing.setMaximum(100.000000000000000)

        self.horizontalLayout_4.addWidget(self.spin_row_spacing)


        self.verticalLayout_7.addLayout(self.horizontalLayout_4)


        self.verticalLayout_4.addWidget(self.f_row_spacing)

        self.f_offset = QFrame(self.stereospacing)
        self.f_offset.setObjectName(u"f_offset")
        self.f_offset.setFrameShape(QFrame.StyledPanel)
        self.f_offset.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.f_offset)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_stero_offset = QLabel(self.f_offset)
        self.label_stero_offset.setObjectName(u"label_stero_offset")

        self.verticalLayout_8.addWidget(self.label_stero_offset)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(12)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.slide_offset = QSlider(self.f_offset)
        self.slide_offset.setObjectName(u"slide_offset")
        self.slide_offset.setOrientation(Qt.Horizontal)

        self.horizontalLayout_5.addWidget(self.slide_offset)

        self.spin_offset = QDoubleSpinBox(self.f_offset)
        self.spin_offset.setObjectName(u"spin_offset")
        self.spin_offset.setMaximum(100.000000000000000)

        self.horizontalLayout_5.addWidget(self.spin_offset)


        self.verticalLayout_8.addLayout(self.horizontalLayout_5)


        self.verticalLayout_4.addWidget(self.f_offset)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.check_auto_column = QCheckBox(self.stereospacing)
        self.check_auto_column.setObjectName(u"check_auto_column")

        self.horizontalLayout_9.addWidget(self.check_auto_column)

        self.check_auto_offset = QCheckBox(self.stereospacing)
        self.check_auto_offset.setObjectName(u"check_auto_offset")

        self.horizontalLayout_9.addWidget(self.check_auto_offset)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)


        self.verticalLayout_2.addWidget(self.stereospacing)


        self.horizontalLayout_2.addWidget(self.parameters)

        self.preview_frame = QFrame(self.centralwidget)
        self.preview_frame.setObjectName(u"preview_frame")
        self.preview_frame.setEnabled(True)
        self.preview_frame.setFrameShape(QFrame.StyledPanel)
        self.preview_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.preview_frame)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(9)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.check_auto_size = QCheckBox(self.preview_frame)
        self.check_auto_size.setObjectName(u"check_auto_size")

        self.horizontalLayout_8.addWidget(self.check_auto_size)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)

        self.height_label = QLabel(self.preview_frame)
        self.height_label.setObjectName(u"height_label")
        self.height_label.setEnabled(True)

        self.horizontalLayout_8.addWidget(self.height_label)

        self.height_adjust_spinbox = QDoubleSpinBox(self.preview_frame)
        self.height_adjust_spinbox.setObjectName(u"height_adjust_spinbox")

        self.horizontalLayout_8.addWidget(self.height_adjust_spinbox)

        self.line_2 = QFrame(self.preview_frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_8.addWidget(self.line_2)

        self.width_label = QLabel(self.preview_frame)
        self.width_label.setObjectName(u"width_label")

        self.horizontalLayout_8.addWidget(self.width_label)

        self.width_adjust_spinbox = QDoubleSpinBox(self.preview_frame)
        self.width_adjust_spinbox.setObjectName(u"width_adjust_spinbox")

        self.horizontalLayout_8.addWidget(self.width_adjust_spinbox)


        self.verticalLayout_11.addLayout(self.horizontalLayout_8)

        self.vframe_preview = QFrame(self.preview_frame)
        self.vframe_preview.setObjectName(u"vframe_preview")
        self.vframe_preview.setFrameShape(QFrame.StyledPanel)
        self.vframe_preview.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.vframe_preview)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 242, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.hframe_preview = QFrame(self.vframe_preview)
        self.hframe_preview.setObjectName(u"hframe_preview")
        self.hframe_preview.setStyleSheet(u"")
        self.hframe_preview.setFrameShape(QFrame.StyledPanel)
        self.hframe_preview.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.hframe_preview)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.img_preview_label = QLabel(self.hframe_preview)
        self.img_preview_label.setObjectName(u"img_preview_label")
        self.img_preview_label.setFrameShape(QFrame.NoFrame)
        self.img_preview_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.img_preview_label)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addWidget(self.hframe_preview)

        self.verticalSpacer_2 = QSpacerItem(20, 242, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.verticalLayout_11.addWidget(self.vframe_preview)

        self.gradient_box = QGroupBox(self.preview_frame)
        self.gradient_box.setObjectName(u"gradient_box")
        self.gradient_box.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_10 = QVBoxLayout(self.gradient_box)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(6, 6, 6, 6)
        self.l_shift = QFrame(self.gradient_box)
        self.l_shift.setObjectName(u"l_shift")
        self.l_shift.setFrameShape(QFrame.StyledPanel)
        self.l_shift.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.l_shift)
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.gradient_select = QComboBox(self.l_shift)
        self.gradient_select.addItem("")
        self.gradient_select.addItem("")
        self.gradient_select.addItem("")
        self.gradient_select.setObjectName(u"gradient_select")

        self.horizontalLayout_7.addWidget(self.gradient_select)

        self.btn_customize = QPushButton(self.l_shift)
        self.btn_customize.setObjectName(u"btn_customize")

        self.horizontalLayout_7.addWidget(self.btn_customize)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)

        self.refresh_btn = QPushButton(self.l_shift)
        self.refresh_btn.setObjectName(u"refresh_btn")

        self.horizontalLayout_7.addWidget(self.refresh_btn)

        self.save_btn = QPushButton(self.l_shift)
        self.save_btn.setObjectName(u"save_btn")

        self.horizontalLayout_7.addWidget(self.save_btn)


        self.verticalLayout_9.addLayout(self.horizontalLayout_7)


        self.verticalLayout_10.addWidget(self.l_shift)


        self.verticalLayout_11.addWidget(self.gradient_box)


        self.horizontalLayout_2.addWidget(self.preview_frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1068, 22))
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuPresets = QMenu(self.menuBar)
        self.menuPresets.setObjectName(u"menuPresets")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuPresets.menuAction())
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionImport_from_Text_File)
        self.menuPresets.addAction(self.actionLoad_Preset)
        self.menuPresets.addAction(self.actionAdd_Preset)

        self.retranslateUi(MainWindow)

        self.gradient_select.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionthis_also_does_something.setText(QCoreApplication.translate("MainWindow", u"this also does something? ", None))
        self.actionthis_does_something.setText(QCoreApplication.translate("MainWindow", u"this does something?", None))
        self.actionno_sep1.setText(QCoreApplication.translate("MainWindow", u"no sep1", None))
        self.actionno_sep2.setText(QCoreApplication.translate("MainWindow", u"no sep2", None))
        self.actionno_sep3.setText(QCoreApplication.translate("MainWindow", u"no sep3", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save file", None))
        self.actionImport_from_Text_File.setText(QCoreApplication.translate("MainWindow", u"Import from Text File", None))
        self.actionLoad_Preset.setText(QCoreApplication.translate("MainWindow", u"Load Gradient Preset", None))
        self.actionAdd_Preset.setText(QCoreApplication.translate("MainWindow", u"Save Gradient Preset", None))
        self.source_numbers_frame.setTitle(QCoreApplication.translate("MainWindow", u"Source Numbers", None))
        self.source_numbers_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter numbers here (200 digits of pi used as default)", None))
        self.import_btn.setText(QCoreApplication.translate("MainWindow", u"Import from File", None))
        self.stereospacing.setTitle(QCoreApplication.translate("MainWindow", u"Stereogram Spacing", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Font Spacing", None))
        self.label_column_spacing.setText(QCoreApplication.translate("MainWindow", u"Column Spacing", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Row Spacing", None))
        self.label_stero_offset.setText(QCoreApplication.translate("MainWindow", u"Stereo Offset", None))
        self.check_auto_column.setText(QCoreApplication.translate("MainWindow", u"Auto Column", None))
        self.check_auto_offset.setText(QCoreApplication.translate("MainWindow", u"Auto Offset", None))
        self.check_auto_size.setText(QCoreApplication.translate("MainWindow", u"Auto Size", None))
        self.height_label.setText(QCoreApplication.translate("MainWindow", u"Height", None))
        self.width_label.setText(QCoreApplication.translate("MainWindow", u"Width", None))
        self.img_preview_label.setText(QCoreApplication.translate("MainWindow", u"image_displays_here", None))
        self.gradient_box.setTitle(QCoreApplication.translate("MainWindow", u"Gradient", None))
        self.gradient_select.setItemText(0, QCoreApplication.translate("MainWindow", u"None (Black)", None))
        self.gradient_select.setItemText(1, QCoreApplication.translate("MainWindow", u"Glacier", None))
        self.gradient_select.setItemText(2, QCoreApplication.translate("MainWindow", u"Last Custom", None))

        self.btn_customize.setText(QCoreApplication.translate("MainWindow", u"Customize...", None))
        self.refresh_btn.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.save_btn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuPresets.setTitle(QCoreApplication.translate("MainWindow", u"Presets", None))
    # retranslateUi

