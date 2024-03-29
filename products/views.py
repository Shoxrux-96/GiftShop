from django.shortcuts import render
from .models import Category,Customer,Product,Order,mashxur
# Create your views here.
def home(request):
    products = Product.objects.all()[:8]
    categorys = Category.objects.all()
    mashxurs = mashxur.objects.all()
    return render(request, 'index.html', {'products':products,
                                          'categorys':categorys,
                                          'mashxurs':mashxurs})

def contact_view(request):
    return render(request, 'contact.html')