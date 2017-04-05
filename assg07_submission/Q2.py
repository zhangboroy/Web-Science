from math import sqrt

# Returns the Pearson correlation coefficient for p1 and p2
def sim_pearson(prefs,p1,p2):
    # Get the list of mutually rated items
    si={}
    for item in prefs[p1]:
        if item in prefs[p2]: si[item]=1

    # Find the number of elements
    n=len(si)

    # if they are no ratings in common, return 0
    if n==0: return 0

    # Add up all the preferences
    sum1=sum([prefs[p1][it] for it in si])
    sum2=sum([prefs[p2][it] for it in si])

    # Sum up the squares
    sum1Sq=sum([pow(prefs[p1][it],2) for it in si])
    sum2Sq=sum([pow(prefs[p2][it],2) for it in si])

    # Sum up the products
    pSum=sum([prefs[p1][it]*prefs[p2][it] for it in si])

    # Calculate Pearson score
    num=pSum-(sum1*sum2/n)
    den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
    if den==0: return 0

    r=num/den
    return r

# Returns the best matches for person from the prefs dictionary.
# Number of results and similarity function are optional params.
def topMatches(prefs,person,reverse=False,n=5,similarity=sim_pearson):
    scores=[(similarity(prefs,person,other),other)
            for other in prefs if other!=person]
    
    # Sort the list so the highest scores appear at the top
    scores.sort()
    if reverse==False:
        scores.reverse()
    return scores[0:n]

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

output=topMatches(prefs,'560')
print ('5 Most Correlated Users:')
for i in range(5):
    print (output[i][1]+'\t{}'.format(output[i][0]))
output=topMatches(prefs,'560',True)
print ('\n5 Least Correlated Users:')
for i in range(5):
    print (output[i][1]+'\t{}'.format(output[i][0]))
