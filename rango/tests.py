from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from rango.models import Category, Page
from django.core.urlresolvers import reverse

class CategoryMethodTest(TestCase):
    
    def test_ensure_views_are_positive(self):
        cat = Category(name='Test', views=-1, likes=0)
        cat.save()
        self.assertEquals((cat.views >= 0), True)
        
    def test_slug_line_creation(self):
        cat = Category(name='Something Do not Know')
        cat.save()
        self.assertEqual(cat.slug, 'something-do-not-know')
def add_catefor
def add_page():
        
class PageMethodTest(TestCase):
    
    def first_visit_last_visit_not_in_feature(self):
        
        
class IndexViewTests(TestCase):
    def add_category(self, name, views, likes):
        c = Category.objects.get_or_create(name=name)[0]
        c.views = 0
        c.likes = 0
        c.save()
        return c
        
    def test_index_view_no_categories(self):
        respose = self.client.get(reverse('index'))
        self.assertEqual(respose.status_code, 200)
        self.assertContains(respose, 'No Categories to display')
        self.assertQuerysetEqual(respose.context['categories'], [])
        
    def test_index_with_categories(self):
        
        self.add_category("test",1,1)
        self.add_category('testing something',1,1)
        self.add_category("testing hey",1,1)
        
        respose = self.client.get(reverse('index'))
        self.assertEqual(respose.status_code, 200)
        self.assertContains(respose, "testing something")
        self.assertEqual(len(respose.context['categories']), 3)
               
    