from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('store/',views.store,name='store'),
    path('<slug:category_slug>/',views.store,name='items_by_category'),
]
