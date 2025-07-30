from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, Category
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from .cart import Cart

# Create your views here.


# def index(request):
#     return render(request, 'product/index.html')

def cart_summary(request):
    cart = Cart(request)

    products = cart.get_products()
    quantity = cart.get_quantity()

    total = cart.get_total_price()

    data = {
        'products': products,
        'quantites': quantity,
        'total': total,
    }

    return render(request,'product/cart_summary.html', context=data)

def cart_add(request):
    cart = Cart(request)


    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        quantity = request.POST.get('product_quantity')


        product = get_object_or_404(Product, id=product_id)


        cart.add(product=product, quantity=quantity)

        return JsonResponse({'product_id':product_id})
    return HttpResponse('Cart Summer')


def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        quantity = request.POST.get('product_quantity')
        product = get_object_or_404(Product, id=product_id)

        cart.product_update(product, quantity)

    return JsonResponse({"status":"salom"})

def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = request.POST.get('product_id')
        cart.delete_product(product_id)
        return JsonResponse({'status':'salom'})

class ProductListView(ListView):
        model = Product
        template_name = 'product/index.html'
        context_object_name = 'products'
        
        
    

class CategoryProductList(DetailView):
    model = Category
    template_name = 'product/categories.html'
    context_object_name = 'mahsulotlar'

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryProductList, self).get_context_data(*args, **kwargs)
        category = context['mahsulotlar']
        context['mahsulotlar'] = category.products.all()
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/detail.html'
    context_object_name = 'product'


