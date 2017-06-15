## Portal

A Django app for listing various items for sale. It's like Craigslist, but much simpler.

This app has basic models for Categories, Subcategories, Brands, etc. There is no cart or check-out system. Manual verification of listings is still required.

### Requirements

- Python 2.7
- Django 1.10.x and above

### Settings

Please add the following fields to your settings.py:

```markdown
ALLOW_MAIL = False
ADMIN_TOOLS_PIN = '1234'
```
