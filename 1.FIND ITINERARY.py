def find(dic):

    hash={}

    for x in dic:
        hash[dic[x]]=x

    first=''

    for x in hash:
        first=x
        break


    while True:
        if first in hash:
            first=hash[first]

        else:
            break


    while True:
        if first in dic:
            print(first,'=>',dic[first])
            first=dic[first]
        else:
            break

d={}
d['Chennai']='Bangalore'
d['Bombay']='Delhi'
d['Goa']='Chennai'
d['Delhi']='Goa'
find(d)

