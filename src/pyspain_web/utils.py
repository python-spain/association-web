# -*- coding: utf-8 -*-

from django.utils.text import Truncator
from markdown import markdown

def markup(text, truncate=None):
    if truncate is not None:
        t = Truncator(text)
        text = t.chars(truncate)

    return markdown(text, safe_mode=False)
