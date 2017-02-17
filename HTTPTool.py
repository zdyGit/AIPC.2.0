import urllib.request

def Getlatestinfo(url):
	res_data = urllib.request.urlopen(url)
	res = res_data.read()
	res =  res.decode("gb2312")
	return res.split("\"")[1]
