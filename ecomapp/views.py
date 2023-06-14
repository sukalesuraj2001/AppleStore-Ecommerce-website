from django.shortcuts import render,redirect
from django.http import HttpResponse
from ecomapp.models import Apple_Product,Cart,Order
from ecomapp.forms import EmpForm,Apple_ProductModelForm,UserForm
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout

from django.db.models import Q
import random
import razorpay
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.forms import PasswordResetForm
from django.contrib import messages

# Create your views here.
def  home(request):
#    data=Product.objects.all() #select * from ecomapp_product; active and inactive
   data=Apple_Product.objects.filter(status=1)#fetch only active Products 
#    print(data)
   content={}
   content['products']=data
   return render(request, 'index.html',content)


# def register(request):
#     return render(request,'register.html')

def payment(request):
    return render(request,'payment.html')
def about(request):
    return render(request,'about.html')
def productlist(request,pid):
    # print("id of product",pid)
    data=Apple_Product.objects.filter(id=pid)
    content={}
    content['products']=data

    return render(request,'product_details.html',content)

def account(request):
    return render(request,'account.html')
def reuse(request):
    return render(request, 'base.html')   

# sorting start

# def sort(request,sv):
#     if sv=='0':
#         params='price'
#     else:
#         params='-price'
#     q1=Q(status=1)
#     q2=Q(cat=1)
    
#     data=Product.objects.order_by(params).filter(q1 & q2)
#     content={}
#     content['products']=data
#     return render(request,'iphones.html',content)

def catfilter(request,catv):
     q1=Q(cat=catv)
     q2=Q(status=1)
     data=Apple_Product.objects.filter(q1 & q2)
     content={}
     content['products']=data
     return render(request,'index.html',content)
#  iphones sorting
def  iphones(request,ipv):
   if ipv=='0':
        params='price'
        
   else:
        params='-price'
        
   q1=Q(cat=1)
   q2=Q(status=1)

  
   
   data=Apple_Product.objects.order_by(params).filter(q1 & q2 )#fetch only active Products 
   print(data)
   content={}
   content['products']=data
   return render(request, 'iphones.html',content)

# ipad sorting
def  ipad(request,iv):
   if iv=='0':
        params='price'
   else:
        params='-price'
   q1=Q(cat=2)
   q2=Q(status=1)
   data=Apple_Product.objects.order_by(params).filter(q1 & q2)#fetch only active Products 
   print(data)
   content={}
   content['products']=data
   return render(request, 'ipad.html',content)

def  watch(request,wv):
   if wv=='0':
        params='price'
   else:
        params='-price'
   q1=Q(cat=3)
   q2=Q(status=1)
   data=Apple_Product.objects.order_by(params).filter(q1 & q2)#fetch only active Products 
   print(data)
   content={}
   content['products']=data
   return render(request, 'apple_watch.html',content)

def tv(request):
    return render(request,'tv&home.html')
# macbook section
def  macbook(request,mv):
   if mv=='0':
        params='price'
   else:
        params='-price'
   q1=Q(cat=4)
   q2=Q(status=1)
   data=Apple_Product.objects.order_by(params).filter(q1 & q2)#fetch only active Products 
   print(data)
   content={}
   content['products']=data
   return render(request, 'macbook.html',content)


# macDesktop section
def  macdesktop(request,mdv):
   if mdv=='0':
        params='price'
   else:
        params='-price'
   q1=Q(cat=5)
   q2=Q(status=1)
   data=Apple_Product.objects.order_by(params).filter(q1 & q2)#fetch only active Products 
   print(data)
   content={}
   content['products']=data
   return render(request, 'macdesktop.html',content)

# acceserise start
def  acceserise(request):
   
   q1=Q(cat=8)
   q2=Q(status=1)
   data=Apple_Product.objects.filter(q1 & q2)#fetch only active Products 
#    print(data)
   content={}
   content['products']=data
   return render(request, 'acceserise.html',content)



# filters start
def pricefilter(request,pv):
    q1=Q(status=1)
    if pv =='0':
       q2=Q(price__lt=5000)
    else:
        q2=Q(price__gte=5000)
    
    data=Apple_Product.objects.filter(q1 & q2)
    content={}
    content['products']=data
    return render(request,'index.html',content)

def pricerange(request):

    low=request.GET['min']
    high=request.GET['max']
    q1=Q(status=1)
    q2=Q(price__gte=low)
    q3=Q(price__lte=high)
    data=Apple_Product.objects.filter(q1 & q2 & q3)
    content={}
    content['products']=data
    return render(request,'index.html',content)

# =================addproduct section================

def addproduct(request):
    # print("Method is:",request.method)
    if request.method == 'POST':
        # print("Inser record in database")
        n=request.POST['pname']
        c=request.POST['pcat']
        amt=request.POST['price']
        s=request.POST['status']
        # print(n)
        # print(cat)
        # print(amt)
        # print(s)
        p=Apple_Product.objects.create(name=n,cat=c,price=amt,status=s)
        p.save()
        return redirect('/addproduct')
    else:
        # print("In else part")
        data=Apple_Product.objects.all()
        content={}
        content['products']=data
        return render(request,'addproduct.html',content)
    
    # ==================delete product=====================

def delproduct(request,rid):
    # print("ID to be deleted:",rid)
    data=Apple_Product.objects.filter(id=rid)
    data.delete()
    return redirect('/addproduct')

    # =======================edit section=====================

def editproduct(request,rid):
    # print('id to be edited',rid)
    if request.method =='POST':
        upname=request.POST['pname']
        ucat=request.POST['pcat']
        uprice=request.POST['price']
        ustatus=request.POST['status']
        p=Apple_Product.objects.filter(id=rid)
        p.update(name=upname,cat=ucat,price=uprice,status=ustatus)
        return redirect('/addproduct')

        
      
    else: 
     p=Apple_Product.objects.filter(id=rid)
     content={}
    content['products']=p
    return render(request,'editproduct.html',content)


# ===========define django forms===============
 
def djangoform(request):
    if request.method =='POST':
        ename=request.POST['name']
        dept=request.POST['dept']
        email=request.POST['email']
        salary=request.POST['salary']
        print(ename)
        print(dept)
        print(email)
        print(salary)
    else:
        eobj=EmpForm()
        content={}
        content['forms']=eobj
        return render(request,'djangoform.html',content)


def modelform(request):
    if request.method=='POST':
        name=request.POST['name']
        cat=request.POST['cat']
        price=request.POST['price']
        status=request.POST['status']
        pimage=request.POST['pimage']
        print('Product Name:',name)
        print('Product Category:',cat)
        print('Product Price:',price)
        print('Product status:',status)
        print('Image Path:',pimage)
    else:
        pobj=Apple_ProductModelForm()
        content={}
        content['forms']=pobj
        return render(request,'modelform.html',content)

def user_register(request):
        
    content={}
    reobj=UserForm()
    content['userform']=reobj


    if request.method=='POST':
        reobj=UserForm(request.POST)
        if reobj.is_valid():
            reobj.save()
            content['success']='User Created Successfully'
            return render(request,'user_register.html',content)
    else:
        # reobj=UserCreationForm()
       
     return render(request,'user_register.html',content)
    


def User_login(request):
    if request.method=='POST':
        dataobj=AuthenticationForm(request=request,data=request.POST)
        # print(dataobj) 
        if dataobj.is_valid():
         uname=dataobj.cleaned_data['username']
         upass=dataobj.cleaned_data['password']
        #  print(uname)
        #  print(upass)
         u=authenticate(username=uname,password=upass)
        #  print(u) 
        if u:
            login(request,u)
            return redirect('/')
    else:
        eobj=AuthenticationForm()
        content={} 
        content['loginform']=eobj
        return render(request,'user_login.html',content)
    
def setsession(request):
    request.session['name']='itvedant'

    return render(request,'setsession.html')

def getsession(request):
    content={}

    content['data']=request.session['name']
    return render(request,'getsession.html',content)

#=================== cart functionality===================

def addtocart(request,pid):
    if request.user.is_authenticated:
        userid=request.user.id
        # print("User id",uid)
        # print("product id",pid)
        q1=Q(pid=pid)
        q2=Q(uid=userid)

       
        c=Cart.objects.filter(q1 & q2)
        p=Apple_Product.objects.filter(id=pid)
        content={}
        content['products']=p
        if c:
            
            content['msg']='Product already added to cart'
            
            return render(request,'product_details.html',content)


        else:
             u=User.objects.filter(id=userid)
        # print()
             c =Cart.objects.create(uid=u[0],pid=p[0])
             c.save()
             
             content['success']='Product added Successfully in cart'
            
             return render(request,'product_details.html',content)

       
    else:
     return redirect('/login')
    
# ===============logout functionality======================
  
def user_logout(request):
    logout(request)
    return redirect('/login')

def viewcart(request):
    userid=request.user.id
    c=Cart.objects.filter(uid=userid)
    # print(c[0])
    # print(c[0].pid)
    # print(c[0].uid)

    # calculating total price
    sum=0
    for x in c:
        # print(type(x.qty))
        # print(type(x.pid.price))
        sum=sum+(x.qty*x.pid.price)
        # print("total price is :",sum)
    content={}
    content['products']=c
    content['nitems']=len(c)
    content['total']=sum
    # print(len(c))
    return render(request,'viewcart.html',content)


def changeqty(request,pid,f):
    # print(type(pid))
    # print(type(f))
    content={}
    c=Cart.objects.filter(pid=pid)
    if f =='1':
        # print('increment')
        x=c[0].qty+1
    else:
        # print('decrement')
        x=c[0].qty-1

    if x>0:
        c.update(qty=x)
    if f=='3':
        c.delete()
    return redirect('/viewcart')
    #     userid=request.user.id
    #     c=Cart.objects.filter(uid=userid)
    #     content['products']=c

    #     content['msg']="Quantity cannot be zero"
    #     return render(request,'viewcart.html',content)

def delcart(request,pid,f):
        c=Cart.objects.filter(pid=pid)
        if f=='3':
            c.delete()
        return redirect('/viewcart')

def placeorder(request):
    oid =random.randrange(1000,9999)
    userid=request.user.id
    # print(userid)
    c=Cart.objects.filter(uid=userid)
    # print(c)
    for x in c:
        # print(x)
        # print(x.pid)
        # print(x.uid)
        # print(x.qty)
        o=Order.objects.create(order_id=oid,pid=x.pid,uid=x.uid,qty=x.qty)
        o.save()
        x.delete()
    o=Order.objects.filter(uid=userid)
    sum=0
    for x in o:
        sum=sum+(x.qty*x.pid.price)
    content={}
    content['products']=o
    content['nitems']=len(o)
    content['total']=sum

    return render(request,'placeorder.html',content)



    # # print(oid)
    # return HttpResponse("order is successfully done")

def makepayment(request):
    userid=request.user.id
    client = razorpay.Client(auth=("rzp_test_m3OSuvZERzvgSZ", "4pDjW9W17PLiUoc12J2WkpSw"))
    o=Order.objects.filter(uid=userid)
    sum=0
    for x in o:
        sum=sum+(x.qty*x.pid.price)
    sum=sum*100 #conversion of Rs to Paise
    print(sum)
    data = { "amount":sum, "currency": "INR", "receipt":str(o[0].id) }
    payment = client.order.create(data=data)
    print(payment)
    content={}
    content['payment']=payment

    return render(request,'pay.html',content)



# def makepayment(request):
#     userid = request.user.id
#     client = razorpay.Client(auth=("rzp_test_m3OSuvZERzvgSZ", "4pDjW9W17PLiUoc12J2WkpSw"))
#     orders = Order.objects.filter(uid=userid)
#     total_amount = 0
    
#     for order in orders:
#         total_amount += order.qty * order.pid.price
    
#     total_amount *= 100  # Conversion of Rs to Paise
#     print(total_amount)
    
#     data = {"amount": total_amount, "currency": "INR", "receipt": str(orders[0].id)}
#     payment = client.order.create(data=data)
#     print(payment)
    
#     content = {"payment": payment}
    
#     # Delete products after successful payment
#     if payment.get("status") == "created":
#         for order in orders:
#             order.pid.delete()
#         orders.delete()
    
#     return render(request, "pay.html", content)

def storedetails(request):
    pay_id=request.GET['pid']
    order_id=request.GET['oid']
    sign=request.GET['sign']
    userid=request.user.id 
    u=User.objects.filter(id=userid)
    #print(u[0])
    #print(u[0].email)
    #print(pay_id)
    #print(order_id)
    #print(sign)
    email=u[0].email
    msg=" Your  Order Placed Successfully. Details are Payment ID:"+pay_id+" and Order Id is:"+order_id
    send_mail(
    "Order Status-Apple Store ",
    msg,
    settings.EMAIL_HOST_USER,
    [email],
fail_silently=False,
    )
    return HttpResponse("Email Sent successfully")


# forgot password functionality


