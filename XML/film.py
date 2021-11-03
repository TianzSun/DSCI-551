import sys
from lxml import etree


category = (' '.join(sys.argv[1:])).upper()    # process the input
tree = etree.parse("main.xml")
films = tree.xpath('/root/film_table/film[category/text()="%s"]' % (category))

if films:
    for film in films:
        list = []
        for element in film:
            text = element.text
            list.append(text)
        list = list[:-1]
        list[2], list[4] = list[4], list[2]
        print(tuple(list))

else:
    print('No results found.')



