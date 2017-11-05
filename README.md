An example base role
====================

This Ansible role is intended to represent an automation baseline for an orgainzation or corporation.

The role is tested by [Molecule](https://molecule.readthedocs.io/en/latest/) and [TestInfra](http://testinfra.readthedocs.io/en/latest/index.html).

Requirements
------------

 * Ansible 2.4


Role Variables
--------------

The variable that can be passed to this role and a brief description of them follows:

 * `install_oracle_jdk` - a boolean to determine if the Oracle JDK should be installed (default: `true`)

Dependencies
------------

None.

Example Playbook
----------------

```yaml
    - hosts: all
      roles:
         - { role: ansible-example-base }
```

License
-------

Apache License 2.0

Author Information
------------------

Jason Harley - jharley@redmind.ca
