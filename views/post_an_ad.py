from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from Portal.forms import PostAnAd
from Portal.helpers import generate_listing_code

def post_an_ad(request):
  if request.method == 'POST':
    form = PostAnAd(request.POST, request.FILES)

    if form.is_valid():
      new_listing = form.save(commit=False)

      # Generate a random listing code, then actually save
      new_listing.code = generate_listing_code()
      new_listing.save()

      # Send notif email
      if settings.ALLOW_MAIL or False:
        send_mail(
            'New listing!',
            'Title: '+str(new_listing.title)+'\nLink: http://website.com/listing/'+str(new_listing.code),
            settings.FROM_EMAIL,
            settings.RECIPIENT_LIST,
            fail_silently=True,
        )

      return redirect('Portal:post_an_ad_success', code=new_listing.code)
      
  else:
    form = PostAnAd()

  return render(request, 'Portal/post_an_ad.html', locals())