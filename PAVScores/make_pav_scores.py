from numpy import max,min,mean

fh = open("../TableS1-features-original-369.csv")
fh.readline()
list_of_genes = set([])
for x in fh:
    y = x.strip().split(',')
    list_of_genes.add(y[0])

bro = {}
fh = open("brohammer.csv")
fh.readline()
fh.readline()
for x in fh:
    y = x.strip().split(',')
    bro[y[0]] = map(float,y[1:])

dd = {}

for agene in sorted(list(list_of_genes)):
    if agene in bro:
        plist = [agene]
        plist.append(max(bro[agene]))
        plist.append(mean(bro[agene]))
        plist.append(min(bro[agene]))
        tcount = 0
        mcount = 0
        for c in bro[agene]:
            tcount += 1
            if c < .5:
                mcount += 1
        plist.append(mcount/float(tcount))
        dd[agene] = plist
    else:
        dd[agene] = [agene,1,1,1,0]
    print(",".join(map(str,dd[agene])))

#print(len(set(list(bro))))
#print(len(set(list(list_of_genes))))

#print(len(set(list(list_of_genes)).intersection(set(list(bro)))))
