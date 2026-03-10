from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views  # ✅ Add this

urlpatterns = [
    path('admin/', admin.site.urls),       
    path('api/', include('api.urls')),     
    path('', include('courses.urls')),     

    # ✅ Add these two lines
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]
