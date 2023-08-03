"""
URL configuration for protfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from farmcom import views
app_name='farmcom'

urlpatterns = [
   path('about.html', views.about, name='about.html'),
   path('contact.html',views.contact, name='contact.html'),
   path('get_a_quote.html', views.get_a_quote, name='get_a_quote.html'),
   path('pricing.html', views.pricing, name='pricing.html'),
   path('index.html', views.index, name='index.html'),
   path('sample_inner_page.html', views.sample_inner_page, name='sample_inner_page.html'),
   path('service_details.html', views.service_details, name='service_details.html'),
   path('services.html', views.services, name='services.html'),


    path('info', views.info, name = 'info'),
        path('register', views.register, name = 'register'),
        path('login_reg', views.login_reg, name = 'login_reg'),
        path('logout', views.logoutuser, name = 'logout'),


        path('product', views.product, name='product'),
    path('products', views.products, name='products'),
    path('order/<int:id>', views.order, name='order'),
    path('kart', views.kart  , name='kart'),

    ]