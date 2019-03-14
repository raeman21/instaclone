from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$',views.index,name='home'),
    url(r'^new/images',views.new_image, name= 'new-image'),
    url(r'^update',views.update_profile, name= 'update'),
    url(r'^profile',views.profile, name= 'profile'),
    url(r'^photo/(\d+)', views.image, name = "myPhoto"),
    url(r'^like/$',views.like_image, name= 'like_image'),
    url(r'^user/(?P<username>\w+)', views.user_profile, name = "user_profile" ),
    url(r'^search/', views.search, name='search'),
    url(r'^follow/$', views.follow_user, name="follow_user")
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)