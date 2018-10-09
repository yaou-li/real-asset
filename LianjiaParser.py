from HTMLParser import HTMLParser 
import json

NEIGHBORHOOD_CLASS = 'xiaoquListItem'
PAGINATION_CLASS = 'house-lst-page-box'
NEIGHBORHOOD_NAME_CLASS = 'title'
NEIGHBORHOOD_HOUSE_CLASS = 'houseInfo'
NEIGHBORHOOD_POS_CLASS = 'positionInfo'
NEIGHBORHOOD_PRICE_CLASS = 'totalPrice'

class LianjiaDistrictParser(HTMLParser):
	
	def __init__(self, url):
		self.enter_district_tag = False
		self.districts = []
		self.district_names = []
		self.root_url = url
		HTMLParser.__init__(self)
		

	def handle_starttag(self, tag, attrs):
		if tag == 'div':
			for attr, val in attrs:
				if attr == 'data-role' and val == 'ershoufang':
					self.enter_district_tag = True
		elif tag == 'a' and self.enter_district_tag == True:
			for attr, val in attrs:
				if attr == 'href':
					url = val
					if 'https' not in url and 'http' not in url:
						url = self.root_url + url
					self.districts.append(url)

	def handle_data(self,data):
		if self.enter_district_tag == True and data.strip(' \n\r\t'):
			self.district_names.append(data.strip(' \n\r\t'))

	def handle_endtag(self, tag):
		if tag == 'div' and self.enter_district_tag == True:
			self.enter_district_tag = False

	def get_district(self):
		return self.districts

	def get_district_name(self):
		return self.district_names


class LianjiaNeighborhoodParser(HTMLParser):
	
	def __init__(self):
		self.enter_neighborhood_tag = False
		self.enter_neighborhood_page_tag = False
		self.enter_title_tag = False
		self.enter_house_info_tag = False
		self.enter_position_info_tag = False
		self.enter_price_tag = False

		self.title = ''
		self.house_info = ''
		self.position_info = ''
		self.price = ''

		self.page_info = {}
		self.page_url = ''
		self.models = []
		self.model = {}
		HTMLParser.__init__(self)
		
	def handle_starttag(self, tag, attrs):
		if tag == 'li':
			for attr, val in attrs:
				if attr == 'class' and NEIGHBORHOOD_CLASS in val:
					self.enter_neighborhood_tag = True
				if self.enter_neighborhood_tag == True and attr == 'data-id':
					self.model['id'] = val

		if tag == 'div' and self.enter_neighborhood_tag:
			for attr, val in attrs:
				if attr == 'class' and NEIGHBORHOOD_NAME_CLASS in val:
					self.enter_title_tag = True
				elif attr == 'class' and NEIGHBORHOOD_HOUSE_CLASS in val:
					self.enter_house_info_tag = True
				elif attr == 'class' and NEIGHBORHOOD_POS_CLASS in val:
					self.enter_position_info_tag = True
				elif attr == 'class' and NEIGHBORHOOD_PRICE_CLASS in val:
					self.enter_price_tag = True

		elif tag == 'div':
			for attr, val in attrs: 
				if attr == 'class' and PAGINATION_CLASS in val:
					self.enter_neighborhood_page_tag = True
				if self.enter_neighborhood_page_tag == True and attr == 'page-data':
					self.page_info = json.loads(val)
					print self.page_info
				if self.enter_neighborhood_page_tag == True and attr == 'page-url':
					self.page_url = val

	def handle_endtag(self, tag):
		if tag == 'li' and self.enter_neighborhood_tag == True:
			self.enter_neighborhood_tag = False
			self.models.append(self.model)
			self.model = {}
		if tag == 'div' and self.enter_neighborhood_tag and self.enter_title_tag == True:
			self.enter_title_tag = False
			self.model['title'] = self.title
			self.title = ''
		elif tag == 'div' and self.enter_neighborhood_tag and self.enter_house_info_tag == True:
			self.enter_house_info_tag = False
			self.model['house_info'] = self.house_info
			self.house_info = ''
		elif tag == 'div' and self.enter_neighborhood_tag and self.enter_position_info_tag == True:
			self.enter_position_info_tag = False
			self.model['position_info'] = self.position_info
			self.position_info = ''
		elif tag == 'div' and self.enter_neighborhood_tag and self.enter_price_tag == True:
			self.enter_price_tag = False
			self.model['price'] = self.price
			self.price = ''
		if tag == 'div' and self.enter_neighborhood_page_tag == True:
			self.enter_neighborhood_page_tag = False

	def handle_data(self,data):
		if self.enter_title_tag == True:
			if data.strip(' \n\t\r'):
				self.title = data.strip(' \n\t\r')
		elif self.enter_house_info_tag == True:
			if data.strip(' \n\t\r'):
				self.house_info += data.strip(' \n\t\r')
		elif self.enter_position_info_tag == True:	
			if data.strip(' \n\t\r'):
				words = [word.strip(' \n\t\r') for word in data.strip(' \n\t\r').split('/')]
				self.position_info += '|'.join(words)
		elif self.enter_price_tag == True:
			if data.strip(' \n\t\r'):	
				self.price += data.strip(' \n\t\r')

	def get_models(self):
		return self.models
		
	def get_page_info(self):
		return { 'page_info': self.page_info, 'page_url': self.page_url }


		