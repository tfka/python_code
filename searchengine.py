import urllib2
import re
from sqlite3 import dbapi2 as sqlite
from bs4 import*
from urlparse import urljoin
class crawler:
	def __init__(self,dbname):
		self.con=sqlite.connect(dbname)
	def __del__(self):
		self.con.close()
	def dbcommit(self):
		self.con.commit()
	def getentryid(self,table,field,value,createnew=True):
		cur=self.con.execute("select rowid from %s where %s = '%s'" % (table,field,value))
		res=cur.fetchone()
		if res == None:
			cur=self.con.execute("insert into %s (%s) values ('%s')" % (table,field,value))
			return cur.lastrowid
		else:
			return res[0]
		return None
	
	def addtoindex(self,url,soup):
		if self.isindexed(url): return
		print 'Indexing %s' % url
		text=self.gettextonly(soup)
		words=self.separatewords(text)
		urlid=self.getentryid('urllist','url',url)
		for i in range(len(words)):
			word=words[i]
			if word in ignorewords:continue
			wordid=self.getentryid('wordlist','word',word)
			self.con.execute("insert into wordlocation(urlid,wordid,location) values (%d,%d,%d)" % (urlid,wordid,i))
	def gettextonly(self,soup):
		v=soup.string
		if v==None:
			c=soup.contents
			resulttext=''
			for t in c:
				subtext=self.gettextonly(t)
				resulttext += subtext+'\n'
			return resulttext
		return v.strip()
	def separatewords(self,text):
		splitter=re.compile('\\W*')
		return [s.lower() for s in splitter.split(text) if s!= ''] 
		return None
	def isindexed(self,url):
		u=self.con.execute("select rowid from urllist where url = '%s'" % url).fetchone()
		if u!=None:
			v=self.con.execute("select * from wordlocation where urlid=%d" %u[0]).fetchone();
			if v!=None: return True
		return False
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
		self.con.execute('create table urllist(url)')
		self.con.execute('create table wordlist(word)')
		self.con.execute('create table wordlocation(urlid,wordid,location)')
		self.con.execute('create table link(fromid integer,toid integer)')
		self.con.execute('create table linkwords(wordid,linkid)')
		self.con.execute('create index wordidx on wordlist(word)')
		self.con.execute('create index urlidx on urllist(url)')
		self.con.execute('create index wordurlidx on wordlocation(wordid)')
		self.con.execute('create index urltoidx on link(toid)')
		self.con.execute('create index urlfromid on link(fromid)')
		self.dbcommit()
ignorewords=set(['the','of','to','and','a','in','is','it'])
		
