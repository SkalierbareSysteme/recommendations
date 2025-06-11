"""
URL configuration for recommendations project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from recommendations_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.healthcheck, name='healthcheck'),
    path('recommendations/', views.get_all_recommendations, name='get_all_recommendations'),
    path('recommendations/<uuid:recommendation_id>/', views.get_recommendation, name='get_recommendation'),
    path('recommendations/new/', views.add_recommendation, name='add_recommendation'),
    path('recommendations/delete/<uuid:recommendation_id>/', views.delete_recommendation, name='delete_recommendation'),
    path('recommendations/update/rec_amount/<uuid:recommendation_id>/', views.update_amount_of_recommendations, name='update_amount_of_recommendations'),
]
