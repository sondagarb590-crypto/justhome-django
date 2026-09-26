from django.urls import path
from . import views

urlpatterns = [
    # Home & Search
    path('', views.home, name='home'),

    # Properties
    path('properties/', views.property_list, name='property_list'),
    path('properties/<int:pk>/', views.property_detail, name='property_detail'),
    path('properties/add/', views.add_property, name='add_property'),
    path('properties/<int:pk>/edit/', views.edit_property, name='edit_property'),
    path('properties/<int:pk>/delete/', views.delete_property, name='delete_property'),
    path('my-properties/', views.my_properties, name='my_properties'),

    # Auth
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Contact & Newsletter
    path('contact/', views.contact_view, name='contact'),
    path('newsletter/subscribe/', views.newsletter_subscribe, name='newsletter_subscribe'),

    # Profile
    path('profile/', views.profile_view, name='profile'),
]
