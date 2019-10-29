from django.urls import path

from .views import login_view, logout_view, register_view, user_activate_view, UserDetailView, \
    UserPersonalInfoChangeView

app_name = 'accounts'

urlpatterns = [

    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('activate/<token>/', user_activate_view, name='user_activate'),
    path('<int:pk>/', UserDetailView.as_view(), name='detail'),
    path('<int:pk>/update', UserPersonalInfoChangeView.as_view(), name='update')
]