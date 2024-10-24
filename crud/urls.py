from django.urls import path
from crud import views


urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register_request,name='register'),
    path('login/',views.login_request,name='login'),
    path('logout/',views.logout_crud,name='logout'),
    path('<int:id>', views.detail, name='detail'),
    path('delete/<int:id>', views.delete , name='delete'),
    path('update/<int:id>', views.update , name='update'),
    path('create/', views.create , name='create'),
    ]