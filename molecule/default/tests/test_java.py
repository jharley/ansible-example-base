import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_oracle_jdk(host):
    f = host.file('/usr/bin/java')
    cmd = "java -version | grep 'Java(TM) SE Runtime Environment (build 1.8.0'"
    host.run_test(cmd)

    assert f.exists
    assert host.run_test(cmd)
