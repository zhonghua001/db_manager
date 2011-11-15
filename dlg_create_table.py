# -*- coding: utf-8 -*-

"""
/***************************************************************************
Name                 : DB Manager
Description          : Database manager plugin for QuantumGIS
Date                 : Oct 13, 2011
copyright            : (C) 2011 by Giuseppe Sucameli
email                : brush.tyler@gmail.com

The content of this file is based on 
- PG_Manager by Martin Dobias (GPLv2 license)
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from .db_plugins.plugin import DbError, NewTableField
from .dlg_db_error import DlgDbError

from ui.DlgCreateTable_ui import Ui_DlgCreateTable

class TableFieldsDelegate(QItemDelegate):
	""" delegate with some special item editors """
	
	def __init__(self, field_types, parent=None):
		QItemDelegate.__init__(self, parent)
		self.fieldTypes = field_types
		
	def createEditor(self, parent, option, index):
		# special combobox for field type
		if index.column() == 1:
			cbo = QComboBox(parent)
			cbo.setEditable(True)
			cbo.setAutoCompletion(True)
			cbo.setFrame(False)
			for item in self.fieldTypes:
				cbo.addItem(item)
			return cbo
		elif index.column() == 2:
			return QCheckBox(parent)
		return QItemDelegate.createEditor(self, parent, option, index)
		
	def setEditorData(self, editor, index):
		""" load data from model to editor """
		m = index.model()
		if index.column() == 1:
			txt = m.data(index, Qt.DisplayRole).toString()
			editor.setEditText(txt)
		elif index.column() == 2:
			checked = m.data(index, Qt.DisplayRole).toBool()
			editor.setChecked( checked )
		else:
			# use default
			QItemDelegate.setEditorData(self, editor, index)
		
	def setModelData(self, editor, model, index):
		""" save data from editor back to model """
		if index.column() == 1:
			model.setData(index, QVariant(editor.currentText()))
		elif index.column() == 1:
			model.setData(index, QVariant(editor.isChecked()))
		else:
			# use default
			QItemDelegate.setModelData(self, editor, model, index)
			if index.column() == 0:
				self.emit(SIGNAL("columnNameChanged()"))



class TableFieldsModel(QStandardItemModel):
	def __init__(self, parent):
		QStandardItemModel.__init__(self, 0,3, parent)
		self.header = ['Name', 'Type', 'Not Null']
		
	def headerData(self, section, orientation, role):
		if orientation == Qt.Horizontal and role == Qt.DisplayRole:
			return QVariant(self.header[section])
		return QVariant()


class DlgCreateTable(QDialog, Ui_DlgCreateTable):
	
	def __init__(self, item, parent=None):
		QDialog.__init__(self, parent)
		self.item = item
		self._debugApp = self.item == None
		self.setupUi(self)

		if not self._debugApp:
			self.db = self.item.database()
			self.schemas = self.db.schemas()
			self.hasSchemas = self.schemas != None
			self.fieldTypes = self.db.connector.fieldTypes()
		else:
			self.db = None
			self.schemas = ['public', 'test']
			self.hasSchemas = True
			self.fieldTypes = ['integer', 'float', 'varchar(n)']
			

		m = TableFieldsModel(self)
		self.fields.setModel(m)
		
		d = TableFieldsDelegate(self.fieldTypes, self)
		self.fields.setItemDelegate(d)
		
		self.fields.setColumnWidth(0,140)
		self.fields.setColumnWidth(1,140)
		self.fields.setColumnWidth(2,50)
		
		b = QPushButton("&Create")
		self.buttonBox.addButton(b, QDialogButtonBox.ActionRole)

		self.connect(self.btnAddField, SIGNAL("clicked()"), self.addField)
		self.connect(self.btnDeleteField, SIGNAL("clicked()"), self.deleteField)
		self.connect(self.btnFieldUp, SIGNAL("clicked()"), self.fieldUp)
		self.connect(self.btnFieldDown, SIGNAL("clicked()"), self.fieldDown)
		self.connect(b, SIGNAL("clicked()"), self.createTable)
		
		self.connect(self.chkGeomColumn, SIGNAL("clicked()"), self.updateUi)
		
		self.connect(self.fields.selectionModel(), SIGNAL("selectionChanged(const QItemSelection &, const QItemSelection &)"), self.updateUiFields)
		self.connect(d, SIGNAL("columnNameChanged()"), self.updatePkeyCombo)

		self.populateSchemas()		
		self.updateUi()
		self.updateUiFields()
		
		
	def populateSchemas(self):
		self.cboSchema.clear()
		if not self.hasSchemas:
			self.hideSchemas()
			return

		index = -1
		for schema in self.schemas:
			self.cboSchema.addItem(schema.name)
			if hasattr(self.item, 'schema') and schema.name == self.item.schema().name:
					index = self.cboSchema.count()-1
		self.cboSchema.setCurrentIndex(index)

		
	def updateUi(self):
		useGeom = self.chkGeomColumn.isChecked()
		self.cboGeomType.setEnabled(useGeom)
		self.editGeomColumn.setEnabled(useGeom)
		self.spinGeomDim.setEnabled(useGeom)
		self.editGeomSrid.setEnabled(useGeom)
		self.chkSpatialIndex.setEnabled(useGeom)
		
	def updateUiFields(self):
		fld = self.selectedField()
		print ">>>", fld
		if fld is not None:
			up_enabled = (fld != 0)
			down_enabled = (fld != self.fields.model().rowCount()-1)
			del_enabled = True
		else:
			up_enabled, down_enabled, del_enabled = False, False, False
		self.btnFieldUp.setEnabled(up_enabled)
		self.btnFieldDown.setEnabled(down_enabled)
		self.btnDeleteField.setEnabled(del_enabled)
		
	def updatePkeyCombo(self, selRow=None):
		""" called when list of columns changes. if 'sel' is None, it keeps current index """
		
		if selRow is None:
			selRow = self.cboPrimaryKey.currentIndex()
		
		self.cboPrimaryKey.clear()
		
		m = self.fields.model()
		for row in xrange(m.rowCount()):
			name = m.data(m.index(row,0)).toString()
			self.cboPrimaryKey.addItem(name)

		self.cboPrimaryKey.setCurrentIndex(selRow)
		
	def addField(self):
		""" add new field to the end of field table """
		m = self.fields.model()
		newRow = m.rowCount()
		m.insertRows(newRow,1)
		
		indexName = m.index(newRow,0,QModelIndex())
		indexType = m.index(newRow,1,QModelIndex())
		indexNull = m.index(newRow,2,QModelIndex())
		
		m.setData(indexName, QVariant("new_field"))
		m.setData(indexType, QVariant( self.fieldTypes[0] if len(self.fieldTypes) > 0 else "integer" ))
		m.setData(indexNull, QVariant(False))
		
		# selects the new row
		sel = self.fields.selectionModel()
		sel.select(indexName, QItemSelectionModel.Rows | QItemSelectionModel.ClearAndSelect)
		
		# starts editing
		self.fields.edit(indexName)
		
		self.updatePkeyCombo(0 if newRow == 0 else None)
		
	def selectedField(self):
		sel = self.fields.selectedIndexes()
		if len(sel) < 1:
			return None
		return sel[0].row()
	
	def deleteField(self):
		""" delete selected field """
		row = self.selectedField()
		if row is None:
			QMessageBox.information(self, "sorry", "no field selected")
		else:
			self.fields.model().removeRows(row,1)
			
		self.updatePkeyCombo()
	
	def fieldUp(self):
		""" move selected field up """
		row = self.selectedField()
		if row is None:
			QMessageBox.information(self, "sorry", "no field selected")
			return
		if row == 0:
			QMessageBox.information(self, "sorry", "field is at top already")
			return
		
		# take row and reinsert it
		rowdata = self.fields.model().takeRow(row)
		self.fields.model().insertRow(row-1, rowdata)
		
		# set selection again
		index = self.fields.model().index(row-1, 0, QModelIndex())
		self.fields.selectionModel().select(index, QItemSelectionModel.Rows | QItemSelectionModel.ClearAndSelect)

		self.updatePkeyCombo()
	
	def fieldDown(self):
		""" move selected field down """
		row = self.selectedField()
		if row is None:
			QMessageBox.information(self, "sorry", "no field selected")
			return
		if row == self.fields.model().rowCount()-1:
			QMessageBox.information(self, "sorry", "field is at bottom already")
			return
		
		# take row and reinsert it
		rowdata = self.fields.model().takeRow(row)
		self.fields.model().insertRow(row+1, rowdata)
		
		# set selection again
		index = self.fields.model().index(row+1, 0, QModelIndex())
		self.fields.selectionModel().select(index, QItemSelectionModel.Rows | QItemSelectionModel.ClearAndSelect)
	
		self.updatePkeyCombo()
	
	def createTable(self):
		""" create table with chosen fields, optionally add a geometry column """
		if not self.hasSchemas:
			schema = None
		else:
			schema = unicode(self.cboSchema.currentText())
			if len(schema) == 0:
				QMessageBox.information(self, "sorry", "select schema!")
				return
		
		table = unicode(self.editName.text())
		if len(table) == 0:
			QMessageBox.information(self, "sorry", "enter table name!")
			return
		
		m = self.fields.model()
		if m.rowCount() == 0:
			QMessageBox.information(self, "sorry", "add some fields!")
			return
		
		useGeomColumn = self.chkGeomColumn.isChecked()
		if useGeomColumn:
			geomColumn = unicode(self.editGeomColumn.text())
			geomType = str(self.cboGeomType.currentText())
			geomDim = self.spinGeomDim.value()
			try:
				geomSrid = int(self.editGeomSrid.text())
			except ValueError:
				geomSrid = -1
			useSpatialIndex = self.chkSpatialIndex.isChecked()
			if len(geomColumn) == 0:
				QMessageBox.information(self, "sorry", "set geometry column name")
				return

		pkey = unicode(self.cboPrimaryKey.currentText())

		flds = []
		for row in xrange(m.rowCount()):
			fld = NewTableField(self.db)
			fld.name = unicode(m.data(m.index(row,0,QModelIndex())).toString())
			fld.dataType = unicode(m.data(m.index(row,1,QModelIndex())).toString())
			fld.notNull = not m.data(m.index(row,2,QModelIndex())).toBool()
			fld.primaryKey = fld.name == pkey
			flds.append( fld )
				
		if not self._debugApp:
			# commit to DB
			QApplication.setOverrideCursor(Qt.WaitCursor)
			try:
				self.db.connector.createTable(table, flds, schema)
				if useGeomColumn:
					self.db.connector.addGeometryColumn(table, geomType, schema, geomColumn, geomSrid, geomDim)

					# commit data definition changes, otherwise index can't be built
					self.db.connector.connection.commit()

					if useSpatialIndex:
						self.db.connector.createSpatialIndex(table, schema, geomColumn)

			except DbError, e:
				DlgDbError.showError(e, self)
				return

			finally:
				self.db.emit(SIGNAL("changed"))
				QApplication.restoreOverrideCursor()

		else:
			print "table:", table
			print "fields:", u", ".join(map(lambda x: x.definitions(), flds))
			if useGeomColumn:
				print "geom:", geomType, " >> ", geomColumn

		QMessageBox.information(self, "Good", "everything went fine")


if __name__ == '__main__':
	import sys
	a = QApplication(sys.argv)
	dlg = DlgCreateTable()
	dlg.show()
	sys.exit(a.exec_())
