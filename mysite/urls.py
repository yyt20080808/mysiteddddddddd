from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from firstproject import views as fistproject_View
from useMysql import views as useMysql_View

urlpatterns = [
    url(r'^$', fistproject_View.index, name='index'),
    url(r'^column/(?P<column_slug>[^/]+)/$',fistproject_View.column_detail,name = 'column'),
    url(r'^article/(?P<pk>\d+)/(?P<article_slug>[^/]+)/$',fistproject_View.article_detail,name = 'article'),
    url(r'^login/$',useMysql_View.login_auth,name='login_auth'),
    url(r'^logout/$',useMysql_View.logout_view,name='logout_view'),
    url(r'^ueditor/',include('DjangoUeditor.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^baidumap/$',fistproject_View.baidumap_view,name='baidumapView'),
    url(r'^file/', include('useMysql.urls')),
]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(
        settings.MEDIA_URL,document_root=settings.MEDIA_ROOT
    )