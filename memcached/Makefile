include ../module.mk

module: memcached.so
	cp manifest usr.manifest
	: > bootfs.manifest

memcachedobjs := assoc.o cache.o daemon.o hash.o items.o memcached.o \
        slabs.o stats.o thread.o util.o
memcachedobjs := $(addprefix src/, $(memcachedobjs))
$(memcachedobjs): CFLAGS += -fPIC -DHAVE_CONFIG_H -isystem /usr/include

memcached.so: CFLAGS+=-levent
memcached.so: $(memcachedobjs)
	$(makedir)
	$(q-build-so)
