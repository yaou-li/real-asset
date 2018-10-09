import os

# make dir
def mk_dir(dir):
	if not os.path.exists(dir):
		print ('Create new directory ', dir)
		os.makedirs(dir)

def create_file(path):
	print ('Create new file ', path)
	f = open(path, 'w')
	f.write('')
	f.close()

# create district file if not exists
def create_neighborhood_file(root_dir, vendor_name):
	vendor_dir = '{}/{}'.format(root_dir,vendor_name)
	root_neighborhood_file = '{}/{}'.format(root_dir,'neighborhood.txt')
	vendor_neighborhood_file = '{}/{}'.format(vendor_dir,'neighborhood.txt')
	
	mk_dir(root_dir)
	mk_dir(vendor_dir)
	#create neighborhood root file if not exists
	if not os.path.isfile(root_neighborhood_file):
		create_file(root_neighborhood_file)

	#create neighborhood root file if not exists
	if not os.path.isfile(vendor_neighborhood_file):
		create_file(vendor_neighborhood_file)