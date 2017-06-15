from django.shortcuts import render

def help(request):
  return render(request, 'Portal/help.html', locals())