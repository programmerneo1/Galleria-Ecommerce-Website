from django.http.response import JsonResponse
from django.shortcuts import redirect, render, redirect
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced, Wishlist
from itertools import chain
from .forms import CustomerRegistrationForm, CustomerProfileForm, contactformemail
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.mail import send_mail


def home(request, data=None):
    items_in_cart = 0
    if request.user.is_authenticated:
        items_in_cart = len(Cart.objects.filter(user=request.user))
    return render(request, 'app/home.html', {'items_in_cart': items_in_cart})


class ProductDetailView(View):
    def get(self, request, pk):
        items_in_cart = 0
        if request.user.is_authenticated:
            items_in_cart = len(Cart.objects.filter(user=request.user))
        product = Product.objects.get(pk=pk)
        # to chek item already in the cart
        item_already_in_cart = False
        if request.user.is_authenticated:
            item_already_in_cart = Cart.objects.filter(
                Q(product=product.id) & Q(user=request.user)).exists()
        item_already_in_wishlist = False
        if request.user.is_authenticated:
            item_already_in_wishlist = Wishlist.objects.filter(
                Q(product=pk) & Q(user=request.user)).exists()
        if not item_already_in_wishlist:
            return render(request, 'app/productdetail.html', {'product': product, 'item_already_in_cart': item_already_in_cart, 'items_in_cart': items_in_cart, 'col': 'white'})
        else:
            return render(request, 'app/productdetail.html', {'product': product, 'item_already_in_cart': item_already_in_cart, 'items_in_cart': items_in_cart, 'col': 'red'})


class Deals(View):
    def get(self, request):
        items_in_cart = 0
        if request.user.is_authenticated:
            items_in_cart = len(Cart.objects.filter(user=request.user))
        productmens = Product.objects.filter(sex='M')
        productwomens = Product.objects.filter(sex='F')
        return render(request, 'app/deals.html', {'productmens': productmens, 'productwomens': productwomens, 'items_in_cart': items_in_cart})


@login_required
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user, product=product).save()
    return redirect('/cart')


def calculate(cart_product):
    amount = 0.0
    for p in cart_product:
        tempamount = (p.quantity * p.product.discounted_price)
        amount += tempamount
    return amount


def final_price(amount):
    shipping_amount = 70.0
    if amount == 0:
        totalamount = shipping_amount = 0
    elif amount < 2000:
        totalamount = amount + shipping_amount
    else:
        totalamount = amount
        shipping_amount = 0
    return totalamount, shipping_amount


@login_required
def show_cart(request):
    items_in_cart = 0
    if request.user.is_authenticated:
        items_in_cart = len(Cart.objects.filter(user=request.user))
        user = request.user
        cart = Cart.objects.filter(user=user)
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        if cart_product:
            amount = calculate(cart_product)
            totalamount, shipping_amount = final_price(amount)
            return render(request, 'app/addtocart.html', {'carts': cart, 'totalamount': totalamount, 'amount': amount, 'shipping_amount': shipping_amount, 'items_in_cart': items_in_cart})
        else:
            return render(request, 'app/emptycart.html')


def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        cart_product = [p for p in Cart.objects.all() if p.user ==
                        request.user]
        shipping_amount = 70.0
        totalamount = amount = 0
        if cart_product:
            amount = calculate(cart_product)
            totalamount, shipping_amount = final_price(amount)
        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': totalamount,
            'shipping_amount': shipping_amount
        }
        return JsonResponse(data)


def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity -= 1
        c.quantity = max(0, c.quantity)
        c.save()
        cart_product = [p for p in Cart.objects.all() if p.user ==
                        request.user]
        shipping_amount = 70.0
        totalamount = amount = 0
        if cart_product:
            amount = calculate(cart_product)
            totalamount, shipping_amount = final_price(amount)
        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': totalamount,
            'shipping_amount': shipping_amount
        }
        return JsonResponse(data)


def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        cart_product = [p for p in Cart.objects.all() if p.user ==
                        request.user]
        shipping_amount = 70.0
        totalamount = amount = 0
        if cart_product:
            amount = calculate(cart_product)
            totalamount, shipping_amount = final_price(amount)
        data = {
            'amount': amount,
            'totalamount': totalamount,
            'shipping_amount': shipping_amount
        }
        print(data)
        return JsonResponse(data)


def buy_now(request):
    return render(request, 'app/buynow.html')


@login_required
def address(request):
    items_in_cart = 0
    if request.user.is_authenticated:
        items_in_cart = len(Cart.objects.filter(user=request.user))
    add = Customer.objects.filter(user=request.user)
    msg = ''
    if not add:
        msg = "You don't have any address registered."
    return render(request, 'app/address.html', {'add': add, 'active': 'btn-outline-info', 'items_in_cart': items_in_cart, 'msg': msg})


@login_required
def orders(request):
    items_in_cart = 0
    if request.user.is_authenticated:
        items_in_cart = len(Cart.objects.filter(user=request.user))
    op = OrderPlaced.objects.filter(user=request.user)
    msg = ''
    if not op:
        msg = "You Have No Orders! :("
    return render(request, 'app/orders.html', {'order_placed': op, 'items_in_cart': items_in_cart, 'msg': msg})


# def mens(request):
#      return render(request, 'app/mens.html')


class MensProductView(View):
    # handling the product view in mens.html

    def get(self, request, data=None):
        items_in_cart = 0
        if request.user.is_authenticated:
            items_in_cart = len(Cart.objects.filter(user=request.user))
        allproducts = Product.objects.filter(sex='M')
        return render(request, 'app/mens.html', {'mensall': allproducts, 'items_in_cart': items_in_cart})

    def post(self, request):
        Shirts = Jeans = Tshirts = Cloth_others = Casual = Sports = Shoe_others = Product.objects.none()
        data = request.POST
        Found = False

        if data.get('Clothes'):
            if data.get('Shirts'):
                Shirts = Product.objects.filter(category='MS')
                Found = True
            if data.get('Jeans'):
                Jeans = Product.objects.filter(category='MJ')
                Found = True
            if data.get('Tshirts'):
                Tshirts = Product.objects.filter(category='MT')
                Found = True
            if data.get('Cloth_others'):
                Cloth_others = Product.objects.filter(category='MCO')
                Found = True
        if data.get('Shoes'):
            if data.get('Casual'):
                Casual = Product.objects.filter(category='MCS')
                Found = True
            if data.get('Sports'):
                Sports = Product.objects.filter(category='MSS')
                Found = True
            if data.get('Shoe_others'):
                Shoe_others = Product.objects.filter(category='MSO')
                Found = True

        if not Found:
            if data.get('Clothes'):
                Shirts = Product.objects.filter(category='MS')
                Jeans = Product.objects.filter(category='MJ')
                Tshirts = Product.objects.filter(category='MT')
                Cloth_others = Product.objects.filter(category='MCO')
            if data.get('Shoes'):
                Casual = Product.objects.filter(category='MCS')
                Sports = Product.objects.filter(category='MSS')
                Shoe_others = Product.objects.filter(category='MSO')

        allproducts = list(chain(Shirts, Jeans, Tshirts,
                                 Cloth_others, Casual, Sports, Shoe_others))
        if data.get('l2h'):
            allproducts = sorted(
                allproducts, key=lambda x:   x.discounted_price)
        elif data.get('h2l'):
            allproducts = sorted(
                allproducts, key=lambda x:   x.discounted_price, reverse=True)
        elif data.get('rating'):
            allproducts = sorted(
                allproducts, key=lambda x:   x.product_rating, reverse=True)

        return render(request, 'app/mens.html', {'mensall': allproducts})


class WomensProductView(View):
    # handling the product view in mens.html

    def get(self, request, data=None):
        allproducts = Product.objects.filter(sex='F')
        items_in_cart = 0
        if request.user.is_authenticated:
            items_in_cart = len(Cart.objects.filter(user=request.user))

        return render(request, 'app/womens.html', {'womensall': allproducts, 'items_in_cart': items_in_cart})

    def post(self, request):
        Shirts = Jeans = Tshirts = Cloth_others = Casual = Sports = Shoe_others = Product.objects.none()
        data = request.POST
        Found = False

        if data.get('Clothes'):
            if data.get('Shirts'):
                Shirts = Product.objects.filter(category='WS')
                Found = True
            if data.get('Jeans'):
                Jeans = Product.objects.filter(category='WJ')
                Found = True
            if data.get('Tshirts'):
                Tshirts = Product.objects.filter(category='WT')
                Found = True
            if data.get('Cloth_others'):
                Cloth_others = Product.objects.filter(category='WCO')
                Found = True
        if data.get('Shoes'):
            if data.get('Casual'):
                Casual = Product.objects.filter(category='WCS')
                Found = True
            if data.get('Sports'):
                Sports = Product.objects.filter(category='WSS')
                Found = True
            if data.get('Shoe_others'):
                Shoe_others = Product.objects.filter(category='WSO')
                Found = True

        if not Found:
            if data.get('Clothes'):
                Shirts = Product.objects.filter(category='WS')
                Jeans = Product.objects.filter(category='WJ')
                Tshirts = Product.objects.filter(category='WT')
                Cloth_others = Product.objects.filter(category='WCO')
            if data.get('Shoes'):
                Casual = Product.objects.filter(category='WCS')
                Sports = Product.objects.filter(category='WSS')
                Shoe_others = Product.objects.filter(category='WSO')

        allproducts = list(chain(Shirts, Jeans, Tshirts,
                                 Cloth_others, Casual, Sports, Shoe_others))
        if data.get('l2h'):
            allproducts = sorted(
                allproducts, key=lambda x:   x.discounted_price)
        elif data.get('h2l'):
            allproducts = sorted(
                allproducts, key=lambda x:   x.discounted_price, reverse=True)
        elif data.get('rating'):
            allproducts = sorted(
                allproducts, key=lambda x:   x.product_rating, reverse=True)

        return render(request, 'app/womens.html', {'womensall': allproducts})


def Mensfilter(request, data=None):
    shirts = Product.objects.filter(category='MS')
    return render(request, 'app/mens.html', {'mensall': shirts})


def mobile(request):
    return render(request, 'app/mobile.html')


class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html', {'form': form})

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(
                request, 'Congratulations!! Registered Successfully')
            form.save()
        return render(request, 'app/customerregistration.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        items_in_cart = 0
        if request.user.is_authenticated:
            items_in_cart = len(Cart.objects.filter(user=request.user))
        form = CustomerProfileForm()
        return render(request, 'app/profile.html', {'form': form, 'active': 'btn-outline-info', 'items_in_cart': items_in_cart})

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            phone_number = form.cleaned_data['phone_number']
            locality = form.cleaned_data['locality']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=usr, name=name, phone_number=phone_number, locality=locality,
                           state=state, zipcode=zipcode)
            reg.save()
            messages.success(
                request, 'Congratulations!! Profile Updated Successfully')
        return render(request, 'app/profile.html', {'form': form, 'active': 'btn-primary'})


@login_required
def checkout(request):
    items_in_cart = 0
    if request.user.is_authenticated:
        items_in_cart = len(Cart.objects.filter(user=request.user))
    user = request.user
    add = Customer.objects.filter(user=user)
    cart_items = Cart.objects.filter(user=user)
    cart_product = [p for p in Cart.objects.all() if p.user ==
                    user]
    shipping_amount = 70.0
    totalamount = amount = 0
    if cart_product:
        amount = calculate(cart_product)
        totalamount, shipping_amount = final_price(amount)

    return render(request, 'app/checkout.html', {'add': add, 'totalamount': totalamount, 'cart_items': cart_items, 'items_in_cart': items_in_cart})


@login_required
def payment_done(request):
    user = request.user
    custid = request.GET.get('custid')
    customer = Customer.objects.get(id=custid)
    cart = Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user, customer=customer,
                    product=c.product, quantity=c.quantity).save()
        c.delete()

    return redirect("order_success")


@login_required
def order_success(request):
    return render(request, 'app/order_success.html')


def about_us(request):
    items_in_cart = 0
    if request.user.is_authenticated:
        items_in_cart = len(Cart.objects.filter(user=request.user))
    return render(request, 'app/about_us.html', {'items_in_cart': items_in_cart})


def terms_and_conditions(request):
    items_in_cart = 0
    if request.user.is_authenticated:
        items_in_cart = len(Cart.objects.filter(user=request.user))
    return render(request, 'app/terms_and_conditions.html', {'items_in_cart': items_in_cart})


def privacy_and_policy(request):
    items_in_cart = 0
    if request.user.is_authenticated:
        items_in_cart = len(Cart.objects.filter(user=request.user))
    return render(request, 'app/privacy_and_policy.html', {'items_in_cart': items_in_cart})


def delivery_information(request):
    items_in_cart = 0
    if request.user.is_authenticated:
        items_in_cart = len(Cart.objects.filter(user=request.user))
    return render(request, 'app/delivery_information.html', {'items_in_cart': items_in_cart})


def contactUs(request):
    if request.method == 'GET':
        form = contactformemail()
    if request.method == 'POST':
        form = contactformemail(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            send_mail(
                subject,
                message,
                email,
                ['theprogrammerneo@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, 'Thank You!')
    items_in_cart = 0
    if request.user.is_authenticated:
        items_in_cart = len(Cart.objects.filter(user=request.user))
    return render(request, 'app/contact_us.html', {'form': form, 'items_in_cart': items_in_cart})


def wishlist(request, pk):
    if request.user.is_authenticated:
        if request.method == 'GET':
            product_id = pk
            item_already_in_cart = Cart.objects.filter(
                Q(product=pk) & Q(user=request.user)).exists()
            # print(item_already_in_cart)
            # if item_already_in_cart:
            #     c = Cart.objects.get(Q(product=pk) & Q(user=request.user))
            #     c.delete()
            if not item_already_in_cart:
                product = Product.objects.get(id=product_id)
                user = request.user
                item_already_in_wishlist = Wishlist.objects.filter(
                    Q(product=pk) & Q(user=request.user)).exists()
                if not item_already_in_wishlist:
                    Wishlist(user=user, product=product).save()
                # items = Wishlist.objects.filter(user=user)
            return redirect('wishlist_items')


def wishlist_items(request):
    if request.user.is_authenticated:
        items = Wishlist.objects.filter(user=request.user)
        newitems = []
        for p in items:
            if not (Cart.objects.filter(Q(product=p.product.id) & Q(user=request.user)).exists()):
                newitems.append(p)
            else:
                c = Wishlist.objects.get(
                    Q(product=p.product.id) & Q(user=request.user))
                c.delete()

        newitems = [p if not (Cart.objects.filter(
            Q(product=p.product.id) & Q(user=request.user)).exists()) else None for p in items]
        if newitems:
            return render(request, 'app/wishlist.html', {'prod': newitems})
        else:
            return render(request, 'app/emptywishlist.html')


def remove_from_wishlist(request):
    user = request.user
    product_id = request.GET.get('prod_id2')
    c = Wishlist.objects.get(Q(product=product_id))
    c.delete()
    return redirect('wishlist_items')
