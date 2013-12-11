.PHONY: module
module: memcached.so
	echo '/memcached.so: $${MODULE_DIR}/memcached.so' > usr.manifest
	ldd memcached.so | grep libevent | \
		sed 's/ *[^ ] *\(.*\) => \(.*\) .*/\/\1: \2/' \
		>> usr.manifest
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

clean:
	rm -rf upstream src
	rm -f bootfs.manifest usr.manifest module.pyc memcached.so
