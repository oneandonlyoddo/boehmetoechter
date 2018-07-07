from django.conf.urls.defaults import *
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^\S*/shop/products/', lambda x: redirect('/shop/products/')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^awards/', include('auszeichnungen.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    #url(r'^catalog/', include('shop_categories.urls')),
    url(r'^shop/', include('shop.urls')),
    url(r'^events/', include('simple_events.urls')),
    url(r'^', include('cms.urls')),
    #url(r'^blog/', include('zinnia.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns