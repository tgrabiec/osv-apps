.PHONY: module
module: haproxy.so
	echo '/haproxy.so: $${MODULE_DIR}/haproxy.so' > usr.manifest
	echo '/haproxy.cfg: $${MODULE_DIR}/haproxy.cfg' >> usr.manifest
	: > bootfs.manifest

haproxy.so:
	make -C haproxy TARGET=linux26 CFLAGS="-fPIC -shared" LDFLAGS="-fPIC -shared" -j4
	cp -vf haproxy/haproxy haproxy.so

src:
	./GET

clean:
	rm -rf haproxy-* *.tar.gz haproxy.so haproxy *.manifest *.pyc

