import logging
from pylons import config
from pylons.i18n import _

import ckan.new_authz as new_authz
import ckan.lib.helpers as h
from ckan.lib.base import abort, c

log = logging.getLogger(__name__)

def comment_create(context, data_dict):
    user = context['user']

    if c.userobj:
        # If currently logged in
        return {'success': True }

    log.debug("User is not logged in")
    # TODO: Once we are able, we should track blocked users.

    return {'success': False, 'msg': _('You must be logged in to add a comment')}
