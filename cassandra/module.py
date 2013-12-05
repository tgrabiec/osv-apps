from osv.modules import api

default = api.run_java(
    jvm_args=[
        '-javaagent:/usr/cassandra/lib/jamm-0.2.5.jar',
        '-XX:+UseThreadPriorities',
        # '-XX:ThreadPriorityPolicy=42',
        '-Xms1968M',
        '-Xmx1968M',
        '-Xmn400M',
        '-XX:+HeapDumpOnOutOfMemoryError',
        '-Xss228k',
        '-XX:+UseParNewGC',
        '-XX:+UseConcMarkSweepGC',
        '-XX:+CMSParallelRemarkEnabled',
        '-XX:SurvivorRatio=8',
        '-XX:MaxTenuringThreshold=1',
        '-XX:CMSInitiatingOccupancyFraction=75',
        '-XX:+UseCMSInitiatingOccupancyOnly',
        '-XX:+UseTLAB',
        '-XX:+UseCondCardMark',
        '-Djava.net.preferIPv4Stack=true',
        '-Djava.rmi.server.hostname=192.168.122.89',
        '-Dcom.sun.management.jmxremote',
        '-Dcom.sun.management.jmxremote.port=7199',
        '-Dcom.sun.management.jmxremote.ssl=false',
        '-Dcom.sun.management.jmxremote.authenticate=false',
        '-Dlog4j.configuration=log4j-server.properties',
        '-Dlog4j.defaultInitOverride=true',
        '-Dcassandra-foreground=yes',
        '-Djna.nounpack=true',
        '-Djna.debug_load=true',
        '-Djna.debug_load.jna=true'
    ],
    classpath=[
        '/usr/cassandra/conf/',
        '/usr/cassandra/lib/*'
    ],
    args=['org.apache.cassandra.service.CassandraDaemon'])
