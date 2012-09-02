A simple, pluggable app for attaching meta tags to objects with their own views.

Installation
============

As it is available on the Python Package Index, you can install django-metatags using your favorite package manager::

   pip install django-metatags
   
   easy_install django-metatags

You can also install directly from the git master branch using the pip package manager::

   pip install git+http://github.com/degenhard/django-metatags.git#egg=metatags

Or you can download django-metatags and install locally::

   setup.py install

Usage
=====

To install, add django-metatags to your ``INSTALLED_APPS`` in your Django settings module::

   INSTALLED_APPS = [
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.sites',
      'django.contrib.messages',
      ...
      'metatags
   ]

Run ``./manage.py syncdb`` to create the requisite database tables. Then, to any ModelAdmin that you'd like the Meta Tag inline to appear, simply add it::

   from django.contrib import admin
   from metatags.admin import MetaTagInline
   from someapp.models import SomeModel
   
   class SomeModelAdmin(admin.ModelAdmin):
       inlines = [
           MetaTagInline
       ]
   admin.site.register(SomeModel, SomeModelAdmin)
