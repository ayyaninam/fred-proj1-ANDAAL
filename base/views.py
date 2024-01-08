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