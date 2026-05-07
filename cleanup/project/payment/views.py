import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.template.context_processors import request
from service.views import ServicesSaves, Mail

import stripe
from django.conf import settings

# Set your Stripe secret key
stripe.api_key = settings.STRIPE_SECRET_KEY
YOUR_DOMAIN = "http://localhost:8000"  # Django usually runs on port 8000

@csrf_exempt
def create_checkout_session(request):
    if request.method == "POST":
        try:
            request.session.pop("summary", None)
            checkout_session = stripe.checkout.Session.create(
                    line_items=[
                        {
                            'price_data': {
                                'currency': 'aud',
                                'product_data': {
                                    'name': 'Vacate Cleaners Service',
                                },
                                'unit_amount': int(float(request.session["form_data"]["totalprice"]) * 100),  # $50.00 → 5000 cents
                            },
                            'quantity': 1,
                        },
                    ],
                
                
                
                mode='payment',
                success_url= 'http://127.0.0.1:8000/payment/success/',
                cancel_url='http://127.0.0.1:8000/payment/cancel/',
            )
            return redirect(checkout_session.url, code=303)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request'}, status=400)


def success(request):
    servicesave=ServicesSaves()
    servicesave.post(request)
    mail=Mail()
    mail.post(request)
    return render(request, "success.html")
def payment(request):
    return render(request, "checkout.html")



def cancel(request):
    return render(request, "cancel.html")



def calculationCancel(request):
    if request.method == "POST":
        try:
            request.session.pop("summary", None)
            request.session.pop("form_data", None)

        except KeyError:
            pass
        return redirect('home')