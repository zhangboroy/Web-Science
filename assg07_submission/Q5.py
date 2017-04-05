def transformPrefs(prefs):
    result={}
    for person in prefs:
        for item in prefs[person]:
            result.setdefault(item,{})

            # Flip item and person
            result[item][person]=prefs[person][item]
    return result

def loadMovies(path='ml-100k'):
    movies={}
    f = open(path+'/u.item', 'r', encoding='ISO-8859-1')
    lines = f.readlines()
    f.close()
    for line in lines:
        line=line.split('|')
        (id,title)=line[0:2]
        URL=line[4]
        movies.setdefault(id,{})
        movies[id]['title']=title
        movies[id]['URL']=URL
    return movies

def loadMovieLens(movies,path='ml-100k'):
    # Load data
    prefs={}
    for line in open(path+'/u.data', 'r', encoding='ISO-8859-1'):
        (user,movieid,rating,ts)=line.split('\t')
        prefs.setdefault(user,{})
        prefs[user][movies[movieid]['title']]=float(rating)
    return prefs

movies = loadMovies()
prefs = loadMovieLens(movies)
films = transformPrefs(prefs)

f = open('IMDBrating.csv', 'r', encoding='UTF-8')
lines = f.readlines()
f.close()
MovieLense=[]
IMDB=[]

for line in lines:
    row = line.strip().split('\t')
    rating = 0
    for item in films[movies[row[0]]['title']]:
        rating = rating + films[movies[row[0]]['title']][item]
    rating = rating/len(films[movies[row[0]]['title']])
    MovieLense.append([rating,len(films[movies[row[0]]['title']]),int(row[0])])
    IMDB.append([row[1],int(row[2].replace(',','')),int(row[0])])

MovieLense.sort(key=lambda x:(x[0],x[1],x[2]), reverse=True)
IMDB.sort(key=lambda x:(x[0],x[1]), reverse=True)

for i in range(len(lines)):
    MovieLense[i]=[MovieLense[i][2],i]
    IMDB[i]=[IMDB[i][2],i]

MovieLense.sort()
IMDB.sort()

f = open('rankContrast.csv', 'w', encoding='utf-8')
f.write('ID\tMovieLense Rank\tIMDB Rank\n')
for i in range(len(lines)):
    f.write('{}'.format(IMDB[i][0])+'\t{}'.format(MovieLense[i][1])+'\t{}'.format(IMDB[i][1])+'\n')
f.close()
