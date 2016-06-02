
from os import environ as env
import keystoneclient.v2_0.client as ksclient
import glanceclient.v2.client as glclient
# from neutronclient.v2_0 import client as neutronclient
import novaclient.client
import auth

def neutronList():
    print "Enter neutronList"

    # print "Insantiate neutron"
    # endpoint_url = keystone.service_catalog.url_for(service_type='network')o
    # neutron = neutronclient.Client(endpoint_url=endpoint_url, token=token)

    print "Return neutronList"

def glanceList():
    print "glance image-list"
    credentials = auth.get_credentials()
    keystone = ksclient.Client(**credentials)
    token = keystone.auth_token

    print "auth_token = " + token

    glance_endpoint = keystone.service_catalog.url_for(service_type='image')
    glance = glclient.Client(glance_endpoint, token=token)

    images = glance.images.list()
    print list(images)

def novaList():
    print "Enter novaList"

    nova_credentials = auth.get_nova_credentials_v2()
    nova = novaclient.client.Client(**nova_credentials)

    print "nova list"
    print nova.servers.list()

    print "nova image-list"
    print nova.images.list()

    print "nova flavor-list"
    print nova.flavors.list()

    print "nova network-list"
    print nova.networks.list()

    print "Retrun novaList"
