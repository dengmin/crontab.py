#!/usr/bin/env python
from core import create_app

class BaseAPI(object):

    def setUp(self):

        app = create_app()
        self.app = app

        self.client = app.test_client()

    def tearDown(self):
        pass