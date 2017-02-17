import sys
sys.path.append("..")
import HTTPTool
import XMLTool
from fund import A

class A1(A.A):
	def __init__(self):
		fund = XMLTool.Getfundinfo("A1")
		self.fundname = fund["name"]
		self.fundurl = fund["url"]
		self.baseindex = fund["data"]["index"]
		self.baseaccount = fund["data"]["account"]
		self.maxdroprange = fund["data"]["maxdroprange"]
		self.maxinterval = fund["data"]["maxinterval"]
		self.lastpurchaseindex = fund["data"]["lastpurchaseindex"]
		self.lastpurchasedate = fund["data"]["lastpurchasedate"]
		self.fund = fund

	def Getlatestindex(self):
		res = HTTPTool.Getlatestinfo(self.fundurl)
		latestindex = res.split(",")[3]
		XMLTool.Setkeyvalue(self.fundname,"currentindex",latestindex)
		return latestindex

	def Getlatestrate(self):
		res = HTTPTool.Getlatestinfo(self.fundurl)
		s = float(res.split(",")[2])
		e = float(res.split(",")[3])
		return (e-s)/s

	def Getstrategy(self):
		baseindex = float(self.baseindex)
		latestindex = float(self.Getlatestindex())
		baseaccount = float(self.baseaccount)
		droprate = (baseindex - latestindex)*1.0/baseindex
		er = (1+droprate*4)
		cm = baseaccount*1.0*er*er
		return cm
		
