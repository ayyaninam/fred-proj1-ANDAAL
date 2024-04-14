from django.db import models
from apps.catalogue.models import Category as Oscar_Category
from oscar.apps.customer.abstract_models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from oscar.apps.address.models import Country as AddressCountry
# from parler.models import TranslatableModel, TranslatedFields

import datetime
# Oscar_Category = get_model('catalogue', 'Category')

# Create your models here.
class User(AbstractUser):
    phone_number = PhoneNumberField(
        _("Phone number"),
        null=True,
        blank=True,
    )
    # email = models.EmailField(_("email address"), null=True, blank=False, unique=True)
    username = models.CharField(_("username"), max_length=1000, null=True, blank=True)

    def __str__(self):
        if self.email:
            return self.email
        else:
            return self.first_name
        


class MainMenu(TranslatableModel):

    def __str__(self):
        return self.name
    
class BooksCategory(TranslatableModel):

    def __str__(self):
        return self.name

class TextbookLanguages(TranslatableModel):
    translations = TranslatedFields(

    name = models.CharField(_("name"), max_length=255, null=False, blank=False, unique=True),
)
    def __str__(self):
        return self.name
    
class TextbookClasses(TranslatableModel):
    translations = TranslatedFields(

    name = models.CharField(_("name"), max_length=255, null=False, blank=False),
    products_category = models.ForeignKey( Oscar_Category, null=False, blank=False, on_delete=models.CASCADE),
)
    def __str__(self):
        return self.name

class TextbooksCategories(TranslatableModel):
    translations = TranslatedFields(

    name = models.CharField(_("name"), max_length=255, null=False, blank=False, unique=True),
    language_associated = models.ForeignKey('TextbookLanguages',null=False,blank=False, on_delete=models.CASCADE),
    child_classes = models.ManyToManyField(TextbookClasses),
    )
    def __str__(self):
        return self.name
    
# class BooksCategoryAssociated(TranslatableModel):
# translations = TranslatedFields(

#     pass


class EducationCategory(TranslatableModel):
    translations = TranslatedFields(

    name = models.CharField(_("name"), max_length=255, null=False, blank=False, unique=True),
    default = models.BooleanField(_("default"),  null=False, default=False, blank=False),
)
    def __str__(self):
        return self.name

class Education(TranslatableModel):
    translations = TranslatedFields(

    owner_or_institution_name = models.CharField(_("owner_or_institution_name"), max_length=250, null=False, blank=False, default='admin'),
    title = models.CharField(_("title"), max_length=250, null=False, blank=False),
    short_description = models.TextField(_("short_description"), null=False, blank=False),
    cover_image = models.ImageField(_("cover_image"), upload_to="base/education_cover/", null=True, blank=True),
    description = models.TextField(_("description"), null=False, blank=False),
    date = models.DateField(_("date"), auto_now=True, null=False, blank=False),
    location = models.CharField(_("location"), max_length=255, null=True, blank=True),
    link_to_orignal = models.URLField(_("link_to_orignal"), max_length = 1000),
    category = models.ManyToManyField(EducationCategory),
)
    def __str__(self):
        return self.title[:50]

    # class Meta:
    #     ordering = ('-date',)


class CultureCategory(TranslatableModel):
    translations = TranslatedFields(

    name = models.CharField(_("name"), max_length=255, null=False, blank=False, unique=True),
    default = models.BooleanField(_("default"),  null=False, default=False, blank=False),
)
    def __str__(self):
        return self.name

class Culture(TranslatableModel):
    translations = TranslatedFields(

    owner_or_institution_name = models.CharField(_("owner_or_institution_name"), max_length=250, null=False, blank=False, default='admin'),
    title = models.CharField(_("title"), max_length=250, null=False, blank=False),
    short_description = models.TextField(_("short_description"), null=False, blank=False),
    cover_image = models.ImageField(_("cover_image"), upload_to="base/culture_cover/", null=True, blank=True),
    description = models.TextField(_("description"), null=False, blank=False),
    date = models.DateField(_("date"), null=False, blank=False),
    location = models.CharField(_("location"), max_length=255, null=True, blank=True),
    link_to_orignal = models.URLField(_("link_to_orignal"), max_length = 1000) ,
    category = models.ManyToManyField(CultureCategory),
    recommended = models.BooleanField(null=False, default=False),
)
    def __str__(self):
        return self.title[:50]

    # class Meta:
    #     ordering = ('-date',)
    

class ShippingMethod(TranslatableModel):
    translations = TranslatedFields(

    child_of = models.ForeignKey('self', on_delete=models.CASCADE, help_text="If you choose this, then this will become a child (not a parent)", blank=True, null=True ),
    name = models.CharField(_("name"), max_length=250, null=False, blank=False),
    code = models.CharField(_("code"), max_length=250, null=True, blank=True, help_text="Please don't give any space in this field"),
    charge_excl_tax = models.IntegerField(_("charge_excl_tax"), null=True, blank=True),
    charge_incl_tax = models.IntegerField(_("charge_incl_tax"), null=True, blank=True),
    countries = models.ManyToManyField(AddressCountry, blank=True, related_name="Countries"),
)
    def clean(self):
        if self.code:
            self.code = self.code.lower().strip().replace(" ", "")
        if not self.child_of:
            self.code = None
            self.charge_excl_tax = None
            self.charge_incl_tax = None
            self.countries.clear()

    def __str__(self):
        return self.name


class RateOfEuro(TranslatableModel):
    translations = TranslatedFields(

    base = models.CharField(_("base"), max_length=200, null=True, blank=True),
    date = models.DateField(_("Date"), default=datetime.date.today),
    xaf_to_euro = models.FloatField(_("xaf_to_euro"), null=False, blank=False),
)
    # class Meta:
    #    ordering = ['-date']

    def __str__(self):
        return f"XAF TO EURO is: {self.xaf_to_euro}"

class FooterDetail(TranslatableModel):
    translations = TranslatedFields(

    email = models.EmailField(_("email"), null=True, blank=True),
    phone_number = models.CharField(_("phone_number"), max_length=200, null=True, blank=True),
    short_description = models.TextField(_("short_description"), null=True, blank=True),
)

    def __str__(self) -> str:
        return f"{self.email} - {self.phone_number}"
    

class FooterImportantLinks(TranslatableModel):
    translations = TranslatedFields(

    name = models.CharField(_("name"), max_length=255, null=False, blank=False),
    detail = models.TextField(_("detail"), null=False, blank=False),
)
    def __str__(self) -> str:
        return f"{self.name}"