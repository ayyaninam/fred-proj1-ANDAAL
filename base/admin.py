from django.contrib import admin
from base.models import *
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


admin.site.register(MainMenu)
admin.site.register(TextbookClasses)
admin.site.register(TextbookLanguages)
admin.site.register(TextbooksCategories)
admin.site.register(EducationCategory)
admin.site.register(CultureCategory)
admin.site.register(Culture)
admin.site.register(ShippingMethod)
admin.site.register(User)
admin.site.register(RateOfEuro)
admin.site.register(FooterDetail)
admin.site.register(FooterImportantLinks, FooterImportantLinksAdmin)
