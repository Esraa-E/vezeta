from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('sun',views.snu,name='sun'),
    path('detail/<int:id>',views.details,name='detail'),
    path('reserv/<int:id>',views.reserv,name='reserv'),
    path('book/<int:id>',views.book,name='book'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('signup',views.signup,name='signup'),
    path('logout',auth_views.LogoutView.as_view(),name='logout'),
    path('login',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('settings/change_password',auth_views.PasswordChangeView.as_view(template_name='change_password.html'),name='password_change'),
    path('settings/change_password/done',auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),name='password_change_done'),
    path('comment/<int:id>',views.commentt,name='comment'),
    path('profile',views.proff,name='profile'),
    path('search',views.searcch,name='search'),
]
