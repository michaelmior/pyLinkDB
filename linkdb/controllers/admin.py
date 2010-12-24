import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from linkdb.lib.base import BaseController
from linkdb.model import *
from linkdb.model.meta import Session

from authkit.permissions import HasAuthKitGroup
from authkit.authorize.pylons_adaptors import authorize

log = logging.getLogger(__name__)

class AdminController(BaseController):

    @authorize(HasAuthKitGroup(['admin']))
    def fix_letters(self):
        """
        Repair the letters index by dropping everything and then
        inserting a row for the first letter of the title of
        each link.
        """
        import unicodedata

        # Empty the letters table
        Session.connection().execute(letter_table.delete())

        # Get all links
        links = Session.query(Link).all()

        for link in links:
            # Grab the first letter of the title
            letter = link.title.strip()[0]

            # Strip any diacritical marks (not important for ordering)
            letter = unicodedata.normalize('NFKD', letter).encode('ASCII', 'ignore')
            if not letter.isalpha():
                letter = '0'
            else:
                letter = letter.upper()

            Session.add(Letter(letter, link.link_id))

        Session.commit()

        return 'Letters table fixed'
