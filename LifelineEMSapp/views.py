from django.shortcuts import render

def index(request):
    
	template_name = "LifelineEMSapp/index.html"
	context={}
	
	return render(request, template_name, context)
def about(request):
    
	template_name = "LifelineEMSapp/about.html"
	context={}
	
	return render(request, template_name, context)
def login(request):
    
	template_name = "LifelineEMSapp/login.html"
	context={}
	
	return render(request, template_name, context)
def admind(request):
    
	template_name = "LifelineEMSapp/admind.html"
	context={}
	
	return render(request, template_name, context)
def student(request):
    
	template_name = "LifelineEMSapp/student.html"
	context={}
	
	return render(request, template_name, context)
def staff(request):
    
	template_name = "LifelineEMSapp/staff.html"
	context={}
	
	return render(request, template_name, context)
def cashier(request):
    
	template_name = "LifelineEMSapp/cashier.html"
	context={}
	
	return render(request, template_name, context)
def register(request):
    
	template_name = "LifelineEMSapp/register.html"
	context={}
	
	return render(request, template_name, context)