import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="dsci551",
    passwd="Dsci-551",
    ##auth_plugin= 'mysql_native_password',
    database="sakila"
)
print(mydb)

mycursor = mydb.cursor()

mycursor.execute("SELECT DISTINCT film.film_id, film.title, actor.first_name FROM film"
                 " LEFT JOIN film_actor ON film.film_id=film_actor.film_id"
                 " LEFT JOIN actor ON film_actor.actor_id=actor.actor_id "
                 " WHERE actor.last_name='Temple'"
                 " ORDER BY film.film_id"


                 )

myresult = mycursor.fetchall()  # fetchall() 获取所有记录
lst=[]
for x in myresult:
    y=['%s(%d)'%(list(x)[1].title(), list(x)[0]), list(x)[2].capitalize()]
    lst.append(y)
dic={}
for e in lst:
    if e[0] in dic.keys():
        dic[e[0]].append(e[1])
    else:
        dic[e[0]]=[]
        dic[e[0]].append(e[1])


print('%d films in total.' % (len(dic)))
for n in dic:
    if len(dic[n])==1:
        print('%s Temple plays %s' % (dic[n][0], n))
    else:
        print('%s Temple and %s Temple play %s' % (dic[n][0], dic[n][1], n))








