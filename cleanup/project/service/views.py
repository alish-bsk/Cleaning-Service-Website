from django.shortcuts import render
import re
from .models import CategoryServices,Services,ChooseServices
from django.db.models import F, Sum
from django.http import HttpResponse
from django.views import View
from django.conf import settings
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.http import JsonResponse



# Create your views here.
class ServicesChoose(View):
    def get(self, request):
        return render(request, "home05.html")

    
    def post(self,request):
        if request.method=="POST":
            ## Request send from book form
            firstname=request.POST.get("firstname")
            middlename=request.POST.get("middlename")
            lastname=request.POST.get("lastname")
            companyname=request.POST.get("comhousname")
            address=request.POST.get("address")
            email=request.POST.get("email")

            phonenumber=request.POST.get("phonenumber")
            date=request.POST.get("date")
            time=request.POST.get("time")
            
            ## Request send from check box
            
            residential=request.POST.get("residential")
            bond=request.POST.get("bond")
            lease=request.POST.get("lease")

            vacate=request.POST.get("vacate")
            moveout=request.POST.get("moveout")
            exit=request.POST.get("exit")
            movein=request.POST.get("movein")
            comind=request.POST.get("comind")
            oven=request.POST.get("oven")
            rental=request.POST.get("rental")

            
            ## patten decalre for input field ####
            textpattern= r'^[a-z]'
            numberpattern=r'^[0-9]'
            patternmail = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}$'
            
            errors = {}

            
             
            ## if field is blank below is show in form #####
            if not firstname:
                errors["first_name"] = "First Name is required"
             
            # check for middle name field
            if not lastname:
                errors["last_name"] = "Last Name is required"

            # check for company name field
            if not companyname:
                errors["company_name"] = "Company Name is required"
                
            # check for address field
            if not address:
                errors["address"] = "Address is required"
                
            # check for email field
            if not email:
                errors["email"] = "Email is required"
            
            # check for phone number field
            if not phonenumber:
                errors["phonenumber"] = "Phone Number is required"
                
           # check for date field 
            if not date:
                errors["date"] = "Date is required"
           
            #check for time field
            if not time:
                errors["time"] = "Time is required"
            ## check for check box
            services = [
                residential, bond, lease, vacate, moveout,
                exit, movein, comind, oven, rental
            ]

            if all(s is None for s in services):
                errors["service"] = "Please choose the services you need from the options above"


            ### check for valid name input by user.using pattern regex
            
            ### check for string a to z
            if firstname:
                if re.match(textpattern,firstname) is None:
                    errors["first_name"] = "Invalid format."
                
### check for middle name if it is not empty            
            if middlename != "":
                # check for string a to z
                if   re.match(textpattern,middlename) is None:
                    errors["middle_name"] = "Invalid format."
                    
           ### check for string a to z 
            if lastname:
                if   re.match(textpattern,lastname) is None :
                    errors["last_name"] = "Invalid format."
                
            ### check for company name
            if companyname:
                if   re.match(textpattern,companyname) is None:
                    errors["company_name"] = "Invalid format."

            ### check for number  0 to 9
            
            if phonenumber:
                if len(phonenumber) < 10:
                    errors["phonenumber"] = "10 digits required."

            ### check for email address 
            if email:
                if   re.match(patternmail,email) is None:
                    errors["email"] = "Invalid email format."
            if errors:
                return JsonResponse({"errors": errors}, status=400)

        
         ### it insert data if middlename is not empty
            else:
                if middlename != "":   
                    ### it insert data in Services table
                    #serverchoose=Services(first_name=firstname,middle_name=middlename,last_name=lastname,company_name=companyname,phonenumber=phonenumber,email=email,address=address,date=date,time=time,start='No',finish='No',remove='No')
                    #serverchoose.save()
                    
                    
                    ### it insert data in ChooseServices database
            
                    servicelist=[]
                    
                    # Append service IDs based on selected checkboxes
                    if residential == "on" :
                        servicelist.append(1)
                    if bond == "on":
                        servicelist.append(2)
                        
                    if lease == "on":
                        servicelist.append(3)
                    if vacate == "on":
                        servicelist.append(4)
                        
                    if moveout == "on":
                        servicelist.append(5)
                        
                    if exit == "on" :
                        servicelist.append(6)
                    
                    if movein == "on":
                        servicelist.append(7)
                    if rental=="on":
                        servicelist.append(8)
                    
                    if comind == "on":
                        servicelist.append(9)

                    if oven == "on":
                        servicelist.append(10)
                        

                    
                        
                    
                    servicechuser=[] 
                    total_price = CategoryServices.objects.filter( services_id__in=servicelist ).aggregate( total=Sum("services_price") )["total"]
                    
                    allservice=CategoryServices.objects.filter(
                        services_id__in=servicelist
                        ).annotate(
                            price=F("services_price")   
                            )


                                
                    for s in allservice:
                        servicechuser.append({s.services_id: s.services_price})
                    request.session["form_data"] = {
                        # User info
                        "firstname": request.POST.get("firstname"),
                        "middlename": request.POST.get("middlename"),
                        "lastname": request.POST.get("lastname"),
                        "companyname": request.POST.get("comhousname"),
                        "address": request.POST.get("address"),
                        "email": request.POST.get("email"),
                        "phonenumber": request.POST.get("phonenumber"),
                        "date": request.POST.get("date"),
                        "time": request.POST.get("time"),

                        # Services / checkboxes
                        "residential": request.POST.get("residential"),
                        "bond": request.POST.get("bond"),
                        "lease": request.POST.get("lease"),
                        "vacate": request.POST.get("vacate"),
                        "moveout": request.POST.get("moveout"),
                        "exit": request.POST.get("exit"),
                        "movein": request.POST.get("movein"),
                        "comind": request.POST.get("comind"),
                        "oven": request.POST.get("oven"),
                        "rental": request.POST.get("rental"),
                        "totalprice":total_price,

                    }
                    request.session["summary"] = {
                    "success": "on",
                    "totalprice": total_price,
                    "userservice": servicechuser,
                }
                    print(request.session["summary"]["userservice"])
                    return JsonResponse({
                        "success": True,
                        "redirect": "/home/"
                    })


        

                    #return render(request,"home06.html",{"success":"on","totalprice":total_price,"userservice":servicechuser})







        ### it insert data if middlename is  empty
            
                else:
                    ### it insert data in Services table

                    #serverchoose=Services(first_name=firstname,middle_name=None,last_name=lastname,company_name=companyname,phonenumber=phonenumber,email=email,address=address,date=date,time=time,start='No',finish='No',remove='No')
                    #serverchoose.save()

                    ### it insert data in ChooseServices database

                    servicelist=[]
                    
                    if residential == "on" :
                        servicelist.append(1)
                    if bond == "on":
                        servicelist.append(2)
                        
                    if lease == "on":
                        servicelist.append(3)
                    if vacate == "on":
                        servicelist.append(4)
                        
                    if moveout == "on":
                        servicelist.append(5)
                        
                    if exit == "on" :
                        servicelist.append(6)
                    
                    if movein == "on":
                        servicelist.append(7)
                    if rental=="on":
                        servicelist.append(8)
                    
                    if comind == "on":
                        servicelist.append(9)

                    if oven == "on":
                        servicelist.append(10)
                        

                    
                

                # bookid=Services.objects.get(first_name=firstname,middle_name=None,last_name=lastname,company_name=companyname,phonenumber=phonenumber,email=email,address=address,date=date,time=time)
                    #for i in range(len(servicelist)):
                        #chooserv=ChooseServices(chebook_id_id=bookid.book_id,cheservices_id_id=servicelist[i])
                        #chooserv.save()
                        
                    
                    servicechuser=[] 
                    total_price = CategoryServices.objects.filter( services_id__in=servicelist ).aggregate( total=Sum("services_price") )["total"]
                    
                    allservice=CategoryServices.objects.filter(
                        services_id__in=servicelist
                        ).annotate(
                            price=F("services_price")   
                            )


                                
                    for s in allservice:
                        servicechuser.append({s.services_id: s.services_price})
                        
                    request.session["form_data"] = {
                        # User info
                        "firstname": request.POST.get("firstname"),
                        "middlename": request.POST.get("middlename"),
                        "lastname": request.POST.get("lastname"),
                        "companyname": request.POST.get("comhousname"),
                        "address": request.POST.get("address"),
                        "email": request.POST.get("email"),
                        "phonenumber": request.POST.get("phonenumber"),
                        "date": request.POST.get("date"),
                        "time": request.POST.get("time"),

                        # Services / checkboxes
                        "residential": request.POST.get("residential"),
                        "bond": request.POST.get("bond"),
                        "lease": request.POST.get("lease"),
                        "vacate": request.POST.get("vacate"),
                        "moveout": request.POST.get("moveout"),
                        "exit": request.POST.get("exit"),
                        "movein": request.POST.get("movein"),
                        "comind": request.POST.get("comind"),
                        "oven": request.POST.get("oven"),
                        "rental": request.POST.get("rental"),
                        "totalprice":total_price,

                    }
    

        

                    return render(request,"home06.html",{"success":"on","totalprice":total_price,"userservice":servicechuser})
                ## return JsonResponse({
                        ##"success": "on",
                        ##"totalprice": total_price,
                        ##"userservice": servicechuser,
                        ##"message": "Booking successful"
                    ##})

   
   
   
   
   
   
            
            
            



# Create your views here.
class ServicesSaves(View):
    def get(self, request):
        return render(request, "home05.html")

    
    def post(self,request):
        ## Request send from book form
        form_data = request.session.get("form_data", {})
        firstname = form_data.get("firstname", "")
        middlename=form_data.get("middlename", "")
        lastname=form_data.get("lastname", "")
        companyname=form_data.get("companyname", "")
        address=form_data.get("address", "") 
        email=form_data.get("email", "")

        phonenumber=form_data.get("phonenumber", "")
        date=form_data.get("date", "")
        time=form_data.get("time", "")
        
        ## Request send from check box

        residential=form_data.get("residential", "")
        bond=form_data.get("bond", "")
        lease=form_data.get("lease", "")

        vacate=form_data.get("vacate", "")
        moveout=form_data.get("moveout", "")
        exit=form_data.get("exit", "")
        movein=form_data.get("movein", "")
        comind=form_data.get("comind", "")
        oven=form_data.get("oven", "")
        rental=form_data.get("rental", "")

        
        ## patten decalre for input field ####
        textpattern= r'^[a-z]'
        numberpattern=r'^[0-9]'
        patternmail = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}$'
            
            
            
             
                  
    
        ### it insert data if middlename is not empty

        if middlename != "":   
            ### it insert data in Services table
            serverchoose=Services(first_name=firstname,middle_name=middlename,last_name=lastname,company_name=companyname,phonenumber=phonenumber,email=email,address=address,date=date,time=time,start='No',finish='No',remove='No')
            serverchoose.save()
            
            
            ### it insert data in ChooseServices database
        
            servicelist=[]
        
            if residential == "on" :
                servicelist.append(1)
            if bond == "on":
                servicelist.append(2)
                
            if lease == "on":
                servicelist.append(3)
            if vacate == "on":
                servicelist.append(4)
                
            if moveout == "on":
                servicelist.append(5)
                
            if exit == "on" :
                servicelist.append(6)
            
            if movein == "on":
                servicelist.append(7)
            if rental=="on":
                servicelist.append(8)
            
            if comind == "on":
                servicelist.append(9)

            if oven == "on":
                servicelist.append(10)
                

            
            bookid=Services.objects.get(first_name=firstname,middle_name=middlename,last_name=lastname,company_name=companyname,phonenumber=phonenumber,email=email,address=address,date=date,time=time)
            for i in range(len(servicelist)):
                chooserv=ChooseServices(chebook_id_id=bookid.book_id,cheservices_id_id=servicelist[i])
                chooserv.save()
            
            







    ### it insert data if middlename is  empty
           
        else:
            ### it insert data in Services table

            serverchoose=Services(first_name=firstname,middle_name=None,last_name=lastname,company_name=companyname,phonenumber=phonenumber,email=email,address=address,date=date,time=time,start='No',finish='No',remove='No')
            serverchoose.save()

            ### it insert data in ChooseServices database

            servicelist=[]
            
            if residential == "on" :
                servicelist.append(1)
            if bond == "on":
                servicelist.append(2)
                
            if lease == "on":
                servicelist.append(3)
            if vacate == "on":
                servicelist.append(4)
                
            if moveout == "on":
                servicelist.append(5)
                
            if exit == "on" :
                servicelist.append(6)
            
            if movein == "on":
                servicelist.append(7)
            if rental=="on":
                servicelist.append(8)
            
            if comind == "on":
                servicelist.append(9)

            if oven == "on":
                servicelist.append(10)
                

            
            

            bookid=Services.objects.get(first_name=firstname,middle_name=None,last_name=lastname,company_name=companyname,phonenumber=phonenumber,email=email,address=address,date=date,time=time)
            for i in range(len(servicelist)):
                chooserv=ChooseServices(chebook_id_id=bookid.book_id,cheservices_id_id=servicelist[i])
                chooserv.save()
               

    

   
   
   
   
   
   
   
class Mail(View):
    def post(self, request):
        form_data = request.session.get("form_data", {})
        listservicename = []

        # Map of session keys to service names
        services = {
            "residential": "Residential Cleaning Service",
            "bond": "Bond Cleaning Service",
            "lease": "Lease Cleaning Service",
            "vacate": "Vacate Cleaning Service",
            "moveout": "Move Out Cleaning Service",
            "exit": "Exit Cleaning Service",
            "movein": "Move In Cleaning Service",
            "rental": "Rental Cleaning Service",
            "comind": "Commercial & Industrial Cleaning Service",
            "oven": "Oven Cleaning Service",
        }

        for key, name in services.items():
            if form_data.get(key) is not None:
                listservicename.append(name)

        mailto = form_data.get("email")
        companyname = form_data.get("companyname", "Our Company")
        scheduled_date = form_data.get("date", "N/A")
        scheduled_time = form_data.get("time", "N/A")
        total_price = form_data.get("totalprice", "0.00")

        # Use f-string for dynamic content
        body = f"""
Dear Customer,

Thank you for choosing {companyname} for your cleaning needs. We are delighted to confirm your booking and appreciate the trust you’ve placed in us.

Here are the details of your order:
Services Selected: {', '.join(listservicename)}
Scheduled Date & Time: {scheduled_date} at {scheduled_time}
Total Price: AUD$ {total_price}

Our team will arrive as scheduled and ensure that your property is cleaned with the highest level of care and professionalism.

If you have any special instructions or additional requests, please feel free to reply to this email or contact us.

We look forward to serving you and making your space shine!

Best regards,
{companyname}
        """

        email = EmailMessage(
            subject="Vacate Cleaners.Pvt.Ltd Cleaning Services",
            body=body,
            from_email=settings.EMAIL_HOST_USER,
            to=[mailto],
        )

        try:
            email.send()
            # Clear session data
            request.session.pop("form_data", None)
            return HttpResponse("Email sent successfully!")
        except Exception as e:
            return HttpResponse(f"Error sending email: {e}")
                                   