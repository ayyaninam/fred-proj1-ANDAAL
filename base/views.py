from django.shortcuts import render

from django.conf import settings
from oscar.core.loading import get_model
from base.models import *
from apps.catalogue.models import Category as Oscar_Category
from django.http import JsonResponse
import json
import stripe
from django.views.decorators.csrf import csrf_exempt
from .all_currencies_avaialble import currencies as all_currencies_avaialble

stripe.api_key = settings.STRIPE_SECRET_KEY
# Create your views here.
def homepage(request):

    book_category = Oscar_Category.objects.filter(main_book_category=True)
    main_menus = MainMenu.objects.all()
    if book_category:
        book_category = book_category[0]
    else:
        book_category = None
    
    context = {
        'book_category':book_category,
        'main_menus':main_menus,
        'all_currencies_avaialble':all_currencies_avaialble,
        'default_currency':settings.OSCAR_DEFAULT_CURRENCY,
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


