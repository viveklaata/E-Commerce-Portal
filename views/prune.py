from django.shortcuts import redirect
from django.conf import settings
from django.utils import timezone
from Portal.models import Listing

def prune(request, pin):
  # todo: instead of a PIN, use decorator to check for admin/staff login in session
  if pin == settings.ADMIN_TOOLS_PIN:
    listings = Listing.objects.filter(status__in=['A', 'P', 'S'])

    for listing in listings:
      delta = timezone.localtime(timezone.now()) - timezone.localtime(listing.added_on)

      if delta.days >= settings.LISTING_EXPIRY:
        listing.status = 'E'
        listing.save()

  return redirect('Portal:home')