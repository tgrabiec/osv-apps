from osv.modules.filemap import FileMap

usr_files = FileMap()

usr_files.add('${OSV_BASE}/apps/openjdk8/upstream/install/jvm/openjdk-1.8.0-internal').to('/usr/lib/jvm') \
    .include('lib/**') \
    .include('jre/**') \
    .exclude('jre/lib/security/cacerts') \
    .exclude('jre/lib/audio/**')
