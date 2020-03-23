from django.shortcuts import render,get_object_or_404, redirect
#from userModule.models import Kitchen
from serviceProviderApp.models import Kitchen2Register,menuItem
from cart.forms import CartAddProductForm
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from userModule.forms import RegularUserCreation

# Create your views here.
def kitchen_list(request):
    #category = None
    #categories = Category.objects.all()
    k = Kitchen2Register.objects.all() #filter(available=True)
    #if category_slug:
    #    category = get_object_or_404(Category, slug=category_slug)
    #    products = products.filter(category=category)
    #return render(request, 'userModule/kitchen_list.html', {'category': category,'categories': categories,'products': products})
    return render(request, 'userModule/kitchen_list.html',{'kitchens':k})

#def kitchen_detail(request, id, slug):
def kitchen_detail(request, id):
    #product = get_object_or_404(Product, id=id, slug=slug, available=True)
    kitchen = get_object_or_404(Kitchen2Register, id=id)
    #for t in kitchen.menu.all():
    #    print(t.id)
    cart_product_form = CartAddProductForm()
    #return render(request,'shop/product/detail.html',{'product': kitchen,'cart_product_form': cart_product_form})
    return render(request, 'userModule/kitchen_detail.html', {'kitchen': kitchen, 'cart_product_form': cart_product_form})
    #return render(request, 'userModule/kitchen_detail.html', {'product': kitchen})

#def createMenuItem(request,id):
#    k=Kitchen2Register.objects.get(id)
#    m=k.menu_set.create()

class createMenuItem(CreateView):
    #model=Kitchen2Register
    model=menuItem
    fields=['name','veg','price']
    template_name = 'userModule/create_menuItem.html'
    success_url = '..'

@login_required
def logout(request):
    logout(request)
    return redirect('myApp:index')

def signup(request):
    if request.method == "POST":
        form = RegularUserCreation(request.POST)
        if form.is_valid():
            form.save()
            # form.instance.username
            username = form.cleaned_data.get('username')
            raw_password = form.clean_password2()
            user = authenticate(username=username,password=raw_password)
            login(request,user)
            return redirect('myApp:index')
    else:
        form = RegularUserCreation()
    return render(request,'userModule/user_signup.html', {'form':form})