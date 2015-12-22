import feedparser
import re

feedlist=['http://today.reuters.com/rss/topNews',
          'http://today.reuters.com/rss/domesticNews',
          'http://today.reuters.com/rss/worldNews',
          'http://hosted.ap.org/lineups/TOPHEADS-rss_2.0.xml',
          'http://hosted.ap.org/lineups/USHEADS-rss_2.0.xml',
          'http://hosted.ap.org/lineups/WORLDHEADS-rss_2.0.xml',
          'http://hosted.ap.org/lineups/POLITICSHEADS-rss_2.0.xml',
          'http://www.nytimes.com/services/xml/rss/nyt/HomePage.xml',
          'http://www.nytimes.com/services/xml/rss/nyt/International.xml',
          'http://news.google.com/?output=rss',
          'http://feeds.salon.com/salon/news',
          'http://www.foxnews.com/xmlfeed/rss/0,4313,0,00.rss',
          'http://www.foxnews.com/xmlfeed/rss/0,4313,80,00.rss',
          'http://www.foxnews.com/xmlfeed/rss/0,4313,81,00.rss',
          'http://rss.cnn.com/rss/edition.rss',
          'http://rss.cnn.com/rss/edition_world.rss',
          'http://rss.cnn.com/rss/edition_us.rss']
def stripHTML(h):
    p=''
    s=0
    for c in h:
        if c=='<':s=1
        elif c=='>':
            s=0
            p+=' '
        elif s==0:p+=c
    return p
def separatewords(text):
    splitter=re.compile('\\W*')
    return [s.lower() for s in splitter.split(text) if len(s)>3]
def getarticlewords():
    allwords={}
    articlewords=[]
    articletitles=[]
    ec=0
    for feed in feedlist:
        f=feedparser.parse(feed)
        for e in f.entries:
            if e.title in articletitles: continue

            txt=e.title.encode('utf8')+stripHTML(e.description.encode('utf8'))
            words=separetewords(txt)
            articlewords.append({})
            articletitle.append(e.title)
            for word in words:
                allwords.setdefault(word,0)
                allwords[word]+=1
                articlewords[ec].setdefault(word,0)
                articlewords[ec][word]+=1
            ec+=1
    return allwords,articlewords,articletitles
def makematrix(allw,articlew):
    wordvec=[]

    for w,c in allw.items():
        if c>3 and c <len(aritclew)*0.6:
            wordvec.append(word)
    l1=[[(word in f and f[word] or 0)for word in wordvec]for f in articlew]
    return l1,wordvec

    
    
