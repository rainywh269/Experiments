#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import dependencies.git_http_backend.git_http_backend

ROOT = os.path.abspath(os.path.abspath(os.path.dirname( __file__)))
REPO_PATHS = os.path.join(ROOT,'repos')

app = dependencies.git_http_backend.git_http_backend.assemble_WSGI_git_app(
        content_path = REPO_PATHS,
        repo_auto_create = False
)
