#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2019, Sacha Boudjema <sachaboudjema@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


class ModuleDocFragment(object):
    DOCUMENTATION = r'''
    notes:
        - Supports check-mode.
    options:
        host:
            description:
                - Hostname or IP Address of the controller.
                - If not set the environment variable C(ANSIBLE_ARUBAOS_HOST) will be used.
            required: true
            type: str
        username:
            description:
                - Username used to login to the controller.
                - If not set the environment variable C(ANSIBLE_ARUBAOS_USERNAME) will be used.
            required: true
            type: str
        password:
            description:
                - Password used to login to the controller.
                - If not set the environment variable C(ANSIBLE_ARUBAOS_PASSWORD) will be used.
            required: true
            type: str
            no_log: true
        validate_certs:
            description:
                - Set to True to validate server SSL certificate upon HTTPS connection. Default option is false.
            required: false
            type: str
            default: None
        client_cert:
            description:
                - Set the file path for client certificate validation from server side. Default option is None.
            required: false
            type: str
            default: None
        client_key:
            description:
                - If the client_cert did not have the key, use this parameter. Default option is None.
            required: false
            type: str
            default: None
    see_also:
        - name: ArubaOS 8.x API Guide
          description: Complete description of ArubaOS API methods with examples.
          link: https://asp.arubanetworks.com/downloads;fileTypes=DOCUMENT;products=Aruba%20Mobility%20Controllers%20%28AOS%29;fileContents=API%20Guide
        - name: ArubaOS API Explorer
          description: Complete reference of ArubaOS API data model.
          link: https://<your_controller>:4343/api/
    notes:
        - ArubaOS version 8.0.0.0 or later required.
    '''
