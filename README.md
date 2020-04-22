# ArubaOS 8 ansible modules

Set of modules to automate ArubaOS 8 controller plateforms with ansible.

An example playbook is provided, illustrating use cases for all modules.

For a detailed description of each module, see ansible docstrings for each module.\
For detailed description of API reponse formats, see [ArubaOS 8.x API Guide](https://asp.arubanetworks.com/downloads;fileTypes=DOCUMENT;products=Aruba%20Mobility%20Controllers%20%28AOS%29;fileContents=API%20Guide).\
For a detailed description of the API data model, see https://your_controller:4343/api.

## List of modules

* **arubaos_controller_config**: Backward compatibility with playbooks based on the module found at aruba/aruba-ansible-modules
* **arubaos_get**: Executes GET operations on API objects
* **arubaos_set**: Add, modify or delete configuration
* **arubaos_facts**: Populates `ansible_facts` with sys_info details about the system to which the query is being sent
* **arubaos_config**: Queries full or partial configuration of a particular configuration node.
* **arubaos_writememory**: Executes a show command on the controller and returns structured data when supported
* **arubaos_showcommand**: Commits the pending configuration (if any) on the specified node

## Noteworthy features

### arubaos_controller_config

* Provides backward compatibility with playbooks based on the module found at aruba/aruba-ansible-modules

### arubaos_get

* Implements all get modifiers (filters) supported by the API

### arubaos_set

* Full idempotency
* Supports check_mode and diff
* Supports normal and mulipart set operations

## Installation and Usage

### Installing the Collection from Ansible Galaxy

Before using the modules you must install them using the snible-galaxy CLI:

```
ansible-galaxy collection install sachaboudjema.arubaos
```

### Using modules from the collection in your playbooks

To use the modules in your playbooks, you can either call them by here fully qualified name (i.e. `sachaboudjema.arubaos.<module_name>`), or add `sachaboudjema.arubaos` to the playbooks collections and call the modules by name.

**Note**: These modules do not implement a proper httpapi connection yet. They have to be exectuted against the local ansible node, connection parameters have to be provided as module arguments.

#### Example playbook

```YAML
---
- name: "Example playbook for ArubaOS modules"
  hosts: 127.0.0.1
  connection: local
  gather_facts: no

  collections:
    - sachaboudjema.arubaos

  environment:
    ANSIBLE_ARUBAOS_HOST: "{{ mm_ip }}"
    ANSIBLE_ARUBAOS_USERNAME: "{{ mm_username }}"
    ANSIBLE_ARUBAOS_PASSWORD: "{{ mm_password }}"

  vars:
    config_path: "/md/branch1/floor1"

  tasks:

    - name: Gather facts
      arubaos_facts:

    - name: Show command
      arubaos_showcommand:
        command: show switches

    - name: Write memory
      arubaos_writememory:
        config_path: "{{ config_path }}"

    - name: Get Config
      arubaos_config:
        config_path: "{{ config_path }}"

    - name: Get Config with type filter
      arubaos_config:
        config_path: "{{ config_path }}"
        type: local

    - name: Get objects
      arubaos_get:
        config_path: "{{ config_path }}"
        object: ap_group

    - name: Get with sort
      arubaos_get:
        config_path: "{{ config_path }}"
        object: ap_group
        sort: '-id'

    - name: Get with pagination
      arubaos_get:
        config_path: "{{ config_path }}"
        object: ap_group
        limit: 2
        offset: 2
        total: 10

    - name: Get with object filter
      arubaos_get:
        config_path: "{{ config_path }}"
        object: ap_group
        object_filters:
          - oper: $eq
            values: ['ap_group.ap_sys_prof', 'ap_group.am_filter_prof']

    - name: Get with data filter
      arubaos_get:
        config_path: "{{ config_path }}"
        object: ap_group
        data_filters:
          - param_name: 'ap_group.profile-name'
            oper: $in
            values: ['default']

    - name: Get with data type filter
      arubaos_get:
        config_path: "{{ config_path }}"
        object: ap_group
        data_types: ['non-default']

    - name: Set single object single instance
      arubaos_set:
        config_path: "{{ config_path }}"
        data:
          ap_group:             
            profile-name: "grp-test-ansible"

    - name: Set single object multiple instance
      arubaos_set:
        config_path: "{{ config_path }}"
        data:
          ap_group: 
            - profile-name: "grp-test-ansible-1"
            - profile-name: "grp-test-ansible-2"

    - name: Set & commit single object multiple instance
      arubaos_set:
        config_path: "{{ config_path }}"
        data:
          ap_group: 
            - profile-name: "grp-test-ansible-1"
            - profile-name: "grp-test-ansible-2"
        commit: true

    - name: Set multiple object multiple instance
      arubaos_set:
        config_path: "{{ config_path }}"
        data:
          server_group_prof:
            - sg_name: "sg_grp-test_ansible-1"
            - sg_name: "sg_grp-test_ansible-2"
          ap_group: 
            - profile-name: "grp-test-ansible-1"
            - profile-name: "grp-test-ansible-2"

    - name: Set multi-part & commit (continue if error)
      arubaos_set:
        config_path: "{{ config_path }}"
        multipart_data:
          - ap_group:
              profile-name: "grp-test-ansible-3"
          - server_group_prof:
              - sg_name: "sg_grp-test_ansible-1"
              - sg_name: "sg_grp-test_ansible-2"
            ap_group: 
              - profile-name: "grp-test-ansible-1"
              - profile-name: "grp-test-ansible-2"
        commit_force: true
```