import requests
import sys

input=(' '.join(sys.argv[1:])).upper() #process the input

url2='https://dsci551-bad6f-default-rtdb.firebaseio.com/actors.json?orderBy="$key"&equalTo="'+ input +'"&print=pretty'
#query url

def sort_dict(dict):#sorting function
    keys = dict.keys()
    sorted_keys=sorted(keys)
    new_dict = {}
    for key in sorted_keys:
        new_dict[key] = dict[key]
    return new_dict


r = requests.get(url2).json() # request

if r:
    res=r[input]
    n = len(res)
    data = []
    for i in range(n):
        data.append(sort_dict(res[list(res)[i]]))
        for key in data[i]:
            inf = (key, str(data[i][key]))
            print(inf)                   #print
else:
    print('No results found.')







