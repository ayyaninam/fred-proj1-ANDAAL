from django.shortcuts import render

from django.conf import settings
from base.models import *
from apps.catalogue.models import Category as Oscar_Category
from django.http import JsonResponse, HttpResponse
import json
import stripe
from django.views.decorators.csrf import csrf_exempt
from .all_currencies_avaialble import currencies as all_currencies_avaialble
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django_celery_beat.models import PeriodicTask, IntervalSchedule
import requests
stripe.api_key = settings.STRIPE_SECRET_KEY


User = get_user_model()
# Product = get_model('catalogue', 'Product')
# Create your views here.



def schedule_task(request):
    interval, _ = IntervalSchedule.objects.get_or_create(
        every=259200,
        period=IntervalSchedule.SECONDS,
    )

    PeriodicTask.objects.create(
        interval=interval,
        name="my-schedule",
        task="base.tasks.my_task",
        #args=json.dumps(["Arg1", "Arg2"])
        #one_off=True
    )

    return HttpResponse("Task scheduled!")

def homepage(request):

    main_menus = MainMenu.objects.all()
    # own logic custom class name
    class_names = []
    current_working_class_name = "pink__to__bottom__gradient"
    for index, i in enumerate(main_menus):
        if index%2:
            if current_working_class_name == "yellow__to__bottom__gradient":
                current_working_class_name = "pink__to__bottom__gradient"
            else:
                current_working_class_name = "yellow__to__bottom__gradient"
        class_names.append(current_working_class_name)

    main_menus_wc = zip(main_menus, class_names)
    # end own logic
    context = {
        'main_menus_wc':main_menus_wc,
    }


    return render(request, "base/homepage.html", context)

def textbook_language_section(request):
    all_languages = TextbookLanguages.objects.all()
    context = {
        "all_languages":all_languages,
    }
    return render(request, "base/textbook_language_section.html", context=context)

def class_categories(request, language):
    language = TextbookLanguages.objects.filter(name=language)[0]
    all_categories = TextbooksCategories.objects.filter(language_associated=language)
    
    context = {
        "all_categories":all_categories,
    }

    return render(request, "base/class_categories.html", context=context)


def education(request, category_id):
    active_category = ""
    if category_id==0:
        category = EducationCategory.objects.filter(default=True)
    else:
        category = EducationCategory.objects.filter(id=category_id)
    
    if category:
        all_post = Education.objects.filter(category=category[0])
        active_category = category[0]
    else:
        all_post = None

    all_categories = EducationCategory.objects.all()

    context = {
        'all_post':all_post,
        'active_category':active_category,
        'all_categories':all_categories,
    }
    
    return render(request, "base/education.html", context=context)

def education_post(request, post_id):
    post = Education.objects.get(id=post_id)

    context = {
        'post':post,
    }

    return render(request, 'base/education_post.html', context)

def culture(request, category_id):
    active_category = ""
    if category_id==0:
        category = CultureCategory.objects.filter(default=True)
    else:
        category = CultureCategory.objects.filter(id=category_id)
    
    if category:
        all_post = Culture.objects.filter(category=category[0])
        active_category = category[0]
    else:
        all_post = None

    all_categories = CultureCategory.objects.all()

    context = {
        'all_post':all_post,
        'active_category':active_category,
        'all_categories':all_categories,
    }
    
    return render(request, "base/education.html", context=context)

def culture_post(request, post_id):
    post = Culture.objects.get(id=post_id)

    context = {
        'post':post,
    }

    return render(request, 'base/education_post.html', context)

@csrf_exempt
def create_payment_intent(request):

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # Create a PaymentIntent with the order amount and currency
            intent = stripe.PaymentIntent.create(
                # {'amount': '2342300', 'stripe_publishable_key': 'pk_test_TYooMQauvdEDq54NiTphI7jx', 'description': '1 items (£23,423.00)', 'shop_name': 'ANDAAL'}
                amount=1000,
                # stripe_publishable_key=data['stripe_publishable_key'],
                # description=data['description'],
                # shop_name=data['shop_name'],
                currency='usd',
                # In the latest version of the API, specifying the `automatic_payment_methods` parameter is optional because Stripe enables its functionality by default.
                automatic_payment_methods={
                    'enabled': True,
                },
            )
            return JsonResponse({
                'clientSecret': intent['client_secret']
            })

        except Exception as e:
            return JsonResponse(error=str(e)), 403


@csrf_exempt
def stripedot(request):
    print(request)

    # check_payment_intent = stripe.PaymentIntent.retrieve(request.GET.get('payment_intent'))
    # print(check_payment_intent.amount_received)

    # print(sd)
    return JsonResponse("true")
    # if request.method == 'POST':
    #     try:
    #         data = json.loads(request.body)
    #         # Create a PaymentIntent with the order amount and currency
    #         intent = stripe.PaymentIntent.create(
    #             # {'amount': '2342300', 'stripe_publishable_key': 'pk_test_TYooMQauvdEDq54NiTphI7jx', 'description': '1 items (£23,423.00)', 'shop_name': 'ANDAAL'}
    #             amount=data['amount'],
    #             # stripe_publishable_key=data['stripe_publishable_key'],
    #             # description=data['description'],
    #             # shop_name=data['shop_name'],
    #             currency='usd',
    #             # In the latest version of the API, specifying the `automatic_payment_methods` parameter is optional because Stripe enables its functionality by default.
    #             automatic_payment_methods={
    #                 'enabled': True,
    #             },
    #         )
    #         return JsonResponse({
    #             'clientSecret': intent['client_secret']
    #         })

    #     except Exception as e:
    #         return JsonResponse(error=str(e)), 403


def after_registration(request):
    return render(request, 'base/after_registration.html')

def verify_my_email(request, email, username):
    final_str = ''
    # try:
    user = User.objects.get(email=email, username=username)
    user.is_active = True
    user.save()
    auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
    final_str = 'Congrats'
    # except:
    #     final_str = 'Sorry'

    context = {
        'final_str': final_str,
    }
    return render(request, 'base/verify_my_email.html', context)

def get_euro_rate(request):
    resp = requests.get(f'http://api.exchangeratesapi.io/v1/latest?access_key={settings.EXCHANGE_RATE_API_KEY}')
    all_rates = RateOfEuro.objects.all()
    
    if all_rates.count() > 9:
        for i in all_rates[9:]:
            i.delete()

    if resp.status_code == 200:
        print("RUN")
        RateOfEuro.objects.create(base="EUR", xaf_to_euro=float(1/float(resp.json()['rates'][f'{settings.OSCAR_DEFAULT_CURRENCY}'])))

    return JsonResponse(resp.json())

def stagehomepage(request):

    return render(request, 'base/stagehomepage.html')