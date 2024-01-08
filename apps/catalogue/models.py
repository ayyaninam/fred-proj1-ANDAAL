from oscar.apps.catalogue.abstract_models import AbstractCategory
from django.db import models


class Category(AbstractCategory):
    show_on_search_menu = models.BooleanField(default=False, null=False)

from oscar.apps.catalogue.models import * 
