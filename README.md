# ArubaOS 8 ansible modules

Set of modules to automate ArubaOS 8 controller plateforms with ansible.\

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

### General

* Arguments `hostname`, `username` and `password` support fallback to env variables `ANSIBLE_ARUBAOS_HOSTNAME`, `ANSIBLE_ARUBAOS_USERNAME`, `ANSIBLE_ARUBAOS_PASSWORD` to avoid having to repeat them on each module call.

### arubaos_controller_config

* Provides backward compatibility with playbooks based on the module found at aruba/aruba-ansible-modules

### arubaos_get

* Implements all get modifiers (filters) supported by the API

### arubaos_set

* Full idempotency
* Supports check_mode and diff
* Supports normal and mulipart set operations

## Installating and using the modules

### Installation

#### Prefered method: stall from Ansible Galaxy

If you are using ansible 2.9 or later you can install the collection using the ansible-galaxy client as so:

```
ansible-galaxy collection install sachaboudjema.arubaos
```

See the offical Ansible documentation on how to use modules provided with collections.

#### Method 2: Clone and copy to your playbook directory

Simplest way is o clone the repo, and merge the `library`, `module_utils` and `doc_fragments` folders to your playbook dir

```
git clone https://github.com/sachaboudjema/ansible-modules-arubaos.git arubaos_modules
cp -r arubaos_modules/library arubaos_modules/module_utils arubaos_modules/doc_fragments <your_playbook_dir>
```

#### Method 3: Clone and copy to your ansible library

If you need to make the modules available form different directories, you will need to copy the contents to your ansible search path.\
You can find the list of directories in the search path as so:

```
[user@localhost ~]$ ansible --version
ansible 2.9.6
  config file = None
  configured module search path = ['/home/schb/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /home/schb/.local/lib/python3.6/site-packages/ansible
  executable location = /home/schb/.local/bin/ansible
  python version = 3.6.8 (default, Oct  7 2019, 17:58:22) [GCC 8.2.1 20180905 (Red Hat 8.2.1-3)]
```

You can then clone the repo and copy the contents to a directory from the search path, as so:

```
git clone https://github.com/sachaboudjema/ansible-modules-arubaos.git arubaos_modules
cp -r arubaos_modules/library <dir_in_search_path>/plugins/modules
cp -r arubaos_modules/module_utils <dir_in_search_path>/plugins/module_utils
cp -r arubaos_modules/doc_fragments <dir_in_search_path>/plugins/doc_fragments
```

## General discussions and help

For general discussions and help about using the modules, please use this [dedicated google mailing list](https://groups.google.com/forum/#!forum/ansible-modules-arubaos).