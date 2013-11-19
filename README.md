OSv Applications
========

Introduction
------------

This repository contains the necessary glue to compile a bunch of
applications for OSv.

Each of the subdirectories here does NOT contain the original application
code. This makes this repository very small, and free of license issues.
Rather for each application this repository contains a script "GET" to
fetch this code from the Internet, patch it (if required) to run on OSv,
a Makefile to compile it for OSv (if compilation is required), and a
manifest of which files from the application should be copied into the
OSv image.

How to use
----------

Each one of the subdirectories in this repository is an application.
To add one, say, "cassandra", to your OSv image, all you need to do
is to
	cd cassandra
	./GET

and then add to the modules list in the "config.json" file the following
specification:
        {
                "name": "cassandra",
                "type": "dir",
                "path": "/home/nyh/osv-apps/cassandra"
        },

(with the path set to where you put the osv-apps directory).

Then run "make clean; make" of OSv, and you're done - you have an
image with Cassandra on it! check out osv-apps/cassandra/start-cassandra
for an example command to run a guest with cassandra.

You can, of course, add multiple applications to config.json, and get
an image which includes multiple applications.
