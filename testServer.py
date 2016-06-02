import auth
from novaclient.client import Client
import novaclient
import time

def createServer(name):
    print "Enter createServer"
    nova_credentials = auth.get_nova_credentials_v2()
    nova = Client(**nova_credentials)

    serversList = nova.servers.list()
    print("List of VMs: %s" % serversList)
    for s in serversList:
        if s.name == name:
            print "server %s exists" % name
            exist = True
            break
    else:
        print "server %s does not exist" % name
        exist = False

    if (not exist):
        image = nova.images.find(name="TestVM")
        flavor = nova.flavors.find(name="VRCS")
        net = nova.networks.find(label="KI10_rcs_oam")
        nics = [{'net-id': net.id}]
        print "creating server %s" % name
        instance = nova.servers.create(name=name, image=image, flavor=flavor, nics=nics)
        print("Sleeping for 5s after create command")
        time.sleep(5)

    print("List of VMs: %s" % nova.servers.list())
    print "Return createServer"


def deleteServer(name):
    print "Enter deleteServer"
    nova_credentials = auth.get_nova_credentials_v2()
    nova = Client(**nova_credentials)
    serversList = nova.servers.list()

    print("List of VMs: %s" % serversList)

    for s in serversList:
        if s.name == name:
            print("The server %s exists. Delete it" % name)
            nova.servers.delete(s)
    else:
        print ("server %s does not exist" % name)

    # time.sleep(10)
    # print("List of VMs: %s" % nova.servers.list())
    print "Return deleteServer"
