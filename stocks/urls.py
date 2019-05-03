"""stocks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import debug_toolbar
from django.conf.urls.static import static
from django.conf import settings
from project import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('project/', include('project.urls')),
    path('learning/', include('learning.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('__debug__/', include(debug_toolbar.urls)),

    path('accounts/role/', views.RoleView.as_view(), name='role-list'),
    path('accounts/dealer/<int:pk>/', views.DealerRoleView.as_view(), name='dealer-home'),
    path('accounts/distributor/<int:pk>/', views.DistributorRoleView.as_view(), name='distributor-home'),
    path('accounts/create_staff/', views.create_staff, name='create-staff'),
    path('accounts/staff_list/', views.StaffList.as_view(), name='staff-list'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
