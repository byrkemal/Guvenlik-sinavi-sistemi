from django.urls import path
from . import views

urlpatterns = [

    path('giris/', views.giris_yap, name='giris'),
    path('sinav/', views.sinav_view, name='sinav'),
    path('sonuc/', views.sinav_sonuc, name='sinav_sonuc'),
    path('admin/sonuclar/', views.admin_sonuc_listesi, name='admin_sonuclar'),
    
]
