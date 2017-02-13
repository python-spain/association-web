# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

from . import views
from . import rss

urlpatterns = patterns('',
    url(r"^$", views.Home.as_view(), name="home"),
    url(r"^article/(?P<slug>[\w\d\-]+)$", views.Article.as_view(), name="article"),
    url(r"^faq$", views.Faq.as_view(), name="faq-list"),
    url(r"^page/(?P<slug>[\w\d\-]+)$", views.Page.as_view(), name="page"),
    url(r"^community/events$", views.CommunityEvents.as_view(), name="community-events"),
    url(r"^rss/news$", rss.ArticlesFeed(), name="rss-news"),
    url(r"^rss/events$", rss.EventsFeed(), name="rss-events"),
)
