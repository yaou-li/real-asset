from util import create_neighborhood_file
from Crawler import Crawler
from models.District import District
from models.Neighborhood import Neighborhood
from database import db
import app


PROJECT_DIR = '/Users/liyaou/Desktop/liyaou/megvii/real-asset'
VENDORS = ['lianjia']

def get_district_id(district_name, district_url):
	district = District.query.filter_by(name=district_name).first()
	if district is None:
		district = District(name=district_name, url=district_url)
		db.session.add(district)
		db.session.commit()
	return district.id

def save_neighborhood(model, district_id):
	params = {
		'vendor_id': 1,
		'district_id': district_id
	}
	if model['title']:
		params['name'] = model['title']
	if model['price']:
		params['price'] = model['price']
	if model['position_info']:
		params['position_info'] = model['position_info']
		infos = model['position_info'].split('|')
		params['area'] = infos[0]
		params['year'] = infos[len(infos) - 1]
	if model['house_info']:
		params['house_info'] = model['house_info']
	if model['id']:
		params['vendor_given_id'] = model['id']

	neighborhood = Neighborhood(**params)
	db.session.add(neighborhood)
	db.session.commit()

	return neighborhood


if __name__ == '__main__':

	for vendor in VENDORS:
		create_neighborhood_file(PROJECT_DIR,vendor)

	crawler = Crawler()
	district_urls, district_names = crawler.get_lianjia_districts()
	for index, url in enumerate(district_urls):
		district_id = get_district_id(district_names[index],district_urls[index])
		if district_id:
			print district_id, district_names[index], district_urls[index]
			models = crawler.get_lianjia_neighborhood_by_district(url)
			print len(models)
			for model in models:
				neighborhood = save_neighborhood(model,district_id)




			