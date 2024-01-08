from . import views
from django.urls import path

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('textbook-language-section', views.textbook_language_section, name="textbook_language_section"),
    path('class-categories/<str:language>', views.class_categories, name="class_categories"),
    
    
]