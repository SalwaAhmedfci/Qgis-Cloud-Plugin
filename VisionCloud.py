# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qgiscloudplugin.ui'
#
# Created by: PyQt5 UI
import pickle

import db_connection
import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont, QIcon, QPixmap
import PyQt5.QtWidgets
from db_connection import *
from User_db import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = PyQt5.QtWidgets.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return PyQt5.QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return PyQt5.QtWidgets.QApplication.translate(context, text, disambig)

list_of_databases = []
names = []
user = CurrentUser
publictoken = ""


def Get_Current_Databases(list_of_databases):
    names = []
    for database in list_of_databases:
        names.append(database.get_Dbname())
        

    # if len(names) != 0:

    ui.tabDatabases.addItems(names)
    ui.cbUploadDatabase.addItems(names)
    # else:
    #      return


class Ui_LoginDialog(object):
    user = CurrentUser
    publictoken = ""

    def Emmit_Login(self):
        LoginDialog = QtWidgets.QDialog()
        ui = Ui_LoginDialog()
        ui.setupUi(LoginDialog)
        LoginDialog.show()
        LoginDialog.exec_()
        if LoginDialog.accept:
            username = ui.editUser.text()
            password = ui.editPassword.text()
            data = {"username": username,
                    "password": password}

            url = creds.URL.format(username, password)
            response = requests.post(url, json=data)

            re = response.json()
            json_data = json.dumps(re, default=lambda o: o.__dict__, indent=4)

            # if json_data[0] == False:
            #     raise Exception('wrong username or password')

            if len(re['data']['UserGeoDatabases']) != 0:
                user_db = re['data']['UserGeoDatabases']
            # number_of_databases = len(re['data']['UserGeoDatabases'])

            list_of_databases = []
            for i in user_db:
                db = DataBase(i['Dbname'],
                              i['UserName'],
                              i['Password'],
                              i['Port'],
                              i['Host'],
                              i['Dbtype'],
                              i['UserId'])
                
                list_of_databases.append(db)

        user = CurrentUser(username, re['data']['Email'], re['data']['displayName'],
                           re['data']['Token'],
                           re['data']['FirstName'], re['data']['LastName'], re['data']['PictureUrl'],
                           re['data']['UserType'], re['data']['Role'], re['data']['Id'],
                           list_of_databases)

        user.set_Token(re['data']['Token'])

        file_to_store = open("stored_object.pickle", "wb")
        pickle.dump(user, file_to_store)

        file_to_store.close()


        Get_Current_Databases(list_of_databases)

    def Create_database(self):
        file_to_read = open("stored_object.pickle", "rb")
        loaded_object = pickle.load(file_to_read)
        file_to_read.close()

        re = db_connection.Request_Database_Creation(loaded_object.Token)
        list_of_databases = []
        for item in re['data']:

            db = DataBase(item['Dbname'],
                          item['UserName'],
                          item['Password'],
                          item['Port'],
                          item['Host'],
                          item['Dbtype'],
                          item['UserId'])

            list_of_databases.append(db)
        Get_Current_Databases(list_of_databases)



    def setupUi(self, LoginDialog):
        LoginDialog.setObjectName("LoginDialog")
        LoginDialog.resize(268, 95)
        self.gridLayout = QtWidgets.QGridLayout(LoginDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(LoginDialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.editUser = QtWidgets.QLineEdit(LoginDialog)
        self.editUser.setEnabled(True)
        self.editUser.setInputMask("")
        self.editUser.setText("")
        self.editUser.setObjectName("editUser")
        self.gridLayout.addWidget(self.editUser, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(LoginDialog)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.editPassword = QtWidgets.QLineEdit(LoginDialog)
        self.editPassword.setEnabled(True)
        self.editPassword.setInputMask("")
        self.editPassword.setText("")
        self.editPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.editPassword.setObjectName("editPassword")
        self.gridLayout.addWidget(self.editPassword, 1, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(LoginDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 2)
        self.label_5.setBuddy(self.editUser)
        self.label_6.setBuddy(self.editPassword)
        self.retranslateUi_Login(LoginDialog)
        self.buttonBox.accepted.connect(LoginDialog.accept)
        self.buttonBox.rejected.connect(LoginDialog.reject)

        # QtCore.QMetaObject.connectSlotsByName(LoginDialog)

    def retranslateUi_Login(self, LoginDialog):
        _translate = QtCore.QCoreApplication.translate
        LoginDialog.setWindowTitle(_translate("LoginDialog", "Login"))
        self.label_5.setText(_translate("LoginDialog", "User:"))
        self.label_6.setText(_translate("LoginDialog", "Password:"))


class Ui_QgisCloudPlugin(object):

    def setupUi(self, QgisCloudPlugin):
        QgisCloudPlugin.setObjectName(_fromUtf8("QgisCloudPlugin"))
        QgisCloudPlugin.resize(501, 703)
        QgisCloudPlugin.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.dockWidgetContents = PyQt5.QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.gridLayout_3 = PyQt5.QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.tabWidget = PyQt5.QtWidgets.QTabWidget(self.dockWidgetContents)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.mapTab = PyQt5.QtWidgets.QWidget()
        self.mapTab.setObjectName(_fromUtf8("mapTab"))
        self.gridLayout_4 = PyQt5.QtWidgets.QGridLayout(self.mapTab)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.logo_2 = PyQt5.QtWidgets.QLabel(self.mapTab)
        self.logo_2.setAutoFillBackground(True)
        self.logo_2.setPixmap(QPixmap(_fromUtf8("logo.png")))
        self.logo_2.setScaledContents(True)
        self.logo_2.setAlignment(QtCore.Qt.AlignCenter)
        self.logo_2.setObjectName(_fromUtf8("logo_2"))
        self.gridLayout_4.addWidget(self.logo_2, 0, 0, 1, 1)
        self.btnBackgroundLayer = PyQt5.QtWidgets.QToolButton(self.mapTab)
        self.btnBackgroundLayer.setPopupMode(PyQt5.QtWidgets.QToolButton.InstantPopup)
        self.btnBackgroundLayer.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.btnBackgroundLayer.setArrowType(QtCore.Qt.NoArrow)
        self.btnBackgroundLayer.setObjectName(_fromUtf8("btnBackgroundLayer"))
        self.gridLayout_4.addWidget(self.btnBackgroundLayer, 1, 0, 1, 1)
        self.labelOpenLayersPlugin = PyQt5.QtWidgets.QLabel(self.mapTab)
        self.labelOpenLayersPlugin.setWordWrap(True)
        self.labelOpenLayersPlugin.setObjectName(_fromUtf8("labelOpenLayersPlugin"))
        self.gridLayout_4.addWidget(self.labelOpenLayersPlugin, 2, 0, 1, 1)
        self.line_2 = PyQt5.QtWidgets.QFrame(self.mapTab)
        self.line_2.setFrameShape(PyQt5.QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(PyQt5.QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout_4.addWidget(self.line_2, 3, 0, 1, 1)
        self.btnPublishMap = PyQt5.QtWidgets.QPushButton(self.mapTab)
        self.btnPublishMap.setObjectName(_fromUtf8("btnPublishMap"))
        self.gridLayout_4.addWidget(self.btnPublishMap, 4, 0, 1, 1)
        self.line_3 = PyQt5.QtWidgets.QFrame(self.mapTab)
        self.line_3.setFrameShape(PyQt5.QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(PyQt5.QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout_4.addWidget(self.line_3, 5, 0, 1, 1)
        self.widgetServices = PyQt5.QtWidgets.QWidget(self.mapTab)
        self.widgetServices.setObjectName(_fromUtf8("widgetServices"))
        self.gridLayout = PyQt5.QtWidgets.QGridLayout(self.widgetServices)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = PyQt5.QtWidgets.QLabel(self.widgetServices)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.lblWMS = PyQt5.QtWidgets.QLabel(self.widgetServices)
        self.lblWMS.setOpenExternalLinks(True)
        self.lblWMS.setObjectName(_fromUtf8("lblWMS"))
        self.gridLayout.addWidget(self.lblWMS, 1, 1, 1, 1)
        self.label_5 = PyQt5.QtWidgets.QLabel(self.widgetServices)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.lblMaps = PyQt5.QtWidgets.QLabel(self.widgetServices)
        self.lblMaps.setOpenExternalLinks(True)
        self.lblMaps.setObjectName(_fromUtf8("lblMaps"))
        self.gridLayout.addWidget(self.lblMaps, 2, 1, 1, 1)
        self.label_8 = PyQt5.QtWidgets.QLabel(self.widgetServices)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)
        self.lblMobileMap_2 = PyQt5.QtWidgets.QLabel(self.widgetServices)
        self.lblMobileMap_2.setEnabled(True)
        self.lblMobileMap_2.setOpenExternalLinks(True)
        self.lblMobileMap_2.setObjectName(_fromUtf8("lblMobileMap_2"))
        self.gridLayout.addWidget(self.lblMobileMap_2, 3, 1, 1, 1)
        self.label_3 = PyQt5.QtWidgets.QLabel(self.widgetServices)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.lblWebmap = PyQt5.QtWidgets.QLabel(self.widgetServices)
        self.lblWebmap.setOpenExternalLinks(True)
        self.lblWebmap.setObjectName(_fromUtf8("lblWebmap"))
        self.gridLayout.addWidget(self.lblWebmap, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.widgetServices, 6, 0, 1, 1)
        spacerItem = PyQt5.QtWidgets.QSpacerItem(20, 20, PyQt5.QtWidgets.QSizePolicy.Minimum,
                                                 PyQt5.QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_4.addItem(spacerItem, 7, 0, 1, 1)
        self.frame = PyQt5.QtWidgets.QFrame(self.mapTab)
        self.frame.setEnabled(True)
        self.frame.setFrameShape(PyQt5.QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(PyQt5.QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(1)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_6 = PyQt5.QtWidgets.QGridLayout(self.frame)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.widgetMaps = PyQt5.QtWidgets.QWidget(self.frame)
        sizePolicy = PyQt5.QtWidgets.QSizePolicy(PyQt5.QtWidgets.QSizePolicy.Preferred,
                                                 PyQt5.QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetMaps.sizePolicy().hasHeightForWidth())
        self.widgetMaps.setSizePolicy(sizePolicy)
        self.widgetMaps.setObjectName(_fromUtf8("widgetMaps"))
        self.gridLayout_2 = PyQt5.QtWidgets.QGridLayout(self.widgetMaps)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.lblMaps_3 = PyQt5.QtWidgets.QLabel(self.widgetMaps)
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblMaps_3.setFont(font)
        self.lblMaps_3.setObjectName(_fromUtf8("lblMaps_3"))
        self.gridLayout_2.addWidget(self.lblMaps_3, 0, 0, 1, 1)
        self.tabMaps = PyQt5.QtWidgets.QListWidget(self.widgetMaps)
        self.tabMaps.setObjectName(_fromUtf8("tabMaps"))
        self.gridLayout_2.addWidget(self.tabMaps, 1, 0, 1, 3)
        self.btnMapLoad = PyQt5.QtWidgets.QPushButton(self.widgetMaps)
        self.btnMapLoad.setObjectName(_fromUtf8("btnMapLoad"))
        self.gridLayout_2.addWidget(self.btnMapLoad, 2, 0, 1, 1)
        self.btnMapDelete = PyQt5.QtWidgets.QPushButton(self.widgetMaps)
        self.btnMapDelete.setEnabled(False)
        self.btnMapDelete.setObjectName(_fromUtf8("btnMapDelete"))
        self.gridLayout_2.addWidget(self.btnMapDelete, 2, 1, 1, 1)
        spacerItem1 = PyQt5.QtWidgets.QSpacerItem(145, 20, PyQt5.QtWidgets.QSizePolicy.Expanding,
                                                  PyQt5.QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 2, 2, 1, 1)
        self.gridLayout_6.addWidget(self.widgetMaps, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame, 8, 0, 1, 1)
        self.tabWidget.addTab(self.mapTab, _fromUtf8(""))
        self.uploadTab = PyQt5.QtWidgets.QWidget()
        self.uploadTab.setEnabled(True)
        self.uploadTab.setObjectName(_fromUtf8("uploadTab"))
        self.verticalLayout_6 = PyQt5.QtWidgets.QVBoxLayout(self.uploadTab)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.horizontalLayout_3 = PyQt5.QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_10 = PyQt5.QtWidgets.QLabel(self.uploadTab)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_3.addWidget(self.label_10)
        self.cbUploadDatabase = PyQt5.QtWidgets.QComboBox(self.uploadTab)
        self.cbUploadDatabase.setObjectName(_fromUtf8("cbUploadDatabase"))
        self.horizontalLayout_3.addWidget(self.cbUploadDatabase)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.lblDbSizeUpload = PyQt5.QtWidgets.QLabel(self.uploadTab)
        self.lblDbSizeUpload.setText(_fromUtf8(""))
        self.lblDbSizeUpload.setObjectName(_fromUtf8("lblDbSizeUpload"))
        self.verticalLayout_6.addWidget(self.lblDbSizeUpload)
        self.tblLocalLayers = PyQt5.QtWidgets.QTableWidget(self.uploadTab)
        self.tblLocalLayers.setSelectionBehavior(PyQt5.QtWidgets.QAbstractItemView.SelectRows)
        self.tblLocalLayers.setObjectName(_fromUtf8("tblLocalLayers"))
        self.tblLocalLayers.setColumnCount(0)
        self.tblLocalLayers.setRowCount(0)
        self.tblLocalLayers.horizontalHeader().setStretchLastSection(True)
        self.tblLocalLayers.verticalHeader().setVisible(False)
        self.verticalLayout_6.addWidget(self.tblLocalLayers)
        self.horizontalLayout_7 = PyQt5.QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        spacerItem2 = PyQt5.QtWidgets.QSpacerItem(40, 20, PyQt5.QtWidgets.QSizePolicy.Expanding,
                                                  PyQt5.QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.btnRefreshLocalLayers = PyQt5.QtWidgets.QPushButton(self.uploadTab)
        self.btnRefreshLocalLayers.setObjectName(_fromUtf8("btnRefreshLocalLayers"))
        self.horizontalLayout_7.addWidget(self.btnRefreshLocalLayers)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.btnUploadData = PyQt5.QtWidgets.QPushButton(self.uploadTab)
        self.btnUploadData.setObjectName(_fromUtf8("btnUploadData"))
        self.verticalLayout_6.addWidget(self.btnUploadData)
        self.progressWidget = PyQt5.QtWidgets.QWidget(self.uploadTab)
        self.progressWidget.setObjectName(_fromUtf8("progressWidget"))
        self.horizontalLayout_6 = PyQt5.QtWidgets.QHBoxLayout(self.progressWidget)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.lblProgress = PyQt5.QtWidgets.QLabel(self.progressWidget)
        self.lblProgress.setSizePolicy(sizePolicy)
        self.lblProgress.setText(_fromUtf8(""))
        self.lblProgress.setObjectName(_fromUtf8("lblProgress"))
        self.horizontalLayout_6.addWidget(self.lblProgress)
        self.verticalLayout_6.addWidget(self.progressWidget)
        self.tabWidget.addTab(self.uploadTab, _fromUtf8(""))
        self.accountTab = PyQt5.QtWidgets.QWidget()
        self.accountTab.setObjectName(_fromUtf8("accountTab"))
        self.gridLayout_5 = PyQt5.QtWidgets.QGridLayout(self.accountTab)

        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.horizontalLayout_4 = PyQt5.QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_2 = PyQt5.QtWidgets.QLabel(self.accountTab)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_4.addWidget(self.label_2)
        self.editServer = PyQt5.QtWidgets.QLineEdit(self.accountTab)
        self.editServer.setEnabled(True)
        self.editServer.setObjectName(_fromUtf8("editServer"))
        self.horizontalLayout_4.addWidget(self.editServer)
        self.resetUrlBtn = PyQt5.QtWidgets.QToolButton(self.accountTab)
        icon = QIcon()
        icon.addPixmap(QPixmap(_fromUtf8("icon.png")), QIcon.Normal, QIcon.Off)
        self.resetUrlBtn.setIcon(icon)
        self.resetUrlBtn.setObjectName(_fromUtf8("resetUrlBtn"))
        self.horizontalLayout_4.addWidget(self.resetUrlBtn)
        self.gridLayout_5.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.horizontalLayout_5 = PyQt5.QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.btnLogin = PyQt5.QtWidgets.QPushButton(self.accountTab)
        self.btnLogin.clicked.connect(Ui_LoginDialog.Emmit_Login)

        self.btnLogin.setObjectName(_fromUtf8("btnLogin"))
        self.horizontalLayout_5.addWidget(self.btnLogin)
        self.lblSignup = PyQt5.QtWidgets.QLabel(self.accountTab)
        self.lblSignup.setAlignment(QtCore.Qt.AlignCenter)
        self.lblSignup.setOpenExternalLinks(True)
        self.lblSignup.setObjectName(_fromUtf8("lblSignup"))
        self.horizontalLayout_5.addWidget(self.lblSignup)
        self.lblLoginStatus = PyQt5.QtWidgets.QLabel(self.accountTab)
        self.lblLoginStatus.setObjectName(_fromUtf8("lblLoginStatus"))
        self.horizontalLayout_5.addWidget(self.lblLoginStatus)
        spacerItem3 = PyQt5.QtWidgets.QSpacerItem(40, 20, PyQt5.QtWidgets.QSizePolicy.Expanding,
                                                  PyQt5.QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.btnLogout = PyQt5.QtWidgets.QPushButton(self.accountTab)
        self.btnLogout.setObjectName(_fromUtf8("btnLogout"))
        self.horizontalLayout_5.addWidget(self.btnLogout)
        self.gridLayout_5.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        self.widgetDatabases = PyQt5.QtWidgets.QWidget(self.accountTab)
        self.widgetDatabases.setSizePolicy(sizePolicy)
        self.widgetDatabases.setObjectName(_fromUtf8("widgetDatabases"))
        self.verticalLayout_3 = PyQt5.QtWidgets.QVBoxLayout(self.widgetDatabases)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.line = PyQt5.QtWidgets.QFrame(self.widgetDatabases)
        self.line.setFrameShape(PyQt5.QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(PyQt5.QtWidgets.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_3.addWidget(self.line)
        self.horizontalLayout_2 = PyQt5.QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_29 = PyQt5.QtWidgets.QLabel(self.widgetDatabases)
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.horizontalLayout_2.addWidget(self.label_29)
        self.lblDbSize = PyQt5.QtWidgets.QLabel(self.widgetDatabases)
        self.lblDbSize.setText(_fromUtf8(""))
        self.lblDbSize.setObjectName(_fromUtf8("lblDbSize"))
        self.horizontalLayout_2.addWidget(self.lblDbSize)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.tabDatabases = PyQt5.QtWidgets.QListWidget(self.widgetDatabases)
        self.tabDatabases.setSelectionBehavior(PyQt5.QtWidgets.QAbstractItemView.SelectRows)
        self.tabDatabases.setObjectName(_fromUtf8("tabDatabases"))
        self.verticalLayout_3.addWidget(self.tabDatabases)
        self.horizontalLayout = PyQt5.QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnDbCreate = PyQt5.QtWidgets.QPushButton(self.widgetDatabases)

        self.btnDbCreate.setObjectName(_fromUtf8("btnDbCreate"))
        self.horizontalLayout.addWidget(self.btnDbCreate)
        self.btnDbDelete = PyQt5.QtWidgets.QPushButton(self.widgetDatabases)
        self.btnDbDelete.setEnabled(False)
        self.btnDbDelete.setObjectName(_fromUtf8("btnDbDelete"))
        self.horizontalLayout.addWidget(self.btnDbDelete)
        spacerItem4 = PyQt5.QtWidgets.QSpacerItem(37, 17, PyQt5.QtWidgets.QSizePolicy.Expanding,
                                                  PyQt5.QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.btnDbRefresh = PyQt5.QtWidgets.QPushButton(self.widgetDatabases)
        self.btnDbRefresh.setObjectName(_fromUtf8("btnDbRefresh"))
        self.horizontalLayout.addWidget(self.btnDbRefresh)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.gridLayout_5.addWidget(self.widgetDatabases, 2, 0, 1, 1)
        self.line_4 = PyQt5.QtWidgets.QFrame(self.accountTab)
        self.line_4.setFrameShape(PyQt5.QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(PyQt5.QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.gridLayout_5.addWidget(self.line_4, 3, 0, 1, 1)
        self.tabWidget.addTab(self.accountTab, _fromUtf8(""))
        self.aboutTab = PyQt5.QtWidgets.QWidget()
        self.aboutTab.setObjectName(_fromUtf8("aboutTab"))
        self.verticalLayout = PyQt5.QtWidgets.QVBoxLayout(self.aboutTab)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.logo = PyQt5.QtWidgets.QLabel(self.aboutTab)
        self.logo.setAutoFillBackground(False)
        self.logo.setPixmap(QPixmap(_fromUtf8("logo.png")))
        self.logo.setScaledContents(True)
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName(_fromUtf8("logo"))
        self.verticalLayout.addWidget(self.logo)
        self.horizontalLayout_8 = PyQt5.QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_6 = PyQt5.QtWidgets.QLabel(self.aboutTab)
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_8.addWidget(self.label_6)
        self.lblVersionPlugin = PyQt5.QtWidgets.QLabel(self.aboutTab)
        self.lblVersionPlugin.setSizePolicy(sizePolicy)
        self.lblVersionPlugin.setText(_fromUtf8(""))
        self.lblVersionPlugin.setObjectName(_fromUtf8("lblVersionPlugin"))
        self.horizontalLayout_8.addWidget(self.lblVersionPlugin)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.aboutText = PyQt5.QtWidgets.QTextEdit(self.aboutTab)
        self.aboutText.setObjectName(_fromUtf8("aboutText"))
        self.verticalLayout.addWidget(self.aboutText)
        self.tabWidget.addTab(self.aboutTab, _fromUtf8(""))
        self.gridLayout_3.addWidget(self.tabWidget, 1, 0, 1, 1)
        QgisCloudPlugin.setWidget(self.dockWidgetContents)
        self.label_2.setBuddy(self.editServer)

        self.retranslateUi(QgisCloudPlugin)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(QgisCloudPlugin)
        self.btnDbCreate.clicked.connect(Ui_LoginDialog.Create_database)

    def retranslateUi(self, QgisCloudPlugin):
        QgisCloudPlugin.setWindowTitle(_translate("VisionCloudPlugin", " Cloud", None))
        self.btnBackgroundLayer.setText(_translate("QgisCloudPlugin", "Add background layer", None))
        self.labelOpenLayersPlugin.setText(
            _translate("QgisCloudPlugin", "<i>To add a background layer to the map, install the OpenLayers plugin.</i>",
                       None))
        self.btnPublishMap.setText(_translate("QgisCloudPlugin", "Publish Map", None))
        self.label.setText(_translate("QgisCloudPlugin", "Public WMS", None))
        self.lblWMS.setText(_translate("QgisCloudPlugin",
                                       "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                       "p, li { white-space: pre-wrap; }\n"
                                       "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                       "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"http://wms.qgiscloud.com/user/map\"><span style=\" font-size:9pt; text-decoration: underline; color:#0057ae;\">https://wms.qgiscloud.com/user/map</span></a></p></body></html>",
                                       None))
        self.label_5.setText(_translate("QgisCloudPlugin", "Map Admin", None))
        self.lblMaps.setText(_translate("QgisCloudPlugin",
                                        "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                        "p, li { white-space: pre-wrap; }\n"
                                        "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"http://qgiscloud.com/maps\"><span style=\" font-size:9pt; text-decoration: underline; color:#0057ae;\">https://qgiscloud.com/maps</span></a></p></body></html>",
                                        None))
        self.label_8.setText(_translate("QgisCloudPlugin", "Support", None))
        self.lblMobileMap_2.setText(_translate("QgisCloudPlugin",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"mailto:support@qgiscloud.com?subject=QGISCloud support\"><span style=\" font-family:\'Ubuntu\'; text-decoration: underline; color:#0057ae;\">support@qgiscloud.com</span></a></p></body></html>",
                                               None))
        self.label_3.setText(_translate("QgisCloudPlugin", "Webmap", None))
        self.lblWebmap.setText(_translate("QgisCloudPlugin",
                                          "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                          "p, li { white-space: pre-wrap; }\n"
                                          "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                          "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"http://qgiscloud.com/user/map\"><span style=\" font-size:9pt; text-decoration: underline; color:#0057ae;\">https://qgiscloud.com/user/map</span></a></p></body></html>",
                                          None))
        self.lblMaps_3.setText(_translate("QgisCloudPlugin", "Published Maps", None))
        self.btnMapLoad.setText(_translate("QgisCloudPlugin", "Open Project", None))
        self.btnMapDelete.setText(_translate("QgisCloudPlugin", "Delete", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mapTab), _translate("QgisCloudPlugin", "Maps", None))
        self.label_10.setText(_translate("QgisCloudPlugin", "Database:", None))
        self.btnRefreshLocalLayers.setText(_translate("QgisCloudPlugin", "Refresh layers", None))
        self.btnUploadData.setText(_translate("QgisCloudPlugin", "Upload data", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.uploadTab),
                                  _translate("QgisCloudPlugin", "Upload Data", None))
        self.label_2.setText(_translate("QgisCloudPlugin", "&Server:", None))
        self.editServer.setText(_translate("QgisCloudPlugin", "http://gis2.geoserver.visionkuwait.com/", None))
        self.resetUrlBtn.setToolTip(_translate("QgisCloudPlugin", "Reset QGIS Cloud API URL", None))
        self.resetUrlBtn.setText(_translate("QgisCloudPlugin", "...", None))
        self.btnLogin.setText(_translate("QgisCloudPlugin", "Login", None))
        self.lblSignup.setText(_translate("QgisCloudPlugin",
                                          "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                          "p, li { white-space: pre-wrap; }\n"
                                          "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                          "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"http://gis2.geoserver.visionkuwait.com/sessions/signup\"><span style=\" text-decoration: underline; color:#0057ae;\">Signup</span></a></p></body></html>",
                                          None))
        self.lblLoginStatus.setText(_translate("QgisCloudPlugin", "Logged in as ...", None))
        self.btnLogout.setText(_translate("QgisCloudPlugin", "Logout", None))
        self.label_29.setText(_translate("QgisCloudPlugin", "Databases", None))
        self.btnDbCreate.setText(_translate("QgisCloudPlugin", "Create", None))
        self.btnDbDelete.setText(_translate("QgisCloudPlugin", "Delete", None))
        self.btnDbRefresh.setText(_translate("QgisCloudPlugin", "Refresh", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.accountTab),
                                  _translate("QgisCloudPlugin", "Account", None))
        self.label_6.setText(_translate("QgisCloudPlugin", "<b>Plugin version:</b>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.aboutTab), _translate("QgisCloudPlugin", "About", None))


if __name__ == "__main__":
    import sys

    app = PyQt5.QtWidgets.QApplication(sys.argv)
    QgisCloudPlugin = PyQt5.QtWidgets.QDockWidget()
    # run the mainwindow
    ui = Ui_QgisCloudPlugin()
    ui.setupUi(QgisCloudPlugin)
    QgisCloudPlugin.show()

    sys.exit(app.exec_())
