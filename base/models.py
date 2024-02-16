from django.db import models
from oscar.core.loading import get_model
from apps.catalogue.models import Category as Oscar_Category
from oscar.apps.customer.abstract_models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

# Oscar_Category = get_model('catalogue', 'Category')

# Create your models here.
class User(AbstractUser):
    phone_number = PhoneNumberField(
        _("Phone number"),
        blank=True,
        unique=True,
    )
    email = models.EmailField(_("email address"), unique=False, blank=True, null=True)

    def __str__(self):
        if self.email:
            return self.email
        else:
            return self.first_name
        


class MainMenu(models.Model):
    name= models.CharField(max_length=200, null=False, blank=False)
    icons_link = models.TextField(max_length=200, null=True, blank=True, help_text='Please go to the link: fonts.google.com/icons and attach the code which is under the "Inserting the icon" menu after slecting the icon.')


    redirect_to_link = models.CharField(max_length=1000, null=True, blank=True, help_text='Please write the url like /abc/abc/1, do not include any domain or IP address before the URL. This url will redirect users to this LINK. Please keep it blank if you want to attached any category to the main menu and select the category in below field(name "Category Attached")')

    category_attached = models.ForeignKey(Oscar_Category, null=True, blank=True, on_delete=models.CASCADE, help_text="Please choose the Category if you don't attach any redirect link, if you will attach the both, priority will be for Category field.")


    def __str__(self):
        return self.name

class TextbookLanguages(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)

    def __str__(self):
        return self.name
    
class TextbookClasses(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    products_category = models.ForeignKey(Oscar_Category, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class TextbooksCategories(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    language_associated = models.ForeignKey('TextbookLanguages',null=False,blank=False, on_delete=models.CASCADE)
    child_classes = models.ManyToManyField(TextbookClasses)
    
    def __str__(self):
        return self.name
    
# class BooksCategoryAssociated(models.Model):
#     pass


class EducationCategory(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    default = models.BooleanField( null=False, default=False, blank=False)

    def __str__(self):
        return self.name

class Education(models.Model):
    title = models.CharField(max_length=250, null=False, blank=False)
    short_description = models.TextField(null=False, blank=False)
    cover_image = models.ImageField(upload_to="base/education_cover/", null=True, blank=True)
    description = models.TextField(null=False, blank=False)
    date = models.DateField(auto_now=True, null=False, blank=False)
    location = models.CharField(max_length=255, null=True, blank=True)
    link_to_orignal = models.URLField(max_length = 1000) 
    category = models.ManyToManyField(EducationCategory)

    def __str__(self):
        return self.title[:50]

class CultureCategory(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    default = models.BooleanField( null=False, default=False, blank=False)

    def __str__(self):
        return self.name

class Culture(models.Model):
    title = models.CharField(max_length=250, null=False, blank=False)
    short_description = models.TextField(null=False, blank=False)
    cover_image = models.ImageField(upload_to="base/culture_cover/", null=True, blank=True)
    description = models.TextField(null=False, blank=False)
    date = models.DateField(auto_now=True, null=False, blank=False)
    location = models.CharField(max_length=255, null=True, blank=True)
    link_to_orignal = models.URLField(max_length = 1000) 
    category = models.ManyToManyField(CultureCategory)

    def __str__(self):
        return self.title[:50]
    

class ShippingMethod(models.Model):
    child_of = models.ForeignKey('self', on_delete=models.CASCADE, help_text="If you choose this, then this will become a child (not a parent)", blank=True, null=True )
    name = models.CharField(max_length=250, null=False, blank=False)
    code = models.CharField(max_length=250, null=True, blank=True, help_text="Please don't give any space in this field")
    charge_excl_tax = models.IntegerField(null=True, blank=True)
    charge_incl_tax = models.IntegerField(null=True, blank=True)

    def clean(self):
        if self.code:
            self.code = self.code.lower().strip().replace(" ", "")
        if not self.child_of:
            self.code = None
            self.charge_excl_tax = None
            self.charge_incl_tax = None

    def __str__(self) -> str:
        return self.name
