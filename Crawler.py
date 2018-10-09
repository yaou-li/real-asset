from HTMLParser import HTMLParser
from LianjiaParser import LianjiaDistrictParser, LianjiaNeighborhoodParser
from http import readHTMLPage
from urlparse import urlparse

class Crawler():
	
	def __init__(self):
		self.district = []
		self.district_name = []
		self.url = {
			'lianjia': 'https://bj.lianjia.com/xiaoqu',
			'lianjia_domain': 'https://bj.lianjia.com'
		}	
		# self.url = {'lianjia': 'http://www.baidu.com'}	

	# def get_districts(self):

	def get_lianjia_districts(self):
		html = readHTMLPage(self.url['lianjia'])
		# try: 
		district_parser = LianjiaDistrictParser(self.url['lianjia_domain'])
		district_parser.feed(html)
		self.district = district_parser.get_district()
		self.district_name = district_parser.get_district_name()
		return self.district, self.district_name
		# except:
		# 	print('failed to crawl page ', self.url['lianjia'])

	def get_lianjia_neighborhood_by_district(self, url):
		parsed_uri = urlparse(url)
		domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
		neighborhood_parser = LianjiaNeighborhoodParser()
		models = []
		pagination = {
			'page_info': { 'totalPage': 1, 'curPage': 0 },
			'page_url': url
		}

		while (pagination['page_info']['totalPage'] != pagination['page_info']['curPage']):
			url = pagination['page_url'].replace('{page}', str(int(pagination['page_info']['curPage']) + 1))
			if 'https' not in url and 'http' not in url:
				url = (domain if domain else self.url['lianjia_domain']) + url
			print url
			html = readHTMLPage(url)
			neighborhood_parser.feed(html)
			pagination = neighborhood_parser.get_page_info()

		neighborhood_parser.close()
		models = neighborhood_parser.get_models()
		return models
