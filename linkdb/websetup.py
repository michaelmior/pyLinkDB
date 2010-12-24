"""Setup the linkdb application"""
import logging

from linkdb.config.environment import load_environment
from linkdb.model import meta
from linkdb.model.auth import MyUsersFromDatabase
from linkdb import model

log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
    """Place any commands to setup linkdb here"""
    load_environment(conf.global_conf, conf.local_conf)

    # Create the tables if they don't already exist
    users = MyUsersFromDatabase(model)
    meta.metadata.create_all(bind=meta.engine)

    # Add indices for later searching
    meta.engine.execute('ALTER TABLE `links` ADD FULLTEXT(`title`, `description`)')

    # Add users
    users.group_create('admin')
    admin = model.User('joe', 'jm878048', 'joe@mior.ca')
    model.meta.Session.add(admin)
    users.user_set_group('joe', group='admin')

    # Add Uncategorized category
    uncategorized = model.Category(u'Uncategorized')
    model.meta.Session.add(uncategorized)

    model.meta.Session.commit()
