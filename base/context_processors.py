from base.models import *
from django.conf import settings
def main_menus(request):
    # Query data from your models or wherever you need
    # For example, get the latest blog posts or user information
    main_menus = MainMenu.objects.all()
    # own logic custom class name
    # Return a dictionary with the data you want to pass to templates
    return {'main_menus': main_menus}

def textBookcategories(request):
    # Query data from your models or wherever you need
    # For example, get the latest blog posts or user information
    textBookcategories = TextbooksCategories.objects.all()
    # own logic custom class name
    # Return a dictionary with the data you want to pass to templates
    return {'textBookcategories': textBookcategories}

def educationCategories(request):
    # Query data from your models or wherever you need
    # For example, get the latest blog posts or user information
    educationCategories = EducationCategory.objects.all()
    # own logic custom class name
    # Return a dictionary with the data you want to pass to templates
    return {'educationCategories': educationCategories}

def cultureCategories(request):
    # Query data from your models or wherever you need
    # For example, get the latest blog posts or user information
    cultureCategories = CultureCategory.objects.all()
    # own logic custom class name
    # Return a dictionary with the data you want to pass to templates
    return {'cultureCategories': cultureCategories}

def footerdetails(request):
    # Query data from your models or wherever you need
    # For example, get the latest blog posts or user information
    footerdetails = FooterDetail.objects.all()
    if footerdetails:
        footerdetails = footerdetails.first()
    # own logic custom class name
    # Return a dictionary with the data you want to pass to templates
    return {'footerdetails': footerdetails}

def homepage_url(request):
    # Query data from your models or wherever you need
    # For example, get the latest blog posts or user information
    homepage_url = settings.OSCAR_HOMEPAGE

    return {'homepage_url': homepage_url}

def important_links(request):
    # Query data from your models or wherever you need
    # For example, get the latest blog posts or user information
    important_links = FooterImportantLinks.objects.all()

    return {'important_links': important_links}
