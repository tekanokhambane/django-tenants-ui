from django.urls import path, include
from django.conf.urls import url
from .admin import team_urls
from .admin import urls as admin_urls
from .profiles import urls as profile_urls
urlpatterns = [
    path('admin/', include(admin_urls)),
    path('admin/', include(team_urls)),
    path('profiles/', include(profile_urls)),
    url(r'support/', include('multitenancy.helpdesk.urls')),
]
