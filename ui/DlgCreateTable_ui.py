# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/DlgCreateTable.ui'
#
# Created: Sat Nov 12 11:39:12 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DlgCreateTable(object):
    def setupUi(self, DlgCreateTable):
        DlgCreateTable.setObjectName(_fromUtf8("DlgCreateTable"))
        DlgCreateTable.resize(474, 562)
        self.gridLayout_2 = QtGui.QGridLayout(DlgCreateTable)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.label_3 = QtGui.QLabel(DlgCreateTable)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridlayout.addWidget(self.label_3, 0, 0, 1, 2)
        self.cboSchema = QtGui.QComboBox(DlgCreateTable)
        self.cboSchema.setObjectName(_fromUtf8("cboSchema"))
        self.gridlayout.addWidget(self.cboSchema, 0, 2, 1, 1)
        self.label = QtGui.QLabel(DlgCreateTable)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridlayout.addWidget(self.label, 1, 0, 1, 2)
        self.editName = QtGui.QLineEdit(DlgCreateTable)
        self.editName.setObjectName(_fromUtf8("editName"))
        self.gridlayout.addWidget(self.editName, 1, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridlayout, 0, 0, 1, 2)
        self.vboxlayout = QtGui.QVBoxLayout()
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.btnAddField = QtGui.QPushButton(DlgCreateTable)
        self.btnAddField.setObjectName(_fromUtf8("btnAddField"))
        self.vboxlayout.addWidget(self.btnAddField)
        self.btnDeleteField = QtGui.QPushButton(DlgCreateTable)
        self.btnDeleteField.setObjectName(_fromUtf8("btnDeleteField"))
        self.vboxlayout.addWidget(self.btnDeleteField)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem)
        self.btnFieldUp = QtGui.QPushButton(DlgCreateTable)
        self.btnFieldUp.setObjectName(_fromUtf8("btnFieldUp"))
        self.vboxlayout.addWidget(self.btnFieldUp)
        self.btnFieldDown = QtGui.QPushButton(DlgCreateTable)
        self.btnFieldDown.setObjectName(_fromUtf8("btnFieldDown"))
        self.vboxlayout.addWidget(self.btnFieldDown)
        self.gridLayout_2.addLayout(self.vboxlayout, 1, 1, 1, 1)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setSpacing(8)
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.label_4 = QtGui.QLabel(DlgCreateTable)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.hboxlayout.addWidget(self.label_4)
        self.cboPrimaryKey = QtGui.QComboBox(DlgCreateTable)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboPrimaryKey.sizePolicy().hasHeightForWidth())
        self.cboPrimaryKey.setSizePolicy(sizePolicy)
        self.cboPrimaryKey.setObjectName(_fromUtf8("cboPrimaryKey"))
        self.hboxlayout.addWidget(self.cboPrimaryKey)
        self.gridLayout_2.addLayout(self.hboxlayout, 2, 0, 1, 2)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.chkGeomColumn = QtGui.QCheckBox(DlgCreateTable)
        self.chkGeomColumn.setObjectName(_fromUtf8("chkGeomColumn"))
        self.gridLayout.addWidget(self.chkGeomColumn, 0, 0, 1, 1)
        self.cboGeomType = QtGui.QComboBox(DlgCreateTable)
        self.cboGeomType.setObjectName(_fromUtf8("cboGeomType"))
        self.cboGeomType.addItem(_fromUtf8(""))
        self.cboGeomType.addItem(_fromUtf8(""))
        self.cboGeomType.addItem(_fromUtf8(""))
        self.cboGeomType.addItem(_fromUtf8(""))
        self.cboGeomType.addItem(_fromUtf8(""))
        self.cboGeomType.addItem(_fromUtf8(""))
        self.cboGeomType.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.cboGeomType, 0, 1, 1, 2)
        self.label_2 = QtGui.QLabel(DlgCreateTable)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.editGeomColumn = QtGui.QLineEdit(DlgCreateTable)
        self.editGeomColumn.setObjectName(_fromUtf8("editGeomColumn"))
        self.gridLayout.addWidget(self.editGeomColumn, 1, 1, 1, 1)
        self.label_5 = QtGui.QLabel(DlgCreateTable)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.spinGeomDim = QtGui.QSpinBox(DlgCreateTable)
        self.spinGeomDim.setMinimum(2)
        self.spinGeomDim.setMaximum(4)
        self.spinGeomDim.setObjectName(_fromUtf8("spinGeomDim"))
        self.gridLayout.addWidget(self.spinGeomDim, 2, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(50, 51, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 2, 2, 1)
        self.label_6 = QtGui.QLabel(DlgCreateTable)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.editGeomSrid = QtGui.QLineEdit(DlgCreateTable)
        self.editGeomSrid.setInputMask(_fromUtf8(""))
        self.editGeomSrid.setObjectName(_fromUtf8("editGeomSrid"))
        self.gridLayout.addWidget(self.editGeomSrid, 3, 1, 1, 1)
        self.chkSpatialIndex = QtGui.QCheckBox(DlgCreateTable)
        self.chkSpatialIndex.setObjectName(_fromUtf8("chkSpatialIndex"))
        self.gridLayout.addWidget(self.chkSpatialIndex, 4, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 3, 0, 1, 2)
        self.buttonBox = QtGui.QDialogButtonBox(DlgCreateTable)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_2.addWidget(self.buttonBox, 4, 0, 1, 2)
        self.fields = QtGui.QTableView(DlgCreateTable)
        self.fields.setObjectName(_fromUtf8("fields"))
        self.fields.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_2.addWidget(self.fields, 1, 0, 1, 1)

        self.retranslateUi(DlgCreateTable)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DlgCreateTable.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DlgCreateTable.reject)
        QtCore.QMetaObject.connectSlotsByName(DlgCreateTable)
        DlgCreateTable.setTabOrder(self.cboSchema, self.editName)
        DlgCreateTable.setTabOrder(self.editName, self.fields)
        DlgCreateTable.setTabOrder(self.fields, self.btnAddField)
        DlgCreateTable.setTabOrder(self.btnAddField, self.btnDeleteField)
        DlgCreateTable.setTabOrder(self.btnDeleteField, self.btnFieldUp)
        DlgCreateTable.setTabOrder(self.btnFieldUp, self.btnFieldDown)
        DlgCreateTable.setTabOrder(self.btnFieldDown, self.cboPrimaryKey)
        DlgCreateTable.setTabOrder(self.cboPrimaryKey, self.chkGeomColumn)
        DlgCreateTable.setTabOrder(self.chkGeomColumn, self.cboGeomType)
        DlgCreateTable.setTabOrder(self.cboGeomType, self.editGeomColumn)
        DlgCreateTable.setTabOrder(self.editGeomColumn, self.spinGeomDim)
        DlgCreateTable.setTabOrder(self.spinGeomDim, self.editGeomSrid)
        DlgCreateTable.setTabOrder(self.editGeomSrid, self.chkSpatialIndex)
        DlgCreateTable.setTabOrder(self.chkSpatialIndex, self.buttonBox)

    def retranslateUi(self, DlgCreateTable):
        DlgCreateTable.setWindowTitle(QtGui.QApplication.translate("DlgCreateTable", "Create Table", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("DlgCreateTable", "Schema", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DlgCreateTable", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAddField.setText(QtGui.QApplication.translate("DlgCreateTable", "Add field", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDeleteField.setText(QtGui.QApplication.translate("DlgCreateTable", "Delete field", None, QtGui.QApplication.UnicodeUTF8))
        self.btnFieldUp.setText(QtGui.QApplication.translate("DlgCreateTable", "Up", None, QtGui.QApplication.UnicodeUTF8))
        self.btnFieldDown.setText(QtGui.QApplication.translate("DlgCreateTable", "Down", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("DlgCreateTable", "Primary key", None, QtGui.QApplication.UnicodeUTF8))
        self.chkGeomColumn.setText(QtGui.QApplication.translate("DlgCreateTable", "Create geometry column", None, QtGui.QApplication.UnicodeUTF8))
        self.cboGeomType.setItemText(0, QtGui.QApplication.translate("DlgCreateTable", "POINT", None, QtGui.QApplication.UnicodeUTF8))
        self.cboGeomType.setItemText(1, QtGui.QApplication.translate("DlgCreateTable", "LINESTRING", None, QtGui.QApplication.UnicodeUTF8))
        self.cboGeomType.setItemText(2, QtGui.QApplication.translate("DlgCreateTable", "POLYGON", None, QtGui.QApplication.UnicodeUTF8))
        self.cboGeomType.setItemText(3, QtGui.QApplication.translate("DlgCreateTable", "MULTIPOINT", None, QtGui.QApplication.UnicodeUTF8))
        self.cboGeomType.setItemText(4, QtGui.QApplication.translate("DlgCreateTable", "MULTILINESTRING", None, QtGui.QApplication.UnicodeUTF8))
        self.cboGeomType.setItemText(5, QtGui.QApplication.translate("DlgCreateTable", "MULTIPOLYGON", None, QtGui.QApplication.UnicodeUTF8))
        self.cboGeomType.setItemText(6, QtGui.QApplication.translate("DlgCreateTable", "GEOMETRYCOLLECTION", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("DlgCreateTable", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.editGeomColumn.setText(QtGui.QApplication.translate("DlgCreateTable", "the_geom", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("DlgCreateTable", "Dimensions", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("DlgCreateTable", "SRID", None, QtGui.QApplication.UnicodeUTF8))
        self.editGeomSrid.setText(QtGui.QApplication.translate("DlgCreateTable", "-1", None, QtGui.QApplication.UnicodeUTF8))
        self.chkSpatialIndex.setText(QtGui.QApplication.translate("DlgCreateTable", "Create spatial index", None, QtGui.QApplication.UnicodeUTF8))

