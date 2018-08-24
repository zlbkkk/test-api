#coding:utf-8
import requests
import json
class RunMethod:
	def post_main(self,url,data,header=None):
		res = None
		if header !=None:
			res = requests.post(url=url,data=data,headers=header)
		# if header == "json":
		# 	res = requests.post(url=url, json=data, headers=header)

		else:
			res = requests.post(url=url,data=data)

		return res.json()

	def get_main(self,url,data=None,header=None):
		res = None
		if header !=None:
			res = requests.get(url=url,data=data,headers=header,verify=False)
		else:
			res = requests.get(url=url,data=data,verify=False)
		return res.json()

	def run_main(self,method,url,data=None,header=None):
		res = None
		if method == 'Post':
			res = self.post_main(url,data,header)
		else:
			res = self.get_main(url,data,header)
		return json.dumps(res,ensure_ascii=False)
# 		#return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)




# url1="http://www.kuaidi100.com/query"
# data1={"type":"tiantian",
# 	"postid":"668956984754"}
# r=requests.get(url=url1,params=data1)
# myjson=r.json()
# # myjson=json.loads(r)
# # newjson=json.dumps(r.json(),ensure_ascii=False)
# print(r.json())
# print(type(r.json()))
# print(r.json()["data"][0]["context"])
# print(myjson["data"][0]["context"])
# print(myjson["data"][""])
# print(r["data"][2]["context"])
# print(type(r))