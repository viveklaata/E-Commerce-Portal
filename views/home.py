from django.shortcuts import render
from Portal.models import Category

def home(request):
  categories = Category.objects.all()
  return render(request, 'Portal/home.html', locals())