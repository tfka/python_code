import random
from sys import *
from clusters import*
def kcluster(rows,distance=pearson,k=4):

 	ranges=[(min([row[i] for row in rows]),max([row[i] for row in rows])) for i in range(len(rows[0]))]

	clusters=[[random.random()*(ranges[i][1]-ranges[i][0])+ranges[i][0] for i in range(len(rows[0]))]for j in range(k)]
	x=open("bug.txt","w+")
	lastmatches=None
	for t in range(100):
		print t
		x.write("666\n")
		bestmatches=[[] for i in range(k)]
		for j in range(len(rows)):
			row = rows[j]
			bestmatch = 0
			for i in range(k):
				d=distance(clusters[i],row)
				m=clusters[i][0]
				x.write(str(m))
				x.write("\n")
				if d < distance(clusters[bestmatch],row):
					bestmatch = i
			bestmatches[bestmatch].append(j)
		print bestmatches
		print lastmatches
		if bestmatches == lastmatches:
			break
		lastmatches = bestmatches
		for i in range(k):
			avgs=[0.0]*len(rows[0])
			if len(bestmatches[i]) > 0:
			
				for rowid in bestmatches[i]:
					for m in range(len(rows[rowid])):
						avgs[m] += rows[rowid][m]
				for j in range(len(avgs)):
					avgs[j] /= len(bestmatches[i])
				clusters[i]=avgs
	return bestmatches
				
