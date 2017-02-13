
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    url(r'^', include('pyspain_backoffice.urls')),
    url(r'^', include('pyspain_web.urls')),
)


def mediafiles_urlpatterns():
    """
    Method for serve media files with runserver.
    """

    _media_url = settings.MEDIA_URL
    if _media_url.startswith('/'):
        _media_url = _media_url[1:]

    from django.views.static import serve
    return patterns('',
        (r'^%s(?P<path>.*)$' % _media_url, serve,
            {'document_root': settings.MEDIA_ROOT})
    )


urlpatterns += staticfiles_urlpatterns(prefix="/static/")
urlpatterns += mediafiles_urlpatterns()


# Special resolvers pages rendered
# via jinja template engine.
from django_jinja import views
handler403 = views.PermissionDenied.as_view()
handler404 = views.PageNotFound.as_view()
handler500 = views.ServerError.as_view()
