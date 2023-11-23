from django.urls import include, path

urlpatterns = [
    path('', include('src.profiles.urls'))
]
