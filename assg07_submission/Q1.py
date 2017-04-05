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

def loadUsers(path='ml-100k'):
    users={}
    for line in open(path+'/u.user', 'r', encoding='ISO-8859-1'):
        (user,age,gender,occupation,zipcode)=line.split('|')
        users.setdefault(user,{})
        users[user]['age']=age
        users[user]['gender']=gender
        users[user]['occupation']=occupation
        users[user]['zipcode']=zipcode
    return users

users = loadUsers()
scores=[(abs(int(users[user]['age'])-32),user)
        for user in users if users[user]['gender']=='M' and users[user]['occupation']=='student']
scores.sort()
movies = loadMovies()
prefs = loadMovieLens(movies)

for i in range(3):
    films=[]
    for movie in prefs[scores[i][1]]:
        row = (prefs[scores[i][1]][movie],movie)
        films.append(row)
    films.sort()
    print ('\nUser'+scores[i][1]+'\'s bottom 3 least favorite films:')
    for j in range(3):
        print (films[j][1]+'\t{}'.format(films[j][0]))
    films.reverse()
    print ('\nUser'+scores[i][1]+'\'s top 3 favorite films:')
    for j in range(3):
        print (films[j][1]+'\t{}'.format(films[j][0]))
