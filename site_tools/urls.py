from django.urls import path, include

from django.contrib import admin

import memba.views

admin.autodiscover()


# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", memba.views.index, name="index"),
    path("db/", memba.views.db, name="db"),
    path("admin/", admin.site.urls),
]
