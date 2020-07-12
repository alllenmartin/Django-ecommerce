from django.shortcuts import render

def store(request):
    return render(request, 'store.html', {'store':store})

def cart(request):
    return render(request, 'cart.html', {'cart':cart})

def checkout(request):
    return render(request, 'checkout.html', {'checkout':checkout})