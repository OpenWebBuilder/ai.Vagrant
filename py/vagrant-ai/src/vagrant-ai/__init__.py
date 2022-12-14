from vagrantfile import Vagrantfile
from ssh import SSH

name = "wordpress"


def named():
    # init
    vm1 = Vagrantfile(name)
    vm1.open_dir()
    vm1.make_vagrantfile()

    # wrapper
    vm1.up()

# named()


def test_ssh():
    vm1 = Vagrantfile(name)
    print(vm1.up())
    conn = SSH(vm1)
    print(conn.test_ssh_string())

if __name__ == '__main__':
    print_hi('Hello Vagrant.AI')
    test_ssh()
