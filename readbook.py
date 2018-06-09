import time
import argparse
import json
import os


parser = argparse.ArgumentParser()
parser.add_argument('-ls','--list')
parser.add_argument('-n','--new')

class book(object):
	def __init__(self,name,all_page,now_page,is_end=False):
		self.context = {}
		self.context['name'] = name
		self.context['all_page'] = all_page
		self.context['now_page'] = now_page
		self.context['is_end'] = is_end

	
	def save(self):
		if(self.context['name'] not in os.listdir()):
			os.system('mkdir '+self.context['name'])
		fp = open(self.context['name']+'/context.json','w')
		json.dump(self.context,fp)
		fp.close()

	def load(self):
		fp = open(self.context['name']+'/context.json','r')
		self.context= json.load(fp)
		fp.close()

class booklist(object):
	def __init__(self):
		self.laod()
	def load(self):
		fp = open('booklist.json','w')
		self.all_book = json.load(fp)
		fp.close()
	def save(self):
		fp = open('booklist.json','r')
		json.dumps(self.all_book,fp)
		fp.close()
	def add_book(self,name,is_end):
		self.all_book[name] = is_end
		self.save()
	
# args = parser.parse_args()

# mybooklist = booklist()
# if args.list:
# 	for item in mybooklist.all_book.keys():
# 		print(item)

# if args.new:
abook = book('maohaoketang',108,22)
print(abook.context['name'])
abook.save()


