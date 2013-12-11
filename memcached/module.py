from osv.modules import api

default = api.run(cmdline="/memcached.so -t 1 -u root")
