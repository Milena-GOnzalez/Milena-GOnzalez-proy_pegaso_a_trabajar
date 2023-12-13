from django.contrib import admin
from django.urls import path
from principal.views import holamundo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', holamundo, name="inicio"),
]
