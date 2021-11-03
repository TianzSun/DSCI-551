import pandas as pd


actor = pd.read_csv('actor.csv', sep=';', usecols=["actor_id", "first_name", "last_name"]) # load and transform the data
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

xf = open("main.xml", "w+")
xf.write('<root>\n')


def write_table(table, tablename):
    xf.write('  <%s_table>\n' % ( tablename ))
    columns=table.columns.tolist()
    for i in range(table.shape[0]):
        xf.write('    <%s %s="%s">\n' % (tablename, columns[0], table.iloc[i, 0]))
        for j in range(table.shape[1]):
            if j>0:
                xf.write('      <%s>%s</%s>\n' % (columns[j], table.iloc[i, j], columns[j]))
        xf.write('    </%s>\n' % (tablename))
    xf.write('  </%s_table>\n' % (tablename))


write_table(film, 'film')
write_table(film_actor, 'film_actor')

xf.write('</root>\n')