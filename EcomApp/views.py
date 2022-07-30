from django.shortcuts import render,HttpResponse
from EcomApp.models import Setting
from product.models import Product,Category
from orderApp.models import ShopCart
# Create your views here.
def Home(request):
    current_user=request.user
    cart_product = ShopCart.objects.filter(user_id=current_user.id)
    total_amount = 0
    for p in cart_product:
        total_amount += p.product.new_price*p.quantity


    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    sliding_image = Product.objects.all().order_by('id')[:5]
    latest_product= Product.objects.all().order_by('-id')
    product= Product.objects.all()
    context={
    'category': category,
    'setting': setting,
    'sliding_image':sliding_image,
    'latest_product':latest_product,
    'product':product,
    'cart_product':cart_product,
    'total_amount':total_amount,
    }
    return render(request,'home.html',context)
def product_single(request,id):
    category = Category.objects.all()

    setting = Setting.objects.get(id=1)
    single_product=Product.objects.get(id=id)
    context={'setting': setting,'category': category, 'single_product':single_product}
    return render(request,'single.html',context)

def category_product(request,id,slug):
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    sliding_image = Product.objects.all().order_by('id')[:5]
    product_cat=Product.objects.filter(category_id=id)
    context={
        'sliding_image':sliding_image,
        'product_cat': product_cat,
        'category': category,
        'setting': setting}
    return render(request,'categoryproduct.html',context)
