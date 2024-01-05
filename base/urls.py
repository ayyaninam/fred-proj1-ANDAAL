from . import views
from django.urls import path

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('textbooks-schools-main-section', views.textbooks_schools_main_section, name="textbooks_schools_main_section"),
    path('class-categories/<str:language>', views.class_categories, name="class_categories"),
    
    
]