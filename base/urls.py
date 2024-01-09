from . import views
from django.urls import path

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('textbook-language-section', views.textbook_language_section, name="textbook_language_section"),
    path('class-categories/<str:language>', views.class_categories, name="class_categories"),
    path('education/<int:category_id>', views.education, name="education"),
    path('education-post/<int:post_id>', views.education_post, name="education_post"),
]