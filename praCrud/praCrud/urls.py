from django.contrib import admin
from django.urls import path
import praCrudApp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', praCrudApp.views.main, name='main'),
    path('new/create', praCrudApp.views.create, name='create'),
    path('post/<str:id>', praCrudApp.views.detail, name='detail'),
    path('edit/<str:id>', praCrudApp.views.edit, name='edit'),
    path('update/<str:id>', praCrudApp.views.update, name='update'),
    path('delete/<str:id>', praCrudApp.views.delete, name='delete'),
]