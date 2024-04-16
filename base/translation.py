from modeltranslation.translator import translator, register, TranslationOptions
from .models import *


@register(MainMenu)
class MainMenuTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(BooksCategory)
class BooksCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(TextbookClasses)
class TextbookClassesTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(TextbookLanguages)
class TextbookLanguagesTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(TextbooksCategories)
class TextbooksCategoriesTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(EducationCategory)
class EducationCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(CultureCategory)
class CultureCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Culture)
class CultureTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'short_description',
        'description',
        'location',
    )

@register(FooterDetail)
class FooterDetailTranslationOptions(TranslationOptions):
    fields = ('short_description', )

@register(FooterImportantLinks)
class FooterImportantLinksTranslationOptions(TranslationOptions):
    fields = ('name', 'detail',)

@register(ShippingMethod)
class ShippingMethodTranslationOptions(TranslationOptions):
    fields = ('name',)