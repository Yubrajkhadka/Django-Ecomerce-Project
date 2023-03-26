from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.contrib import messages
from django.db.models import Q
from django.core.mail import send_mail
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
import requests, json
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from .forms import ContactForm ,AddCategory,AddProductForm
from django.contrib.auth import authenticate, login,logout




# Create your views here.
def index(request):
    if request.GET.get('search'):
        search = request.GET.get('search')
        search = search.lower()
        prod = Product.objects.filter(
            Q(name__icontains = search) |
            Q(description__icontains=search) |
            Q(category__name__icontains=search)|
            Q(price__icontains = search) 
        )

        data = {
            'productData': prod,

        }
        return render(request, 'pages/product_list.html', data)

    else:
        cat = Category.objects.all()
        prod = Product.objects.all()
        data = {
            'categoryData': cat,
            'productData': prod,

        }

        return render(request, 'pages/index.html', data)
    
def contact(request):
    form = ContactForm()
    if request.method == "POST":
       form = ContactForm(request.POST)
       if form.is_valid():
            name = request.POST.get('fullname')
            email = request.POST.get('email')
            number = request.POST.get('number')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            contact = Contact(
                name = name,
                email = email,
                number = number,
                subject = subject,
                message = message,
                )
            subject = subject
            message = message
            email_from = settings.EMAIL_HOST_USER
            try:
                send_mail(subject, message ,email_from,['yubarajkhadka@kcc.edu.np'])
                contact.save()
                messages.success(request,"Message sent successfully")
                return redirect('/')
            except:
         
                    return redirect('/contact')
       else:
            messages.error(request, 'Wrong Captcha!')
    context = {'form':form}      
    return render(request, 'pages/contact.html',context)  
    
def category_list(request):
    if request.GET.get('search'):
        search = request.GET.get('search')
        search = search.lower()
        prod = Product.objects.filter(
            Q(name__icontains=search) |
            Q(description__icontains=search) |
            Q(category__name__icontains=search)|
            Q(price__icontains = search) 
        )

        data = {
            'productData': prod,

        }
        return render(request, 'pages/product_list.html', data)
    else:
     cat = Category.objects.all()
     data ={
        'categoryData':cat
    }
     return render(request,'pages/category_list.html',data)
def product_list(request):
    if request.GET.get('search'):
        search = request.GET.get('search')
        search = search.lower()
        prod = Product.objects.filter(
            Q(name__icontains=search) |
            Q(description__icontains=search) |
            Q(category__name__icontains=search)|
            Q(price__icontains = search) 
        )

        data = {
            'productData': prod,

        }
        return render(request, 'pages/product_list.html', data)
        
    prod = Product.objects.all()
    cat = Product.objects.all()
    data = {
        'productData':prod,
        'categoryData':cat
    }
    

    return render(request,'pages/product_list.html',data)

def product_details(request,slug):
    if request.GET.get('search'):
        search = request.GET.get('search')
        search = search.lower()
        prod = Product.objects.filter(
            Q(name__icontains=search) |
            Q(description__icontains=search) |
            Q(category__name__icontains=search)|
            Q(price__icontains = search) 
        )

        data = {
            'productData': prod,
              }
        return render(request, 'pages/product_list.html', data)
    prod = Product.objects.get(slug=slug)
    related_products=Product.objects.filter (category=prod.category).exclude(slug=prod.slug)
    data = {
        'productData':prod,
        'relateddata':related_products,
    }
    return render(request, 'pages/product_details.html',data)
    
def category_details(request,slug):
    if request.GET.get('search'):
        search = request.GET.get('search')
        search = search.lower()
        prod = Product.objects.filter(
            Q(name__icontains=search) |
            Q(description__icontains=search) |
            Q(category__name__icontains=search)|
            Q(price__icontains = search) 
        )

        data = {
            'productData': prod,

        }
        return render(request, 'pages/product_list.html', data) 
    
    cat = Category.objects.get(slug=slug)
    data = {
        'categoryData' :cat
     }
    return render(request, 'pages/category_details.html',data)




@login_required(login_url ='loginpage')
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    if product.stock < 1:
        messages.success(request,"Product is Not Available")
        redirect_back = request.META.get('HTTP_REFERER')
        return redirect(redirect_back)
    else:
        cart.add(product=product)
        messages.success(request,"Product added successfully")
        redirect_back = request.META.get('HTTP_REFERER')
        return redirect(redirect_back)



@login_required(login_url ='loginpage')
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url ='loginpage')
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    max_item = 5
    if cart.cart[str(product.id)]['quantity'] < max_item:
        cart.add(product=product)
    else:
        messages.error(request,"The Product quantity more than 5 are not added to cart")
    return redirect("cart_detail")


@login_required(login_url ='loginpage')
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    min_item = 1
    if cart.cart[str(product.id)]['quantity'] > min_item:
          cart.decrement(product=product)
    else:
        messages.error(request,"The Product quantity must not be less than 1")  
    return redirect("cart_detail")


@login_required(login_url ='loginpage')
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url ='loginpage')
def cart_detail(request):
    if request.GET.get('search'):
        search = request.GET.get('search')
        search = search.lower()
        prod = Product.objects.filter(
            Q(name__icontains=search) |
            Q(description__icontains=search) |
            Q(category__name__icontains=search)|
            Q(price__icontains = search) 
        )

        data = {
            'productData': prod,

        }
        return render(request, 'pages/product_list.html', data)
    return render(request, 'pages/cart_detail.html')
    
# wishlist #
@login_required(login_url ='loginpage')
def wishlist(request):
   wishlist = Wishlist.objects.filter(user=request.user)
   return render(request, 'pages/wishlist.html', {'wishlist_items': wishlist})


@login_required(login_url ='loginpage')
def addwishlist(request,product_id):
    product = get_object_or_404(Product, id=product_id)
    created = Wishlist.objects.get_or_create(user=request.user, product=product)
    if created :
         messages.success(request,"Wishlist added successfully")
    else:
         messages.success(request,"Product  are already in  Wishlist")
    redirect_back = request.META.get('HTTP_REFERER')
    return redirect(redirect_back)
   

def removewishlist(request,wishlist_id):
    wishlist_item = get_object_or_404(Wishlist, id=wishlist_id, user=request.user)
    product_name = wishlist_item.product.name
    wishlist_item.delete()
    messages.success(request,"Product delete successfully")
    redirect_back = request.META.get('HTTP_REFERER')
    return redirect(redirect_back)




def checkout(request):
    ord = Order.objects.all()
    if request.GET.get('search'):
        search = request.GET.get('search')
        search = search.lower()
        prod = Product.objects.filter(
            Q(name__icontains=search) |
            Q(description__icontains=search) |
            Q(category__name__icontains=search)|
            Q(price__icontains = search) 
        )

        data = {
            'productData': prod,
            

        }
        return render(request, 'pages/product_list.html', data)
   
    return render(request,"pages/checkout.html",{'ord':ord})


def placeorder(request):
    if request.method == 'POST':
        uid = request.session.get('_auth_user_id')
        user = User.objects.get(id = uid)
        cart = request.session.get('cart')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        phone = request.POST.get('number')
        email = request.POST.get('email')
        additional_info  = request.POST.get('description')
        address = request.POST.get('address')
        amount = request.POST.get('total')
        order_status = request.POST.get('status')
        payment_method =request.POST.get('payment')
        order = Order(
            user = user,
            firstname = firstname,
            lastname = lastname,
            phone = phone,
            email = email,
            additional_info = additional_info,
            address = address,
            payment_method = payment_method,
            amount = amount,
        

            )
        order.save()
        for i in cart:
            a = cart[i]['price']
            b = (int(cart[i]['quantity']))
    
            total = a*b
            item = OrderItem(
                order = order, 
                product = cart[i]['name'],
                image = cart[i]['image'],
                quantity =cart[i]['quantity'],
                price=cart[i]['price'],
                total = total
            )
            item.save()
        if payment_method == "Khalti":
            order.paid = True
            order.save()
            return render(request,'pages/placeorder.html')
        elif payment_method == "Cash On Delivery":
            return render(request,'pages/thankyou.html')

    cart = Cart(request)
    cart.clear()    
    return render(request, 'pages/placeorder.html')

def thankyou(request):
    return render(request,'pages/thankyou.html')


def userprofile(request):
    ord = Order.objects.filter(user=request.user).order_by('-id')
    ordid = OrderItem.objects.filter(order__in=ord).order_by('-id')
    show_all = request.GET.get('show_all', False)
    items_per_page = 4
    paginator = Paginator(ordid, items_per_page)
    if show_all:
        current_page = paginator.get_page(1)
    else:
        page_number = request.GET.get('page')
        current_page = paginator.get_page(page_number)
    data = {
             'order':ord,
             'orderitem': current_page,
             'total_items': ordid.count(), 
             'show_all': show_all,
         }
    return render(request,'pages/userprofile.html',data)




#Khalti Payment#
@csrf_exempt
def verify_payment(request):
   data = request.POST
   product_id = data['product_identity']
   token = data['token']
   amount = data['amount']
   
   url = "https://khalti.com/api/v2/payment/verify/"
   payload = {
   "token": token,
   "amount": amount
   }
   headers = {
   "Authorization": "test_secret_key_2a5470ef5de946dc922f74fe7ba7cf9a"
   }
   

   response = requests.post(url, payload, headers = headers)

   response_data = json.loads(response.text)
   status_code = str(response.status_code)

   if status_code == '400':
      response = JsonResponse({'status':'false','message':response_data['detail']}, status=500)
      return response

   import pprint 
   pp = pprint.PrettyPrinter(indent=4)
   pp.pprint(response_data)
   
   return JsonResponse(f"Payment Done !! With IDX. {response_data['user']['idx']}",safe=False)

#admin
def admin_login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        passwrd = request.POST.get('pswd')
        user = authenticate(request, username=name, password=passwrd)
        if user is not None and Admin.objects.filter(user=user).exists():
            login(request, user)
            return redirect('adminhome')
        else:
             messages.error(request,"Invalid username or password")
             return redirect('/adminlogin')
    else:
        return render(request, 'dashboard/adminlogin.html')
    
def adminlogout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged Out Successfully")
    return redirect('adminhome')



@login_required(login_url='admin_login')
def adminhome(request):
    order = Order.objects.filter( order_status = 'Order Received').order_by("-id")
    context = {
        'data': order,
        }
    return render(request,'dashboard/orderlist.html',context)


@login_required(login_url='admin_login')
def adminproduct(request):
    product = Product.objects.all().order_by('-id')
    show_all = request.GET.get('show_all', False)
    items_per_page = 4
    paginator = Paginator(product, items_per_page)
    if show_all:
        current_page = paginator.get_page(1)
    else:
        page_number = request.GET.get('page')
        current_page = paginator.get_page(page_number)
    context = {
        'product':current_page,
        'total_items': product.count(), 
        'show_all': show_all,
    }
    return render(request,'dashboard/productlist.html',context)


def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    messages.success(request,"Product delete successfully")
    redirect_back = request.META.get('HTTP_REFERER')
    return redirect(redirect_back)

@login_required(login_url='admin_login')
def adminorder(request):
    order = Order.objects.all().order_by("-id")
    show_all = request.GET.get('show_all', False)
    items_per_page = 7
    paginator = Paginator(order, items_per_page)
    if show_all:
        current_page = paginator.get_page(1)
    else:
        page_number = request.GET.get('page')
        current_page = paginator.get_page(page_number)
    context = {
        'order':current_page,
        'total_items': order.count(), 
        'show_all': show_all,
    }
    return render(request,'dashboard/allorder.html',context)




def delete_order(request,order_id):
    order = get_object_or_404(Order, id=order_id)
    order.delete()
    messages.success(request, 'Order has been deleted successfully.')
    redirect_back = request.META.get('HTTP_REFERER')
    return redirect(redirect_back)


def adminorderdetail(request,pk):
    ord = get_object_or_404(Order, pk=pk)
    orderitem = ord.items.all()
    allstatus = ORDER_STATUS
    context = {'order': ord, 
               'allstatus': allstatus,
               'orderitem':orderitem
               
               }

    return render(request, "dashboard/orderdetail.html", context)


def adminupdatestatus(request,pk):
    order = get_object_or_404(Order, id=pk)
    if request.method == "POST":
      new_status = request.POST.get("status")
      order.order_status = new_status
      order.save()
      messages.success(request, 'Order Status has been updated successfully.')
      return redirect("adminorderdetail", pk=pk)
    return render(request, "orderdetail.html", {"order": order})
        


def addcategory(request):
    if request.method == 'POST':
        form = AddCategory(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category has been added successfully.')
            return redirect('viewcategory')
    else:
        form = AddCategory()
    return render(request, 'dashboard/addcategory.html', {'form': form})

 
@login_required(login_url='admin_login') 
def viewcategory(request):
    cat = Category.objects.all()
    data = {
        'category':cat
    }
    return render(request,'dashboard/categorylist.html',data)


def delete_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    category.delete()
    messages.success(request, 'Category has been deleted successfully.')
    redirect_back = request.META.get('HTTP_REFERER')
    return redirect(redirect_back)


def addproduct(request):
 if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Product has been added successfully.")
            return redirect('adminproduct')
 else:
        form = AddProductForm()
 return render(request, 'dashboard/addproduct.html', {'form': form})

  
def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request,"Product has been updated successfully.")
            return redirect('adminproduct')
    else:
        form = AddProductForm(instance=product)
    return render(request, 'dashboard/updateproduct.html', {'form': form, 'product': product})




@login_required(login_url='admin_login')
def adminmessages(request):
    msg = Contact.objects.order_by("-id")
    show_all = request.GET.get('show_all', False)
    items_per_page = 6
    paginator = Paginator(msg, items_per_page)
    if show_all:
        current_page = paginator.get_page(1)
    else:
        page_number = request.GET.get('page')
        current_page = paginator.get_page(page_number)
    context = {
        'message':current_page,
        'total_items': msg.count(), 
        'show_all': show_all,
        }
    return render(request, 'dashboard/contact.html',context)


def messagedelete(request,id):
    contact = get_object_or_404(Contact, id=id)
    contact.delete()
    messages.success(request," Contact has been deleted successfully.")
    redirect_back = request.META.get('HTTP_REFERER')
    return redirect(redirect_back)



