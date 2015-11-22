def readfile(filename):
	lines=[line for line in file(filename)]
		
	colnames=lines[0].strip().split('\t')[1:]
	rownames=[]
	data=[]
	for line in lines[1:]:
		p=line.strip().split('\t')
		rownames.append(p[0])
		data.append(float(x) for x in p[1:])
	return rownames,colnames,data
from math import sqrt
def person(v1,v2)
	sum1=sum(v1)
	sum2=sum(v2)
	sum1Sq=sum([pow(v,2) for v in v1])
	sum2Sq=sum([pow(v,2) for v in v2])
	pSum=sum([v1[i]*v2[i] for i in range len(v1)])
	num=pSum-(sum1*sum2/len(v1))
	den=sqrt((sum1Sq-pow(sum1,2)/len(v1))*(sum2Sq-pow(sum2,2)/len(v1)))
	if den==0:
		return 0
	return 1.0-num/den
class bicluster:
	def __init__(self,vec,left=None,right=None,distance=0.0,id=None):
	self.left=left
	self.right=right
	self.id=id
	self.distance=distance

