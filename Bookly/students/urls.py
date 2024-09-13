from django.urls import path, include
from students.views import *
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('index/', index, name='students.index'),
    path('show/<int:id>', show, name='students.show'),
    path('delete/<int:id>', delete, name='students.delete'),
    path('edit/<int:id>', edit, name='students.edit'),
    path('profile/', profile, name='profile'),
    path('profile/<int:pk>', login_required(AccountsDetailView.as_view()), name='students.profile'),
    path("signup", StudentCreateView.as_view(), name="signup"),
]