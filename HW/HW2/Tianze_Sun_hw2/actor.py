import sys
from lxml import etree


actor_name = (' '.join(sys.argv[1:])).upper()    # process the input
tree = etree.parse("main.xml")
film_actors = tree.xpath('/root/film_actor_table/film_actor[actor_name/text()="%s"]' % (actor_name))

if film_actors:
    film_id_list = []
    for film_actor in film_actors:
        film_id_list.append(film_actor[0].text)

    for film_id in film_id_list:
        list = []
        film = tree.xpath('/root/film_table/film[@film_id="%s"]' % (film_id))
        list.append(film[0][0].text)
        list.append(film[0][1].text)
        print(tuple(list))

else:
    print('No results found.')



