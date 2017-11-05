import os

import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('f',
                         ['/etc/update-motd.d/10-help-text', '/etc/update-motd.d/51-cloudguest'])
def test_banners_removed(host, f):
    f = host.file(f)

    assert not f.exists

def test_rngd_service(host):
    package = host.package('rng-tools')
    service = host.service('rng-tools')

    assert package.is_installed
    assert service.is_enabled
    assert service.is_running

def test_system_editor(host):
    package = host.package('vim-tiny')
    file = host.file('/etc/alternatives/editor')

    assert package.is_installed
    assert file.linked_to == '/usr/bin/vim.tiny'
