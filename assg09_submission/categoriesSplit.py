import feedparser
import re

entries={}
out=open('entries.txt','w',encoding='utf-8')
out.write('title\tclassification\n')
feedlist=[line.strip() for line in open('feedlist.txt','r')]
for feedurl in feedlist:
    print (feedurl)
    
    d=feedparser.parse(feedurl)
    print (d.feed.title)

    # Loop over all the entries
    for e in d.entries:
        print (e.title)

        summary=''
        if 'content' in e:
            for content in e.content:
                print (content)
                print ()
                summary=summary+content.value+' '
        elif 'summary' in e and e.summary!='':
            print (e.summary)
            print ()
            summary=summary+e.summary+' '
        elif 'description' in e and e.description!='':
            print (e.description)
            print ()
            summary=summary+e.description+' '
        else:
            print ('error!!!!!!!!!!!!!!')
            print ()

        if e.title not in entries:
            entries.setdefault(e.title,[summary,d.feed.title])

f=open('summary.txt','w',encoding='utf-8')
i=0
for entry in entries:
    if i<100:
        out.write(entry+'\t'+entries[entry][1].split(' ')[2]+'\n')
        f.write(entries[entry][0]+'\n')
        i=i+1
    else: break
out.close()
f.close()
