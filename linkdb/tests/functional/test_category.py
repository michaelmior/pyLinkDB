from linkdb.tests import *

class TestCategoryController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='category', action='index'))
        # Test response...
