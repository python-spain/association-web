#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import django

def test_current_django_version():
    assert django.VERSION >= (1, 6, 1)


if __name__ == '__main__':
    pytest.main()
