import csv
import fnmatch
import os

def extract(log):
    xy = log[log.index('[')+1:log.index(']')]
    xy = xy.split(',')[:2]
    spd = log[log.index('"spd":')+7:].split(',')[:2]
    rcv = log[log.index('"rcvTime":')+10:].split(',')[0:1]
    return xy + spd + rcv

#list of filename strings
file = fnmatch.filter(os.listdir('.'), 'JSONlog-*.json')

de = [] #type 3 logs extract

Dict = {} #vehicle number using ID
DictA = {} #attacker status using ID

for i in range(len(file)):
    f = open(file[i],"r")
    a = f.read().split("\n")
    a.pop()

    #file structure: JSONlog-[0]-[1]-[2].json
    cut = file[i][8:file[i].index('.')].split('-')

    Dict.update({cut[1]:cut[0]}) #3 type 3 dictionary use
    
    if (cut[2] == 'A0'): DictA.update({cut[1]:'0'}) #3 type 3 dictionary use
    else: DictA.update({cut[1]:'1'}) #3 type 3 dictionary use

    de.append([]) #3 type 3 extract
    for j in range(len(a)):
        if '"type":3' in a[j]:
            de[i].append(a[j]) #3

    f.close()


dataset = [['Displacement','Acceleration','Class']]

for m in range(len(de)):

    d3 = [] #type 3 extracts
    sender = []
    for n in range(len(de[m])):

        cut = de[m][n].split(',')

        #{"type":3,"rcvTime":10800.392893331087,"sendTime":10800.392784793165,"sender":13,"messageID":38,
        #1 & 3 ; 10 & 9 ; time   ID

        mid = cut[3][9:] #module ID

        data = extract(de[m][n])
        
        if (mid not in sender):
            sender.append(mid)
            d3.append([])

        d3[sender.index(mid)].append(data)
            
    for n in range(len(d3)):
        for o in range(len(d3[n])):
            if o > 0:
                dx = float(d3[n][o][0]) - float(d3[n][o-1][0])
                dy = float(d3[n][o][1]) - float(d3[n][o-1][1])
                d = (dx**2 + dy**2)**.5

                dvx = float(d3[n][o][2]) - float(d3[n][o-1][2])
                dvy = float(d3[n][o][3]) - float(d3[n][o-1][3])
                dt = float(d3[n][o][4]) - float(d3[n][o-1][4])

                ax = dvx/dt
                ay = dvy/dt
                
##                v = (vx**2 + vy**2)**.5
                a = (ax**2 + ay**2)**.5

                dataset.append([d,a,DictA[sender[n]]])

##                ######displacement in x and y
##                dataset.append([(dx**2)**.5,(dy**2)**.5,DictA[sender[n]]])

##                dataset.append([dx,dy,DictA[sender[n]]])

##                ######displacement magnitude and initial speed
##                dataset.append([d,v,DictA[sender[n]]])
                
    #change filename to specific attack setup for adding datasets
    with open('dataset.csv', 'w') as l:
        writer3 = csv.writer(l)
        writer3.writerows(dataset)

    l.close()
