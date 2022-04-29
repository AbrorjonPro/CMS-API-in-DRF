"""codecraftuz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from api.views import PasswordResetView, PasswordResetConfirmView
from dj_rest_auth.registration.views import VerifyEmailView

from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("api.urls", namespace='api')),
    path('auth/password/reset/', PasswordResetView.as_view(), name="password_reset"),
    path('auth/password/reset/confirm/', PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('auth/', include("dj_rest_auth.urls")),
    path('auth/account-confirm-email/', VerifyEmailView.as_view(), name="account_verification_email_sent"),
    path('auth/registration/', include("dj_rest_auth.registration.urls")),
    path('docs/', include_docs_urls(title='Codecraft.uz Documentation')),
    path('ckeditor/', include('ckeditor_uploader.urls'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

