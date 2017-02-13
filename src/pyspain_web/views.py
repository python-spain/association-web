# -*- coding: utf-8 -*-

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import get_model
from django.shortcuts import get_object_or_404

from pyspain.views import GenericTemplateView
from pyspain_web import utils


class MarkupMixin(object):
    def markup(self, text, truncate=None):
        return utils.markup(text, truncate)


class Home(MarkupMixin, GenericTemplateView):
    tmpl_name = "web/home.jinja"

    def get_context_data(self):
        ctx = super().get_context_data()

        article_cls = get_model("content", "Article")

        queryset = article_cls.objects.all().order_by("-created_at")
        paginator = Paginator(queryset, 5)

        page = self.request.GET.get('page')
        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            articles = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            articles = paginator.page(paginator.num_pages)

        ctx["paginator"] = paginator
        ctx["page"] = articles

        return ctx


class Article(MarkupMixin, GenericTemplateView):
    tmpl_name = "web/article.jinja"

    def get_context_data(self):
        ctx = super().get_context_data()
        article_cls = get_model("content", "Article")
        article = get_object_or_404(article_cls, slug=self.kwargs["slug"])

        ctx["article"] = article
        return ctx


class Page(MarkupMixin, GenericTemplateView):
    tmpl_name = "web/page.jinja"

    def get_context_data(self):
        ctx = super().get_context_data()

        page_cls = get_model("content", "Page")
        ctx["page"] = get_object_or_404(page_cls, slug=self.kwargs["slug"])

        return ctx


class Faq(MarkupMixin, GenericTemplateView):
    tmpl_name = "web/faq-list.jinja"

    def get_context_data(self):
        ctx = super().get_context_data()
        faq_entry_cls = get_model("content", "FaqEntry")
        ctx["entries"] = faq_entry_cls.objects.all().order_by("question")
        return ctx


class CommunityEvents(MarkupMixin, GenericTemplateView):
    tmpl_name = "web/community-events.jinja"

    def get_context_data(self):
        ctx = super().get_context_data()
        faq_entry_cls = get_model("community", "Event")

        queryset = faq_entry_cls.objects.all().order_by("-created_at")
        paginator = Paginator(queryset, 5)

        page = self.request.GET.get('page')
        try:
            events = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            events = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            events = paginator.page(paginator.num_pages)

        ctx["paginator"] = paginator
        ctx["page"] = events
        return ctx
