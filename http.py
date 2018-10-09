import urllib2

#read html content
def readHTMLPage(url):
	html = ''
	if not url:
		return html
	
	response = urllib2.urlopen(url)
	if 'text/html' in response.info().getheader('Content-Type'):
		html = response.read()

	return html