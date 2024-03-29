"""vgucsi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from csi import views 
from . import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500, handler403, handler400

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path("events/", views.events, name="events"),
    path("team/", views.team, name="team"),
    path("contact/", views.contact, name="contact"),
    path("blog/", views.blog, name="blog"),
    path("blogpost/<int:id>", views.blogpost, name="blogHome"),
    path("eventspost/<int:eid>", views.eventspost, name="eventHome"),

    
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

handler404 = views.error_404
handler500 = views.error_500
handler403 = views.error_403
handler400 = views.error_400
