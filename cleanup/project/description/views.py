from django.shortcuts import render
import re
from django.http import HttpResponse
from django.views import View
from django.conf import settings
from django.core.mail import EmailMessage

from django.http import JsonResponse


class MailDes(View):
    def post(self, request):
        firstname = request.POST.get("first_name")
        lastname = request.POST.get("last_name")
        mailto = request.POST.get("email")
        phonenumber = request.POST.get("phone")
        inquiry = request.POST.get("inquiry_type")
        mesg = request.POST.get("message")
        textpattern= r'^[a-z]'
        numberpattern=r'^[0-9]'
        errors = {}


        # Use f-string for dynamic content
      # Use f-string for dynamic content
        if not firstname:
            errors["first_name"] = "First Name is required"
        if not lastname:
            errors["last_name"] = "Last Name is required"
        if not mailto:
            errors["email"] = "Email is required"

        if not phonenumber:
            errors["phone"] = "Phone number is required"
        if not inquiry:
            errors["inquiry_type"] = "Inquiry Type is required"
        if not mesg:
            errors["message"] = "Message is required"

        if  firstname:
            if re.match(textpattern,firstname) is None:
                errors["first_name"] = "Invalid format."
 
        if  lastname:
           
            if re.match(textpattern,lastname) is None:
                errors["last_name"] = "Invalid format."
            
        if  phonenumber:

            if len(phonenumber)<10:
                errors["phone"] = "10 digits required."

        if errors:
           return JsonResponse({"errors": errors}, status=400)
        else:
           

          
            body = f"""
            Dear {firstname} {lastname},

            Thank you for reaching out to Vacate Cleaners.Pvt.Ltd. We have received your inquiry and will get back to you shortly.

            Here are the details you submitted:
            -----------------------------------
            Name: {firstname} {lastname}
            Email: {mailto}
            Phone: {phonenumber}
            Inquiry Type: {inquiry}
            Message: {mesg}

            -----------------------------------

            Our team will review your request and respond within 4 hours during business hours.

            Best regards,
            Vacate Cleaners.Pvt.Ltd      
            """

            email = EmailMessage(
                subject="Vacate Cleaners.Pvt.Ltd Cleaning Services",
                body=body,
                from_email=settings.EMAIL_HOST_USER,
                to=['sport.app7895@gmail.com',mailto],
            )

            try:
                email.send()
                # Clear session data
                request.session.pop("form_data", None)
                errors["sendmessage"] = "Message sent to company."

                return JsonResponse({"errors": errors}, status=400)

                return HttpResponse("Email sent successfully!")
            except Exception as e:
                return HttpResponse(f"Error sending email: {e}")
                                   