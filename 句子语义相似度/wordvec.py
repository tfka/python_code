
from gensim.models import word2vec
import logging
import math
def cal_sim(x,y):
    m =0.0
    x1=0.0
    y1=0.0
    for i in range(len(x)):
        m+=x[i]*y[i]
        x1+=x[i]*x[i]
        y1+=y[i]*y[i]
    return m/(math.sqrt(x1)*math.sqrt(y1))
def deal(x):
    length=len(x)
    if '\'' in x:x=x.replace('\'',' ')
    if '-' in x:x=x.replace('-',' ')
    if '\n' in x:x=x.replace('\n','')
    m=x.split(' ')
    if m[0]=='' :return m[1]
    else:return m[0]

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
sentences=word2vec.Text8Corpus('text8')
model=word2vec.Word2Vec(sentences,min_count=10,size=200)
model.save('text8.model')
model.save_word2vec_format('text8.model.bin',binary=True)
model=word2vec.Word2Vec.load_word2vec_format('text8.model.bin',binary=True)

out=open("output.txt","w+")
for line in file('input.txt'):
    sentence=line.split('\t')
    sentence1=sentence[0].split(' ')
    sentence2=sentence[1].split(' ')
    for i in range(len(sentence1)):
        if i == 0:
            try:
                x=model[deal(sentence1[i].lower())]
            except:
                   pass

        else:
            try:
                x+=model[deal(sentence1[i].lower())]
            except:
                    pass
        print sentence1[i].lower()
    x=x/len(sentence1)
    for j in range(len(sentence2)):
        if j == 0:
            try:
                y=model[deal(sentence2[j].lower())]
            except:
                    pass
        else:
            try:
                y+=model[deal(sentence2[j].lower())]
            except:
                    pass
        print sentence2[j].lower()
    y=y/len(sentence1)
    z=cal_sim(x,y)
    out.write(str(z))
    out.write('\t')
    out.write(sentence[0]+'\t'+sentence[1])





