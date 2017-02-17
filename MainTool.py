import XMLTool
import HTTPTool
from  datetime  import  *
from fund import *


#工厂方法创建基金实例
def FundFactory(fundname):
	basefund = A.A()
	fundname = fundname.upper().strip() 
	if  fundname== "A1":
		basefund = A1.A1()
	elif fundname == "A2":
		basefund = A2.A2()
	return basefund


#单个基金主程
def GetInvestment(fundinstance):
	costmoney = 0
	if Isoverdroprange(fundinstance):
		costmoney = fundinstance.Getstrategy()
	else:
		d = Isoverintervaldate(fundinstance)
		if  d == 0:
			costmoney = fundinstance.Getstrategy()
		else:
			costmoney = 0
	return costmoney


#跌幅超过指定值
def Isoverdroprange(fundinstance):
	lindex = float(fundinstance.lastpurchaseindex)
	cindex = float(fundinstance.Getlatestindex())
	rate = float(fundinstance.maxdroprange)
	if cindex>=lindex:
		return False
	crate = (lindex-cindex)*1.0/lindex
	if crate < rate:
		return False
	return True

#距上次购买时间超过间隔值
def Isoverintervaldate(fundinstance):
	lastdate = fundinstance.lastpurchasedate
	interdate = int(fundinstance.maxinterval)
	now = date.today()
	lastdate = datetime.strptime(lastdate,'%Y-%m-%d').date()
	datediff = (now-lastdate).days
	if datediff >= interdate:
		return 0
	return interdate-datediff
