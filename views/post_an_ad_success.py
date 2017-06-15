from django.shortcuts import render, get_object_or_404
from Portal.models import Listing

def post_an_ad_success(request, code):
  listing = get_object_or_404(Listing, code=code, status__in=['P'])
  return render(request, 'Portal/post_an_ad_success.html', locals())