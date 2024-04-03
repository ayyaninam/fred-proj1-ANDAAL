from django.test import SimpleTestCase
from django.template import Template, Context
from base.templatetags.newfilters import next, previous

class TemplateFiltersTestCase(SimpleTestCase):
    def test_next_filter(self):
        some_list = ['A', 'B', 'C']
        context = Context({'some_list': some_list})
        
        template = Template("{% load newfilters %}{{ some_list|next:0 }}")
        self.assertEqual(template.render(context), 'B')

        template = Template("{% load newfilters %}{{ some_list|next:2 }}")
        self.assertEqual(template.render(context), '')

        template = Template("{% load newfilters %}{{ some_list|next:3 }}")
        self.assertEqual(template.render(context), '')

    def test_previous_filter(self):
        some_list = ['A', 'B', 'C']
        context = Context({'some_list': some_list})
        
        template = Template("{% load newfilters %}{{ some_list|previous:1 }}")
        self.assertEqual(template.render(context), 'A')

        template = Template("{% load newfilters %}{{ some_list|previous:0 }}")
        self.assertEqual(template.render(context), 'C')

        template = Template("{% load newfilters %}{{ some_list|previous:-1 }}")
        self.assertEqual(template.render(context), 'B')
