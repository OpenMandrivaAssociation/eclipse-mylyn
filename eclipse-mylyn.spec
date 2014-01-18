
%undefine _compress
%undefine _extension
%global _duplicate_files_terminate_build 0
%global _files_listed_twice_terminate_build 0
%global _unpackaged_files_terminate_build 0
%global _nonzero_exit_pkgcheck_terminate_build 0
%global _use_internal_dependency_generator 0
%global __find_requires /bin/sed -e 's/.*//'
%global __find_provides /bin/sed -e 's/.*//'

Name:		eclipse-mylyn
Version:	3.10.0
Release:	1.0
License:	GPLv3+
Source0:	eclipse-mylyn-3.10.0-1.0-omv2014.0.noarch.rpm
Source1:	eclipse-mylyn-builds-3.10.0-1.0-omv2014.0.noarch.rpm
Source2:	eclipse-mylyn-builds-hudson-3.10.0-1.0-omv2014.0.noarch.rpm
Source3:	eclipse-mylyn-context-cdt-3.10.0-1.0-omv2014.0.noarch.rpm
Source4:	eclipse-mylyn-context-java-3.10.0-1.0-omv2014.0.noarch.rpm
Source5:	eclipse-mylyn-context-pde-3.10.0-1.0-omv2014.0.noarch.rpm
Source6:	eclipse-mylyn-context-team-3.10.0-1.0-omv2014.0.noarch.rpm
Source7:	eclipse-mylyn-docs-epub-3.10.0-1.0-omv2014.0.noarch.rpm
Source8:	eclipse-mylyn-docs-htmltext-3.10.0-1.0-omv2014.0.noarch.rpm
Source9:	eclipse-mylyn-docs-wikitext-3.10.0-1.0-omv2014.0.noarch.rpm
Source10:	eclipse-mylyn-ide-3.10.0-1.0-omv2014.0.noarch.rpm
Source11:	eclipse-mylyn-tasks-bugzilla-3.10.0-1.0-omv2014.0.noarch.rpm
Source12:	eclipse-mylyn-tasks-trac-3.10.0-1.0-omv2014.0.noarch.rpm
Source13:	eclipse-mylyn-tasks-web-3.10.0-1.0-omv2014.0.noarch.rpm
Source14:	eclipse-mylyn-versions-3.10.0-1.0-omv2014.0.noarch.rpm
Source15:	eclipse-mylyn-versions-cvs-3.10.0-1.0-omv2014.0.noarch.rpm
Source16:	eclipse-mylyn-versions-git-3.10.0-1.0-omv2014.0.noarch.rpm
Source17:	eclipse-mylyn-versions-subclipse-3.10.0-1.0-omv2014.0.noarch.rpm

URL:		https://abf.rosalinux.ru/openmandriva/eclipse-mylyn
BuildArch:	noarch
Summary:	eclipse-mylyn bootstrap version
Requires:	javapackages-bootstrap
Requires:	apache-commons-discovery >= 0.5-2
Requires:	apache-commons-io >= 2.3
Requires:	apache-commons-lang >= 2.6-6
Requires:	apache-commons-logging
Requires:	eclipse-platform >= 1:4.2.0
Requires:	eclipse-rcp >= 1:4.2.0-0.6
Requires:	httpcomponents-client >= 4.1.3-2
Requires:	httpcomponents-core >= 4.1.4
Requires:	jakarta-commons-httpclient
Requires:	javamail >= 1.4.3-11
Requires:	jdom >= 1.1.2-3
Requires:	jpackage-utils
Requires:	lucene
Requires:	osgi(com.google.gson)
Requires:	osgi(com.google.guava)
Requires:	osgi(javax.xml.rpc)
Requires:	osgi(javax.xml.soap)
Requires:	osgi(org.apache.ant)
Requires:	osgi(org.apache.axis)
Requires:	osgi(org.apache.commons.codec)
Requires:	osgi(org.apache.commons.httpclient)
Requires:	osgi(org.apache.commons.lang)
Requires:	osgi(org.apache.lucene.core)
Requires:	osgi(org.apache.xmlrpc)
Requires:	osgi(org.apache.xmlrpc.common)
Requires:	osgi(org.eclipse.compare)
Requires:	osgi(org.eclipse.core.databinding)
Requires:	osgi(org.eclipse.core.databinding.beans)
Requires:	osgi(org.eclipse.core.expressions)
Requires:	osgi(org.eclipse.core.net)
Requires:	osgi(org.eclipse.core.resources)
Requires:	osgi(org.eclipse.core.runtime)
Requires:	osgi(org.eclipse.equinox.common)
Requires:	osgi(org.eclipse.equinox.p2.core)
Requires:	osgi(org.eclipse.equinox.p2.engine)
Requires:	osgi(org.eclipse.equinox.p2.metadata)
Requires:	osgi(org.eclipse.equinox.p2.operations)
Requires:	osgi(org.eclipse.equinox.p2.repository)
Requires:	osgi(org.eclipse.equinox.p2.ui)
Requires:	osgi(org.eclipse.equinox.security)
Requires:	osgi(org.eclipse.jface)
Requires:	osgi(org.eclipse.jface.databinding)
Requires:	osgi(org.eclipse.jface.text)
Requires:	osgi(org.eclipse.osgi)
Requires:	osgi(org.eclipse.search)
Requires:	osgi(org.eclipse.swt)
Requires:	osgi(org.eclipse.ui)
Requires:	osgi(org.eclipse.ui.browser)
Requires:	osgi(org.eclipse.ui.editors)
Requires:	osgi(org.eclipse.ui.forms)
Requires:	osgi(org.eclipse.ui.ide)
Requires:	osgi(org.eclipse.ui.navigator)
Requires:	osgi(org.eclipse.ui.views)
Requires:	osgi(org.eclipse.ui.views.log)
Requires:	osgi(org.eclipse.ui.workbench)
Requires:	osgi(org.eclipse.ui.workbench.texteditor)
Requires:	osgi(org.jdom)
Requires:	osgi(org.junit)
Requires:	rome >= 0.9-9
Requires:	ws-commons-util >= 1.0.1-21
Requires:	xml-commons-apis
Requires:	xmlrpc-client >= 3.1.3
Requires:	xmlrpc-common >= 3.1.3
Provides:	eclipse-mylyn = 3.10.0-1.0:2014.0
Provides:	eclipse-mylyn-commons = 3.10.0-1.0
Provides:	eclipse-mylyn-context = 3.10.0-1.0
Provides:	osgi(org.eclipse.core.runtime.compatibility.auth) = 3.2.200
Provides:	osgi(org.eclipse.mylyn.commons.activity.ui) = 3.10.0
Provides:	osgi(org.eclipse.mylyn.commons.core) = 3.10.0
Provides:	osgi(org.eclipse.mylyn.commons.identity.core) = 1.2.0
Provides:	osgi(org.eclipse.mylyn.commons.net) = 3.10.0
Provides:	osgi(org.eclipse.mylyn.commons.notifications.core) = 1.2.0
Provides:	osgi(org.eclipse.mylyn.commons.notifications.feed) = 1.2.0
Provides:	osgi(org.eclipse.mylyn.commons.notifications.ui) = 1.2.0
Provides:	osgi(org.eclipse.mylyn.commons.repositories.core) = 1.2.0
Provides:	osgi(org.eclipse.mylyn.commons.repositories.http.core) = 1.2.0
Provides:	osgi(org.eclipse.mylyn.commons.repositories.ui) = 1.2.0
Provides:	osgi(org.eclipse.mylyn.commons.screenshots) = 3.10.0
Provides:	osgi(org.eclipse.mylyn.commons.sdk.util) = 3.10.0
Provides:	osgi(org.eclipse.mylyn.commons.soap) = 3.10.0
Provides:	osgi(org.eclipse.mylyn.commons.ui) = 3.10.0
Provides:	osgi(org.eclipse.mylyn.commons.workbench) = 3.10.0
Provides:	osgi(org.eclipse.mylyn.commons.xmlrpc) = 3.10.0
Provides:	osgi(org.eclipse.mylyn.context.core) = 3.10.0
Provides:	osgi(org.eclipse.mylyn.context.tasks.ui) = 3.10.0
Provides:	osgi(org.eclipse.mylyn.context.ui) = 3.10.0
Provides:	osgi(org.eclipse.mylyn.discovery.core) = 3.10.0
Provides:	osgi(org.eclipse.mylyn.discovery.ui) = 3.10.0
Provides:	osgi(org.eclipse.mylyn.discovery.ui.source) = 3.10.0
Provides:	osgi(org.eclipse.mylyn.help.ui) = 3.10.0
Provides:	osgi(org.eclipse.mylyn.monitor.core) = 3.10.0
Provides:	osgi(org.eclipse.mylyn.monitor.ui) = 3.10.0
Provides:	osgi(org.eclipse.mylyn.oslc.core) = 3.10.0
Provides:	osgi(org.eclipse.mylyn.oslc.ui) = 3.10.0
Provides:	osgi(org.eclipse.mylyn.resources.ui) = 3.10.0
Provides:	osgi(org.eclipse.mylyn.tasks.bugs) = 3.10.0
Provides:	osgi(org.eclipse.mylyn.tasks.core) = 3.10.0
Provides:	osgi(org.eclipse.mylyn.tasks.index.core) = 3.10.0
Provides:	osgi(org.eclipse.mylyn.tasks.index.ui) = 3.10.0
Provides:	osgi(org.eclipse.mylyn.tasks.search) = 3.10.0
Provides:	osgi(org.eclipse.mylyn.tasks.ui) = 3.10.0
Obsoletes:	eclipse-mylyn-commons < 3.10.0-1.0
Obsoletes:	eclipse-mylyn-context < 3.10.0-1.0

%description
eclipse-mylyn bootstrap version.

%files
/usr/share/doc/eclipse-mylyn
/usr/share/doc/eclipse-mylyn/epl-v10.html
/usr/share/doc/eclipse-mylyn/license.html
/usr/share/eclipse/dropins/mylyn
/usr/share/eclipse/dropins/mylyn/eclipse
/usr/share/eclipse/dropins/mylyn/eclipse/features
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.activity_3.10.0.201401180805
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.activity_3.10.0.201401180805/META-INF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.activity_3.10.0.201401180805/META-INF/MANIFEST.MF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.activity_3.10.0.201401180805/META-INF/eclipse.inf
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.activity_3.10.0.201401180805/META-INF/maven
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.activity_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.commons
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.activity_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.commons/org.eclipse.mylyn.commons.activity
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.activity_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.commons/org.eclipse.mylyn.commons.activity/pom.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.activity_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.commons/org.eclipse.mylyn.commons.activity/pom.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.activity_3.10.0.201401180805/epl-v10.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.activity_3.10.0.201401180805/feature.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.activity_3.10.0.201401180805/feature.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.activity_3.10.0.201401180805/license.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.compatibility_3.10.0.201401180805
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.compatibility_3.10.0.201401180805/META-INF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.compatibility_3.10.0.201401180805/META-INF/MANIFEST.MF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.compatibility_3.10.0.201401180805/META-INF/eclipse.inf
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.compatibility_3.10.0.201401180805/META-INF/maven
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.compatibility_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.commons
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.compatibility_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.commons/org.eclipse.mylyn.commons.compatibility
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.compatibility_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.commons/org.eclipse.mylyn.commons.compatibility/pom.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.compatibility_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.commons/org.eclipse.mylyn.commons.compatibility/pom.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.compatibility_3.10.0.201401180805/epl-v10.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.compatibility_3.10.0.201401180805/feature.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.compatibility_3.10.0.201401180805/feature.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.compatibility_3.10.0.201401180805/license.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.compatibility_3.10.0.201401180805/p2.inf
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.identity_1.2.0.201401180805
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.identity_1.2.0.201401180805/META-INF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.identity_1.2.0.201401180805/META-INF/MANIFEST.MF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.identity_1.2.0.201401180805/META-INF/eclipse.inf
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.identity_1.2.0.201401180805/META-INF/maven
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.identity_1.2.0.201401180805/META-INF/maven/org.eclipse.mylyn.commons
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.identity_1.2.0.201401180805/META-INF/maven/org.eclipse.mylyn.commons/org.eclipse.mylyn.commons.identity
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.identity_1.2.0.201401180805/META-INF/maven/org.eclipse.mylyn.commons/org.eclipse.mylyn.commons.identity/pom.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.identity_1.2.0.201401180805/META-INF/maven/org.eclipse.mylyn.commons/org.eclipse.mylyn.commons.identity/pom.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.identity_1.2.0.201401180805/epl-v10.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.identity_1.2.0.201401180805/feature.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.identity_1.2.0.201401180805/feature.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.identity_1.2.0.201401180805/license.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.notifications_1.2.0.201401180805
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.notifications_1.2.0.201401180805/META-INF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.notifications_1.2.0.201401180805/META-INF/MANIFEST.MF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.notifications_1.2.0.201401180805/META-INF/eclipse.inf
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.notifications_1.2.0.201401180805/META-INF/maven
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.notifications_1.2.0.201401180805/META-INF/maven/org.eclipse.mylyn.commons
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.notifications_1.2.0.201401180805/META-INF/maven/org.eclipse.mylyn.commons/org.eclipse.mylyn.commons.notifications
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.notifications_1.2.0.201401180805/META-INF/maven/org.eclipse.mylyn.commons/org.eclipse.mylyn.commons.notifications/pom.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.notifications_1.2.0.201401180805/META-INF/maven/org.eclipse.mylyn.commons/org.eclipse.mylyn.commons.notifications/pom.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.notifications_1.2.0.201401180805/epl-v10.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.notifications_1.2.0.201401180805/feature.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.notifications_1.2.0.201401180805/feature.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.notifications_1.2.0.201401180805/license.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.repositories.http_1.2.0.201401180805
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.repositories.http_1.2.0.201401180805/META-INF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.repositories.http_1.2.0.201401180805/META-INF/MANIFEST.MF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.repositories.http_1.2.0.201401180805/META-INF/eclipse.inf
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.repositories.http_1.2.0.201401180805/META-INF/maven
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.repositories.http_1.2.0.201401180805/META-INF/maven/org.eclipse.mylyn.commons
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.repositories.http_1.2.0.201401180805/META-INF/maven/org.eclipse.mylyn.commons/org.eclipse.mylyn.commons.repositories.http
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.repositories.http_1.2.0.201401180805/META-INF/maven/org.eclipse.mylyn.commons/org.eclipse.mylyn.commons.repositories.http/pom.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.repositories.http_1.2.0.201401180805/META-INF/maven/org.eclipse.mylyn.commons/org.eclipse.mylyn.commons.repositories.http/pom.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.repositories.http_1.2.0.201401180805/epl-v10.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.repositories.http_1.2.0.201401180805/feature.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.repositories.http_1.2.0.201401180805/feature.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.repositories.http_1.2.0.201401180805/license.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.repositories_1.2.0.201401180805
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.repositories_1.2.0.201401180805/META-INF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.repositories_1.2.0.201401180805/META-INF/MANIFEST.MF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.repositories_1.2.0.201401180805/META-INF/eclipse.inf
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.repositories_1.2.0.201401180805/META-INF/maven
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.repositories_1.2.0.201401180805/META-INF/maven/org.eclipse.mylyn.commons
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.repositories_1.2.0.201401180805/META-INF/maven/org.eclipse.mylyn.commons/org.eclipse.mylyn.commons.repositories
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.repositories_1.2.0.201401180805/META-INF/maven/org.eclipse.mylyn.commons/org.eclipse.mylyn.commons.repositories/pom.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.repositories_1.2.0.201401180805/META-INF/maven/org.eclipse.mylyn.commons/org.eclipse.mylyn.commons.repositories/pom.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.repositories_1.2.0.201401180805/epl-v10.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.repositories_1.2.0.201401180805/feature.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.repositories_1.2.0.201401180805/feature.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.repositories_1.2.0.201401180805/license.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.soap_feature_3.10.0.201401180805
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.soap_feature_3.10.0.201401180805/META-INF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.soap_feature_3.10.0.201401180805/META-INF/MANIFEST.MF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.soap_feature_3.10.0.201401180805/META-INF/eclipse.inf
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.soap_feature_3.10.0.201401180805/META-INF/maven
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.soap_feature_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.commons
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.soap_feature_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.commons/org.eclipse.mylyn.commons.soap_feature
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.soap_feature_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.commons/org.eclipse.mylyn.commons.soap_feature/pom.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.soap_feature_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.commons/org.eclipse.mylyn.commons.soap_feature/pom.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.soap_feature_3.10.0.201401180805/epl-v10.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.soap_feature_3.10.0.201401180805/feature.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.soap_feature_3.10.0.201401180805/feature.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons.soap_feature_3.10.0.201401180805/license.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons_3.10.0.201401180805
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons_3.10.0.201401180805/META-INF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons_3.10.0.201401180805/META-INF/MANIFEST.MF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons_3.10.0.201401180805/META-INF/eclipse.inf
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons_3.10.0.201401180805/META-INF/maven
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.commons
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.commons/org.eclipse.mylyn.commons
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.commons/org.eclipse.mylyn.commons/pom.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.commons/org.eclipse.mylyn.commons/pom.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons_3.10.0.201401180805/epl-v10.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons_3.10.0.201401180805/feature.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons_3.10.0.201401180805/feature.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.commons_3.10.0.201401180805/license.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.context_feature_3.10.0.201401180805
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.context_feature_3.10.0.201401180805/META-INF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.context_feature_3.10.0.201401180805/META-INF/MANIFEST.MF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.context_feature_3.10.0.201401180805/META-INF/eclipse.inf
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.context_feature_3.10.0.201401180805/META-INF/maven
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.context_feature_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.context
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.context_feature_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.context/org.eclipse.mylyn.context_feature
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.context_feature_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.context/org.eclipse.mylyn.context_feature/pom.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.context_feature_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.context/org.eclipse.mylyn.context_feature/pom.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.context_feature_3.10.0.201401180805/epl-v10.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.context_feature_3.10.0.201401180805/feature.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.context_feature_3.10.0.201401180805/feature.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.context_feature_3.10.0.201401180805/license.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.discovery_3.10.0.201401180805
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.discovery_3.10.0.201401180805/META-INF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.discovery_3.10.0.201401180805/META-INF/MANIFEST.MF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.discovery_3.10.0.201401180805/META-INF/eclipse.inf
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.discovery_3.10.0.201401180805/META-INF/maven
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.discovery_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.commons
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.discovery_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.commons/org.eclipse.mylyn.discovery
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.discovery_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.commons/org.eclipse.mylyn.discovery/pom.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.discovery_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.commons/org.eclipse.mylyn.discovery/pom.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.discovery_3.10.0.201401180805/epl-v10.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.discovery_3.10.0.201401180805/feature.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.discovery_3.10.0.201401180805/feature.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.discovery_3.10.0.201401180805/license.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.monitor_3.10.0.201401180805
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.monitor_3.10.0.201401180805/META-INF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.monitor_3.10.0.201401180805/META-INF/MANIFEST.MF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.monitor_3.10.0.201401180805/META-INF/eclipse.inf
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.monitor_3.10.0.201401180805/META-INF/maven
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.monitor_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.commons
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.monitor_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.commons/org.eclipse.mylyn.monitor
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.monitor_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.commons/org.eclipse.mylyn.monitor/pom.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.monitor_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.commons/org.eclipse.mylyn.monitor/pom.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.monitor_3.10.0.201401180805/epl-v10.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.monitor_3.10.0.201401180805/feature.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.monitor_3.10.0.201401180805/feature.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.monitor_3.10.0.201401180805/license.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.tasks.ide_3.10.0.201401180805
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.tasks.ide_3.10.0.201401180805/META-INF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.tasks.ide_3.10.0.201401180805/META-INF/MANIFEST.MF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.tasks.ide_3.10.0.201401180805/META-INF/eclipse.inf
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.tasks.ide_3.10.0.201401180805/META-INF/maven
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.tasks.ide_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.tasks
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.tasks.ide_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.tasks/org.eclipse.mylyn.tasks.ide
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.tasks.ide_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.tasks/org.eclipse.mylyn.tasks.ide/pom.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.tasks.ide_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.tasks/org.eclipse.mylyn.tasks.ide/pom.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.tasks.ide_3.10.0.201401180805/epl-v10.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.tasks.ide_3.10.0.201401180805/feature.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.tasks.ide_3.10.0.201401180805/feature.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.tasks.ide_3.10.0.201401180805/license.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn_feature_3.10.0.201401180805
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn_feature_3.10.0.201401180805/META-INF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn_feature_3.10.0.201401180805/META-INF/MANIFEST.MF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn_feature_3.10.0.201401180805/META-INF/eclipse.inf
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn_feature_3.10.0.201401180805/META-INF/maven
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn_feature_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.tasks
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn_feature_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.tasks/org.eclipse.mylyn_feature
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn_feature_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.tasks/org.eclipse.mylyn_feature/pom.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn_feature_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.tasks/org.eclipse.mylyn_feature/pom.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn_feature_3.10.0.201401180805/epl-v10.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn_feature_3.10.0.201401180805/feature.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn_feature_3.10.0.201401180805/feature.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn_feature_3.10.0.201401180805/license.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn_feature_3.10.0.201401180805/p2.inf
/usr/share/eclipse/dropins/mylyn/eclipse/plugins
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/apache-commons-discovery.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/apache-commons-io.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/apache-commons-lang.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/axis.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/commons-httpclient.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/google-gson.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/guava.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/jaxp.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/jaxrpc.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/jdom.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/mail.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.core.runtime.compatibility.auth_3.2.200.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.commons.activity.ui_3.10.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.commons.core_3.10.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.commons.identity.core_1.2.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.commons.net_3.10.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.commons.notifications.core_1.2.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.commons.notifications.feed_1.2.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.commons.notifications.ui_1.2.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.commons.repositories.core_1.2.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.commons.repositories.http.core_1.2.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.commons.repositories.ui_1.2.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.commons.screenshots_3.10.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.commons.sdk.util_3.10.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.commons.soap_3.10.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.commons.ui_3.10.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.commons.workbench_3.10.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.commons.xmlrpc_3.10.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.context.core_3.10.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.context.tasks.ui_3.10.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.context.ui_3.10.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.discovery.core_3.10.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.discovery.ui.source_3.10.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.discovery.ui_3.10.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.help.ui_3.10.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.monitor.core_3.10.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.monitor.ui_3.10.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.oslc.core_3.10.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.oslc.ui_3.10.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.resources.ui_3.10.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.tasks.bugs_3.10.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.tasks.core_3.10.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.tasks.index.core_3.10.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.tasks.index.ui_3.10.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.tasks.search_3.10.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.tasks.ui_3.10.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/rome.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/saaj.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/ws-commons-util.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/wsdl4j.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/xmlrpc-client.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/xmlrpc-common.jar

#------------------------------------------------------------------------
%package	-n eclipse-mylyn-builds
Version:	3.10.0
Release:	1.0
Summary:	eclipse-mylyn-builds bootstrap version
Requires:	javapackages-bootstrap
Requires:	eclipse-emf
Requires:	eclipse-mylyn = 3.10.0-1.0
Requires:	eclipse-mylyn-context = 3.10.0-1.0
Requires:	eclipse-mylyn-versions = 3.10.0-1.0
Requires:	osgi(org.eclipse.compare)
Requires:	osgi(org.eclipse.core.databinding.observable)
Requires:	osgi(org.eclipse.core.databinding.property)
Requires:	osgi(org.eclipse.core.expressions)
Requires:	osgi(org.eclipse.core.resources)
Requires:	osgi(org.eclipse.core.runtime)
Requires:	osgi(org.eclipse.emf.databinding)
Requires:	osgi(org.eclipse.emf.ecore)
Requires:	osgi(org.eclipse.emf.ecore.xmi)
Requires:	osgi(org.eclipse.jface.databinding)
Requires:	osgi(org.eclipse.jface.text)
Requires:	osgi(org.eclipse.mylyn.commons.core)
Requires:	osgi(org.eclipse.mylyn.commons.notifications.core)
Requires:	osgi(org.eclipse.mylyn.commons.notifications.ui)
Requires:	osgi(org.eclipse.mylyn.commons.repositories.core)
Requires:	osgi(org.eclipse.mylyn.commons.repositories.ui)
Requires:	osgi(org.eclipse.mylyn.commons.ui)
Requires:	osgi(org.eclipse.mylyn.commons.workbench)
Requires:	osgi(org.eclipse.mylyn.tasks.core)
Requires:	osgi(org.eclipse.mylyn.tasks.ui)
Requires:	osgi(org.eclipse.mylyn.team.ui)
Requires:	osgi(org.eclipse.mylyn.versions.core)
Requires:	osgi(org.eclipse.mylyn.versions.ui)
Requires:	osgi(org.eclipse.team.core)
Requires:	osgi(org.eclipse.team.ui)
Requires:	osgi(org.eclipse.ui)
Requires:	osgi(org.eclipse.ui.forms)
Requires:	osgi(org.eclipse.ui.navigator)
Requires:	xml-commons-apis
Provides:	eclipse-mylyn-builds = 3.10.0-1.0:2014.0
Provides:	osgi(org.eclipse.mylyn.builds.core) = 1.2.0
Provides:	osgi(org.eclipse.mylyn.builds.ui) = 1.2.0

%description	-n eclipse-mylyn-builds
eclipse-mylyn-builds bootstrap version.

%files		-n eclipse-mylyn-builds
/usr/share/doc/eclipse-mylyn-builds
/usr/share/doc/eclipse-mylyn-builds/epl-v10.html
/usr/share/doc/eclipse-mylyn-builds/license.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.builds_1.2.0.201401180805
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.builds_1.2.0.201401180805/META-INF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.builds_1.2.0.201401180805/META-INF/MANIFEST.MF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.builds_1.2.0.201401180805/META-INF/eclipse.inf
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.builds_1.2.0.201401180805/META-INF/maven
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.builds_1.2.0.201401180805/META-INF/maven/org.eclipse.mylyn.builds
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.builds_1.2.0.201401180805/META-INF/maven/org.eclipse.mylyn.builds/org.eclipse.mylyn.builds
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.builds_1.2.0.201401180805/META-INF/maven/org.eclipse.mylyn.builds/org.eclipse.mylyn.builds/pom.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.builds_1.2.0.201401180805/META-INF/maven/org.eclipse.mylyn.builds/org.eclipse.mylyn.builds/pom.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.builds_1.2.0.201401180805/epl-v10.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.builds_1.2.0.201401180805/feature.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.builds_1.2.0.201401180805/feature.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.builds_1.2.0.201401180805/license.html
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.builds.core_1.2.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.builds.ui_1.2.0.201401180805.jar

#------------------------------------------------------------------------
%package	-n eclipse-mylyn-builds-hudson
Version:	3.10.0
Release:	1.0
Summary:	eclipse-mylyn-builds-hudson bootstrap version
Requires:	javapackages-bootstrap
Requires:	eclipse-mylyn = 3.10.0-1.0
Requires:	eclipse-mylyn-builds = 3.10.0-1.0
Requires:	eclipse-platform >= 1:4.2.0-0.6
Requires:	google-gson >= 1.6.0
Requires:	java >= 1:1.7.0
Requires:	osgi(org.eclipse.core.runtime)
Requires:	osgi(org.eclipse.emf.ecore)
Requires:	osgi(org.eclipse.mylyn.builds.core)
Requires:	osgi(org.eclipse.mylyn.builds.ui)
Requires:	osgi(org.eclipse.mylyn.commons.core)
Requires:	osgi(org.eclipse.mylyn.commons.notifications.ui)
Requires:	osgi(org.eclipse.mylyn.commons.repositories.core)
Requires:	osgi(org.eclipse.mylyn.commons.repositories.http.core)
Requires:	osgi(org.eclipse.mylyn.commons.repositories.ui)
Requires:	osgi(org.eclipse.ui)
Provides:	eclipse-mylyn-builds-hudson = 3.10.0-1.0:2014.0
Provides:	osgi(org.eclipse.mylyn.hudson.core) = 1.2.0
Provides:	osgi(org.eclipse.mylyn.hudson.ui) = 1.2.0

%description	-n eclipse-mylyn-builds-hudson
eclipse-mylyn-builds-hudson bootstrap version.

%files		-n eclipse-mylyn-builds-hudson
/usr/share/doc/eclipse-mylyn-builds-hudson
/usr/share/doc/eclipse-mylyn-builds-hudson/epl-v10.html
/usr/share/doc/eclipse-mylyn-builds-hudson/license.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.hudson_1.2.0.201401180805
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.hudson_1.2.0.201401180805/META-INF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.hudson_1.2.0.201401180805/META-INF/MANIFEST.MF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.hudson_1.2.0.201401180805/META-INF/eclipse.inf
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.hudson_1.2.0.201401180805/META-INF/maven
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.hudson_1.2.0.201401180805/META-INF/maven/org.eclipse.mylyn.builds
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.hudson_1.2.0.201401180805/META-INF/maven/org.eclipse.mylyn.builds/org.eclipse.mylyn.hudson
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.hudson_1.2.0.201401180805/META-INF/maven/org.eclipse.mylyn.builds/org.eclipse.mylyn.hudson/pom.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.hudson_1.2.0.201401180805/META-INF/maven/org.eclipse.mylyn.builds/org.eclipse.mylyn.hudson/pom.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.hudson_1.2.0.201401180805/epl-v10.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.hudson_1.2.0.201401180805/feature.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.hudson_1.2.0.201401180805/feature.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.hudson_1.2.0.201401180805/license.html
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.hudson.core_1.2.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.hudson.ui_1.2.0.201401180805.jar

#------------------------------------------------------------------------
%package	-n eclipse-mylyn-context-cdt
Version:	3.10.0
Release:	1.0
Summary:	eclipse-mylyn-context-cdt bootstrap version
Requires:	javapackages-bootstrap
Requires:	eclipse-cdt
Requires:	eclipse-mylyn-context = 3.10.0-1.0
Requires:	osgi(org.eclipse.cdt.core)
Requires:	osgi(org.eclipse.cdt.ui)
Requires:	osgi(org.eclipse.core.resources)
Requires:	osgi(org.eclipse.core.runtime)
Requires:	osgi(org.eclipse.jface.text)
Requires:	osgi(org.eclipse.mylyn.commons.core)
Requires:	osgi(org.eclipse.mylyn.commons.ui)
Requires:	osgi(org.eclipse.mylyn.context.core)
Requires:	osgi(org.eclipse.mylyn.context.ui)
Requires:	osgi(org.eclipse.mylyn.monitor.core)
Requires:	osgi(org.eclipse.mylyn.monitor.ui)
Requires:	osgi(org.eclipse.ui)
Requires:	osgi(org.eclipse.ui.editors)
Requires:	osgi(org.eclipse.ui.ide)
Requires:	osgi(org.eclipse.ui.views)
Provides:	eclipse-cdt-mylyn = 2:1.0.0-1.fc12
Provides:	eclipse-mylyn-cdt = 3.10.0-1.0
Provides:	eclipse-mylyn-context-cdt = 3.10.0-1.0:2014.0
Provides:	osgi(org.eclipse.cdt.mylyn.ui) = 3.10.0
Obsoletes:	eclipse-cdt-mylyn < 2:1.0.0
Obsoletes:	eclipse-context-cdt < 3.10.0-1.0

%description	-n eclipse-mylyn-context-cdt
eclipse-mylyn-context-cdt bootstrap version.

%files		-n eclipse-mylyn-context-cdt
/usr/share/doc/eclipse-mylyn-context-cdt
/usr/share/doc/eclipse-mylyn-context-cdt/epl-v10.html
/usr/share/doc/eclipse-mylyn-context-cdt/license.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.cdt.mylyn_5.6.0.201401180805
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.cdt.mylyn_5.6.0.201401180805/META-INF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.cdt.mylyn_5.6.0.201401180805/META-INF/MANIFEST.MF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.cdt.mylyn_5.6.0.201401180805/META-INF/eclipse.inf
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.cdt.mylyn_5.6.0.201401180805/META-INF/maven
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.cdt.mylyn_5.6.0.201401180805/META-INF/maven/org.eclipse.mylyn.context
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.cdt.mylyn_5.6.0.201401180805/META-INF/maven/org.eclipse.mylyn.context/org.eclipse.cdt.mylyn
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.cdt.mylyn_5.6.0.201401180805/META-INF/maven/org.eclipse.mylyn.context/org.eclipse.cdt.mylyn/pom.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.cdt.mylyn_5.6.0.201401180805/META-INF/maven/org.eclipse.mylyn.context/org.eclipse.cdt.mylyn/pom.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.cdt.mylyn_5.6.0.201401180805/epl-v10.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.cdt.mylyn_5.6.0.201401180805/feature.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.cdt.mylyn_5.6.0.201401180805/feature.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.cdt.mylyn_5.6.0.201401180805/license.html
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.cdt.mylyn.ui_3.10.0.201401180805.jar

#------------------------------------------------------------------------
%package	-n eclipse-mylyn-context-java
Version:	3.10.0
Release:	1.0
Summary:	eclipse-mylyn-context-java bootstrap version
Requires:	javapackages-bootstrap
Requires:	eclipse-jdt
Requires:	eclipse-mylyn-context = 3.10.0-1.0
Requires:	osgi(org.eclipse.ant.ui)
Requires:	osgi(org.eclipse.core.resources)
Requires:	osgi(org.eclipse.core.runtime)
Requires:	osgi(org.eclipse.debug.core)
Requires:	osgi(org.eclipse.debug.ui)
Requires:	osgi(org.eclipse.jdt.core)
Requires:	osgi(org.eclipse.jdt.debug)
Requires:	osgi(org.eclipse.jdt.debug.ui)
Requires:	osgi(org.eclipse.jdt.junit)
Requires:	osgi(org.eclipse.jdt.launching)
Requires:	osgi(org.eclipse.jdt.ui)
Requires:	osgi(org.eclipse.jface.text)
Requires:	osgi(org.eclipse.mylyn.commons.core)
Requires:	osgi(org.eclipse.mylyn.commons.ui)
Requires:	osgi(org.eclipse.mylyn.context.core)
Requires:	osgi(org.eclipse.mylyn.context.ui)
Requires:	osgi(org.eclipse.mylyn.monitor.core)
Requires:	osgi(org.eclipse.mylyn.monitor.ui)
Requires:	osgi(org.eclipse.mylyn.resources.ui)
Requires:	osgi(org.eclipse.mylyn.tasks.core)
Requires:	osgi(org.eclipse.mylyn.tasks.ui)
Requires:	osgi(org.eclipse.search)
Requires:	osgi(org.eclipse.ui)
Requires:	osgi(org.eclipse.ui.editors)
Requires:	osgi(org.eclipse.ui.forms)
Requires:	osgi(org.eclipse.ui.ide)
Requires:	osgi(org.eclipse.ui.navigator)
Requires:	osgi(org.eclipse.ui.views)
Requires:	osgi(org.eclipse.ui.workbench.texteditor)
Provides:	eclipse-mylyn-context-java = 3.10.0-1.0:2014.0
Provides:	eclipse-mylyn-java = 3.10.0-1.0
Provides:	osgi(org.eclipse.mylyn.debug.ui) = 3.10.0
Provides:	osgi(org.eclipse.mylyn.ide.ant) = 3.10.0
Provides:	osgi(org.eclipse.mylyn.ide.ui) = 3.10.0
Provides:	osgi(org.eclipse.mylyn.java.tasks) = 3.10.0
Provides:	osgi(org.eclipse.mylyn.java.ui) = 3.10.0
Obsoletes:	eclipse-context-java < 3.10.0-1.0

%description	-n eclipse-mylyn-context-java
eclipse-mylyn-context-java bootstrap version.

%files		-n eclipse-mylyn-context-java
/usr/share/doc/eclipse-mylyn-context-java
/usr/share/doc/eclipse-mylyn-context-java/epl-v10.html
/usr/share/doc/eclipse-mylyn-context-java/license.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.java_feature_3.10.0.201401180805
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.java_feature_3.10.0.201401180805/META-INF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.java_feature_3.10.0.201401180805/META-INF/MANIFEST.MF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.java_feature_3.10.0.201401180805/META-INF/eclipse.inf
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.java_feature_3.10.0.201401180805/META-INF/maven
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.java_feature_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.context
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.java_feature_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.context/org.eclipse.mylyn.java_feature
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.java_feature_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.context/org.eclipse.mylyn.java_feature/pom.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.java_feature_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.context/org.eclipse.mylyn.java_feature/pom.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.java_feature_3.10.0.201401180805/epl-v10.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.java_feature_3.10.0.201401180805/feature.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.java_feature_3.10.0.201401180805/feature.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.java_feature_3.10.0.201401180805/license.html
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.debug.ui_3.10.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.ide.ant_3.10.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.ide.ui_3.10.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.java.tasks_3.10.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.java.ui_3.10.0.201401180805.jar

#------------------------------------------------------------------------
%package	-n eclipse-mylyn-context-pde
Version:	3.10.0
Release:	1.0
Summary:	eclipse-mylyn-context-pde bootstrap version
Requires:	javapackages-bootstrap
Requires:	eclipse-mylyn-java = 3.10.0-1.0
Requires:	eclipse-pde
Requires:	osgi(org.eclipse.core.resources)
Requires:	osgi(org.eclipse.core.runtime)
Requires:	osgi(org.eclipse.debug.core)
Requires:	osgi(org.eclipse.debug.ui)
Requires:	osgi(org.eclipse.jdt.core)
Requires:	osgi(org.eclipse.jdt.debug.ui)
Requires:	osgi(org.eclipse.jdt.junit)
Requires:	osgi(org.eclipse.jdt.launching)
Requires:	osgi(org.eclipse.jdt.ui)
Requires:	osgi(org.eclipse.jface.text)
Requires:	osgi(org.eclipse.mylyn.commons.core)
Requires:	osgi(org.eclipse.mylyn.commons.ui)
Requires:	osgi(org.eclipse.mylyn.context.core)
Requires:	osgi(org.eclipse.mylyn.context.ui)
Requires:	osgi(org.eclipse.mylyn.ide.ui)
Requires:	osgi(org.eclipse.mylyn.java.ui)
Requires:	osgi(org.eclipse.mylyn.monitor.core)
Requires:	osgi(org.eclipse.mylyn.monitor.ui)
Requires:	osgi(org.eclipse.mylyn.resources.ui)
Requires:	osgi(org.eclipse.pde.api.tools.ui)
Requires:	osgi(org.eclipse.pde.ui)
Requires:	osgi(org.eclipse.search)
Requires:	osgi(org.eclipse.ui)
Requires:	osgi(org.eclipse.ui.editors)
Requires:	osgi(org.eclipse.ui.forms)
Requires:	osgi(org.eclipse.ui.ide)
Requires:	osgi(org.eclipse.ui.workbench.texteditor)
Provides:	eclipse-mylyn-context-pde = 3.10.0-1.0:2014.0
Provides:	eclipse-mylyn-pde = 3.10.0-1.0
Provides:	osgi(org.eclipse.mylyn.pde.ui) = 3.10.0
Obsoletes:	eclipse-context-pde < 3.10.0-1.0

%description	-n eclipse-mylyn-context-pde
eclipse-mylyn-context-pde bootstrap version.

%files		-n eclipse-mylyn-context-pde
/usr/share/doc/eclipse-mylyn-context-pde
/usr/share/doc/eclipse-mylyn-context-pde/epl-v10.html
/usr/share/doc/eclipse-mylyn-context-pde/license.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.pde_feature_3.10.0.201401180805
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.pde_feature_3.10.0.201401180805/META-INF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.pde_feature_3.10.0.201401180805/META-INF/MANIFEST.MF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.pde_feature_3.10.0.201401180805/META-INF/eclipse.inf
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.pde_feature_3.10.0.201401180805/META-INF/maven
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.pde_feature_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.context
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.pde_feature_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.context/org.eclipse.mylyn.pde_feature
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.pde_feature_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.context/org.eclipse.mylyn.pde_feature/pom.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.pde_feature_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.context/org.eclipse.mylyn.pde_feature/pom.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.pde_feature_3.10.0.201401180805/epl-v10.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.pde_feature_3.10.0.201401180805/feature.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.pde_feature_3.10.0.201401180805/feature.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.pde_feature_3.10.0.201401180805/license.html
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.pde.ui_3.10.0.201401180805.jar

#------------------------------------------------------------------------
%package	-n eclipse-mylyn-context-team
Version:	3.10.0
Release:	1.0
Summary:	eclipse-mylyn-context-team bootstrap version
Requires:	javapackages-bootstrap
Requires:	eclipse-mylyn-context = 3.10.0-1.0
Requires:	osgi(org.eclipse.compare)
Requires:	osgi(org.eclipse.core.resources)
Requires:	osgi(org.eclipse.core.runtime)
Requires:	osgi(org.eclipse.mylyn.commons.core)
Requires:	osgi(org.eclipse.mylyn.commons.ui)
Requires:	osgi(org.eclipse.mylyn.commons.workbench)
Requires:	osgi(org.eclipse.mylyn.context.core)
Requires:	osgi(org.eclipse.mylyn.context.ui)
Requires:	osgi(org.eclipse.mylyn.monitor.core)
Requires:	osgi(org.eclipse.mylyn.resources.ui)
Requires:	osgi(org.eclipse.mylyn.tasks.core)
Requires:	osgi(org.eclipse.mylyn.tasks.ui)
Requires:	osgi(org.eclipse.team.core)
Requires:	osgi(org.eclipse.team.ui)
Requires:	osgi(org.eclipse.ui)
Requires:	osgi(org.eclipse.ui.forms)
Requires:	osgi(org.eclipse.ui.navigator)
Requires:	osgi(org.eclipse.ui.navigator.resources)
Provides:	eclipse-mylyn-context-team = 3.10.0-1.0:2014.0
Provides:	osgi(org.eclipse.mylyn.team.ui) = 3.10.0

%description	-n eclipse-mylyn-context-team
eclipse-mylyn-context-team bootstrap version.

%files		-n eclipse-mylyn-context-team
/usr/share/doc/eclipse-mylyn-context-team
/usr/share/doc/eclipse-mylyn-context-team/epl-v10.html
/usr/share/doc/eclipse-mylyn-context-team/license.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.team_feature_3.10.0.201401180805
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.team_feature_3.10.0.201401180805/META-INF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.team_feature_3.10.0.201401180805/META-INF/MANIFEST.MF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.team_feature_3.10.0.201401180805/META-INF/eclipse.inf
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.team_feature_3.10.0.201401180805/META-INF/maven
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.team_feature_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.context
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.team_feature_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.context/org.eclipse.mylyn.team_feature
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.team_feature_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.context/org.eclipse.mylyn.team_feature/pom.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.team_feature_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.context/org.eclipse.mylyn.team_feature/pom.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.team_feature_3.10.0.201401180805/epl-v10.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.team_feature_3.10.0.201401180805/feature.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.team_feature_3.10.0.201401180805/feature.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.team_feature_3.10.0.201401180805/license.html
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.team.ui_3.10.0.201401180805.jar

#------------------------------------------------------------------------
%package	-n eclipse-mylyn-docs-epub
Version:	3.10.0
Release:	1.0
Summary:	eclipse-mylyn-docs-epub bootstrap version
Requires:	javapackages-bootstrap
Requires:	eclipse-platform >= 1:3.8.0
Requires:	osgi(org.apache.ant)
Requires:	osgi(org.eclipse.ant.core)
Requires:	osgi(org.eclipse.core.databinding)
Requires:	osgi(org.eclipse.core.databinding.beans)
Requires:	osgi(org.eclipse.core.resources)
Requires:	osgi(org.eclipse.core.runtime)
Requires:	osgi(org.eclipse.emf.common)
Requires:	osgi(org.eclipse.emf.ecore)
Requires:	osgi(org.eclipse.emf.ecore.xmi)
Requires:	osgi(org.eclipse.jface.databinding)
Requires:	osgi(org.eclipse.mylyn.wikitext.core)
Requires:	osgi(org.eclipse.mylyn.wikitext.ui)
Requires:	osgi(org.eclipse.ui)
Provides:	eclipse-mylyn-docs-epub = 3.10.0-1.0:2014.0
Provides:	osgi(org.eclipse.mylyn.docs.epub.ant.core) = 1.2.0
Provides:	osgi(org.eclipse.mylyn.docs.epub.core) = 1.2.0
Provides:	osgi(org.eclipse.mylyn.docs.epub.help) = 1.2.0
Provides:	osgi(org.eclipse.mylyn.docs.epub.ui) = 1.2.0

%description	-n eclipse-mylyn-docs-epub
eclipse-mylyn-docs-epub bootstrap version.

%files		-n eclipse-mylyn-docs-epub
/usr/share/doc/eclipse-mylyn-docs-epub
/usr/share/doc/eclipse-mylyn-docs-epub/epl-v10.html
/usr/share/doc/eclipse-mylyn-docs-epub/license.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.docs.epub_1.2.0.201401180805
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.docs.epub_1.2.0.201401180805/META-INF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.docs.epub_1.2.0.201401180805/META-INF/MANIFEST.MF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.docs.epub_1.2.0.201401180805/META-INF/eclipse.inf
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.docs.epub_1.2.0.201401180805/META-INF/maven
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.docs.epub_1.2.0.201401180805/META-INF/maven/org.eclipse.mylyn.docs.epub
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.docs.epub_1.2.0.201401180805/META-INF/maven/org.eclipse.mylyn.docs.epub/org.eclipse.mylyn.docs.epub
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.docs.epub_1.2.0.201401180805/META-INF/maven/org.eclipse.mylyn.docs.epub/org.eclipse.mylyn.docs.epub/pom.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.docs.epub_1.2.0.201401180805/META-INF/maven/org.eclipse.mylyn.docs.epub/org.eclipse.mylyn.docs.epub/pom.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.docs.epub_1.2.0.201401180805/epl-v10.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.docs.epub_1.2.0.201401180805/feature.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.docs.epub_1.2.0.201401180805/feature.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.docs.epub_1.2.0.201401180805/license.html
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.docs.epub.ant.core_1.2.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.docs.epub.core_1.2.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.docs.epub.help_1.2.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.docs.epub.ui_1.2.0.201401180805.jar

#------------------------------------------------------------------------
%package	-n eclipse-mylyn-docs-htmltext
Version:	3.10.0
Release:	1.0
Summary:	eclipse-mylyn-docs-htmltext bootstrap version
Requires:	javapackages-bootstrap
Requires:	eclipse-platform >= 1:3.8.0
Requires:	osgi(org.eclipse.core.runtime)
Requires:	osgi(org.eclipse.ui)
Provides:	eclipse-mylyn-docs-htmltext = 3.10.0-1.0:2014.0
Provides:	osgi(org.eclipse.mylyn.htmltext.ui) = 1.2.0

%description	-n eclipse-mylyn-docs-htmltext
eclipse-mylyn-docs-htmltext bootstrap version.

%files		-n eclipse-mylyn-docs-htmltext
/usr/share/doc/eclipse-mylyn-docs-htmltext
/usr/share/doc/eclipse-mylyn-docs-htmltext/epl-v10.html
/usr/share/doc/eclipse-mylyn-docs-htmltext/license.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.htmltext_1.2.0.201401180805
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.htmltext_1.2.0.201401180805/META-INF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.htmltext_1.2.0.201401180805/META-INF/MANIFEST.MF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.htmltext_1.2.0.201401180805/META-INF/eclipse.inf
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.htmltext_1.2.0.201401180805/META-INF/maven
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.htmltext_1.2.0.201401180805/META-INF/maven/org.eclipse.mylyn.docs
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.htmltext_1.2.0.201401180805/META-INF/maven/org.eclipse.mylyn.docs/org.eclipse.mylyn.htmltext
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.htmltext_1.2.0.201401180805/META-INF/maven/org.eclipse.mylyn.docs/org.eclipse.mylyn.htmltext/pom.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.htmltext_1.2.0.201401180805/META-INF/maven/org.eclipse.mylyn.docs/org.eclipse.mylyn.htmltext/pom.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.htmltext_1.2.0.201401180805/epl-v10.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.htmltext_1.2.0.201401180805/feature.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.htmltext_1.2.0.201401180805/feature.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.htmltext_1.2.0.201401180805/license.html
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.htmltext.ui_1.2.0.201401180805.jar

#------------------------------------------------------------------------
%package	-n eclipse-mylyn-docs-wikitext
Version:	3.10.0
Release:	1.0
Summary:	eclipse-mylyn-docs-wikitext bootstrap version
Requires:	javapackages-bootstrap
Requires:	eclipse-mylyn = 3.10.0-1.0
Requires:	eclipse-mylyn-context = 3.10.0-1.0
Requires:	eclipse-platform >= 1:3.8.0
Requires:	jsoup
Requires:	osgi(org.eclipse.core.expressions)
Requires:	osgi(org.eclipse.core.resources)
Requires:	osgi(org.eclipse.core.runtime)
Requires:	osgi(org.eclipse.help)
Requires:	osgi(org.eclipse.jface.text)
Requires:	osgi(org.eclipse.mylyn.commons.ui)
Requires:	osgi(org.eclipse.mylyn.commons.workbench)
Requires:	osgi(org.eclipse.mylyn.context.core)
Requires:	osgi(org.eclipse.mylyn.context.ui)
Requires:	osgi(org.eclipse.mylyn.monitor.core)
Requires:	osgi(org.eclipse.mylyn.monitor.ui)
Requires:	osgi(org.eclipse.mylyn.tasks.core)
Requires:	osgi(org.eclipse.mylyn.tasks.ui)
Requires:	osgi(org.eclipse.ui)
Requires:	osgi(org.eclipse.ui.editors)
Requires:	osgi(org.eclipse.ui.ide)
Requires:	osgi(org.eclipse.ui.views)
Requires:	osgi(org.eclipse.ui.workbench.texteditor)
Provides:	eclipse-mylyn-docs-wikitext = 3.10.0-1.0:2014.0
Provides:	eclipse-mylyn-wikitext = 3.10.0-1.0
Provides:	osgi(org.eclipse.mylyn.wikitext.confluence.core) = 1.9.0
Provides:	osgi(org.eclipse.mylyn.wikitext.confluence.ui) = 1.9.0
Provides:	osgi(org.eclipse.mylyn.wikitext.context.ui) = 1.9.0
Provides:	osgi(org.eclipse.mylyn.wikitext.core) = 1.9.0
Provides:	osgi(org.eclipse.mylyn.wikitext.help.ui) = 1.9.0
Provides:	osgi(org.eclipse.mylyn.wikitext.mediawiki.core) = 1.9.0
Provides:	osgi(org.eclipse.mylyn.wikitext.mediawiki.ui) = 1.9.0
Provides:	osgi(org.eclipse.mylyn.wikitext.tasks.ui) = 1.9.0
Provides:	osgi(org.eclipse.mylyn.wikitext.textile.core) = 1.9.0
Provides:	osgi(org.eclipse.mylyn.wikitext.textile.ui) = 1.9.0
Provides:	osgi(org.eclipse.mylyn.wikitext.tracwiki.core) = 1.9.0
Provides:	osgi(org.eclipse.mylyn.wikitext.tracwiki.ui) = 1.9.0
Provides:	osgi(org.eclipse.mylyn.wikitext.twiki.core) = 1.9.0
Provides:	osgi(org.eclipse.mylyn.wikitext.twiki.ui) = 1.9.0
Provides:	osgi(org.eclipse.mylyn.wikitext.ui) = 1.9.0

%description	-n eclipse-mylyn-docs-wikitext
eclipse-mylyn-docs-wikitext bootstrap version.

%files		-n eclipse-mylyn-docs-wikitext
/usr/share/doc/eclipse-mylyn-docs-wikitext
/usr/share/doc/eclipse-mylyn-docs-wikitext/epl-v10.html
/usr/share/doc/eclipse-mylyn-docs-wikitext/license.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.wikitext_feature_1.9.0.201401180805
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.wikitext_feature_1.9.0.201401180805/META-INF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.wikitext_feature_1.9.0.201401180805/META-INF/MANIFEST.MF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.wikitext_feature_1.9.0.201401180805/META-INF/eclipse.inf
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.wikitext_feature_1.9.0.201401180805/META-INF/maven
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.wikitext_feature_1.9.0.201401180805/META-INF/maven/org.eclipse.mylyn.docs
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.wikitext_feature_1.9.0.201401180805/META-INF/maven/org.eclipse.mylyn.docs/org.eclipse.mylyn.wikitext_feature
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.wikitext_feature_1.9.0.201401180805/META-INF/maven/org.eclipse.mylyn.docs/org.eclipse.mylyn.wikitext_feature/pom.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.wikitext_feature_1.9.0.201401180805/META-INF/maven/org.eclipse.mylyn.docs/org.eclipse.mylyn.wikitext_feature/pom.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.wikitext_feature_1.9.0.201401180805/epl-v10.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.wikitext_feature_1.9.0.201401180805/feature.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.wikitext_feature_1.9.0.201401180805/feature.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.wikitext_feature_1.9.0.201401180805/license.html
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/jsoup.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.wikitext.confluence.core_1.9.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.wikitext.confluence.ui_1.9.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.wikitext.context.ui_1.9.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.wikitext.core_1.9.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.wikitext.help.ui_1.9.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.wikitext.mediawiki.core_1.9.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.wikitext.mediawiki.ui_1.9.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.wikitext.tasks.ui_1.9.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.wikitext.textile.core_1.9.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.wikitext.textile.ui_1.9.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.wikitext.tracwiki.core_1.9.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.wikitext.tracwiki.ui_1.9.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.wikitext.twiki.core_1.9.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.wikitext.twiki.ui_1.9.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.wikitext.ui_1.9.0.201401180805.jar

#------------------------------------------------------------------------
%package	-n eclipse-mylyn-ide
Version:	3.10.0
Release:	1.0
Summary:	eclipse-mylyn-ide bootstrap version
Requires:	javapackages-bootstrap
Requires:	eclipse-mylyn = 3.10.0-1.0
Requires:	eclipse-mylyn-context = 3.10.0-1.0
Requires:	eclipse-mylyn-context-team = 3.10.0-1.0
Requires:	osgi(org.eclipse.core.resources)
Requires:	osgi(org.eclipse.core.runtime)
Requires:	osgi(org.eclipse.jface)
Requires:	osgi(org.eclipse.jface.text)
Requires:	osgi(org.eclipse.mylyn.commons.core)
Requires:	osgi(org.eclipse.mylyn.commons.ui)
Requires:	osgi(org.eclipse.mylyn.context.core)
Requires:	osgi(org.eclipse.mylyn.context.ui)
Requires:	osgi(org.eclipse.mylyn.monitor.core)
Requires:	osgi(org.eclipse.mylyn.resources.ui)
Requires:	osgi(org.eclipse.mylyn.tasks.core)
Requires:	osgi(org.eclipse.mylyn.tasks.ui)
Requires:	osgi(org.eclipse.mylyn.team.ui)
Requires:	osgi(org.eclipse.team.core)
Requires:	osgi(org.eclipse.team.cvs.core)
Requires:	osgi(org.eclipse.team.cvs.ui)
Requires:	osgi(org.eclipse.ui)
Requires:	osgi(org.eclipse.ui.ide)
Requires:	osgi(org.eclipse.ui.navigator)
Requires:	osgi(org.eclipse.ui.navigator.resources)
Requires:	osgi(org.eclipse.ui.workbench)
Provides:	eclipse-mylyn-ide = 3.10.0-1.0:2014.0
Provides:	osgi(org.eclipse.mylyn.bugzilla.ide) = 3.10.0
Provides:	osgi(org.eclipse.mylyn.ide.ui) = 3.10.0
Provides:	osgi(org.eclipse.mylyn.team.cvs) = 3.10.0

%description	-n eclipse-mylyn-ide
eclipse-mylyn-ide bootstrap version.

%files		-n eclipse-mylyn-ide
/usr/share/doc/eclipse-mylyn-ide
/usr/share/doc/eclipse-mylyn-ide/epl-v10.html
/usr/share/doc/eclipse-mylyn-ide/license.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.ide_feature_3.10.0.201401180805
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.ide_feature_3.10.0.201401180805/META-INF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.ide_feature_3.10.0.201401180805/META-INF/MANIFEST.MF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.ide_feature_3.10.0.201401180805/META-INF/eclipse.inf
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.ide_feature_3.10.0.201401180805/META-INF/maven
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.ide_feature_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.context
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.ide_feature_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.context/org.eclipse.mylyn.ide_feature
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.ide_feature_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.context/org.eclipse.mylyn.ide_feature/pom.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.ide_feature_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.context/org.eclipse.mylyn.ide_feature/pom.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.ide_feature_3.10.0.201401180805/epl-v10.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.ide_feature_3.10.0.201401180805/feature.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.ide_feature_3.10.0.201401180805/feature.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.ide_feature_3.10.0.201401180805/license.html
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.bugzilla.ide_3.10.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.ide.ui_3.10.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.team.cvs_3.10.0.201401180805.jar

#------------------------------------------------------------------------
%package	-n eclipse-mylyn-tasks-bugzilla
Version:	3.10.0
Release:	1.0
Summary:	eclipse-mylyn-tasks-bugzilla bootstrap version
Requires:	javapackages-bootstrap
Requires:	eclipse-mylyn = 3.10.0-1.0
Requires:	eclipse-platform >= 1:4.2.0
Requires:	osgi(org.apache.xmlrpc)
Requires:	osgi(org.apache.xmlrpc.common)
Requires:	osgi(org.eclipse.compare)
Requires:	osgi(org.eclipse.core.net)
Requires:	osgi(org.eclipse.core.resources)
Requires:	osgi(org.eclipse.core.runtime)
Requires:	osgi(org.eclipse.jface.text)
Requires:	osgi(org.eclipse.mylyn.commons.core)
Requires:	osgi(org.eclipse.mylyn.commons.net)
Requires:	osgi(org.eclipse.mylyn.commons.ui)
Requires:	osgi(org.eclipse.mylyn.commons.workbench)
Requires:	osgi(org.eclipse.mylyn.commons.xmlrpc)
Requires:	osgi(org.eclipse.mylyn.tasks.core)
Requires:	osgi(org.eclipse.mylyn.tasks.ui)
Requires:	osgi(org.eclipse.ui)
Requires:	osgi(org.eclipse.ui.editors)
Requires:	osgi(org.eclipse.ui.forms)
Requires:	osgi(org.eclipse.ui.views)
Requires:	osgi(org.eclipse.ui.workbench.texteditor)
Provides:	eclipse-mylyn-bugzilla = 3.10.0-1.0
Provides:	eclipse-mylyn-tasks-bugzilla = 3.10.0-1.0:2014.0
Provides:	osgi(org.eclipse.mylyn.bugzilla.core) = 3.10.0
Provides:	osgi(org.eclipse.mylyn.bugzilla.ui) = 3.10.0

%description	-n eclipse-mylyn-tasks-bugzilla
eclipse-mylyn-tasks-bugzilla bootstrap version.

%files		-n eclipse-mylyn-tasks-bugzilla
/usr/share/doc/eclipse-mylyn-tasks-bugzilla
/usr/share/doc/eclipse-mylyn-tasks-bugzilla/epl-v10.html
/usr/share/doc/eclipse-mylyn-tasks-bugzilla/license.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.bugzilla_feature_3.10.0.201401180805
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.bugzilla_feature_3.10.0.201401180805/META-INF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.bugzilla_feature_3.10.0.201401180805/META-INF/MANIFEST.MF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.bugzilla_feature_3.10.0.201401180805/META-INF/eclipse.inf
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.bugzilla_feature_3.10.0.201401180805/META-INF/maven
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.bugzilla_feature_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.tasks
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.bugzilla_feature_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.tasks/org.eclipse.mylyn.bugzilla_feature
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.bugzilla_feature_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.tasks/org.eclipse.mylyn.bugzilla_feature/pom.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.bugzilla_feature_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.tasks/org.eclipse.mylyn.bugzilla_feature/pom.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.bugzilla_feature_3.10.0.201401180805/epl-v10.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.bugzilla_feature_3.10.0.201401180805/feature.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.bugzilla_feature_3.10.0.201401180805/feature.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.bugzilla_feature_3.10.0.201401180805/license.html
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.bugzilla.core_3.10.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.bugzilla.ui_3.10.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/redhat-bugzilla-custom-transitions.txt

#------------------------------------------------------------------------
%package	-n eclipse-mylyn-tasks-trac
Version:	3.10.0
Release:	1.0
Summary:	eclipse-mylyn-tasks-trac bootstrap version
Requires:	javapackages-bootstrap
Requires:	eclipse-mylyn = 3.10.0-1.0
Requires:	eclipse-mylyn-context = 3.10.0-1.0
Requires:	eclipse-platform >= 1:4.2.0
Requires:	google-gson
Requires:	osgi(org.apache.xmlrpc)
Requires:	osgi(org.apache.xmlrpc.common)
Requires:	osgi(org.eclipse.core.runtime)
Requires:	osgi(org.eclipse.jface.text)
Requires:	osgi(org.eclipse.mylyn.commons.core)
Requires:	osgi(org.eclipse.mylyn.commons.net)
Requires:	osgi(org.eclipse.mylyn.commons.ui)
Requires:	osgi(org.eclipse.mylyn.commons.workbench)
Requires:	osgi(org.eclipse.mylyn.commons.xmlrpc)
Requires:	osgi(org.eclipse.mylyn.tasks.core)
Requires:	osgi(org.eclipse.mylyn.tasks.ui)
Requires:	osgi(org.eclipse.team.ui)
Requires:	osgi(org.eclipse.ui)
Requires:	osgi(org.eclipse.ui.editors)
Requires:	osgi(org.eclipse.ui.forms)
Provides:	eclipse-mylyn-tasks-trac = 3.10.0-1.0:2014.0
Provides:	eclipse-mylyn-trac = 3.10.0-1.0
Provides:	osgi(org.eclipse.mylyn.trac.core) = 3.10.0
Provides:	osgi(org.eclipse.mylyn.trac.ui) = 3.10.0
Provides:	osgi(org.eclipse.mylyn.trac.wiki) = 3.10.0

%description	-n eclipse-mylyn-tasks-trac
eclipse-mylyn-tasks-trac bootstrap version.

%files		-n eclipse-mylyn-tasks-trac
/usr/share/doc/eclipse-mylyn-tasks-trac
/usr/share/doc/eclipse-mylyn-tasks-trac/epl-v10.html
/usr/share/doc/eclipse-mylyn-tasks-trac/license.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.trac.wiki_feature_3.10.0.201401180805
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.trac.wiki_feature_3.10.0.201401180805/META-INF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.trac.wiki_feature_3.10.0.201401180805/META-INF/MANIFEST.MF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.trac.wiki_feature_3.10.0.201401180805/META-INF/eclipse.inf
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.trac.wiki_feature_3.10.0.201401180805/META-INF/maven
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.trac.wiki_feature_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.tasks
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.trac.wiki_feature_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.tasks/org.eclipse.mylyn.trac.wiki_feature
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.trac.wiki_feature_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.tasks/org.eclipse.mylyn.trac.wiki_feature/pom.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.trac.wiki_feature_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.tasks/org.eclipse.mylyn.trac.wiki_feature/pom.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.trac.wiki_feature_3.10.0.201401180805/epl-v10.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.trac.wiki_feature_3.10.0.201401180805/feature.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.trac.wiki_feature_3.10.0.201401180805/feature.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.trac.wiki_feature_3.10.0.201401180805/license.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.trac_feature_3.10.0.201401180805
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.trac_feature_3.10.0.201401180805/META-INF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.trac_feature_3.10.0.201401180805/META-INF/MANIFEST.MF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.trac_feature_3.10.0.201401180805/META-INF/eclipse.inf
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.trac_feature_3.10.0.201401180805/META-INF/maven
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.trac_feature_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.tasks
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.trac_feature_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.tasks/org.eclipse.mylyn.trac_feature
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.trac_feature_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.tasks/org.eclipse.mylyn.trac_feature/pom.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.trac_feature_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.tasks/org.eclipse.mylyn.trac_feature/pom.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.trac_feature_3.10.0.201401180805/epl-v10.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.trac_feature_3.10.0.201401180805/feature.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.trac_feature_3.10.0.201401180805/feature.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.trac_feature_3.10.0.201401180805/license.html
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.trac.core_3.10.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.trac.ui_3.10.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.trac.wiki_3.10.0.201401180805.jar

#------------------------------------------------------------------------
%package	-n eclipse-mylyn-tasks-web
Version:	3.10.0
Release:	1.0
Summary:	eclipse-mylyn-tasks-web bootstrap version
Requires:	javapackages-bootstrap
Requires:	eclipse-mylyn = 3.10.0-1.0
Requires:	eclipse-platform >= 1:4.2.0
Requires:	jdom >= 1.1.2-3
Requires:	osgi(com.sun.syndication)
Requires:	osgi(org.eclipse.core.runtime)
Requires:	osgi(org.eclipse.mylyn.commons.core)
Requires:	osgi(org.eclipse.mylyn.commons.net)
Requires:	osgi(org.eclipse.mylyn.commons.ui)
Requires:	osgi(org.eclipse.mylyn.commons.workbench)
Requires:	osgi(org.eclipse.mylyn.tasks.core)
Requires:	osgi(org.eclipse.mylyn.tasks.ui)
Requires:	osgi(org.eclipse.ui)
Requires:	osgi(org.eclipse.ui.forms)
Requires:	osgi(org.jdom)
Requires:	rome >= 0.9-9
Provides:	eclipse-mylyn-tasks-web = 3.10.0-1.0:2014.0
Provides:	eclipse-mylyn-webtasks = 3.10.0-1.0
Provides:	osgi(org.eclipse.mylyn.web.tasks) = 3.10.0

%description	-n eclipse-mylyn-tasks-web
eclipse-mylyn-tasks-web bootstrap version.

%files		-n eclipse-mylyn-tasks-web
/usr/share/doc/eclipse-mylyn-tasks-web
/usr/share/doc/eclipse-mylyn-tasks-web/epl-v10.html
/usr/share/doc/eclipse-mylyn-tasks-web/license.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.web.tasks_feature_3.10.0.201401180805
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.web.tasks_feature_3.10.0.201401180805/META-INF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.web.tasks_feature_3.10.0.201401180805/META-INF/MANIFEST.MF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.web.tasks_feature_3.10.0.201401180805/META-INF/eclipse.inf
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.web.tasks_feature_3.10.0.201401180805/META-INF/maven
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.web.tasks_feature_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.tasks
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.web.tasks_feature_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.tasks/org.eclipse.mylyn.web.tasks_feature
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.web.tasks_feature_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.tasks/org.eclipse.mylyn.web.tasks_feature/pom.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.web.tasks_feature_3.10.0.201401180805/META-INF/maven/org.eclipse.mylyn.tasks/org.eclipse.mylyn.web.tasks_feature/pom.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.web.tasks_feature_3.10.0.201401180805/epl-v10.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.web.tasks_feature_3.10.0.201401180805/feature.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.web.tasks_feature_3.10.0.201401180805/feature.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.web.tasks_feature_3.10.0.201401180805/license.html
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.web.tasks_3.10.0.201401180805.jar

#------------------------------------------------------------------------
%package	-n eclipse-mylyn-versions
Version:	3.10.0
Release:	1.0
Summary:	eclipse-mylyn-versions bootstrap version
Requires:	javapackages-bootstrap
Requires:	eclipse-mylyn = 3.10.0-1.0
Requires:	osgi(org.eclipse.compare)
Requires:	osgi(org.eclipse.core.filesystem)
Requires:	osgi(org.eclipse.core.resources)
Requires:	osgi(org.eclipse.core.runtime)
Requires:	osgi(org.eclipse.jface)
Requires:	osgi(org.eclipse.mylyn.commons.core)
Requires:	osgi(org.eclipse.team.core)
Requires:	osgi(org.eclipse.team.ui)
Requires:	osgi(org.eclipse.ui.workbench)
Provides:	eclipse-mylyn-versions = 3.10.0-1.0:2014.0
Provides:	osgi(org.eclipse.mylyn.versions.core) = 1.2.0
Provides:	osgi(org.eclipse.mylyn.versions.ui) = 1.2.0

%description	-n eclipse-mylyn-versions
eclipse-mylyn-versions bootstrap version.

%files		-n eclipse-mylyn-versions
/usr/share/doc/eclipse-mylyn-versions
/usr/share/doc/eclipse-mylyn-versions/epl-v10.html
/usr/share/doc/eclipse-mylyn-versions/license.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.versions_1.2.0.201401180805
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.versions_1.2.0.201401180805/META-INF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.versions_1.2.0.201401180805/META-INF/MANIFEST.MF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.versions_1.2.0.201401180805/META-INF/eclipse.inf
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.versions_1.2.0.201401180805/META-INF/maven
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.versions_1.2.0.201401180805/META-INF/maven/org.eclipse.mylyn.versions
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.versions_1.2.0.201401180805/META-INF/maven/org.eclipse.mylyn.versions/org.eclipse.mylyn.versions
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.versions_1.2.0.201401180805/META-INF/maven/org.eclipse.mylyn.versions/org.eclipse.mylyn.versions/pom.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.versions_1.2.0.201401180805/META-INF/maven/org.eclipse.mylyn.versions/org.eclipse.mylyn.versions/pom.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.versions_1.2.0.201401180805/epl-v10.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.versions_1.2.0.201401180805/feature.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.versions_1.2.0.201401180805/feature.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.versions_1.2.0.201401180805/license.html
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.versions.core_1.2.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.versions.ui_1.2.0.201401180805.jar

#------------------------------------------------------------------------
%package	-n eclipse-mylyn-versions-cvs
Version:	3.10.0
Release:	1.0
Summary:	eclipse-mylyn-versions-cvs bootstrap version
Requires:	javapackages-bootstrap
Requires:	eclipse-mylyn-versions = 3.10.0-1.0
Requires:	eclipse-platform >= 1:3.8.0
Requires:	osgi(org.eclipse.core.resources)
Requires:	osgi(org.eclipse.core.runtime)
Requires:	osgi(org.eclipse.mylyn.versions.core)
Requires:	osgi(org.eclipse.team.core)
Requires:	osgi(org.eclipse.team.cvs.core)
Provides:	eclipse-mylyn-versions-cvs = 3.10.0-1.0:2014.0
Provides:	osgi(org.eclipse.mylyn.cvs.core) = 1.2.0

%description	-n eclipse-mylyn-versions-cvs
eclipse-mylyn-versions-cvs bootstrap version.

%files		-n eclipse-mylyn-versions-cvs
/usr/share/doc/eclipse-mylyn-versions-cvs
/usr/share/doc/eclipse-mylyn-versions-cvs/epl-v10.html
/usr/share/doc/eclipse-mylyn-versions-cvs/license.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.cvs_1.2.0.201401180805
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.cvs_1.2.0.201401180805/META-INF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.cvs_1.2.0.201401180805/META-INF/MANIFEST.MF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.cvs_1.2.0.201401180805/META-INF/eclipse.inf
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.cvs_1.2.0.201401180805/META-INF/maven
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.cvs_1.2.0.201401180805/META-INF/maven/org.eclipse.mylyn.versions
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.cvs_1.2.0.201401180805/META-INF/maven/org.eclipse.mylyn.versions/org.eclipse.mylyn.cvs
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.cvs_1.2.0.201401180805/META-INF/maven/org.eclipse.mylyn.versions/org.eclipse.mylyn.cvs/pom.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.cvs_1.2.0.201401180805/META-INF/maven/org.eclipse.mylyn.versions/org.eclipse.mylyn.cvs/pom.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.cvs_1.2.0.201401180805/epl-v10.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.cvs_1.2.0.201401180805/feature.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.cvs_1.2.0.201401180805/feature.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.cvs_1.2.0.201401180805/license.html
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.cvs.core_1.2.0.201401180805.jar

#------------------------------------------------------------------------
%package	-n eclipse-mylyn-versions-git
Version:	3.10.0
Release:	1.0
Summary:	eclipse-mylyn-versions-git bootstrap version
Requires:	javapackages-bootstrap
Requires:	eclipse-egit >= 0.10.1
Requires:	eclipse-mylyn-versions = 3.10.0-1.0
Requires:	eclipse-platform >= 1:3.8.0
Requires:	osgi(com.google.guava)
Requires:	osgi(org.eclipse.core.filesystem)
Requires:	osgi(org.eclipse.core.resources)
Requires:	osgi(org.eclipse.core.runtime)
Requires:	osgi(org.eclipse.egit.core)
Requires:	osgi(org.eclipse.egit.ui)
Requires:	osgi(org.eclipse.jgit)
Requires:	osgi(org.eclipse.mylyn.commons.core)
Requires:	osgi(org.eclipse.mylyn.versions.core)
Requires:	osgi(org.eclipse.mylyn.versions.ui)
Requires:	osgi(org.eclipse.team.core)
Requires:	osgi(org.eclipse.ui)
Requires:	osgi(org.eclipse.ui.forms)
Provides:	eclipse-mylyn-versions-git = 3.10.0-1.0:2014.0
Provides:	osgi(org.eclipse.mylyn.git.core) = 1.2.0
Provides:	osgi(org.eclipse.mylyn.git.ui) = 1.2.0

%description	-n eclipse-mylyn-versions-git
eclipse-mylyn-versions-git bootstrap version.

%files		-n eclipse-mylyn-versions-git
/usr/share/doc/eclipse-mylyn-versions-git
/usr/share/doc/eclipse-mylyn-versions-git/epl-v10.html
/usr/share/doc/eclipse-mylyn-versions-git/license.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.git_1.2.0.201401180805
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.git_1.2.0.201401180805/META-INF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.git_1.2.0.201401180805/META-INF/MANIFEST.MF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.git_1.2.0.201401180805/META-INF/eclipse.inf
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.git_1.2.0.201401180805/META-INF/maven
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.git_1.2.0.201401180805/META-INF/maven/org.eclipse.mylyn.versions
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.git_1.2.0.201401180805/META-INF/maven/org.eclipse.mylyn.versions/org.eclipse.mylyn.git
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.git_1.2.0.201401180805/META-INF/maven/org.eclipse.mylyn.versions/org.eclipse.mylyn.git/pom.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.git_1.2.0.201401180805/META-INF/maven/org.eclipse.mylyn.versions/org.eclipse.mylyn.git/pom.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.git_1.2.0.201401180805/epl-v10.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.git_1.2.0.201401180805/feature.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.git_1.2.0.201401180805/feature.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.git_1.2.0.201401180805/license.html
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.git.core_1.2.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.git.ui_1.2.0.201401180805.jar

#------------------------------------------------------------------------
%package	-n eclipse-mylyn-versions-subclipse
Version:	3.10.0
Release:	1.0
Summary:	eclipse-mylyn-versions-subclipse bootstrap version
Requires:	javapackages-bootstrap
Requires:	eclipse-mylyn-versions = 3.10.0-1.0
Requires:	eclipse-platform >= 1:3.8.0
Requires:	eclipse-subclipse
Requires:	osgi(org.eclipse.core.filesystem)
Requires:	osgi(org.eclipse.core.resources)
Requires:	osgi(org.eclipse.core.runtime)
Requires:	osgi(org.eclipse.mylyn.commons.core)
Requires:	osgi(org.eclipse.mylyn.versions.core)
Requires:	osgi(org.eclipse.mylyn.versions.ui)
Requires:	osgi(org.eclipse.team.core)
Requires:	osgi(org.eclipse.ui)
Requires:	osgi(org.eclipse.ui.forms)
Requires:	osgi(org.tigris.subversion.subclipse.core)
Provides:	eclipse-mylyn-versions-subclipse = 3.10.0-1.0:2014.0
Provides:	osgi(org.eclipse.mylyn.subclipse.core) = 1.2.0
Provides:	osgi(org.eclipse.mylyn.subclipse.ui) = 1.2.0

%description	-n eclipse-mylyn-versions-subclipse
eclipse-mylyn-versions-subclipse bootstrap version.

%files		-n eclipse-mylyn-versions-subclipse
/usr/share/doc/eclipse-mylyn-versions-subclipse
/usr/share/doc/eclipse-mylyn-versions-subclipse/epl-v10.html
/usr/share/doc/eclipse-mylyn-versions-subclipse/license.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.subclipse_1.2.0.201401180805
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.subclipse_1.2.0.201401180805/META-INF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.subclipse_1.2.0.201401180805/META-INF/MANIFEST.MF
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.subclipse_1.2.0.201401180805/META-INF/eclipse.inf
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.subclipse_1.2.0.201401180805/META-INF/maven
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.subclipse_1.2.0.201401180805/META-INF/maven/org.eclipse.mylyn.versions
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.subclipse_1.2.0.201401180805/META-INF/maven/org.eclipse.mylyn.versions/org.eclipse.mylyn.subclipse
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.subclipse_1.2.0.201401180805/META-INF/maven/org.eclipse.mylyn.versions/org.eclipse.mylyn.subclipse/pom.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.subclipse_1.2.0.201401180805/META-INF/maven/org.eclipse.mylyn.versions/org.eclipse.mylyn.subclipse/pom.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.subclipse_1.2.0.201401180805/epl-v10.html
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.subclipse_1.2.0.201401180805/feature.properties
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.subclipse_1.2.0.201401180805/feature.xml
/usr/share/eclipse/dropins/mylyn/eclipse/features/org.eclipse.mylyn.subclipse_1.2.0.201401180805/license.html
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.subclipse.core_1.2.0.201401180805.jar
/usr/share/eclipse/dropins/mylyn/eclipse/plugins/org.eclipse.mylyn.subclipse.ui_1.2.0.201401180805.jar

#------------------------------------------------------------------------
%prep

%build

%install
cd %{buildroot}
rpm2cpio %{SOURCE0} | cpio -id
rpm2cpio %{SOURCE1} | cpio -id
rpm2cpio %{SOURCE2} | cpio -id
rpm2cpio %{SOURCE3} | cpio -id
rpm2cpio %{SOURCE4} | cpio -id
rpm2cpio %{SOURCE5} | cpio -id
rpm2cpio %{SOURCE6} | cpio -id
rpm2cpio %{SOURCE7} | cpio -id
rpm2cpio %{SOURCE8} | cpio -id
rpm2cpio %{SOURCE9} | cpio -id
rpm2cpio %{SOURCE10} | cpio -id
rpm2cpio %{SOURCE11} | cpio -id
rpm2cpio %{SOURCE12} | cpio -id
rpm2cpio %{SOURCE13} | cpio -id
rpm2cpio %{SOURCE14} | cpio -id
rpm2cpio %{SOURCE15} | cpio -id
rpm2cpio %{SOURCE16} | cpio -id
rpm2cpio %{SOURCE17} | cpio -id
