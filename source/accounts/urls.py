from django.urls import path
from .views import login_view, logout_view, register_view, user_activate_view, UserDetailView, \
     UserPasswordChangeView, UserView, update_profile

app_name = 'accounts'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('activate/<token>/', user_activate_view, name='user_activate'),
    path('<int:pk>/', UserDetailView.as_view(), name='detail'),
    # path('<int:pk>/update', UserPersonalInfoChangeView.as_view(), name='update'),
    path('<int:pk>/update/', update_profile, name='update'),
    path('<int:pk>/password_change', UserPasswordChangeView.as_view(), name='password_change'),
    path('user/', UserView.as_view(), name='user'),
]

