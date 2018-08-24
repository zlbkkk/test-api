#coding:utf-8
import sys,json
sys.path.append("E:/www/ImoocInterface")
from base.runmethod import RunMethod
from data.get_data import GetData
from util.common_util import CommonUtil
from data.dependent_data import DependdentData
from util.send_email import SendEmail
from util.operation_header import OperationHeader
from util.operation_json import OperetionJson
class RunTest:
	def __init__(self):
		self.run_method = RunMethod()
		self.data = GetData()
		self.com_util = CommonUtil()
		self.send_mai = SendEmail()

	#程序执行的
	def go_on_run(self):
		res = None
		pass_count = []
		fail_count = []
		#10  0,1,2,3
		rows_count = self.data.get_case_lines()
		for i in range(1,rows_count):
			is_run = self.data.get_is_run(i)
			if is_run:
				url = self.data.get_request_url(i)
				method = self.data.get_request_method(i)
				request_data = self.data.get_data_for_json(i)
				# expect = self.data.get_expcet_data_for_mysql(i)
				expect=self.data.get_expcet_data(i)
				header = self.data.is_header(i)
				depend_case = self.data.is_depend(i)
				if depend_case != None:
					self.depend_data = DependdentData(depend_case)
					#获取依赖的响应数据
					depend_response_data = self.depend_data.get_data_for_key(i)
					#获取依赖的key
					depend_key = self.data.get_depend_field(i)
					request_data[depend_key] = depend_response_data
				if header == 'write':
					res = self.run_method.run_main(method,url,request_data)
					op_header = OperationHeader(res)
					op_header.write_cookie()

				elif header == 'yes':
					op_json = OperetionJson('../dataconfig/cookie.json')
					cookie = op_json.get_data('apsid')
					cookies = {
						'apsid':cookie
					}
					res = self.run_method.run_main(method,url,request_data,cookies)
				else:
					res = self.run_method.run_main(method,url,request_data)
					# print(res["data"][2]["context"])
					print(res)
					# print(type(res))

				#自己写的：这个是判断字段是否在结果中
				if expect in res:
					self.data.write_result(i,"pass")
					pass_count.append(i)
				else:
					self.data.write_result(i,"fail")
					fail_count.append(i)

				#现有的封装的函数
				# if self.com_util.is_contain(expect,json.dumps(res))==True:
				# 	self.data.write_result(i, 'pass')
				# 	pass_count.append(i)
				# else:
				# 	self.data.write_result(i, 'fail')
				# 	fail_count.append(i)


				#这个是通过查询数据库去判断是否相等
				# if self.com_util.is_equal_dict(expect,res) == 0:
				# 	self.data.write_result(i,'pass')
				# 	pass_count.append(i)
				# else:
				# 	self.data.write_result(i,'fail')
				# 	fail_count.append(i)
		# self.send_mai.send_main(pass_count,fail_count)

	#将执行判断封装
	#def get_cookie_run(self,header):


if __name__ == '__main__':
	run = RunTest()
	run.go_on_run()
#

# import requests
#
# url1="http://127.0.0.1/zentao/user-login.html"
# data1={"account":"admin",
# 	  "password":123456,
# 	  "referer":"http://127.0.0.1/zentao/my/"
#
# }
#
# cookie={"lang":"zh-cn",
#          "theme":"default",
#          "sid":"2to05fujhuvfuivr15kcq7su65"}
#
#
#
#
# c=requests.cookies.RequestsCookieJar()
# s=requests.session()
# print s.get(url1).cookies
#
# c=requests.cookies.RequestsCookieJar()
# c.set(sid="e9tef71k46hvdq1tk6fhsqr9m1",lang="zh-cn",theme="default")
# # c.set(lastProject=1)
# # c.set(projectTaskOrder="status%2Cid_desc")
# # c.set(sid="1kd8tpvcqlk3v3clppii341uo1")
# s.cookies.update(c)
# #
# url2="http://127.0.0.1/zentao/project-create.html"
#
# data2={"name":"02",
#        "code":"02",
#        "begin":"2018-08-09",
#        "end":"2018-08-11",
#        "days":"2",
#        "team":"",
#        "type":"sprint",
#        "products[0]":"0",
#        "desc":"",
#        "acl":"open"
#        }
#
# # r=s.post(url=url1)
# # print(r.content)
#
# r=s.post(url=url2,data=data2,verify=False)
#
# print(r.content)
#
# # c.set('cookie-name','cookie-value')
# # s.cookies.update(c)
# # print(s.cookies.get_dict())
#
# # print(r.content)

# count_su=0
# count_fa=0
# with open("C:\\55.txt","r") as f:
#     data=f.readlines()
# print(data)
# count_su = 0
# count_fa = 0
# for i in data:
#
#
#
#     for j in i.split(","):
#
#         # print j.split()
#         for k in j:
#             if "success" in k:
#                 count_su += 1
#             elif "fail" in k:
#                 count_fa += 1
# print count_fa
# print count_su

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
python实现任一个英文的纯文本文件，统计其中的单词出现的个数、行数、字符数
"""

# file_name = "c:\\55.txt"
#
# line_counts = 0
# word_counts = 0
# character_counts = 0
#
# with open(file_name, 'r') as f:
#     for line in f:
#         words = line.split()
#
#         line_counts += 1
#         word_counts += len(words)
#         character_counts += len(line)
#
# print "line_counts ", line_counts
# print "word_counts ", word_counts
# print "character_counts ", character_counts
# with open('C:\\55.txt','r') as f:
#     line_count=0
#     word_count=0
#     cha_count=0
#     for line in f:
#         words=line.split()
#         line_count+=1
#         word_count+=len(words)
#         cha_count+=len(line)
#     print line_count
#     print word_count
#     print cha_count


# import requests
# import json
# import re
# s=requests.session()
# # print s.headers
#
# url="https://passport.lagou.com/login/login.json"
#
# url1 = 'https://passport.lagou.com/login/login.html'
#
# # headers = {
# #     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
# #     'Origin': 'https://passport.lagou.com',
# #     'Referer': 'https://passport.lagou.com/login/login.html',
# #     'Host': 'www.v2ex.com',
# #     "Accept-Language":"zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
# # }
#
# h = {
#          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
#         }
# s.headers.update(h)
#
# h1={"isValidate":"true",
#     "username":"18680674921",
#     "password":"40937409078c8090cbd2ec96fe97c2ee",
#     "request_form_verifyCode":"",
#     "submit":""}
#
#
# data=s.post(url,data=h1,verify=False)
# print data.content



