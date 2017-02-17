from xml.etree import ElementTree as ET

#读取基金信息
def Getfundinfo(fundname):
	tree = ET.parse("source.xml")
	root = tree.getroot()
	fundlist = root.findall("fund")
	fundinfo = {}
	for fund in fundlist:
		if fund.get("name") == fundname:
			fundinfo["name"] = fundname
			fundinfo["url"] = fund.get("url")
			funddata = {}
			basedatanode = fund.find("basedata")
			for child in basedatanode.getchildren():
				funddata[child.tag.lower()] = child.text
			recorddatanode = fund.find("record")
			for child in recorddatanode.getchildren():
				funddata[child.tag.lower()] = child.text
			fundinfo["data"] = funddata
	return fundinfo

def Getkeyvalue(fundname,key):
	fund = Getfundinfo(fundname)
	key = key.lower().strip()
	if key in fund["data"].keys():
		return fund["data"][key]
	return fund[key]

def Setkeyvalue(fundname,key,value):
	tree = ET.parse("source.xml")
	root = tree.getroot()
	fundlist = root.findall("fund")
	key = key.lower().strip()
	for fund in fundlist:
		if fund.get("name") == fundname:
			basedatanode = fund.find("basedata")
			for child in basedatanode.getchildren():
				if child.tag == key:
					child.text = str(value)
					break
			recorddatanode = fund.find("record")
			for child in recorddatanode.getchildren():
				if child.tag == key:
					child.text = str(value)
					break
			break
	tree.write("source.xml")
