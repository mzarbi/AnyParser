# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1063, 845)
        MainWindow.setStyleSheet("/*Copyright (c) DevSec Studio. All rights reserved.\n"
"\n"
"MIT License\n"
"\n"
"Permission is hereby granted, free of charge, to any person obtaining a copy\n"
"of this software and associated documentation files (the \"Software\"), to deal\n"
"in the Software without restriction, including without limitation the rights\n"
"to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n"
"copies of the Software, and to permit persons to whom the Software is\n"
"furnished to do so, subject to the following conditions:\n"
"\n"
"The above copyright notice and this permission notice shall be included in all\n"
"copies or substantial portions of the Software.\n"
"\n"
"THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n"
"IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n"
"FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n"
"AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n"
"LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n"
"OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n"
"*/\n"
"\n"
"/*-----QWidget-----*/\n"
"QWidget\n"
"{\n"
"    background-color: #3a3a3a;\n"
"    color: #fff;\n"
"    selection-background-color: #b78620;\n"
"    selection-color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"    background-color: transparent;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QMenuBar-----*/\n"
"QMenuBar \n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(57, 57, 57, 255),stop:1 rgba(50, 50, 50, 255));\n"
"    border: 1px solid #000;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item \n"
"{\n"
"    background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item:selected \n"
"{\n"
"    background-color: rgba(183, 134, 32, 20%);\n"
"    border: 1px solid #b78620;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item:pressed \n"
"{\n"
"    background-color: rgb(183, 134, 32);\n"
"    border: 1px solid #b78620;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QMenu-----*/\n"
"QMenu\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(57, 57, 57, 255),stop:1 rgba(50, 50, 50, 255));\n"
"    border: 1px solid #222;\n"
"    padding: 4px;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item\n"
"{\n"
"    background-color: transparent;\n"
"    padding: 2px 20px 2px 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::separator\n"
"{\n"
"       background-color: rgb(183, 134, 32);\n"
"    height: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item:disabled\n"
"{\n"
"    color: #555;\n"
"    background-color: transparent;\n"
"    padding: 2px 20px 2px 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    background-color: rgba(183, 134, 32, 20%);\n"
"    border: 1px solid #b78620;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QToolBar-----*/\n"
"QToolBar\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(69, 69, 69, 255),stop:1 rgba(58, 58, 58, 255));\n"
"    border-top: none;\n"
"    border-bottom: 1px solid #4f4f4f;\n"
"    border-left: 1px solid #4f4f4f;\n"
"    border-right: 1px solid #4f4f4f;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolBar::separator\n"
"{\n"
"    background-color: #2e2e2e;\n"
"    width: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QToolButton-----*/\n"
"QToolButton \n"
"{\n"
"    background-color: transparent;\n"
"    color: #fff;\n"
"    padding: 5px;\n"
"    padding-left: 8px;\n"
"    padding-right: 8px;\n"
"    margin-left: 1px;\n"
"}\n"
"\n"
"\n"
"QToolButton:hover\n"
"{\n"
"    background-color: rgba(183, 134, 32, 20%);\n"
"    border: 1px solid #b78620;\n"
"    color: #fff;\n"
"    \n"
"}\n"
"\n"
"\n"
"QToolButton:pressed\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(57, 57, 57, 255),stop:1 rgba(50, 50, 50, 255));\n"
"    border: 1px solid #b78620;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton:checked\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(57, 57, 57, 255),stop:1 rgba(50, 50, 50, 255));\n"
"    border: 1px solid #222;\n"
"}\n"
"\n"
"\n"
"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(84, 84, 84, 255),stop:1 rgba(59, 59, 59, 255));\n"
"    color: #ffffff;\n"
"    min-width: 80px;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 3px;\n"
"    border-color: #051a39;\n"
"    padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::flat\n"
"{\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::disabled\n"
"{\n"
"    background-color: #404040;\n"
"    color: #656565;\n"
"    border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"    background-color: rgba(183, 134, 32, 20%);\n"
"    border: 1px solid #b78620;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(74, 74, 74, 255),stop:1 rgba(49, 49, 49, 255));\n"
"    border: 1px solid #b78620;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::checked\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(74, 74, 74, 255),stop:1 rgba(49, 49, 49, 255));\n"
"    border: 1px solid #222;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLineEdit-----*/\n"
"QLineEdit\n"
"{\n"
"    background-color: #131313;\n"
"    color : #eee;\n"
"    border: 1px solid #343434;\n"
"    border-radius: 2px;\n"
"    padding: 3px;\n"
"    padding-left: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QPlainTExtEdit-----*/\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #131313;\n"
"    color : #eee;\n"
"    border: 1px solid #343434;\n"
"    border-radius: 2px;\n"
"    padding: 3px;\n"
"    padding-left: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTabBar-----*/\n"
"QTabBar::tab\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(84, 84, 84, 255),stop:1 rgba(59, 59, 59, 255));\n"
"    color: #ffffff;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: #666;\n"
"    border-bottom: none;\n"
"    padding: 5px;\n"
"    padding-left: 15px;\n"
"    padding-right: 15px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabWidget::pane \n"
"{\n"
"    background-color: red;\n"
"    border: 1px solid #666;\n"
"    top: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:last\n"
"{\n"
"    margin-right: 0; \n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:first:!selected\n"
"{\n"
"    background-color: #0c0c0d;\n"
"    margin-left: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    border-bottom-style: solid;\n"
"    background-color: #0c0c0d;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    margin-bottom: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"    border-top-color: #b78620;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QComboBox-----*/\n"
"QComboBox\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(84, 84, 84, 255),stop:1 rgba(59, 59, 59, 255));\n"
"    border: 1px solid #000;\n"
"    padding-left: 6px;\n"
"    color: #ffffff;\n"
"    height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::disabled\n"
"{\n"
"    background-color: #404040;\n"
"    color: #656565;\n"
"    border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    background-color: #b78620;\n"
"    color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    background-color: #383838;\n"
"    color: #ffffff;\n"
"    border: 1px solid black;\n"
"    selection-background-color: #b78620;\n"
"    outline: 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(57, 57, 57, 255),stop:1 rgba(50, 50, 50, 255));\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: black;\n"
"    border-left-style: solid; \n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"    image: url(://arrow-down.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"}\n"
"\n"
"\n"
"/*-----QSpinBox & QDateTimeEdit-----*/\n"
"QSpinBox,\n"
"QDateTimeEdit \n"
"{\n"
"    background-color: #131313;\n"
"    color : #eee;\n"
"    border: 1px solid #343434;\n"
"    padding: 3px;\n"
"    padding-left: 5px;\n"
"    border-radius : 2px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button, \n"
"QDateTimeEdit::up-button\n"
"{\n"
"    border-top-right-radius:2px;\n"
"    background-color: #777777;\n"
"    width: 16px; \n"
"    border-width: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button:hover, \n"
"QDateTimeEdit::up-button:hover\n"
"{\n"
"    background-color: #585858;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button:pressed, \n"
"QDateTimeEdit::up-button:pressed\n"
"{\n"
"    background-color: #252525;\n"
"    width: 16px; \n"
"    border-width: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-arrow,\n"
"QDateTimeEdit::up-arrow\n"
"{\n"
"    image: url(://arrow-up.png);\n"
"    width: 7px;\n"
"    height: 7px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-button, \n"
"QDateTimeEdit::down-button\n"
"{\n"
"    border-bottom-right-radius:2px;\n"
"    background-color: #777777;\n"
"    width: 16px; \n"
"    border-width: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-button:hover, \n"
"QDateTimeEdit::down-button:hover\n"
"{\n"
"    background-color: #585858;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-button:pressed, \n"
"QDateTimeEdit::down-button:pressed\n"
"{\n"
"    background-color: #252525;\n"
"    width: 16px; \n"
"    border-width: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-arrow,\n"
"QDateTimeEdit::down-arrow\n"
"{\n"
"    image: url(://arrow-down.png);\n"
"    width: 7px;\n"
"    height: 7px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QGroupBox-----*/\n"
"QGroupBox \n"
"{\n"
"    border: 1px solid;\n"
"    border-color: #666666;\n"
"    border-radius: 5px;\n"
"    margin-top: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QGroupBox::title  \n"
"{\n"
"    background-color: transparent;\n"
"    color: #eee;\n"
"    subcontrol-origin: margin;\n"
"    padding: 5px;\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QHeaderView-----*/\n"
"QHeaderView::section\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(60, 60, 60, 255),stop:1 rgba(50, 50, 50, 255));\n"
"    border: 1px solid #000;\n"
"    color: #fff;\n"
"    text-align: left;\n"
"    padding: 4px;\n"
"    \n"
"}\n"
"\n"
"\n"
"QHeaderView::section:disabled\n"
"{\n"
"    background-color: #525251;\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:checked\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(60, 60, 60, 255),stop:1 rgba(50, 50, 50, 255));\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::vertical::first,\n"
"QHeaderView::section::vertical::only-one\n"
"{\n"
"    border-top: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::vertical\n"
"{\n"
"    border-top: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::horizontal::first,\n"
"QHeaderView::section::horizontal::only-one\n"
"{\n"
"    border-left: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::horizontal\n"
"{\n"
"    border-left: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableCornerButton::section\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(60, 60, 60, 255),stop:1 rgba(50, 50, 50, 255));\n"
"    border: 1px solid #000;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTreeWidget-----*/\n"
"QTreeView\n"
"{\n"
"    show-decoration-selected: 1;\n"
"    alternate-background-color: #3a3a3a;\n"
"    selection-color: #fff;\n"
"    background-color: #2d2d2d;\n"
"    border: 1px solid gray;\n"
"    padding-top : 5px;\n"
"    color: #fff;\n"
"    font: 8pt;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item:selected\n"
"{\n"
"    color:#fff;\n"
"    background-color: #b78620;\n"
"    border-radius: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item:!selected:hover\n"
"{\n"
"    background-color: #262626;\n"
"    border: none;\n"
"    color: white;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed,\n"
"QTreeView::branch:closed:has-children:has-siblings \n"
"{\n"
"    image: url(://tree-closed.png);\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings,\n"
"QTreeView::branch:open:has-children:has-siblings  \n"
"{\n"
"    image: url(://tree-open.png);\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QListView-----*/\n"
"QListView \n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(83, 83, 83, 255),stop:0.293269 rgba(81, 81, 81, 255),stop:0.634615 rgba(79, 79, 79, 255),stop:1 rgba(83, 83, 83, 255));\n"
"    border : none;\n"
"    color: white;\n"
"    show-decoration-selected: 1; \n"
"    outline: 0;\n"
"    border: 1px solid gray;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::disabled \n"
"{\n"
"    background-color: #656565;\n"
"    color: #1b1b1b;\n"
"    border: 1px solid #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item \n"
"{\n"
"    background-color: #2d2d2d;\n"
"    padding: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:alternate \n"
"{\n"
"    background-color: #3a3a3a;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:selected \n"
"{\n"
"    background-color: #b78620;\n"
"    border: 1px solid #b78620;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:selected:!active \n"
"{\n"
"    background-color: #b78620;\n"
"    border: 1px solid #b78620;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:selected:active \n"
"{\n"
"    background-color: #b78620;\n"
"    border: 1px solid #b78620;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:hover {\n"
"    background-color: #262626;\n"
"    border: none;\n"
"    color: white;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QCheckBox-----*/\n"
"QCheckBox\n"
"{\n"
"    background-color: transparent;\n"
"    color: lightgray;\n"
"    border: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator\n"
"{\n"
"    background-color: #323232;\n"
"    border: 1px solid darkgray;\n"
"    width: 12px;\n"
"    height: 12px;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(\"./ressources/check.png\");\n"
"    background-color: #b78620;\n"
"    border: 1px solid #3a546e;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:unchecked:hover\n"
"{\n"
"    border: 1px solid #b78620; \n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::disabled\n"
"{\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:disabled\n"
"{\n"
"    background-color: #656565;\n"
"    color: #656565;\n"
"    border: 1px solid #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QRadioButton-----*/\n"
"QRadioButton \n"
"{\n"
"    color: lightgray;\n"
"    background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator::unchecked:hover \n"
"{\n"
"    background-color: lightgray;\n"
"    border: 2px solid #b78620;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator::checked \n"
"{\n"
"    border: 2px solid #b78620;\n"
"    border-radius: 6px;\n"
"    background-color: rgba(183,134,32,20%);  \n"
"    width: 9px; \n"
"    height: 9px; \n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QSlider-----*/\n"
"QSlider::groove:horizontal \n"
"{\n"
"    background-color: transparent;\n"
"    height: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::sub-page:horizontal \n"
"{\n"
"    background-color: #b78620;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::add-page:horizontal \n"
"{\n"
"    background-color: #131313;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal \n"
"{\n"
"    background-color: #b78620;\n"
"    width: 14px;\n"
"    margin-top: -6px;\n"
"    margin-bottom: -6px;\n"
"    border-radius: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal:hover \n"
"{\n"
"    background-color: #d89e25;\n"
"    border-radius: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::sub-page:horizontal:disabled \n"
"{\n"
"    background-color: #bbb;\n"
"    border-color: #999;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::add-page:horizontal:disabled \n"
"{\n"
"    background-color: #eee;\n"
"    border-color: #999;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal:disabled \n"
"{\n"
"    background-color: #eee;\n"
"    border: 1px solid #aaa;\n"
"    border-radius: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QScrollBar-----*/\n"
"QScrollBar:horizontal\n"
"{\n"
"    border: 1px solid #222222;\n"
"    background-color: #3d3d3d;\n"
"    height: 15px;\n"
"    margin: 0px 16px 0 16px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(97, 97, 97, 255),stop:1 rgba(90, 90, 90, 255));\n"
"    border: 1px solid #2d2d2d;\n"
"    min-height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(97, 97, 97, 255),stop:1 rgba(90, 90, 90, 255));\n"
"    border: 1px solid #2d2d2d;\n"
"    width: 15px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(97, 97, 97, 255),stop:1 rgba(90, 90, 90, 255));\n"
"    border: 1px solid #2d2d2d;\n"
"    width: 15px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::right-arrow:horizontal\n"
"{\n"
"    image: url(://arrow-right.png);\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::left-arrow:horizontal\n"
"{\n"
"    image: url(://arrow-left.png);\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"    background: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"    background-color: #3d3d3d;\n"
"    width: 16px;\n"
"    border: 1px solid #2d2d2d;\n"
"    margin: 16px 0px 16px 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(97, 97, 97, 255),stop:1 rgba(90, 90, 90, 255));\n"
"    border: 1px solid #2d2d2d;\n"
"    min-height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(97, 97, 97, 255),stop:1 rgba(90, 90, 90, 255));\n"
"    border: 1px solid #2d2d2d;\n"
"    height: 15px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(97, 97, 97, 255),stop:1 rgba(90, 90, 90, 255));\n"
"    border: 1px solid #2d2d2d;\n"
"    height: 15px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical\n"
"{\n"
"    image: url(://arrow-up.png);\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::down-arrow:vertical\n"
"{\n"
"    image: url(://arrow-down.png);\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"    background: none;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QProgressBar-----*/\n"
"QProgressBar\n"
"{\n"
"    border: 1px solid #666666;\n"
"    text-align: center;\n"
"    color: #000;\n"
"    font-weight: bold;\n"
"\n"
"}\n"
"\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #b78620;\n"
"    width: 30px;\n"
"    margin: 0.5px;\n"
"\n"
"}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setMinimumSize(QtCore.QSize(0, 34))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.filePathLineEdit = QtWidgets.QLineEdit(self.frame)
        self.filePathLineEdit.setReadOnly(True)
        self.filePathLineEdit.setObjectName("filePathLineEdit")
        self.horizontalLayout_2.addWidget(self.filePathLineEdit)
        self.browseButton = QtWidgets.QPushButton(self.frame)
        self.browseButton.setObjectName("browseButton")
        self.horizontalLayout_2.addWidget(self.browseButton)
        self.reloadButton = QtWidgets.QPushButton(self.frame)
        self.reloadButton.setObjectName("reloadButton")
        self.horizontalLayout_2.addWidget(self.reloadButton)
        self.verticalLayout_2.addWidget(self.frame)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_2.addWidget(self.plainTextEdit)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.toolBox = QtWidgets.QToolBox(self.tab_2)
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 1025, 681))
        self.page.setObjectName("page")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget_2 = QtWidgets.QWidget(self.page)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 34))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.applySubstitutionsButton = QtWidgets.QPushButton(self.widget_2)
        self.applySubstitutionsButton.setObjectName("applySubstitutionsButton")
        self.horizontalLayout_3.addWidget(self.applySubstitutionsButton)
        self.addSubstitutionButton = QtWidgets.QPushButton(self.widget_2)
        self.addSubstitutionButton.setObjectName("addSubstitutionButton")
        self.horizontalLayout_3.addWidget(self.addSubstitutionButton)
        self.deleteSubstitutionButton = QtWidgets.QPushButton(self.widget_2)
        self.deleteSubstitutionButton.setObjectName("deleteSubstitutionButton")
        self.horizontalLayout_3.addWidget(self.deleteSubstitutionButton)
        self.saveSubstitutionsButton = QtWidgets.QPushButton(self.widget_2)
        self.saveSubstitutionsButton.setObjectName("saveSubstitutionsButton")
        self.horizontalLayout_3.addWidget(self.saveSubstitutionsButton)
        self.loadSubstitutionsButton = QtWidgets.QPushButton(self.widget_2)
        self.loadSubstitutionsButton.setObjectName("loadSubstitutionsButton")
        self.horizontalLayout_3.addWidget(self.loadSubstitutionsButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_5.addWidget(self.widget_2)
        self.substitutionTableWidget = QtWidgets.QTableWidget(self.page)
        self.substitutionTableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.substitutionTableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.substitutionTableWidget.setTextElideMode(QtCore.Qt.ElideNone)
        self.substitutionTableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.substitutionTableWidget.setObjectName("substitutionTableWidget")
        self.substitutionTableWidget.setColumnCount(2)
        self.substitutionTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.substitutionTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.substitutionTableWidget.setHorizontalHeaderItem(1, item)
        self.substitutionTableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.substitutionTableWidget.horizontalHeader().setDefaultSectionSize(106)
        self.substitutionTableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.substitutionTableWidget.horizontalHeader().setStretchLastSection(True)
        self.substitutionTableWidget.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_5.addWidget(self.substitutionTableWidget)
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 1025, 681))
        self.page_2.setObjectName("page_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.widget_3 = QtWidgets.QWidget(self.page_2)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.computeClustersButton = QtWidgets.QPushButton(self.widget_3)
        self.computeClustersButton.setObjectName("computeClustersButton")
        self.horizontalLayout_4.addWidget(self.computeClustersButton)
        self.deleteClustersButton = QtWidgets.QPushButton(self.widget_3)
        self.deleteClustersButton.setObjectName("deleteClustersButton")
        self.horizontalLayout_4.addWidget(self.deleteClustersButton)
        self.freezeButton = QtWidgets.QPushButton(self.widget_3)
        self.freezeButton.setObjectName("freezeButton")
        self.horizontalLayout_4.addWidget(self.freezeButton)
        self.setParentButton = QtWidgets.QPushButton(self.widget_3)
        self.setParentButton.setObjectName("setParentButton")
        self.horizontalLayout_4.addWidget(self.setParentButton)
        self.showHistogramButton = QtWidgets.QPushButton(self.widget_3)
        self.showHistogramButton.setObjectName("showHistogramButton")
        self.horizontalLayout_4.addWidget(self.showHistogramButton)
        self.similarityMeasureCombobox = QtWidgets.QComboBox(self.widget_3)
        self.similarityMeasureCombobox.setMinimumSize(QtCore.QSize(133, 0))
        self.similarityMeasureCombobox.setObjectName("similarityMeasureCombobox")
        self.similarityMeasureCombobox.addItem("")
        self.horizontalLayout_4.addWidget(self.similarityMeasureCombobox)
        self.windowSpinBox = QtWidgets.QSpinBox(self.widget_3)
        self.windowSpinBox.setMinimumSize(QtCore.QSize(106, 0))
        self.windowSpinBox.setMaximum(500)
        self.windowSpinBox.setProperty("value", 15)
        self.windowSpinBox.setObjectName("windowSpinBox")
        self.horizontalLayout_4.addWidget(self.windowSpinBox)
        self.thresholdSpinBox = QtWidgets.QSpinBox(self.widget_3)
        self.thresholdSpinBox.setMaximum(100)
        self.thresholdSpinBox.setProperty("value", 90)
        self.thresholdSpinBox.setObjectName("thresholdSpinBox")
        self.horizontalLayout_4.addWidget(self.thresholdSpinBox)
        self.thresholdSpinBox_2 = QtWidgets.QSpinBox(self.widget_3)
        self.thresholdSpinBox_2.setMaximum(500)
        self.thresholdSpinBox_2.setObjectName("thresholdSpinBox_2")
        self.horizontalLayout_4.addWidget(self.thresholdSpinBox_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_6.addWidget(self.widget_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.clustersTableWidget = QtWidgets.QTableWidget(self.page_2)
        self.clustersTableWidget.setMaximumSize(QtCore.QSize(650, 16777215))
        self.clustersTableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.clustersTableWidget.setObjectName("clustersTableWidget")
        self.clustersTableWidget.setColumnCount(5)
        self.clustersTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.clustersTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.clustersTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.clustersTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.clustersTableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.clustersTableWidget.setHorizontalHeaderItem(4, item)
        self.clustersTableWidget.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout_5.addWidget(self.clustersTableWidget)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.centroidPlainTextEdit = QtWidgets.QPlainTextEdit(self.page_2)
        self.centroidPlainTextEdit.setMaximumSize(QtCore.QSize(16777215, 50))
        self.centroidPlainTextEdit.setReadOnly(True)
        self.centroidPlainTextEdit.setObjectName("centroidPlainTextEdit")
        self.verticalLayout_7.addWidget(self.centroidPlainTextEdit)
        self.ExamplesListWidget = QtWidgets.QListView(self.page_2)
        self.ExamplesListWidget.setObjectName("ExamplesListWidget")
        self.verticalLayout_7.addWidget(self.ExamplesListWidget)
        self.horizontalLayout_5.addLayout(self.verticalLayout_7)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.toolBox.addItem(self.page_2, "")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.loadClustersButton = QtWidgets.QPushButton(self.page_3)
        self.loadClustersButton.setObjectName("loadClustersButton")
        self.horizontalLayout_7.addWidget(self.loadClustersButton)
        self.generateExportButton = QtWidgets.QPushButton(self.page_3)
        self.generateExportButton.setObjectName("generateExportButton")
        self.horizontalLayout_7.addWidget(self.generateExportButton)
        self.testFunctionButton = QtWidgets.QPushButton(self.page_3)
        self.testFunctionButton.setObjectName("testFunctionButton")
        self.horizontalLayout_7.addWidget(self.testFunctionButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.verticalLayout_9.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.ClustersTreeWidget = QtWidgets.QTreeWidget(self.page_3)
        self.ClustersTreeWidget.setObjectName("ClustersTreeWidget")
        self.horizontalLayout_6.addWidget(self.ClustersTreeWidget)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.examplesListWidget_2 = QtWidgets.QListView(self.page_3)
        self.examplesListWidget_2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.examplesListWidget_2.setObjectName("examplesListWidget_2")
        self.verticalLayout_11.addWidget(self.examplesListWidget_2)
        self.functionTextEdit = QtWidgets.QPlainTextEdit(self.page_3)
        self.functionTextEdit.setTabStopWidth(10)
        self.functionTextEdit.setObjectName("functionTextEdit")
        self.verticalLayout_11.addWidget(self.functionTextEdit)
        self.outputTextEdit = QtWidgets.QPlainTextEdit(self.page_3)
        self.outputTextEdit.setMaximumSize(QtCore.QSize(16777215, 50))
        self.outputTextEdit.setReadOnly(True)
        self.outputTextEdit.setObjectName("outputTextEdit")
        self.verticalLayout_11.addWidget(self.outputTextEdit)
        self.horizontalLayout_6.addLayout(self.verticalLayout_11)
        self.verticalLayout_9.addLayout(self.horizontalLayout_6)
        self.toolBox.addItem(self.page_3, "")
        self.verticalLayout_3.addWidget(self.toolBox)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget = QtWidgets.QWidget(self.tab_3)
        self.widget.setMinimumSize(QtCore.QSize(0, 32))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.copyOutputButton = QtWidgets.QPushButton(self.widget)
        self.copyOutputButton.setObjectName("copyOutputButton")
        self.horizontalLayout.addWidget(self.copyOutputButton)
        self.saveOutputButton = QtWidgets.QPushButton(self.widget)
        self.saveOutputButton.setObjectName("saveOutputButton")
        self.horizontalLayout.addWidget(self.saveOutputButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_4.addWidget(self.widget)
        self.outputTextEdit_2 = QtWidgets.QPlainTextEdit(self.tab_3)
        self.outputTextEdit_2.setObjectName("outputTextEdit_2")
        self.verticalLayout_4.addWidget(self.outputTextEdit_2)
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.browseButton.setText(_translate("MainWindow", "..."))
        self.reloadButton.setText(_translate("MainWindow", "reload"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "report"))
        self.applySubstitutionsButton.setText(_translate("MainWindow", "apply"))
        self.addSubstitutionButton.setText(_translate("MainWindow", "add"))
        self.deleteSubstitutionButton.setText(_translate("MainWindow", "delete"))
        self.saveSubstitutionsButton.setText(_translate("MainWindow", "save"))
        self.loadSubstitutionsButton.setText(_translate("MainWindow", "load"))
        self.substitutionTableWidget.setSortingEnabled(True)
        item = self.substitutionTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "original"))
        item = self.substitutionTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "substitute"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "substitutions"))
        self.computeClustersButton.setText(_translate("MainWindow", "compute"))
        self.deleteClustersButton.setText(_translate("MainWindow", "delete"))
        self.freezeButton.setText(_translate("MainWindow", "freeze"))
        self.setParentButton.setText(_translate("MainWindow", "set parent"))
        self.showHistogramButton.setText(_translate("MainWindow", "histogram"))
        self.similarityMeasureCombobox.setItemText(0, _translate("MainWindow", "jaro distance"))
        self.windowSpinBox.setSuffix(_translate("MainWindow", " (chars)"))
        self.windowSpinBox.setPrefix(_translate("MainWindow", "window : "))
        self.thresholdSpinBox.setSuffix(_translate("MainWindow", " (%)"))
        self.thresholdSpinBox.setPrefix(_translate("MainWindow", "threshold : "))
        self.thresholdSpinBox_2.setSuffix(_translate("MainWindow", " (chars)"))
        self.thresholdSpinBox_2.setPrefix(_translate("MainWindow", "offset : "))
        self.clustersTableWidget.setSortingEnabled(True)
        item = self.clustersTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "cluster"))
        item = self.clustersTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "parent"))
        item = self.clustersTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "line count"))
        item = self.clustersTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "lines"))
        item = self.clustersTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "score"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "reductions"))
        self.loadClustersButton.setText(_translate("MainWindow", "load clusters"))
        self.generateExportButton.setText(_translate("MainWindow", "generate"))
        self.testFunctionButton.setText(_translate("MainWindow", "test"))
        self.ClustersTreeWidget.setSortingEnabled(True)
        self.ClustersTreeWidget.headerItem().setText(0, _translate("MainWindow", "cluster"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("MainWindow", "extractions"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "clusters"))
        self.copyOutputButton.setText(_translate("MainWindow", "copy"))
        self.saveOutputButton.setText(_translate("MainWindow", "save"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "output"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

