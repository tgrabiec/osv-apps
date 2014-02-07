from osv.modules import api

_catalina_base = "/usr/tomcat"
_catalina_home = _catalina_base
_catalina_tmpdir = _catalina_base + "/temp"

_classpath = [_catalina_home + "/bin/bootstrap.jar"]

_logging_config = [
    "-Djava.util.logging.config.file=%s/conf/logging.properties" % _catalina_base,
    "-Djava.util.logging.manager=org.apache.juli.ClassLoaderLogManager"
]
_classpath.append("%s/bin/tomcat-juli.jar" % _catalina_base)

default = api.run_java(
        classpath=_classpath,
        jvm_args=['-Xmx2g -Xms2g'],
        args=_logging_config + [
            "-Dcatalina.base=%s" % _catalina_base,
            "-Dcatalina.home=%s" % _catalina_base,
            "-Djava.io.tmpdir=%s" % _catalina_tmpdir,
            "org.apache.catalina.startup.Bootstrap", "start"
        ])
