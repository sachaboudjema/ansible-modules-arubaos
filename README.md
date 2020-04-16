# ArubaOS 8 ansible modules

Set of modules to automate ArubaOS 8 controller plateforms with ansible.\
The directory structure can be imported as is alongside playbooks.

An example playbook is provided, illustrating use cases for all modules.

For a detailed description of each module, see ansible docstrings for each module.\
For detailed description of API reponse formats, see [ArubaOS 8.x API Guide](https://asp.arubanetworks.com/downloads;fileTypes=DOCUMENT;products=Aruba%20Mobility%20Controllers%20%28AOS%29;fileContents=API%20Guide).
For a detailed description of the API data model, see ()

## List of modules

* **arubaos_controller_config**: Backward compatibility with playbooks based on the module found at aruba/aruba-ansible-modules
* **arubaos_get**: Executes GET operations on API objects
* **arubaos_set**: Add, modify or delete configuration
* **arubaos_facts**: Populates `ansible_facts` with sys_info details about the system to which the query is being sent
* **arubaos_config**: Queries full or partial configuration of a particular configuration node.
* **arubaos_writememory**: Executes a show command on the controller and returns structured data when supported
* **arubaos_showcommand**: Commits the pending configuration (if any) on the specified node

## Main features

### arubaos_controller_config

* Provides backward compatibility with playbooks based on the module found at aruba/aruba-ansible-modules

### arubaos_get

* Implements all get modifiers (filters) supported by the API

### arubaos_set

* Full idempotentency
* Supports check_mode and diff
* Supports normal and mulipart set operations