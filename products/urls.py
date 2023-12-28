
# ecommerce/urls.py

from django.urls import path

from products import views as v



urlpatterns = [
    path('', v.index , name='home'),
    path('productdetail/<int:pk>', v.ProductDetailView.as_view() , name='productdetail'),
]

# This assumes you have a separate `views.py` file where you define your views.
