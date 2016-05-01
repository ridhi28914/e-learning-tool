from django.conf.urls import url
from . import views


from django.conf import settings
from django.conf.urls.static import static

app_name = 'birds'
urlpatterns = [
	

    url(r'^$', views.index, name='index'),
    url(r'^welcome/$',views.wel, name='wel'),
    url(r'^welcome/$',views.progress, name='progress'),
    #url(r'^welcome/(?P<name>[a-z]+)/$',views.welname, name='welname'),

    url(r'^welcome/vocabulary/$',views.vocab, name='vocab'),
    url(r'^welcome/vocabulary/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^welcome/vocabulary/(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

    url(r'^welcome/mathematics/$',views.maths, name='mathematics'),
    url(r'^welcome/mathematics/(?P<question_id>[0-9]+)/$', views.detailmaths, name='detailmaths'),
    url(r'^welcome/mathematics/(?P<question_id>[0-9]+)/vote/$', views.votemaths,  name='votemaths'),
]
#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)