from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'tcapp'
urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',auth_views.LoginView.as_view(),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('detail/',views.DetailPage.as_view(),name='detail'),
    path('<int:pk>',views.InfoDetail.as_view(),name='detailview'),
    path('update/<int:pk>',views.InfoUpdate.as_view(),name='update'),
    path('delete/<int:pk>',views.InfoDelete.as_view(),name='delete'),
]
