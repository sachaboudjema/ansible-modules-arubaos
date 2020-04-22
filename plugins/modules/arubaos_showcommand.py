#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright: (c) 2019, Sacha Boudjema <sachaboudjema@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = r'''
---
author: Sacha Boudjema (@sachaboudjema)
module: arubaos_showcommand
version_added: 2.9.6
extends_documentation_fragment: sachaboudjema.arubaos.arubaos
short_description: Executes a show command on the controller and returns structured data when supported
description:
    - "Executes a C(show) command on the controller and returns structured data when supported."
options:
    command:
        descriptition:
            - Any show command supported by the controller.
            - The command is executed on the target controller node (i.e. mynode).
            - Invalid commands return empty data.
        required: true
        type: str
'''

EXAMPLES = r'''
environment:
  ANSIBLE_ARUBAOS_HOST: 192.168.1.1
  ANSIBLE_ARUBAOS_USERNAME: admin
  ANSIBLE_ARUBAOS_PASSWORD: aruba123

tasks:

  - name: Get list of managed devices
    arubaos_showcommand:
      command: show switches
'''

RETURNS = r'''
response:
    description: Data set returned by the GET request.
    returned: on success
    type: dict
'''

import json
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_native
from ansible_collections.sachaboudjema.arubaos.plugins.module_utils.arubaos import ArubaOsApi, argspec_common


def run_module():
    argspec = argspec_common.copy()
    argspec.update(
        command=dict(required=True, type='str')
    )

    module = AnsibleModule(
        argument_spec=argspec,
        supports_check_mode=True
    )

    with ArubaOsApi(module) as api:

        url = api.get_url(
            '/configuration/showcommand',
            params={'command': module.params.get('command')}
        )
        _, response_json = api.send_request(url, 'GET')

        module.exit_json(
            changed=False,
            msg='Success',
            response=response_json
        )


def main():
    run_module()


if __name__ == '__main__':
    main()
