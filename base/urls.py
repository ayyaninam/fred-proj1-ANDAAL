from . import views
from django.urls import path

urlpatterns = [
    path("schedule", views.schedule_task, name="schedule"), 
    path("get-euro-rate", views.get_euro_rate, name="get_euro_rate"), 

    
    path('', views.homepage, name="homepage"),
    path('after-registration', views.after_registration, name="after_registration"),
    path('verify-my-email/<str:email>/<str:username>', views.verify_my_email, name="verify_my_email"),
    path('textbook-language-section', views.textbook_language_section, name="textbook_language_section"),
    path('class-categories/<str:language>', views.class_categories, name="class_categories"),
    path('education/<int:category_id>', views.education, name="education"),
    path('education-post/<int:post_id>', views.education_post, name="education_post"),
    path('culture/<int:category_id>', views.culture, name="culture"),
    path('culture-post/<int:post_id>', views.culture_post, name="culture_post"),
    path('create-payment-intent', views.create_payment_intent, name="create_payment_intent"),
    path('stripedot', views.stripedot, name="stripedot")
]