from django.shortcuts import render

from oscar.core.loading import get_model

# Create your views here.
def homepage(request):
    return render(request, "base/homepage.html")

def textbooks_schools_main_section(request):
    Category = get_model('catalogue', 'Category')
    all_categories = [x for x in Category.objects.all() if not x.full_name.find(">") != -1]

    context = {
        "all_categories":all_categories,
    }
    return render(request, "base/textbooks_schools_main_section.html", context=context)

def class_categories(request, language):
    Category = get_model('catalogue', 'Category')
    all_categories = [x for x in Category.objects.all() if x.full_name.find(language) != -1 and x.full_name.find(">") != -1]

    context = {
        "all_categories":all_categories,
    }
    return render(request, "base/class_categories.html", context=context)