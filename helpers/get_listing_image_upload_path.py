def get_listing_image_upload_path(instance, filename):
  return 'listing/{0}/{1}'.format(instance.code, filename)