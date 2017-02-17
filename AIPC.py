from  datetime  import  *
from  optparse  import  OptionParser
import MainTool
import XMLTool
import sys


#命令行提示
def RegisterOption():
	usage = "usage: %prog -n [fundname] [options]"
	parser = OptionParser(usage)
	parser.add_option("-n","--fundname",action="store",dest="fundname",help="fundname")
	parser.add_option("-c","--latestindex",action="store_true",dest="latestindex",help="get latest Index")
	parser.add_option("-g","--getspend",action="store_true",dest="getspend",help="get current account over computed")
	parser.add_option("-s","--savespend",action="store_true",dest="savespend",help="save current purchase info")
	parser.add_option("-l","--lastpurchaseinfo",action="store_true",dest="lastpurchaseinfo",help="get last purchase Info")
	parser.add_option("-t",action="store_true",help="cyb:A1,sz:A2")
	return parser

#主程序
def Main():
	now = datetime.now()
	maxpurchasedate = now.replace(hour = 23,minute = 59,second = 30)
	minsavedate = now.replace(hour = 15,minute = 30,second = 0)
	parser = RegisterOption()
	(options,args) = parser.parse_args()

	if options.fundname == None:
		print("FUND Not Find,Type -h For Help")
		return 

	fn = options.fundname
	fn = fn.upper().strip()
	fundinstance = MainTool.FundFactory(fn)
	if not hasattr(fundinstance,"fundname"):
		print("FUND Not Find,Type -h For Help")
		return 

	#获取实时金额
	if options.getspend == True:
		if(now < maxpurchasedate):
			cm = MainTool.GetInvestment(fundinstance)
			cm = float(cm)
			print("NOW IN : %.2f"%cm)
			if cm == 0:
				print(str(MainTool.Isoverintervaldate(fundinstance))+" DAYS LEFT")
		else:
			print("TIME PASS")
	#保存购买信息
	if options.savespend == True:
		if(now >= minsavedate):
			latestindex = fundinstance.Getlatestindex()
			now = date.today()
			currentdate = now.strftime('%Y-%m-%d')
			XMLTool.Setkeyvalue(fn,"lastpurchaseindex",latestindex)
			XMLTool.Setkeyvalue(fn,"lastpurchasedate",currentdate)
			print("INDEX : "+latestindex)
			print("DATE : " +currentdate)
			print("SAVE SUCCESSFULLY ")
		else:
			print("TIME EARLY THAN 15:30")
	#获取上次购买信息
	if options.lastpurchaseinfo == True:
		print("LASTININDEX : "+fundinstance.lastpurchaseindex)
		print("LASTINDATE : "+fundinstance.lastpurchasedate)
	#获取当前最新数据
	if options.latestindex == True:
		l = float(fundinstance.lastpurchaseindex)
		s = float(fundinstance.Getlatestindex())
		d = float(fundinstance.Getlatestrate())
		print("CURRENTINDEX : %s (%.2f %%)[%.2f %%] "%(str(s),d*100,(s-l)*100/l))
		now = date.today()
		s = now.strftime('%Y-%m-%d')
		print("CURRENTDATE : " +s)

if __name__ == "__main__":
	Main()