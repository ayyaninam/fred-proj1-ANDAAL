from django.shortcuts import render

from oscar.core.loading import get_model
from base.models import *

# Create your views here.
def homepage(request):
    return render(request, "base/homepage.html")

def textbook_language_section(request):
    all_languages = TextbookLanguages.objects.all()
    context = {
        "all_languages":all_languages,
    }
    return render(request, "base/textbook_language_section.html", context=context)

def class_categories(request, language):
    language = TextbookLanguages.objects.filter(name=language)[0]
    all_categories = TextbooksCategories.objects.filter(language_associated=language)


    context = {
        "all_categories":all_categories,
    }

    return render(request, "base/class_categories.html", context=context)


def education(request, category_id):
    active_category = ""
    if category_id==0:
        category = EducationCategory.objects.filter(default=True)
    else:
        category = EducationCategory.objects.filter(id=category_id)
    
    if category:
        all_post = Education.objects.filter(category=category[0])
        active_category = category[0]
    else:
        all_post = None

    all_categories = EducationCategory.objects.all()

    context = {
        'all_post':all_post,
        'active_category':active_category,
        'all_categories':all_categories,
    }
    
    return render(request, "base/education.html", context=context)

def education_post(request, post_id):
    post = Education.objects.get(id=post_id)

    context = {
        'post':post,
    }

    return render(request, 'base/education_post.html', context)