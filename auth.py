
from os import environ as env

def get_credentials():
    print "Enter get_credentials"
    d = {}
    d['auth_url'] = env['OS_AUTH_URL']
    d['username'] = env['OS_USERNAME']
    d['password'] = env['OS_PASSWORD']
    d['auth_url'] = env['OS_AUTH_URL']
    d['tenant_name'] = env['OS_TENANT_NAME']
    print d
    print "Return get_credentials"
    return d

def get_nova_credentials_v2():
    print "Enter get_nova_credentials_v2"
    d = {}
    d['version'] = '2.1'
    d['username'] = env['OS_USERNAME']
    d['api_key'] = env['OS_PASSWORD']
    d['auth_url'] = env['OS_AUTH_URL']
    d['project_id'] = env['OS_TENANT_NAME']
    d['region_name'] = env['OS_REGION_NAME']
    print d
    print "Return get_nova_credentials_v2"
    return d
