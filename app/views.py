from django.shortcuts import render,redirect
from .forms import RegisterForm,UserForm,customerprofile
from django.contrib.auth import login,authenticate, logout
from django.contrib import messages
from .models import Cart, Customer, OrderPlaced, Product
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q 
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

def home(request):
    bottomwear=Product.objects.filter(category='BW')
    topmwear=Product.objects.filter(category='TW') 
    mobile=Product.objects.filter(category='M')    
    return render(request, 'app/home.html',{'bw':bottomwear,'top':topmwear,'mob':mobile})

def product_detail(request,pro_id):
    pro_detail=Product.objects.get(id=pro_id)
    return render(request,'app/productdetail.html',{'p_detail':pro_detail})

@login_required()
def add_to_cart(request):
    usr=request.user
    prod_id=request.GET.get('prod_id')
    product=Product.objects.get(id=prod_id)
    Cart(user=usr,product=product).save()
    return redirect('/cart')

@login_required()
def showcart(request):
    if request.user.is_authenticated:
        usr=request.user
        cart=Cart.objects.filter(user=usr)
        amount=0.0
        shipping_amount=70.0
        total_amount=0.0
        prod_list=[p for p in Cart.objects.all() if p.user==usr]
        if prod_list:
            for i in prod_list:
                tempamt=(i.product.selling_price * i.quantity)-(i.product.discounted_price * i.quantity)
                amount+=tempamt
                total_amount=amount+shipping_amount
            return render(request,'app/addtocart.html',{'carts':cart,'totalamt':total_amount,'amount':amount})
        return render(request,'app/emptycart.html')

@login_required()
def buy_now(request):
 return render(request, 'app/buynow.html')

@login_required()
def profile(request):
    if request.method=='POST':
        form=customerprofile(request.POST)
        usr=request.user
        if form.is_valid():
            name=form.cleaned_data['name']
            locality=form.cleaned_data['locality']
            city=form.cleaned_data['city']
            zipcode=form.cleaned_data['zipcode']
            state=form.cleaned_data['state']
            reg=Customer(user=usr,name=name,locality=locality,city=city,zipcode=zipcode,state=state)
            reg.save()
            messages.success(request,'congratulation data has saved...')
            form=customerprofile()
    else:
        form=customerprofile()
    return render(request, 'app/profile.html',{'form':form,'active':'btn-primary'})

    
@login_required()
def address(request):
    add=Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html',{'address':add,'active':'btn-primary'})

@login_required()
def orders(request):
    orderplaced=OrderPlaced.objects.filter(user=request.user)
    return render(request, 'app/orders.html',{'orderplaced':orderplaced})

def mobile(request):
    mobiles=Product.objects.filter(category='M')
    return render(request, 'app/mobile.html',{'mob':mobiles})

def laptop(request):
    return render(request, 'app/laptop.html')

def customerregistration(request):
    if request.method=='POST':
        fo=RegisterForm(request.POST)
        if fo.is_valid():
            messages.success(request,'congratulation you are successfully registered..!!')
            print('data is svae')
    else:        
        fo=RegisterForm()
        print('data is not save')
    return render(request, 'app/customerregistration.html',{'fom':fo})

@login_required()
def checkout(request):
    usr=request.user
    prod=Cart.objects.filter(user=usr)
    addres=Customer.objects.filter(user=usr)
    amount=0.0
    shipping_amount=70.0
    total_amount=0.0
    prod_list=[p for p in Cart.objects.all() if p.user==usr]
    if prod_list:
        for i in prod_list:
            tempamt=(i.product.selling_price * i.quantity)-(i.product.discounted_price * i.quantity)
            amount+=tempamt
        total_amount=amount+shipping_amount
    return render(request, 'app/checkout.html',{'address':addres,'totalamount':total_amount,'cartdetails':prod})

def pluscart(request):
    if request.method=='GET':
        usr=request.user
        prod_id=request.GET['prod_id']
        c=Cart.objects.get(Q(product=prod_id)& Q(user=request.user))
        c.quantity+=1
        c.save()
        prod_list=[p for p in Cart.objects.all() if p.user==request.user]
        amount=0.0
        shipping_amount=70.0
        total_amount=0.0
        prod_list=[p for p in Cart.objects.all() if p.user==usr]
        
        for i in prod_list:
            tempamt=(i.product.selling_price * i.quantity)-(i.product.discounted_price * i.quantity)
            amount+=tempamt
            total_amount=amount+shipping_amount
        data={
           'quantity':c.quantity,
            'amount':amount,
           'total_amount':total_amount
            }
        return JsonResponse(data)

def minuscart(request):
    if request.method=='GET':
        usr=request.user
        prod_id=request.GET['prod_id']
        c=Cart.objects.get(Q(product=prod_id)& Q(user=request.user))
        c.quantity-=1
        c.save()
        prod_list=[p for p in Cart.objects.all() if p.user==request.user]
        amount=0.0
        shipping_amount=70.0
        total_amount=0.0
        prod_list=[p for p in Cart.objects.all() if p.user==usr]
        
        for i in prod_list:
            tempamt=(i.product.selling_price * i.quantity)-(i.product.discounted_price * i.quantity)
            amount+=tempamt
            total_amount=amount+shipping_amount
        data={
           'quantity':c.quantity,
            'amount':amount,
           'total_amount':total_amount
            }
        return JsonResponse(data)

def removecart(request):
    if request.method=='GET':
        usr=request.user
        prod_id=request.GET['prod_id']
        c=Cart.objects.get(Q(product=prod_id)& Q(user=request.user))
        c.delete()
        prod_list=[p for p in Cart.objects.all() if p.user==request.user]
        amount=0.0
        shipping_amount=70.0
        total_amount=0.0
        prod_list=[p for p in Cart.objects.all() if p.user==usr]
        
        for i in prod_list:
            tempamt=(i.product.selling_price * i.quantity)-(i.product.discounted_price * i.quantity)
            amount+=tempamt
            total_amount=amount+shipping_amount
        data={
            'amount':amount,
           'total_amount':total_amount
            }
        return JsonResponse(data)

def paymentdone(request):
    user=request.user
    custid=request.GET.get('custid')
    customer=Customer.objects.get(id=custid)
    cart=Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user,customer=customer,product=c.product,quantity=c.quantity).save()
        c.delete()
    return redirect("orders")
        
