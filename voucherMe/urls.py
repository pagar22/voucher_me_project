
from django.urls import path
from voucherMe import views

app_name = 'voucherMe'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('profile/<str:username>', views.profile, name='profile'),
    path('business/', views.all_businesses, name='all_businesses'),
    path('posts/', views.all_posts, name='all_posts'),
    path('search/<str:type>', views.search, name='search'),
    path('<str:username>/business/add_business/', views.add_business, name='add_business'),
    path('business/<slug:business_name_slug>/', views.show_business, name='show_business'),
    path('business/<slug:business_name_slug>/add_post/', views.add_post, name='add_post'),
    path('business/<slug:business_name_slug>/<int:post_id>/', views.show_post, name='show_post'),
    path('add_data/', views.add_data, name='add_data'),
]
