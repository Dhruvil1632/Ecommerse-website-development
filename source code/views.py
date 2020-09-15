from django.shortcuts import render
from django.http import HttpResponse
from .models import product_details
from .models import user_details
from .models import user_cart
# Create your views here.
all_product  = product_details.objects.all()
def index(request):
    global all_product 
    return render(request , 'home.html' , {'products' : all_product})

def slider(request):
    all_product  = product_details.objects.all()
    return render(request , 'slider.html' ,{'products' : all_product[:15]} )
shown_product = ['one']
def cart(request):
    if log_user != "None":
        total_product = user_cart.objects.all()
        added_product_id = []
        for i in total_product:
            if i.user_name == log_user:
                added_product_id.append(i.product_id)
        database_product = product_details.objects.all()
        global shown_product 
        shown_product = []
        for i in added_product_id:
            for j in database_product:
                if j.product_id == i:
                    shown_product.append(j)
        return render(request , 'mycart.html' ,{'products' : shown_product})
    else:
        return render(request , 'mycart.html' ,{'dynamic' : "Nothing here"})



def return_login(request):
    return render(request,'login.html')

def payment(request):
    return render(request , 'payment.html')

def purchase(request):
    return render(request , 'purchase.html')

def add_to_cart(request):
    new_product = user_cart()
    new_product.product_id = int(request.POST['selected_product'])
    new_product.user_name = log_user
    if new_product.user_name == "None":
        return render(request , 'home1.html' ,{'dynamic':"Please log in",'products' : all_product})
    else:
        cart_product = user_cart.objects.all()
        for i in cart_product:
            if i.user_name == new_product.user_name and i.product_id == new_product.product_id:
                return render(request , 'home1.html' ,{'dynamic':"Product is already there",'products' : all_product})
        new_product.save()
        return render(request , 'home1.html' ,{'dynamic':"Success! your product has been added",'products' : all_product})



def add_to_cart1(request):
    new_product = user_cart()
    new_product.product_id = int(request.POST['select_product'])
    new_product.user_name = log_user
    if new_product.user_name == "None":
        return render(request , 'home1.html' ,{'dynamic':"Please log in" , 'products' : all_product})
    else:
        cart_product = user_cart.objects.all()
        for i in cart_product:
            if i.user_name == new_product.user_name and i.product_id == new_product.product_id:
                return render(request , 'home1.html' ,{'dynamic':"Product is already there",'products' : all_product})
        new_product.save()
        return render(request , 'home1.html' ,{'dynamic':"Success! your product has been added",'products' : all_product})



log_user = "None"
def login(request):
    global log_user
    users , passwords = [] , [] 
    sample = user_details.objects.all()
    for i in sample:
        users.append(i.user_name)
        passwords.append(i.psw)
    log_user = request.POST['uname']
    log_pass = request.POST['psw']
    for i in range(0,len(users)):
        if users[i] == log_user:
            if passwords[i] == log_pass:
                return render(request , 'login.html' , {'dynamic' : "log in successfully"})
    return render(request , 'login.html' , { 'dynamic' : "invalid user name or password"})




def return_sign(request):
    return render(request , 'signup.html')



def signup(request):
    new_user = user_details()
    new_user.user_name = request.POST["uname"]
    new_user.psw = request.POST["psw"]
    confirm_pass  = request.POST['psw_repeat']
    new_user.age = request.POST["age"]
    new_user.xender = request.POST.get("gender")
    data1 = user_details.objects.all()
    veri_name , veri_pass = [] , []
    for i in data1:
        veri_name.append(i.user_name)
        veri_pass.append(i.psw)
    if new_user.user_name in veri_name or new_user.psw in veri_pass:
        return render(request , 'signup.html' , { 'dynamic' : "user name or password already taken"}) 
    if new_user.psw == confirm_pass:
        new_user.save()
        return render(request , 'signup.html' , { 'dynamic' : "sign up  successfully"})
    else:
        return render(request , 'signup.html' , { 'dynamic' : "password does not match"})



def contact(request):
    return render(request,'contact.html')



def search(request):
    search_ = request.POST['search_product']
    max_price = int(request.POST['search_product_price'])
    searched_result = []
    all_product  = product_details.objects.all()
    if search_ == 'all' :
        for i in all_product:
            if i.product_price <= max_price:
                searched_result.append(i)
        return render(request,'home.html', {'products' : searched_result})
    else:
        for i in all_product:
            if i.category == search_ and i.product_price <= max_price:
                searched_result.append(i)
        return render(request , 'search.html' , {'products' : searched_result})


def search_in_cart(request):
    search_ = request.POST['search_product']
    max_price = int(request.POST['search_product_price'])
    filtered_cart_product = []
    for j in shown_product:
        if j.category == search_ and j.product_price <= max_price:
            filtered_cart_product.append(j)
    return render(request , 'mycart.html' , {'products' : filtered_cart_product})


    
def remove_product(request):
    product_id = request.POST['delete_product']
    user_cart.objects.filter(product_id= product_id , user_name = log_user).delete()
    total_product = user_cart.objects.all()
    added_product_id = []
    for i in total_product:
        if i.user_name == log_user:
            added_product_id.append(i.product_id)
    database_product = product_details.objects.all()
    shown_product = []
    for i in added_product_id:
        for j in database_product:
            if j.product_id == i:
                shown_product.append(j)
    return render(request , 'mycart.html' ,{'products' : shown_product})

