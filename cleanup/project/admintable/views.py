from django.shortcuts import render
from django.views import View
from rest_framework import pagination
from service.models import CategoryServices,Services,ChooseServices
from django.core.paginator import Paginator
from django.db.models import F, Sum
from django.shortcuts import redirect

class Admintable(View):
    # GET method for displaying the admin table
    def get(self,request):

        services = Services.objects.all().order_by('book_id')

        paginator = Paginator(services, 100)   # 100 per page

        allcount=len(services)
        pagenum=int(allcount/100)+1

        

        if request.session.get('pagenum', '') == '':
            page_obj = paginator.get_page(1)

        else:
            page_obj = paginator.get_page(request.session['pagenum'])

            

        totalprice=[] 
        checkservice=[]
        num = allcount/100
        
        for i in page_obj:
            bookid=Services.objects.get(book_id=i.book_id)
            

            total_price = ChooseServices.objects.filter(
            chebook_id_id=bookid.book_id
        ).annotate(
            price=F("cheservices_id__services_price")
        ).aggregate(
            total=Sum("price")
        )["total"]
            list=[{"id" :bookid.book_id,"total":total_price}]
            totalprice.append(list)
        

            allservice= ChooseServices.objects.filter(
            chebook_id_id=bookid.book_id
        ).annotate(
            price=F("cheservices_id__services_price")).values("chebook_id_id", "cheservices_id_id", "price")
            for s in allservice:
                list=[{"id":s["chebook_id_id"],"serviceid":s["cheservices_id_id"],"price": s["price"]}]
                checkservice.append(list)

        listnum=len(checkservice)
        
        m=1
        mone=0
        mtwo=0
        ##categoryservice=10
        for i in page_obj:        
            for j in range(0,10):
                for c in range(0,len(checkservice)):
                    #print(f"{i.book_id},{j+1}")
                    if  checkservice[c][0]['id'] == i.book_id and checkservice[c][0]['serviceid'] == j+1 :
                        mone=0
                        mtwo=0
                        break
                    else:
                        mone=i.book_id
                        mtwo=j+1
                        
                if  mone !=0 and mtwo !=0 :
                    list=[{"id":mone,"serviceid":mtwo,"price":0}]
                    checkservice.append(list)
                    mone =0
                    mtwo =0 



        
        sorted_data = sorted(checkservice, key=lambda x: (x[0]["id"], x[0]["serviceid"]))  

        return render(request, "admintable01.html", {"page": page_obj,"userdata":sorted_data,"total":totalprice,"pagenum":range(1,pagenum+1)})
      
# POST method for handling form submissions
    def post(self,request):
        page = request.POST.get('page')  # gets the value of the clicked button
        start = request.POST.get('start')  # gets the value of the clicked button
        finish = request.POST.get('finish')  # gets the value of the clicked button
        remove = request.POST.get('remove')  # gets the value of the clicked button
       # print("page number is " + str(start))
        
        
        
        if remove is not None:
            catsevices=ChooseServices.objects.filter(chebook_id_id=int(remove))
            for i in catsevices:
                i.delete()

            services = Services.objects.get(book_id=int(remove))
            services.delete()


        if page is not None:
            request.session['pagenum'] = int(page)  
            print( request.session['pagenum'])          


        services = Services.objects.all().order_by('book_id')
        allcount=len(services)


        paginator = Paginator(services, 100)   # 100 per page

        pagenum=int(allcount/100)+1
        ### for color change of start ###

        if start is not None:
            servicesstart = Services.objects.get(book_id=start)
            if servicesstart.start == 'No':
                services = Services.objects.get(book_id=int(start))
                services.start = "Yes"
                services.save() 
                #if request.session['pagenum'] is None:
                   # page=1
                ##else:
                    #page=int(request.session['pagenum'])
                return redirect('admintable')

                    
            else:
                services = Services.objects.get(book_id=int(start))
                services.start = "No"
                services.save() 
                #if request.session['pagenum']  is None:
                    #page=1
                #else:
                    #page=int(request.session['pagenum'])
                return redirect('admintable')            
            
        if finish is not None:
            servicesfinish = Services.objects.get(book_id=finish)
            ## for color change finish ##

            if servicesfinish.finish == 'No':
                services = Services.objects.get(book_id=int(finish))
                services.finish = "Yes"
                services.save() 
                #if request.session['pagenum']  is None:
                    #page=1
                #else:
                    #page=request.session['pagenum']                
                return redirect(request.path) # refresh page safely
            else:
                services = Services.objects.get(book_id=int(finish))
                services.finish = "No"
                services.save() 
                #if request.session['pagenum']  is None:
                    #page=1
                #else:
                   # page=request.session['pagenum'] 
                   # print(page)                  
                return redirect(request.path) # refresh page safely



        




        page_obj = paginator.get_page(page)

        
        ## for price total and price and service name
        
        

            
        totalprice=[] 
        checkservice=[]
        
        
        for i in page_obj:
            bookid=Services.objects.get(book_id=i.book_id)
            

            total_price = ChooseServices.objects.filter(
            chebook_id_id=bookid.book_id
        ).annotate(
            price=F("cheservices_id__services_price")
        ).aggregate(
            total=Sum("price")
        )["total"]
            list=[{"id" :bookid.book_id,"total":total_price}]
            totalprice.append(list)
        

            allservice= ChooseServices.objects.filter(
            chebook_id_id=bookid.book_id
        ).annotate(
            price=F("cheservices_id__services_price")).values("chebook_id_id", "cheservices_id_id", "price")
            for s in allservice:
                list=[{"id":s["chebook_id_id"],"serviceid":s["cheservices_id_id"],"price": s["price"]}]
                checkservice.append(list)

        listnum=len(checkservice)
        
        m=1
        mone=0
        mtwo=0
        ##categoryservice=10
        for i in page_obj:        
            for j in range(0,10):
                for c in range(0,len(checkservice)):
                    if  checkservice[c][0]['id'] == i.book_id and checkservice[c][0]['serviceid'] == j+1 :
                        mone=0
                        mtwo=0
                        break
                    else:
                        mone=i.book_id
                        mtwo=j+1
                        
                if  mone !=0 and mtwo !=0 :
                    list=[{"id":mone,"serviceid":mtwo,"price":0}]
                    checkservice.append(list)
                    mone =0
                    mtwo =0 



        
        sorted_data = sorted(checkservice, key=lambda x: (x[0]["id"], x[0]["serviceid"]))    
        


        return render(request, "admintable01.html", {"page": page_obj,"userdata":sorted_data,"total":totalprice,"pagenum":range(1,pagenum+1)})



