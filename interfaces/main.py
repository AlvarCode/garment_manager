# Form implementation generated from reading ui file 'ui_files/main.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 344)
        MainWindow.setMinimumSize(QtCore.QSize(519, 297))
        font = QtGui.QFont()
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("QLineEdit, QDoubleSpinBox, QComboBox {\n"
"    font-size: 11pt;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    min-height: 20px;\n"
"    padding: 4px; \n"
"}\n"
"\n"
"QDoubleSpinBox, QComboBox {\n"
"    min-height: 26px;\n"
"}\n"
"\n"
"#data_container {\n"
"    border: none;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stackedWidget.setMinimumSize(QtCore.QSize(80, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setObjectName("stackedWidget")
        self.view_data_page = QtWidgets.QWidget()
        self.view_data_page.setObjectName("view_data_page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.view_data_page)
        self.verticalLayout_2.setSpacing(12)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.title = QtWidgets.QLabel(parent=self.view_data_page)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.title.setObjectName("title")
        self.verticalLayout_2.addWidget(self.title)
        self.garments = QtWidgets.QTableWidget(parent=self.view_data_page)
        self.garments.setObjectName("garments")
        self.garments.setColumnCount(5)
        self.garments.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.garments.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.garments.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.garments.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.garments.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.garments.setHorizontalHeaderItem(4, item)
        self.garments.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_2.addWidget(self.garments)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.add_garment_btn = QtWidgets.QPushButton(parent=self.view_data_page)
        self.add_garment_btn.setMinimumSize(QtCore.QSize(100, 32))
        self.add_garment_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.add_garment_btn.setObjectName("add_garment_btn")
        self.horizontalLayout.addWidget(self.add_garment_btn)
        self.delete_garment_btn = QtWidgets.QPushButton(parent=self.view_data_page)
        self.delete_garment_btn.setMinimumSize(QtCore.QSize(100, 32))
        self.delete_garment_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.delete_garment_btn.setObjectName("delete_garment_btn")
        self.horizontalLayout.addWidget(self.delete_garment_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.stackedWidget.addWidget(self.view_data_page)
        self.register_page = QtWidgets.QWidget()
        self.register_page.setObjectName("register_page")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.register_page)
        self.verticalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_3.setSpacing(16)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.back_btn = QtWidgets.QPushButton(parent=self.register_page)
        self.back_btn.setMinimumSize(QtCore.QSize(80, 32))
        self.back_btn.setMaximumSize(QtCore.QSize(80, 32))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.back_btn.setFont(font)
        self.back_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.back_btn.setObjectName("back_btn")
        self.horizontalLayout_2.addWidget(self.back_btn)
        self.label_2 = QtWidgets.QLabel(parent=self.register_page)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.save_btn = QtWidgets.QPushButton(parent=self.register_page)
        self.save_btn.setMinimumSize(QtCore.QSize(100, 32))
        self.save_btn.setMaximumSize(QtCore.QSize(100, 32))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.save_btn.setFont(font)
        self.save_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.save_btn.setObjectName("save_btn")
        self.horizontalLayout_2.addWidget(self.save_btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.data_container = QtWidgets.QFrame(parent=self.register_page)
        self.data_container.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.data_container.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.data_container.setObjectName("data_container")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.data_container)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(16)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtWidgets.QLabel(parent=self.data_container)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.code = QtWidgets.QLineEdit(parent=self.data_container)
        self.code.setMaxLength(6)
        self.code.setObjectName("code")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.code)
        self.label_5 = QtWidgets.QLabel(parent=self.data_container)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
        self.name = QtWidgets.QLineEdit(parent=self.data_container)
        self.name.setObjectName("name")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.name)
        self.label_8 = QtWidgets.QLabel(parent=self.data_container)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_8)
        self.price = QtWidgets.QDoubleSpinBox(parent=self.data_container)
        self.price.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.price.setMaximum(99999.99)
        self.price.setObjectName("price")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.price)
        self.label_7 = QtWidgets.QLabel(parent=self.data_container)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_7)
        self.sizes = QtWidgets.QLineEdit(parent=self.data_container)
        self.sizes.setObjectName("sizes")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.sizes)
        self.label_6 = QtWidgets.QLabel(parent=self.data_container)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_6)
        self.category = QtWidgets.QComboBox(parent=self.data_container)
        self.category.setObjectName("category")
        self.category.addItem("")
        self.category.addItem("")
        self.category.addItem("")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.category)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.formLayout.setItem(5, QtWidgets.QFormLayout.ItemRole.FieldRole, spacerItem1)
        self.horizontalLayout_3.addLayout(self.formLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.add_color_btn = QtWidgets.QPushButton(parent=self.data_container)
        self.add_color_btn.setMinimumSize(QtCore.QSize(100, 32))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.add_color_btn.setFont(font)
        self.add_color_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.add_color_btn.setObjectName("add_color_btn")
        self.gridLayout.addWidget(self.add_color_btn, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.data_container)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 3)
        self.delete_color_btn = QtWidgets.QPushButton(parent=self.data_container)
        self.delete_color_btn.setMinimumSize(QtCore.QSize(100, 32))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.delete_color_btn.setFont(font)
        self.delete_color_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.delete_color_btn.setObjectName("delete_color_btn")
        self.gridLayout.addWidget(self.delete_color_btn, 3, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 0, 1, 1)
        self.colors = QtWidgets.QTableWidget(parent=self.data_container)
        self.colors.setObjectName("colors")
        self.colors.setColumnCount(2)
        self.colors.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.colors.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.colors.setHorizontalHeaderItem(1, item)
        self.colors.horizontalHeader().setStretchLastSection(True)
        self.colors.verticalHeader().setCascadingSectionResizes(False)
        self.colors.verticalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.colors, 1, 0, 1, 3)
        self.horizontalLayout_3.addLayout(self.gridLayout)
        self.verticalLayout_3.addWidget(self.data_container)
        self.stackedWidget.addWidget(self.register_page)
        self.verticalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 20))
        self.menubar.setObjectName("menubar")
        self.menuCargar_datos = QtWidgets.QMenu(parent=self.menubar)
        self.menuCargar_datos.setObjectName("menuCargar_datos")
        MainWindow.setMenuBar(self.menubar)
        self.load_file_act = QtGui.QAction(parent=MainWindow)
        self.load_file_act.setObjectName("load_file_act")
        self.generate_file_act = QtGui.QAction(parent=MainWindow)
        self.generate_file_act.setObjectName("generate_file_act")
        self.menuCargar_datos.addAction(self.load_file_act)
        self.menuCargar_datos.addAction(self.generate_file_act)
        self.menubar.addAction(self.menuCargar_datos.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Garment Manager"))
        self.title.setText(_translate("MainWindow", "Prendas Registradas"))
        item = self.garments.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Código"))
        item = self.garments.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.garments.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Precio ($)"))
        item = self.garments.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Tallas"))
        item = self.garments.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Categoría"))
        self.add_garment_btn.setText(_translate("MainWindow", "Nuevo"))
        self.delete_garment_btn.setText(_translate("MainWindow", "Borrar"))
        self.back_btn.setText(_translate("MainWindow", "Atras"))
        self.label_2.setText(_translate("MainWindow", "Nueva Prenda"))
        self.save_btn.setText(_translate("MainWindow", "Registrar"))
        self.label_4.setText(_translate("MainWindow", "Código"))
        self.code.setPlaceholderText(_translate("MainWindow", "XX-999"))
        self.label_5.setText(_translate("MainWindow", "Nombre"))
        self.label_8.setText(_translate("MainWindow", "Precio"))
        self.price.setPrefix(_translate("MainWindow", "$ "))
        self.label_7.setText(_translate("MainWindow", "Tallas"))
        self.label_6.setText(_translate("MainWindow", "Categoría"))
        self.category.setItemText(0, _translate("MainWindow", "Nuevo elemento"))
        self.category.setItemText(1, _translate("MainWindow", "Nuevo elemento"))
        self.category.setItemText(2, _translate("MainWindow", "Nuevo elemento"))
        self.add_color_btn.setText(_translate("MainWindow", "Nuevo"))
        self.label_3.setText(_translate("MainWindow", "Colores"))
        self.delete_color_btn.setText(_translate("MainWindow", "Borrar"))
        item = self.colors.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Código"))
        item = self.colors.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "URL de imagen"))
        self.menuCargar_datos.setTitle(_translate("MainWindow", "Datos"))
        self.load_file_act.setText(_translate("MainWindow", "Cargar desde archivo"))
        self.generate_file_act.setText(_translate("MainWindow", "Generar archivo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
