from django.urls import path
from . import views
app_name='store_app'

urlpatterns=[
    path('',views.index,name='index'),
    # path('',views.departments,name='departments'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout, name='logout'),
    path('user_page',views.user_page,name='user_page'),
]