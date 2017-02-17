import sys
sys.path.append("..")
import HTTPTool
import XMLTool
from fund import A

class A2(A.A):
	def __init__(self):
		fund = XMLTool.Getfundinfo("A2")
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
		latestindex = res.split(",")[1]
		XMLTool.Setkeyvalue(self.fundname,"currentindex",latestindex)
		return latestindex

	def Getlatestrate(self):
		res = HTTPTool.Getlatestinfo(self.fundurl)
		e = float(res.split(",")[3])
		return e/100

	def Getstrategy(self):
		cm = self.baseaccount
		return cm
		
