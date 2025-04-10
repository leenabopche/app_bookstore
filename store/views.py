from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Book

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('book_list')
        else:
            return render(request, 'store/login.html', {'error': 'Invalid credentials'})
    return render(request, 'store/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'store/book_list.html', {'books': books})

@login_required
def add_to_cart(request, book_id):
    cart = request.session.get('cart', [])
    if book_id not in cart:
        cart.append(book_id)
        request.session['cart'] = cart
    return redirect('book_list')

@login_required
def cart_view(request):
    cart = request.session.get('cart', [])
    books = Book.objects.filter(id__in=cart)
    return render(request, 'store/cart.html', {'books': books})


def show_cart(request):
    book_ids = request.session.get('cart', [])
    books = Book.objects.filter(id__in=book_ids)
    last_page = request.session.get('last_page', 'book_list')
    return render(request, 'store/cart.html', {'books': books, 'last_page': last_page})


from django.shortcuts import render

def cart_view(request):
    return render(request, 'store/cart.html')
