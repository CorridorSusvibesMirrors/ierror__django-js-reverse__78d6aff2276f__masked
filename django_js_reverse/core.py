# -*- coding: utf-8 -*-
import json
import re
import sys
from distutils.version import LooseVersion

import django
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

from . import rjsmin
from .js_reverse_settings import (JS_EXCLUDE_NAMESPACES, JS_GLOBAL_OBJECT_NAME,
                                  JS_INCLUDE_ONLY_NAMESPACES, JS_MINIFY,
                                  JS_VAR_NAME)

try:
    from django import urls as urlresolvers
except ImportError:
    from django.core import urlresolvers

if sys.version < '3':
    text_type = unicode  # NOQA
else:
    text_type = str

JS_IDENTIFIER_RE = re.compile(r'^[$A-Z_][\dA-Z_$]*$')






