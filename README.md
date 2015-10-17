Django gettr command
===

I love the Qt library, surely some Django developers love it too, which could explain why the *"events"* are called *"signals"*.
Sadly they follow the convention of naming the xgettext methods with an underscore '_'. It feels weird to me call any 
variable or method like that so, I've made this command which will add the tr keyword to the xgettext options. It will detect all the strings that detect the default [makemessages](https://docs.djangoproject.com/en/1.8/ref/django-admin/#django-admin-makemessages) as well as strings translated with the tr keyword.

**Example:**

	from django.utils.translation import ugettext_lazy as tr
	
	def hello_view(request):
		return str(tr('Hello'))

Installation
---
Just copy the `management` folder to any of your [apps](https://docs.djangoproject.com/en/1.8/intro/tutorial01/#creating-models) or just copy the `management/commands/gettr.py` to an existent [management module](https://docs.djangoproject.com/en/1.8/howto/custom-management-commands/)

Usage
---

it's the same as the default `makemessages` but using `gettr` instead.

**Example:**

	python manage.py gettr --locale=es
	