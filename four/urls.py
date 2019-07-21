from django.contrib import admin
from django.urls import path, include
import fou.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',fou.views.home, name="home"),
    path('fou1/',include('fou1.urls')),
    path('fou/',include('fou.urls')),
    path('accounts/', include('accounts.urls')),
]
