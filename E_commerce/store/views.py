from django.shortcuts import render, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
import datetime
# Create your views here.

def Items(request):
    user = request.user
    total_items = 0
    if user.is_authenticated:
        customer = Customer.objects.get(user=user)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total_items = order.get_total_items

    return total_items

def Store(request):

    total_items = Items(request)
    products = Product.objects.all()
    context = {
        'products':products,
        'shipping':False,
        'total': total_items
    }
    return render(request, 'store/store.html', context)

@login_required(login_url='login')
def Cart(request):
    user = request.user
    if user.is_authenticated:
        customer = user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_total = order.get_cart_total

    else:
        items = []
        cart_total = 0
    context = {
        'items':items,
        'count':Items(request),
        'total_price':cart_total,
        'shipping':False,
        'total':Items(request)
    }
    return render(request, 'store/cart.html', context)

@login_required(login_url='login')
def Checkout(request):

    user = request.user
    if user.is_authenticated:
        customer = user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all
    else:
        order = {
            'get_cart_total':0,
            'get_total_items':0,
            'shipping':False,
            
        }
        items = []
    context = {
        'items':items,
        'order':order,
        'total':Items(request)
    }
    return render(request, 'store/checkout.html', context)


@login_required(login_url='login')
def updateItem(request):
    user = request.user
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    customer = user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False) 
    orderItem, created = OrderItem.objects.get_or_create(product=product, order=order)

    if action == 'add':
        orderItem.quantity = orderItem.quantity + 1
    elif action == 'remove':
        orderItem.quantity = orderItem.quantity - 1
    orderItem.save()

    if orderItem.quantity == 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def processOrder(request):
    
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    user = request.user
    if user.is_authenticated:
        customer = user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transcation_id = transaction_id

        if total == float(order.get_total_items):
            order.complete = True
        order.save()

        if order.shipping ==  True:
            ShippingAddress.objects.create(
                customer = customer,
                order = order,
                address = data['shipping']['address'],
                city = data['shipping']['city'],
                state = data['shipping']['state'],
                zipcode = data['shipping']['zipcode']

            )
    return JsonResponse('Payment complate..', safe=False)


def ShopSingle(request, pro_id):
    user = request.user
    product = get_object_or_404(Product, id=pro_id)
    properties = product.properties_product

    context = {
        'product':product,
        'properties':properties,
        'total':Items(request)
    }
    return render(request, 'store/shopsingle.html', context)
