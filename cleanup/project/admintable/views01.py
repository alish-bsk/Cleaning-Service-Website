from django.shortcuts import render
from django.views import View
from rest_framework import pagination
from service.models import CategoryServices,Services,ChooseServices
from django.core.paginator import Paginator
from django.db.models import F, Sum
from django.shortcuts import redirect

class Admintable(View):
    def get(self,request):

        services = Services.objects.all().order_by('book_id')

        paginator = Paginator(services, 100)   # 100 per page

        page_number =1
        page=1
        allcount=len(services)
        pagenum=0

        
        if request.session['pagenum'] is not None:
            page=request.session['pagenum']
            if allcount<100:
                if allcount % 100 != 0:                

                    pagenum=int(allcount/100)+1
                    start=1
                    end=allcount

            
                else:
                        pagenum=allcount/100
                        start=1
                        end=allcount
                
            if int(page)*100==100:
                if allcount % 100 != 0:
                    pagenum=int(allcount/100)+1
                    start=1
                    end=int(page)*100
                else:
                    pagenum=allcount/100
                    start=1
                    end=int(page)*100
                    print(end)

            if int(page)*100 >100:
                if allcount % 100 != 0:                
                    pagenum=int(allcount/100)+1
                    start=(((int(page)*100)-100)+1)
                    end=int(page)*100

                    
                else:
                    pagenum=allcount/100
                    start=(((int(page)*100)-100)+1)
                    end=int(page)*100

        

        else:
            ##services = Services.objects.all().annotate(price="book_id__servicprice")
            if allcount<=100:
                pagenum=1
                start=1
                end=allcount

                

                

            if allcount>100:
                if allcount % 100 != 0:                
                    pagenum=int(allcount/100)+1
                    start=1
                    end=100

                else:
                    pagenum=int(allcount/100)
                    start=1
                    end=100
        

        if request.session['pagenum'] is not None:
            page_obj = paginator.get_page(page)
        else:
            page_obj = paginator.get_page(1)

            
        print(f" 'ss': {request.session['pagenum']}")

        totalprice=[] 
        checkservice=[]
        num = allcount/100
       ## while num <=allcount/100:
        if allcount<=100:
            for i in range(start,end+1):
                bookid=Services.objects.get(book_id=i)

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
                    ##print(list)
            listnum=len(checkservice)
            print(listnum)
            m=1
            mone=0
            mtwo=0
            ##categoryservice=10
            for i in range(start,end+1):        
                for j in range(0,end):
                    for c in range(0,len(checkservice)):
                        if  checkservice[c][0]['id'] == i and checkservice[c][0]['serviceid'] == m :
                            mone=0
                            mtwo=0
                            break
                        else:
                            mone=i
                            mtwo=m
                            
                    if  mone !=0 and mtwo !=0 :
                        list=[{"id":mone,"serviceid":mtwo,"price":0}]
                        checkservice.append(list)
                        mone =0
                        mtwo =0 

                    m=m+1
                    if m==11:
                        m=1   
                    

            
            sorted_data = sorted(checkservice, key=lambda x: (x[0]["id"], x[0]["serviceid"]))        
            ##print(sorted_data)
            
        else:
            for i in range(start,end+1):
                bookid=Services.objects.get(book_id=i)

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
                    ##print(list)
                if allcount==i:
                    break

            listnum=len(checkservice)
            
           ## print(listnum)
            m=1
            mone=0
            mtwo=0
            ##categoryservice=10
            for i in range(start,end+1):        
                for j in range(0,end):
                    for c in range(0,len(checkservice)):
                        if  checkservice[c][0]['id'] == i and checkservice[c][0]['serviceid'] == m :
                            mone=0
                            mtwo=0
                            break
                        else:
                            mone=i
                            mtwo=m
                            
                    if  mone !=0 and mtwo !=0 :
                        list=[{"id":mone,"serviceid":mtwo,"price":0}]
                        checkservice.append(list)
                        mone =0
                        mtwo =0 

                    m=m+1
                    if m==11:
                        m=1   

                if allcount == i:
                    break  

            
            sorted_data = sorted(checkservice, key=lambda x: (x[0]["id"], x[0]["serviceid"]))        
            ##print(sorted_data)
              
            
   
    
                    
            ##if i*100 ==allcount:
               ## break
            ##num += 0.01
            ##start=end
            ##end=end+100
        
        print(page_obj)

        return render(request, "admintable01.html", {"page": page_obj,"userdata":sorted_data,"total":totalprice,"pagenum":range(1,pagenum+1)})
      

    def post(self,request):
        page = request.POST.get('page')  # gets the value of the clicked button
        start = request.POST.get('start')  # gets the value of the clicked button
        finish = request.POST.get('finish')  # gets the value of the clicked button
        remove = request.POST.get('remove')  # gets the value of the clicked button
        
        
        
        if remove is not None:
            catsevices=ChooseServices.objects.get(chebook_id_id=id(remove))
            catsevices.delete()

            services = Services.objects.get(book_id=int(remove))
            services.delete()

            


        if page is not None:
            request.session['pagenum'] = int(page)  
            print( request.session['pagenum'])          
        ##page = request.POST.get('page')  # gets the value of the clicked button


        services = Services.objects.all().order_by('book_id')
        allcount=len(services)


        paginator = Paginator(services, 100)   # 100 per page

        page_number =1  
        ### for color change of start ###

        if start is not None:
            servicesstart = Services.objects.get(book_id=start)
            if servicesstart.start == 'No':
                services = Services.objects.get(book_id=int(start))
                services.start = "Yes"
                services.save() 
                if request.session['pagenum'] is None:
                    page=1
                else:
                    page=int(request.session['pagenum'])
                return redirect('admintable')

                    
            else:
                services = Services.objects.get(book_id=int(start))
                services.start = "No"
                services.save() 
                if request.session['pagenum']  is None:
                    page=1
                else:
                    page=int(request.session['pagenum'])
                return redirect('admintable')            
            
        if finish is not None:
            servicesfinish = Services.objects.get(book_id=finish)
            ## for color change finish ##

            if servicesfinish.finish == 'No':
                services = Services.objects.get(book_id=int(finish))
                services.finish = "Yes"
                services.save() 
                if request.session['pagenum']  is None:
                    page=1
                else:
                    page=request.session['pagenum']                
                return redirect(request.path) # refresh page safely
            else:
                services = Services.objects.get(book_id=int(finish))
                services.finish = "No"
                services.save() 
                if request.session['pagenum']  is None:
                    page=1
                else:
                    page=request.session['pagenum'] 
                    print(page)                  
                return redirect(request.path) # refresh page safely



        




        page_obj = paginator.get_page(page)

        
        ## for price total and price and service name
        
        
        ##services = Services.objects.all().annotate(price="book_id__servicprice")

            
        pagenum=0
        if allcount<100:
            if allcount % 100 != 0:                

                pagenum=int(allcount/100)+1
                start=1
                end=allcount

        
            else:
                    pagenum=allcount/100
                    start=1
                    end=allcount
            
        if int(page)*100==100:
            if allcount % 100 != 0:
                pagenum=int(allcount/100)+1
                start=1
                end=int(page)*100
            else:
                pagenum=allcount/100
                start=1
                end=int(page)*100
                print(end)

            

        if int(page)*100 >100:
            if allcount % 100 != 0:                
                pagenum=int(allcount/100)+1
                start=(((int(page)*100)-100)+1)
                end=int(page)*100

                
            else:

                pagenum=allcount/100
                start=(((int(page)*100)-100)+1)
                end=int(page)*100


            

        totalprice=[] 
        checkservice=[]
        num = allcount/100
       ## while num <=allcount/100:
        if int(page)*100<=100:
            for i in range(start,end+1):
                bookid=Services.objects.get(book_id=i)

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
                    ##print(list)
                if allcount == i:
                    break  
                    
  ########## next program for  arrange service price in admitable and checkservice keep zero in missing price of service #####        
            listnum=len(checkservice)
            print(listnum)
            m=1
            mone=0
            mtwo=0
            ##categoryservice=10
            for i in range(start,end+1):        
                for j in range(0,end):
                    for c in range(0,len(checkservice)):
                        if  checkservice[c][0]['id'] == i and checkservice[c][0]['serviceid'] == m :
                            mone=0
                            mtwo=0
                            break
                        else:
                            mone=i
                            mtwo=m
                            
                    if  mone !=0 and mtwo !=0 :
                        list=[{"id":mone,"serviceid":mtwo,"price":0}]
                        checkservice.append(list)
                        mone =0
                        mtwo =0 

                    m=m+1
                    if m==11:
                        m=1   

            
            sorted_data = sorted(checkservice, key=lambda x: (x[0]["id"], x[0]["serviceid"]))        

            
        else:
            for i in range(start,end+1):
                bookid=Services.objects.get(book_id=i)

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
                    ##print(list)
                    
                if allcount==i:
                    break
            listnum=len(checkservice)
            print(listnum)
            m=1
            mone=0
            mtwo=0
            ##categoryservice=10
            for i in range(start,end+1):        
                for j in range(0,end):
                    for c in range(0,len(checkservice)):
                        if  checkservice[c][0]['id'] == i and checkservice[c][0]['serviceid'] == m :
                            mone=0
                            mtwo=0
                            break
                        else:
                            mone=i
                            mtwo=m
                            
                    if  mone !=0 and mtwo !=0 :
                        list=[{"id":mone,"serviceid":mtwo,"price":0}]
                        checkservice.append(list)
                        mone =0
                        mtwo =0 

                    m=m+1
                    if m==11:
                        m=1 
                if allcount == i:
                    break  

            
            sorted_data = sorted(checkservice, key=lambda x: (x[0]["id"], x[0]["serviceid"]))        
           ## print(totalprice)
              
            
   
    
                    
            ##if i*100 ==allcount:
               ## break
            ##num += 0.01
            ##start=end
            ##end=end+100
        


        return render(request, "admintable01.html", {"page": page_obj,"userdata":sorted_data,"total":totalprice,"pagenum":range(1,pagenum+1)})
