# -*- coding: utf-8 -*-

from django.views.generic import View
from django.template import RequestContext, loader
from django.shortcuts import render_to_response

from . import http


class GenericView(View):
    response_cls = http.HttpResponse
    content_type = "text/html"

    def init(self, *args, **kwargs):
        pass

    def get_context_data(self):
        context = {"view": self}
        context.update(self.kwargs)
        return context

    def dispatch(self, request, *args, **kwargs):
        self.init(request, *args, **kwargs)
        return super(GenericView, self).dispatch(request, *args, **kwargs)

    def render(self, template=None, context=None, data=None,
               response_cls=None, content_type=None):

        output_data = data or b""

        if template:
            _context = self.get_context_data()
            _context.update(context or {})

            context_instance = RequestContext(self.request)
            output_data = loader.render_to_string(
                                template, _context,
                                context_instance=context_instance)

        if content_type is None:
            content_type = self.content_type

        if not response_cls:
            response_cls = self.response_cls

        return response_cls(output_data, content_type=content_type)


class GenericTemplateView(GenericView):
    tmpl_name = None

    def get_tmpl_name(self):
        if self.tmpl_name is None:
            raise ValueError("tmpl_name attr must be a valid template name")
        return self.tmpl_name

    def get(self, request, *args, **kwargs):
        return self.render(self.get_tmpl_name())
