# encoding: utf-8

import MySQLdb
import mConfig

class cMySql:
	"""
	This class is ophidian.wang's testing mysql shell in python v2.79

	Attributes:
		dConfig:config dictionary given
		oConn: connection object create by calling MySQLdb.connect()
	"""
	dInstances = {}

	@staticmethod
	def oDB(sDBName):
		if sDBName not in cMySql.dInstances.keys():
			oInstance = cMySql(mConfig.dMysql[sDBName])
			if oInstance != None:
				cMySql.dInstances[sDBName] = oInstance
		
		return cMySql.dInstances[sDBName]

	def __init__(self,dConfig):
		"constructor"
		self.dConfig = dConfig
		self.oConn = MySQLdb.connect(**dConfig)
		if (self.oConn != None):
			self.oConn.set_character_set("utf8")
			#self.oConn.escape_string()
		return

	def oQuery(self,sSql):
		"exec sql query"
		oCursor = self.oConn.cursor()
		oCursor.execute(sSql)
		return oCursor

	def oInsert(self,sTable,dInsert):
		"insert given row into target table"
		oCursor = self.oConn.cursor()
		
		sField = "(`" + "`,`".join(dInsert.keys()) + "`)"
		sValue = "(" + ",".join(["%s"]*len(dInsert)) + ")"

		sSql = "INSERT INTO " + sTable + " " + sField + " VALUES " + sValue

		oCursor.execute(sSql,dInsert.values())
		return oCursor

	def oUpdate(self,sTable,dUpdate,sWhere):
		"update target table set rows match where to given values"
		oCursor = self.oConn.cursor()

		sSql = "UPDATE " + sTable + " SET "
		for index in dUpdate:
			sSql += "`" + index + "`=%s"
		else:
			sSql += " WHERE " + sWhere

		oCursor.execute(sSql,dInsert.values())
		return oCursor

	def vCommit(self):
		"commit data modified query"
		self.oConn.commit()

	def iInsertId(self):
		"return last insert_id"
		return self.oConn.insert_id()

	@staticmethod
	def lFetchAll(oCursor):
		"fetch all query result in a list of dictionary"
		lReturn = []

		tAllRow = oCursor.fetchall()	#first key is row order, second key is field order
		tField = oCursor.description

		for tRow in tAllRow:
			count=0
			dRow = {}
			while (count<len(tRow)):
				dRow[tField[count][0]] = tRow[count]
				count = count+1

			lReturn.append(dRow)
		
		return lReturn