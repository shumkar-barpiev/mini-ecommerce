from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Member



def products_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.newmanager.all()
    if category_slug:
        category = get_object_or_404(Category,slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'index.html',    {'categories': categories,
                                             'category': category,
                                             'products': products, })


def product_detail(request, id):
    product = get_object_or_404(Product, id= id)
    return render(request, 'product_detail.html', {'product': product})


def login(request):
    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            member = Member.objects.get(username=request.POST['username'], password=request.POST['password'])
            global tempuser
            global temppassword
            tempuser = request.POST['username']
            temppassword = request.POST['password']
            return render(request, 'userprofile.html', {'member': member})
        else:
            context = {'msg': 'Invalid username or password!!!'}
            return render(request, 'login.html', context)
    else:
        return render(request, 'login.html', {})


def register(request):
    if request.method == 'POST':
        member = Member(username=request.POST['username'], password=request.POST['password'],
                        firstname=request.POST['firstname'], lastname=request.POST['lastname'])
        member.save()
        return redirect('/')
    else:
        return render(request, 'register.html')


def myprofile(request):
    if request.method == 'POST':

        Member.objects.filter(password=temppassword, username=tempuser).update(username=request.POST['un'],
                                                                               password=request.POST['pw'],
                                                                               firstname=request.POST['fn'],
                                                                               lastname=request.POST['ln'])
        print(tempuser)
        print(temppassword)
        return redirect('/')
    else:
        return render(request, 'userprofile.html')

