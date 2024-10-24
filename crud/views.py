from django.shortcuts import (
     get_object_or_404, render, HttpResponseRedirect, redirect)
from crud.models import  CrudModel
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,authenticate,login
from .forms import NewUserForm, CrudForm, CrudUpdate 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 



def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("/")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})
   
def index(request):
    crud_items = CrudModel.objects.all()
    context = {'crud_items': crud_items}
    return render(request, 'index.html', context)     

def logout_crud(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect('/')
from datetime import datetime  
def detail(request, id):
    crud_item = CrudModel.objects.get(id = id) 
    for x in crud_item.updated_date:
        #x = datetime.strptime(x, '%Y-%m-%dT%H:%M:%S%z')
        print(x)
    zipped = zip(reversed(crud_item.update_description),
                reversed(crud_item.update_location),
                reversed(crud_item.update_machine),
                reversed(crud_item.update_network),
                reversed(crud_item.update_ip),
                reversed(crud_item.update_hostname),
                reversed(crud_item.update_IPAddr),
                reversed(crud_item.update_ipconf),
                reversed(crud_item.update_ram_memory),
                reversed(crud_item.update_ram_used),
                reversed(crud_item.updated_date),
                )
    context = {'crud_item': crud_item, 'zipped': zipped}
    
    return render(request, "detail.html", context)

@login_required(login_url='login')
def create(request):
    form = CrudForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    context = { 'form': form  }
    return render(request, "create.html", context)


@login_required(login_url='login')
def update(request,id):
    obj = get_object_or_404(CrudModel, id =id)
    form = CrudUpdate(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    context = { 'form': form, 'obj': obj }
    return render(request, "update.html", context)
  
@login_required(login_url='login')
def delete(request, id):
    obj = get_object_or_404(CrudModel, id = id)
    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("/")
    return render(request, "delete.html")
 
