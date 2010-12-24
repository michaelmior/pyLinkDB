from linkdb.tests import *

class TestLinkController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='link', action='index'))
        # Test response...
