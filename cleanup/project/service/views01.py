from django.shortcuts import render
import re
from .models import CategoryServices,Services,ChooseServices
from django.db.models import F, Sum
from django.http import HttpResponse
from django.views import View
from django.conf import settings
from django.core.mail import EmailMessage


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
            
            
            
             
            ## if field is blank below is show in form #####
            if not firstname:
                return render(request,"home06.html",{"err":"This is a required field","firstnameerr":"on"})
            
            if not lastname:
                return render(request,"home06.html",{"err":"This is a required field","lastnameerr":"on"})

            
            if not companyname:
                return render(request,"home06.html",{"err":"This is a required field","companynameerr":"on"})
            
            if not address:
                return render(request,"home06.html",{"err":"This is a required field","addresserr":"on"})
            
            if not email:
                return render(request,"home06.html",{"err":"This is a required field","emailerr":"on"})
            
            if not phonenumber:
                return render(request,"home06.html",{"err":"This is a required field","phonenumbererr":"on"})
            
            if not date:
                return render(request,"home06.html",{"err":"This is a required field","dateerr":"on"})
            
            if not time:
                return render(request,"home06.html",{"err":"This is a required field","timeerr":"on"})
            ## check for check box
            services = [
                residential, bond, lease, vacate, moveout,
                exit, movein, comind, oven, rental
            ]

            if all(s is None for s in services):
                return render(request, "home06.html", {
                    "errcheckbox": "Please choose the services you need from the options above.",
                    "checkchosse": "on"
                })

            ### check for valid name input by user.using pattern regex
            
            ### check for string a to z
            if re.match(textpattern,firstname) is None:
                return render(request,"home06.html",{"err":"Invalid format.","firstnameerr":"on"})
            
            if middlename != "":
                if   re.match(textpattern,middlename) is None:
                    return render(request,"home05.html",{"err":"Invalid format.","middlenameerr":"on"})
            
            if   re.match(textpattern,lastname) is None :
                return render(request,"home06.html",{"err":"Invalid format.","lastnameerr":"on"})
            
            if   re.match(textpattern,companyname) is None:
                return render(request,"home06.html",{"err":"Invalid format.","companynameerr":"on"})

            ### check for number  0 to 9
            
            if   re.match(numberpattern,phonenumber) is None:
                return render(request,"home06.html",{"err":"Invalid format.","phonenumbererr":"on"})

            ### check for email address 
            if   re.match(patternmail,email) is None:
                return render(request,"home06.html",{"err":"Invalid email format.","emailerr":"on"})
            
        
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
                    
                
                servicechuser=[] 
                total_price = ChooseServices.objects.filter(
                    chebook_id_id=bookid.book_id
                ).annotate(
                    price=F("cheservices_id__services_price")
                ).aggregate(
                    total=Sum("price")
                )["total"]
                
                allservice= ChooseServices.objects.filter(
                    chebook_id_id=bookid.book_id
                ).annotate(
                    price=F("cheservices_id__services_price"))

                            
                for s in allservice:
                    servicechuser.append({s.cheservices_id_id: s.price})
                    

       

                return render(request,"home06.html",{"success":"on","totalprice":total_price,"userservice":servicechuser})







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
                    
                
                servicechuser=[] 
                total_price = ChooseServices.objects.filter(
                    chebook_id_id=bookid.book_id
                ).annotate(
                    price=F("cheservices_id__services_price")
                ).aggregate(
                    total=Sum("price")
                )["total"]
                
                allservice= ChooseServices.objects.filter(
                    chebook_id_id=bookid.book_id
                ).annotate(
                    price=F("cheservices_id__services_price"))

                            
                for s in allservice:
                    servicechuser.append({s.cheservices_id_id: s.price})
                    

       

                return render(request,"home06.html",{"success":"on","totalprice":total_price,"userservice":servicechuser})
   
   
   
   
   
   
   
class Mail(View):
    def post(self, request):
        email = EmailMessage(
            subject="Cleaning Services",
            body="Hello, this is a test email!",
            from_email=settings.EMAIL_HOST_USER,
            to=["tryuse34@gmail.com"]  # replace with actual recipient
        )
        try:
            email.send()
            return HttpResponse("Email sent successfully!")
        except Exception as e:
            return HttpResponse(f"Error sending email: {e}")
            
            
            

                   