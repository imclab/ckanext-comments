import logging
from pylons import config
from pylons.i18n import _

import ckan.logic as logic
import ckan.new_authz as new_authz
import ckan.lib.helpers as h
from ckan.lib.base import abort, c

log = logging.getLogger(__name__)

def comment_delete(context, data_dict):
    model = context['model']
    user = context['user']

    logic.check_access("comment_delete", context, data_dict)

    return {}
