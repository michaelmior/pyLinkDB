import formencode
from formencode import validators
from formencode.api import *

from sqlalchemy import *

import linkdb.model
from linkdb.model.meta import Session

class LinkExists(formencode.FancyValidator):

    messages = {
        'invalid'  : 'The link you specified is invalid',
        'not_exist': 'The link you specified does not exist',
    }

    def _to_python(self, value, state):
        try:
            return int(value)
        except (TypeError, ValueError):
            raise Invalid(self.message('invalid', state),
                value, state)

    def validate_python(self, value, state):
        # Check the database for the existence of the link
        if not Session.query(linkdb.model.Link).get(value):
            raise Invalid(self.message('not_exist', state), value, state)

# XXX: This is essentially just a copy of the above, should be parametrized
class CategoryExists(formencode.FancyValidator):

    messages = {
        'invalid'  : 'The category you specified is invalid',
        'not_exist': 'The category you specified does not exist',
    }

    def _to_python(self, value, state):
        try:
            return int(value)
        except (TypeError, ValueError):
            raise Invalid(self.message('invalid', state),
                value, state)

    def validate_python(self, value, state):
        # Check the database for the existence of the category
        if not Session.query(linkdb.model.Category).get(value):
            raise Invalid(self.message('not_exist', state), value, state)

class UniqueURL(validators.FormValidator):

    messages = {
        'exists' : 'The specified URL already exists in the database',
    }

    def validate_python(self, field_dict, state):
        query = Session.query(linkdb.model.Link).filter(linkdb.model.Link.url==field_dict['url'])

        # Grab the id if the link is existing to make sure 
        # we don't give a warning for a URL already listed
        if field_dict['id']:
            query = query.filter(linkdb.model.Link.link_id != int(field_dict['id']))

        if query.count() > 0:
            raise Invalid(self.message('exists', state), field_dict, state)

class LinkForm(formencode.Schema):
    id = LinkExists(if_empty=None)
    title = validators.UnicodeString(not_empty=True, max=255)
    url = formencode.All(validators.URL(add_http=True))
    description = validators.UnicodeString(not_empty=True)
    category_id = CategoryExists(if_empty=None)

    # This needs to be here since we
    # need the id as well as the URL
    chained_validators = [UniqueURL()]
