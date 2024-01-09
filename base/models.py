from django.db import models
from oscar.core.loading import get_model
from apps.catalogue.models import Category as Oscar_Category


# Oscar_Category = get_model('catalogue', 'Category')

# Create your models here.
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