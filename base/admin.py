from django.contrib import admin
from base.models import *
# Register your models here.
from django.contrib import admin
from modeltranslation.admin import TranslationTabularInline, TranslationAdmin


def duplicate_selected(modeladmin, request, queryset):
    for obj in queryset:
        obj.pk = None  # Set primary key to None to create a new entry
        obj.save()

duplicate_selected.short_description = "Duplicate selected entries"

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    actions = [duplicate_selected]

# @admin.register(Culture)
# class CultureAdmin(admin.ModelAdmin):
#     actions = [duplicate_selected]

class FooterImportantLinksAdmin(TranslationAdmin):
    class Media:
        from django.conf import settings
        media_url = getattr(settings, 'MEDIA_URL', '/media')
        js = [ media_url+'/tinyMceIntegration.js', ]



class MainMenuAdmin(TranslationAdmin):
    pass

class MainMenuAdmin(TranslationAdmin):
    pass
class BooksCategoryAdmin(TranslationAdmin):
    pass
class TextbookClassesAdmin(TranslationAdmin):
    pass
class TextbookLanguagesAdmin(TranslationAdmin):
    pass
class TextbooksCategoriesAdmin(TranslationAdmin):
    pass
class EducationCategoryAdmin(TranslationAdmin):
    pass

class CultureCategoryAdmin(TranslationAdmin):
    pass
class CultureAdmin(TranslationAdmin):
    pass
class FooterDetailAdmin(TranslationAdmin):
    pass

class ShippingMethodAdmin(TranslationAdmin):
    pass


admin.site.register(MainMenu,MainMenuAdmin)
admin.site.register(TextbookClasses,TextbookClassesAdmin)
admin.site.register(TextbookLanguages,TextbookLanguagesAdmin)
admin.site.register(TextbooksCategories,TextbooksCategoriesAdmin)
admin.site.register(EducationCategory,EducationCategoryAdmin)
admin.site.register(BooksCategory,BooksCategoryAdmin)
admin.site.register(CultureCategory,CultureCategoryAdmin)
admin.site.register(Culture,CultureAdmin)
admin.site.register(ShippingMethod,ShippingMethodAdmin)
admin.site.register(User)
admin.site.register(RateOfEuro)
admin.site.register(FooterDetail,FooterDetailAdmin)
admin.site.register(FooterImportantLinks,FooterImportantLinksAdmin)
