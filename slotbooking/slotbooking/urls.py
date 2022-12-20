
from django.contrib import admin
from django.urls import path
from mysql_data.views import Home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home.index,name="index_page"),
    path('data/',Home.index_home,name="index")
]
