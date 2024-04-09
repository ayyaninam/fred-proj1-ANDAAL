from django.contrib import admin
from base.models import *
from parler.admin import TranslatableAdmin
# Register your models here.
from django.contrib import admin

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

class FooterImportantLinksAdmin(admin.ModelAdmin):
    class Media:
        from django.conf import settings
        media_url = getattr(settings, 'MEDIA_URL', '/media')
        js = [ media_url+'/tinyMceIntegration.js', ]


admin.site.register(MainMenu, TranslatableAdmin)
admin.site.register(TextbookClasses, TranslatableAdmin)
admin.site.register(TextbookLanguages, TranslatableAdmin)
admin.site.register(TextbooksCategories, TranslatableAdmin)
admin.site.register(EducationCategory, TranslatableAdmin)
admin.site.register(BooksCategory, TranslatableAdmin)
admin.site.register(CultureCategory, TranslatableAdmin)
admin.site.register(Culture, TranslatableAdmin)
admin.site.register(ShippingMethod, TranslatableAdmin)
admin.site.register(User, TranslatableAdmin)
admin.site.register(RateOfEuro, TranslatableAdmin)
admin.site.register(FooterDetail, TranslatableAdmin)
admin.site.register(FooterImportantLinks, FooterImportantLinksAdmin)
