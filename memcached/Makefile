.PHONY: module
module: memcached.so
	cp manifest usr.manifest
	: > bootfs.manifest

src:
	./GET

sources := assoc.c cache.c daemon.c hash.c items.c memcached.c slabs.c \
	stats.c thread.c util.c

sources := $(addprefix src/, $(sources))
objects := $(sources:c=o)

$(sources): src

CFLAGS = -std=gnu99 -fPIC -DHAVE_CONFIG_H
LDFLAGS = -shared -levent

memcached.so: $(objects)
	$(CC) -o $@ $(LDFLAGS) $(objects)
