import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():
    #Primero se crean los diccionarios con las páginas que queremos que se creen
    #Después creamos un diccionario de diccionarios para las categorias

    python_pages = [{
        "title": "Official Python Tutorial",
        "url": "http://docs.python.org/2/tutorial",
        "views":10 },
        {"title": "How to think like a computer scientist",
         "url": "http://www.greenteapress.com/thinkpython/",
         "views":12 },
        {"title": "Learn Python in 10 minutes",
         "url": "http://www.korokithakis.net/tutorials/python/",
         "views":15 }
        ]

    django_pages =[
        {"title":"Official Django Tutorial",
        "url":"https://docs.djangoproject.com/en/1.9/intro/tutorial01/",
        "views":20 },
        {"title":"Django Rocks",
        "url":"http://www.djangorocks.com/",
        "views":26 },
        {"title":"How to Tango with Django",
        "url":"http://www.tangowithdjango.com/",
        "views":32 } ]
     
    other_pages = [
        {"title":"Bottle",
        "url":"http://bottlepy.org/docs/dev/",
        "views":10},
        {"title":"Flask",
         "url":"http://flask.pocoo.org",
         "views":12 } ]
    cats = {"Python":{"pages": python_pages,"views":128,"likes":64},
            "Django":{"pages": django_pages,"views":64,"likes":32},
            "Other Frameworks":{"pages": other_pages,"views":32,"likes":16}}

    for cat, cat_data in cats.items():
        c = add_cat(cat,cat_data["views"],cat_data["likes"])
        for p in cat_data["pages"]:
            add_page(c,p["title"],p["url"],p["views"])

    # Print Categories
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("-{0} - {1}".format(str(c), str(p)))
    
def add_page(cat,title,url, views):
    p = Page.objects.get_or_create(category = cat, title= title)[0]
    p.url = url
    p.views = views
    p.save()
    return p

def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name= name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c

if __name__ == '__main__':
    print("Starting the rango paputlation script...")
    populate()


