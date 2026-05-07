from django.shortcuts import render

# Create your views here.

class Record:
    @staticmethod
    def home_page(request):
        return render(request,'home06.html') 
    @staticmethod
    def residential_page(request):
        return render(request,'residential01.html')          
    
    @staticmethod
    def bond_page(request):
        return render(request,'bond01.html')  
    @staticmethod
    def findlease_page(request):
        return render(request,'find of lease01.html')   
    
    @staticmethod
    def vacate_page(request):
        return render(request,'vacate01.html')    
    
    @staticmethod
    def moveout_page(request):
        return render(request,'move out01.html')    

    @staticmethod
    def exit_page(request):
        return render(request,'exit01.html')    
    @staticmethod
    def movein_page(request):
        return render(request,'move in01.html')    
    @staticmethod
    def rental_page(request):
        return render(request,'rental01.html')    
    @staticmethod
    def cominst_page(request):
        return render(request,'commercial industrial01.html')    

    @staticmethod
    def oven_page(request):
        return render(request,'oven01.html')    
   
   
    
    
                                                                         