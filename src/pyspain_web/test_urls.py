#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import django

if django.VERSION >= (1, 9, 0):
    from django.urls import resolve
else:
    from django.core.urlresolvers import reverse


def test_home():
    assert reverse('home') == '/'


def test_faq():
    assert reverse('faq-list') == '/faq'


def test_article():
    assert reverse('article', kwargs={'slug': 'test'}) == '/article/test'


def test_page():
    assert reverse('page', kwargs={'slug': 'test'}) == '/page/test'


def test_community_events():
    assert reverse('community-events') == '/community/events'


def test_rss_news():
    assert reverse('rss-news') == '/rss/news'


def test_rss_events():
    assert reverse('rss-events') == '/rss/events'


if __name__ == "__main__":
    pytest.main()
