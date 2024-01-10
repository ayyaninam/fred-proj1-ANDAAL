from django.contrib import admin
from base.models import *
# Register your models here.
admin.site.register(TextbookClasses)
admin.site.register(TextbookLanguages)
admin.site.register(TextbooksCategories)
admin.site.register(EducationCategory)
admin.site.register(Education)
admin.site.register(CultureCategory)
admin.site.register(Culture)