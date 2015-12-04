
import sys

def pre_deal():
    words=[]
    types=[]
    fathers=[]
    relas=[]
    sen_id=0
    part_id=0
    vobs=[]
    sbvs=[]
    dict={}
    out=open('pre_deal_res','w+')
    for line in file('essays_document.parser'):
        if line!='\n':
            word,type,father,rela=line.strip().split('\t')
            words.append(word)
            types.append(type)
            fathers.append(father)
            relas.append(rela)
            if rela=='VOB':
                vobs.append(part_id)
            elif rela=='SBV':
                sbvs.append(part_id)
            part_id+=1
        else:
           if len(vobs)!=0:
               dict[sen_id]=[]
               for i in range(len(vobs)):
                   dict[sen_id].append((words[int(fathers[vobs[i]])-1],words[vobs[i]]))
           elif len(sbvs)!=0:
              # print sbvs[0]
               dict[sen_id]=[]
               for j in range(len(sbvs)):
                    dict[sen_id].append((words[sbvs[j]],words[int(fathers[sbvs[j]])-1]))
           else:pass
           if dict.has_key(sen_id):
               out.write(str(sen_id)+':\t')
               for k in range(len(dict[sen_id])):
                   out.write('('+dict[sen_id][k][0]+','+dict[sen_id][k][1]+')')
                   #print dict[sen_id][k][0]
                   out.write('\t')
               out.write('\n')
           sen_id+=1
           part_id=0
           words=[]
           types=[]
           fathers=[]
           relas=[]
           vobs=[]
           sbvs=[]
    out.close()

pre_deal()

