from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import os

from ansible.plugins.lookup import LookupBase


class LookupModule(LookupBase):
    def run(self, terms, variables=None, **kwargs):
        return [os.path.abspath(os.curdir)]
