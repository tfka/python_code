import urllib2
from bs4 import*
from urlparse import urljoin
class crawler:
	def __init__(self,dbname):
		pass
	def __del__(self):
		pass
	def dbcommit(self):
		pass
	def getentryid(self,table,field,value,createnew=True):
		return None
	
	def addtoindex(self,url,soup):
		print 'Indexing %s' % url
	
	def gettextonly(self,soup):
		return None
	def separatewords(self,text):
		return None
	def isindexed(self,url):
		return False
	def addlinkref(self,urlFrom,urlTo,linkText):
		pass
	def crawl(self,pages,depth=2):
		for i in range(depth):
			newpages=set()
			for page in pages:
				try:
					c=urllib2.urlopen(page)
				except:
					print "could not open"
				soup=BeautifulSoup(c.read())
				self.addtoindex(page,soup)
				links=soup('a')
				for link in links:
					#because in a ,there are many attrs,but we just want the 'href',so we must be sure the 'href' attr exsits.ri le dog le ,bu neng yong zhong wen
					if('href' in dict(link.attrs)):
# connect xiangdui dizhi + gaiyemian dizhi
						url=urljoin(page,link['href'])
#zhe li bu shi hen ming bai
						if url.find("'")!=-1:continue
# you de di fang hui you # hao,wo zhuan men da kai wang ye kan le ,dique
						url=url.split('#')[0]
						if url[0:4]=='http' and not self.isindexed(url):
							newpages.add(url)
						linkText=self.gettextonly(link)
						self.addlinkref(page,url,linkText)
				self.dbcommit()
			
			pages=newpages
	def createindextables(self):
		pass
ignorewords=set(['the','of','to','and','a','in','is','it'])
		
