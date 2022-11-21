import requests
import json
import pandas as pd

url1='https://dsci551-bad6f-default-rtdb.firebaseio.com/films.json'
url2='https://dsci551-bad6f-default-rtdb.firebaseio.com/actors.json' # urls of database

actor = pd.read_csv('actor.csv', sep=';', usecols=["actor_id", "first_name", "last_name"])#load and transform the data
category = pd.read_csv('category.csv', sep=';', usecols=["category_id", "name"])
category.rename(columns={"name": "category"}, inplace=True)
category['category']=category['category'].str.upper()
film = pd.read_csv('film.csv', sep=';', usecols=["film_id", "title", "release_year",
                                                 "rating", "rental_rate", "rental_duration"])
film_actor = pd.read_csv('film_actor.csv', sep=';', usecols=["actor_id", "film_id"])
film_category = pd.read_csv('film_category.csv', sep=';', usecols=["film_id", "category_id"])

actor['actor_name'] = actor['first_name']+' '+actor['last_name']
actor.drop(columns=["first_name", "last_name"], inplace=True)

film_actor = pd.merge(film_actor, actor, on="actor_id")
actors = film_actor.groupby('film_id')['actor_name'].apply(list).to_dict()

film_category = pd.merge(film_category, category, on="category_id")

film = pd.merge(film, film_category, on="film_id")
film.drop(columns=["category_id"], inplace=True)

data_film= {}
for obj in film.to_dict('records'):
    title = obj['title']
    del (obj['film_id'])
    data_film[title] = obj
    #preparing for json

r1 = requests.put(url1, json.dumps(data_film)) #request

film1=pd.read_csv('film.csv', sep=';', usecols=["film_id", "title", "release_year"])
film_actor1 = pd.merge(film_actor, film1, on="film_id")
film_actor1.drop(columns=["film_id", "actor_name"], inplace=True)
film_actor_id={}
for obj in film_actor1.to_dict('records'):
    if  obj['actor_id'] in film_actor_id.keys():
        film_actor_id[obj['actor_id']][obj['title']]=obj['release_year']
    else:
        film_actor_id[obj['actor_id']] = {}
        film_actor_id[obj['actor_id']][obj['title']]=obj['release_year']#data transform


data_actor={}
for obj in actor.to_dict('records'):
    if  obj['actor_name'] in data_actor.keys():
        data_actor[obj['actor_name']][obj['actor_id']]=film_actor_id[obj['actor_id']]
    else:
        data_actor[obj['actor_name']] = {}
        data_actor[obj['actor_name']][obj['actor_id']]=film_actor_id[obj['actor_id']]


r2 = requests.put(url2,json.dumps(data_actor)) # request

json.dump(data_film, open('data_film.json', "w"))# json dump
json.dump(data_actor, open('data_actor.json', "w"))








