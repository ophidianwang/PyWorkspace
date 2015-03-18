# coding=utf8

#BASIC SETTING START
import sys
import os
path = os.getcwd()
sys.path.append(path)
#BASIC SETTING END

#IMPORT SETTING START
from pModel.mTest import cTest
from mMisc import vPrintR
#IMPORT SETTING END

#MAIN CODE START

lAll = cTest.lGetAll()
for oTest in lAll:
	vPrintR(oTest)

dSingle = {"key1":"value1"}
lSub = [1,2,3,4,5,'這是中文 in list',u'這是中文 in list']
tSub = (1,2,'這是中文 in tuple',u'這是中文 in tuple')
dSingle["list"] = lSub
dSingle["tuple"] = tSub

#print dSingle
vPrintR(dSingle)
