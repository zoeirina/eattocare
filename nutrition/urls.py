from django.urls import path
from . import views

app_name = 'nutrition'

urlpatterns = [
    path('', views.product_catalog, name='catalog'),
    path(
        'categoria/<slug:category_slug>/',
        views.product_catalog,
        name='product_list_by_category',
    ),
    path('sobre-mi/', views.about_view, name='about'),
]