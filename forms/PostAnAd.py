from django.forms import *
from Portal.models import Listing

class PostAnAd(ModelForm):
  title = CharField(required=True,
                    widget=TextInput(attrs={
                      'class': 'PostAnAd__title',
                      'placeholder': 'Enter brand and name of the item.',
                      'autofocus': 'autofocus'
                    }))

  location = CharField(required=True,
                       widget=TextInput(attrs={
                        'class': 'PostAnAd__location',
                        'placeholder': 'Enter city, state and country.'
                       }))

  contact_info = CharField(required=True,
                           widget=TextInput(attrs={
                            'class': 'PostAnAd__contact_info',
                            'placeholder': 'Enter a way for sellers to contact you (e-mail, phone number, etc.)'
                           }))

  email = EmailField(required=True,
                           widget=TextInput(attrs={
                            'class': 'PostAnAd__email',
                            'placeholder': 'Enter your e-mail address'
                           }))

  class Meta:
    model = Listing

    fields = ['title',
              'description',
              'price',
              'condition',
              'location',
              'contact_info',
              'email',
              'photo_1',
              'photo_2',
              'photo_3',
              'photo_4']

    widgets = {
      'description': Textarea(attrs={
                  'class': 'PostAnAd__description',
                  'placeholder': 'Enter item details like size, color, offset, etc.'
               }),
      'price': TextInput(attrs={
                  'class': 'PostAnAd__price',
                  'placeholder': 'Enter price and currency (USD, CAD, EUR, etc).',
               }),
      'condition': Select(attrs={
                  'class': 'PostAnAd__condition'
               }),
      'photo_1':  FileInput(attrs={
                  'class': 'PostAnAd__photo_1'
               }),
      'photo_2':  FileInput(attrs={
                  'class': 'PostAnAd__photo_2'
               }),
      'photo_3':  FileInput(attrs={
                  'class': 'PostAnAd__photo_3'
               }),
      'photo_4':  FileInput(attrs={
                  'class': 'PostAnAd__photo_4'
               })
    }

  def clean(self):
    cleaned_data = super(PostAnAd, self).clean()
    limit = 5 * 1024 * 1024 # First number is MB
    has_photo = False

    for photo in ('photo_1', 'photo_2', 'photo_3', 'photo_4'):
      if cleaned_data[photo]:
        has_photo = True
        clean_photo = cleaned_data[photo]

        if clean_photo.size > limit:
          self.add_error(photo, 'File size should not be greater than 5 MB!')

        if clean_photo.name.endswith('.gif') or clean_photo.name.endswith('.gifv'):
          self.add_error(photo, 'Cannot upload GIFs!')

    if not has_photo:
      self.add_error('photo_1', 'You must upload at least one image!')