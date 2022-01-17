from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chat.api.urls'), name="chat"),
    path('auth/', include('dj_rest_auth.urls'))
]
