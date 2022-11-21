import requests
import sys

url1='https://dsci551-bad6f-default-rtdb.firebaseio.com/films.json?orderBy="category"&equalTo="'\
     +str(sys.argv[1]).upper()+'"&print=pretty'
# get the input and query

r = requests.get(url1) #quest

def sort_dict(dict): #a sort function
    keys = dict.keys()
    sorted_keys=sorted(keys)
    new_dict = {}
    for key in sorted_keys:
        new_dict[key] = dict[key]
    return new_dict


res=sort_dict(r.json()) #json decoding and sorting


if res:
    for key in res:
        obj = res[key]
        inf = (key, str(obj['release_year']), obj['rating'], str(obj['rental_rate']), str(obj['rental_duration']))

        print(inf)# data printing
else:
    print('No results found.')


