from linkdb.tests import *

class TestBrowseController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='browse', action='index'))
        # Test response...
