from django.urls import path
from . import views as accountsViews

urlpatterns = [
    path('', accountsViews.signupUsers, name='signup'),
    path('login/', accountsViews.login_view, name='login'),
    path('logout/', accountsViews.logoutUsers, name='logout'),
    path('AfterLogout/', accountsViews.AfterLogout, name='afterlogout'),
]