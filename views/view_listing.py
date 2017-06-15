from django.shortcuts import render, get_object_or_404
from Portal.models import Listing

def view_listing(request, code):
  listing = get_object_or_404(Listing, code=code, status__in=['A', 'S'])
  return render(request, 'Portal/view_listing.html', locals())