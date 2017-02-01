import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():
    python_pages = [{"title": "Official python tutorial1",
                     "url": "http://google.com",'views': 12,},
                    {"title": "Official python tutorial2",
                     "url": "http://google.com",'views': 13,},
                    {"title": "Official python tutorial3",
                     "url": "http://google.com",'views': 14,},
                    {"title": "Official python tutorial4",
                     "url": "http://google.com",'views': 15,},
                    {"title": "Official python tutorial5",
                     "url": "http://google.com",'views': 16,},
                    ]
    django_pages = [{"title": "Official django tutorial1",
                     "url": "http://google.com",'views': 14,},
                    {"title": "Official django tutorial2",
                     "url": "http://google.com",'views': 15,},
                    {"title": "Official django tutorial3",
                     "url": "http://google.com",'views': 16,},
                    {"title": "Official django tutorial4",
                     "url": "http://google.com",'views': 17,},
                    {"title": "Official django tutorial5",
                     "url": "http://google.com",'views': 18,},
                    ]
    other_pages = [{"title": "Official other tutorial1",
                     "url": "http://google.com",'views': 19,},
                    {"title": "Official other tutorial2",
                     "url": "http://google.com",'views': 18,},
                    {"title": "Official other tutorial3",
                     "url": "http://google.com",'views': 17,},
                    {"title": "Official other tutorial4",
                     "url": "http://google.com",'views': 16,},
                    {"title": "Official other tutorial5",
                     "url": "http://google.com",'views': 18,},
                    ]
    
    cats = {"Python": {'pages': python_pages, 'views': 10, 'likes': 20},
            "Django": {'pages': django_pages, 'views': 40, 'likes': 20},
            "Other Framework": {'pages': other_pages, 'views': 30, 'likes': 50}}
    
    def add_cat(cat, views, likes):
        c = Category.objects.get_or_create(name=cat)[0]
        c.views = views
        c.likes = likes
        c.save()
        return c
    
    def add_page(cat, title, url, views=0):
        p = Page.objects.get_or_create(category=cat,
                                       title=title)[0]
        p.url = url
        p.views = views
        p.save()
        return p    
    
    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data['views'], cat_data['likes'])
        for page in cat_data['pages']:
            p = add_page(c, page['title'], page['url'], page['views'])
            
    for c in Category.objects.all():
        for p in Page.objects.all():
            print "{0} - {1}".format(str(c), str(p))    
    

if __name__ == '__main__':
    print ("Starting Rango Population script")
    populate()