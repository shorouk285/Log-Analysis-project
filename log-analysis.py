#!/usr/bin/env python3

import psycopg2

DBNAME = "news"


def top_articles():
    """Print the top three articles by views.

    Prints a list of article titles, along with the number of views each title
    has, ordered by the number of views. Only the top three are printed. The
    list is printed to the console.
    """
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""select title, views
     from articles join (select path, count(*) as views from log
      where status = '200 OK' group by path) logs
       on concat('/article/',articles.slug)=logs.path
       order by views desc limit 3;""")
    rows = c.fetchall()
    db.close()
    print("\nWhat are the most popular three articles of all time?")
    for i in rows:
        print('"{}" -- {} views'.format(i[0], i[1]))


def top_author():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(""" select name, SUM(views) top_views
   from articles join (select path, count(*) as views from log
    where status = '200 OK' group by path) logs
     on concat('/article/',articles.slug)=logs.path
     join authors on articles.author=authors.id
     group by name order by top_views desc; """)
    author = c.fetchall()
    db.close()
    print("\nWho are the most popular article authors of all time?")
    for i in author:
        print('{} -- {} views'.format(i[0], i[1]))


def error_percentage():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""select to_char, percentage from errors_prcentage
    where percentage >1 order by percentage desc""")
    error = c.fetchall()
    print("\nOn which days did more than 1% of requests lead to errors?")
    for i in error:
        print('{} -- {}% errors'.format(i[0], i[1]))


if __name__ == '__main__':
    top_articles()
    top_author()
    error_percentage()
