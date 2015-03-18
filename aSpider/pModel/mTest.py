# coding=utf8
import mMisc
from pDatabase.mMySql import cMySql

class cTest():
	"""
	This class is ophidian.wang's testing ORM model in python v2.79

	Attributes:
		iTestNo: auto increase key
		sValue: content
		iCreateTime: timestamp
	"""

	__dInstances__ = {} #use string form key
	__sDBName__ = "test"

	@staticmethod
	def oGetOne(iTestNo):
		"get an instance by unique index"
		sTestNo = str(iTestNo)
		if sTestNo not in cTest.__dInstances__.keys():
			#query from database
			sSql = "SELECT * FROM test WHERE iTestNo=\'" + sTestNo + "\'"
			oDB = cMySql.oDB(cTest.__sDBName__)
			oCursor = oDB.oQuery(sSql)
			if oCursor.rowcount != 1:
				raise UserWarning("cTest.oGetOne: "+sTestNo+" duplicated, check database indexing")

			oInstance = cTest(cMySql.dFetchOne(oCursor))
			cTest.__dInstances__[sTestNo] = oInstance
		
		return cTest.__dInstances__[sTestNo]

	@staticmethod
	def lGetAll(sWhere=""):
		"get instances match given condition"
		lReturn = []

		sSql = "SELECT * FROM test "
		if sWhere!="":
			sSql += " WHERE " + sWhere

		oDB = cMySql.oDB(cTest.__sDBName__)
		oCursor = oDB.oQuery(sSql)

		lResult = cMySql.lFetchAll(oCursor)
		
		for dRow in lResult:
			sTestNo = str(dRow["iTestNo"])
			if sTestNo not in cTest.__dInstances__.keys():
				oInstance = cTest(dRow)
				cTest.__dInstances__[sTestNo] = oInstance

			lReturn.append(cTest.__dInstances__[sTestNo])

		return lReturn

	def __init__(self,dRow):
		"constructor, set class member corresponding to table field"
		
		for key in dRow:
			setattr(self,key,dRow[key])

		self.lList = [1,2,3,4,5]
		self.dDict = {"key1":"value1","key2":"value2"}
		self.tTuple = (6,7,8,9,10)
		self.origin = '這是中文'
		self.uni = u'這是中文'

		return

	def __str__(self):
		return str(self.dAttr())

	def sCreateTime(self):
		"return createtime in string form"
		return mMisc.sDatetime(self.iCreateTime)
