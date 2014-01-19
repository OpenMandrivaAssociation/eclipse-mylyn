%{?_javapackages_macros:%_javapackages_macros}
%{?scl:%scl_package eclipse-mylyn}
%{!?scl:%global pkg_name %{name}}

%global install_loc         %{_datadir}/eclipse/dropins
%global tag R_3_10_0 
%global incubator_tag 	e93a849274d90e71a08afedc1d65c63053aaeb6c

%{!?scl:%global _non_scl_javadir %{_javadir}}
%{?scl:%global _non_scl_javadir /usr/share/java}

Name:    %{?scl_prefix}eclipse-mylyn
Summary: Eclipse Mylyn main feature.
Version: 3.10.0
Release: 1.1%{?dist}
License: EPL
URL: http://www.eclipse.org/mylyn

# bash fetch-eclipse-mylyn.sh
Source0: %{pkg_name}-%{tag}-fetched-src.tar.xz
Source1: fetch-eclipse-mylyn.sh
Source2: org.eclipse.core.runtime.compatibility.auth.tar.xz
Source3: fetch-compatibility.sh
Source4: eclipse-mylyn-compatibility-pom.xml
Source6: redhat-bugzilla-custom-transitions.txt

Source7: eclipse-mylyn-%{incubator_tag}-incubator-fetched-src.tar.xz
Source8: fetch-eclipse-mylyn-incubator.sh 

Patch0: %{pkg_name}-remove-hudson-discovery.patch
Patch1: %{pkg_name}-add-apache-xmlrpc.patch
Patch2: %{pkg_name}-ensure-sites-build-after-changes.patch
Patch3: %{pkg_name}-disable-online-tests.patch

Patch4: %{pkg_name}-merge-incubator.patch
Patch5: %{pkg_name}-remove-javax-activation.patch
Patch6: %{pkg_name}-bug-419133.patch
Patch7: %{pkg_name}-build-compat.patch

BuildArch: noarch

BuildRequires: java-devel >= 1.7.0
BuildRequires: jpackage-utils >= 1.7.5-18.1
BuildRequires: eclipse-platform >= 1:4.2.0
BuildRequires: eclipse-pde >= 1:4.2.0-0.6
BuildRequires: eclipse-rcp >= 1:4.2.0-0.6
BuildRequires: eclipse-cdt
BuildRequires: eclipse-egit
BuildRequires: eclipse-jgit
BuildRequires: eclipse-subclipse
BuildRequires: tycho >= 0.14.1-5
BuildRequires: eclipse-egit
BuildRequires: jacoco
BuildRequires: lucene
BuildRequires: maven-local

BuildRequires: axis >= 1.4
BuildRequires: apache-commons-lang >= 2.6-6
BuildRequires: apache-commons-logging
BuildRequires: apache-commons-io >= 2.3
BuildRequires: ws-commons-util >= 1.0.1-21
BuildRequires: xmlrpc-client >= 3.1.3
BuildRequires: xmlrpc-common >= 3.1.3
BuildRequires: jdom >= 1.1.2-3
BuildRequires: rome >= 0.9-9
BuildRequires: jakarta-commons-httpclient
BuildRequires: httpcomponents-client >= 4.1.3-2
BuildRequires: httpcomponents-core >= 4.1.4
BuildRequires: apache-commons-discovery >= 0.5-2
#BuildRequires: jacoco-maven-plugin
BuildRequires: google-gson >= 2.0.0
BuildRequires: javamail >= 1.4.3-11
BuildRequires: guava
BuildRequires: xalan-j2
BuildRequires: junit
BuildRequires: hamcrest
BuildRequires: objenesis
BuildRequires: mockito
BuildRequires: maven-install-plugin
BuildRequires: maven-deploy-plugin
BuildRequires: maven-plugin-build-helper

Requires: eclipse-platform >= 1:4.2.0
Requires: eclipse-rcp >= 1:4.2.0-0.6
Requires: apache-commons-lang >= 2.6-6
Requires: apache-commons-logging
Requires: apache-commons-io >= 2.3
Requires: ws-commons-util >= 1.0.1-21
Requires: xmlrpc-client  >= 3.1.3
Requires: xmlrpc-common  >= 3.1.3
Requires: jpackage-utils
Requires: rome >= 0.9-9
Requires: xml-commons-apis
Requires: httpcomponents-client >= 4.1.3-2
Requires: httpcomponents-core >= 4.1.4
Requires: jakarta-commons-httpclient
Requires: apache-commons-discovery >= 0.5-2
Requires: jdom >= 1.1.2-3
Requires: javamail >= 1.4.3-11
Requires: lucene
%{?scl:Requires: %scl_runtime}

Provides: %{name}-commons = %{version}-%{release}
Obsoletes: %{name}-commons < %{version}-%{release}
Provides: %{name}-context = %{version}-%{release}
Obsoletes: %{name}-context < %{version}-%{release}




%description
Mylyn integrates task support into Eclipse. It supports offline editing
for certain task repositories and monitors work activity to hide
information that is not relevant to the current task.

%package context-java
Summary:  Mylyn Bridge:  Java Development
Requires: %{?scl_prefix}eclipse-jdt
Requires: %{name}-context = %{version}-%{release}
Provides: %{name}-java = %{version}-%{release}
%{!?scl:Obsoletes: eclipse-context-java < %{version}-%{release}}


%description context-java
Mylyn Task-Focused UI extensions for JDT.  Provides focusing of Java
element views and editors.

%package context-pde
Summary:  Mylyn Bridge:  Plug-in Development
Requires: %{?scl_prefix}eclipse-pde
Requires: %{name}-java = %{version}-%{release}
Provides: %{name}-pde = %{version}-%{release}
%{!?scl:Obsoletes: eclipse-context-pde < %{version}-%{release}}


%description context-pde
Mylyn Task-Focused UI extensions for PDE, Ant, Team Support and CVS.

%package context-cdt
Summary:  Mylyn Bridge:  C/C++ Development
Requires: %{name}-context = %{version}-%{release}
Requires: %{?scl_prefix}eclipse-cdt

%{!?scl:Provides: eclipse-cdt-mylyn = 2:1.0.0-1.fc12}
Provides: %{name}-cdt = %{version}-%{release}
%{!?scl:Obsoletes: eclipse-context-cdt < %{version}-%{release}}
%{!?scl:Obsoletes: eclipse-cdt-mylyn < 2:1.0.0}

%description context-cdt
Mylyn Task-Focused UI extensions for CDT.  Provides focusing of C/C++
element views and editors.


%package context-team
Summary:  Mylyn Context Connector: Team Support
Requires: %{name}-context = %{version}-%{release}


%description context-team
Mylyn Task-Focused UI extensions for Team version control.

%package ide
Summary: Mylyn Context Connector: Eclipse IDE
Requires: %{name} = %{version}-%{release}
Requires: %{name}-context = %{version}-%{release}
Requires: %{name}-context-team = %{version}-%{release}

%description ide
Mylyn Task-Focused UI extensions for the Eclipse IDE. 
Provides focusing of common IDE views and editors.

%package tasks-bugzilla
Summary: Mylyn Tasks Connector: Bugzilla
Requires: %{?scl_prefix}eclipse-platform >= 1:4.2.0
Requires: %{name} = %{version}-%{release}
Provides: %{name}-bugzilla = %{version}-%{release}


%description tasks-bugzilla
Provides Task List integration, offline support and rich editing for the
open source Bugzilla bug tracker.


%package docs-wikitext
Summary: Mylyn WikiText
Requires: %{?scl_prefix}eclipse-platform >= 1:3.8.0
Requires: %{name} = %{version}-%{release}
Requires: %{name}-context = %{version}-%{release}
Requires: jsoup
Provides: %{name}-wikitext = %{version}-%{release}


%description docs-wikitext
Enables parsing and display of lightweight markup (wiki text).


%package docs-htmltext
Summary: Mylyn HtmlText
Requires: %{?scl_prefix}eclipse-platform >= 1:3.8.0


%description docs-htmltext
Enables editing of HTML text.

%package docs-epub
Summary: Mylyn EPub
Requires: %{?scl_prefix}eclipse-platform >= 1:3.8.0


%description docs-epub
The EPUB framework in Mylyn Docs offers API to create, manipulate,
read and write EPUB formatted files. 

%package  tasks-trac
Summary: Mylyn Tasks Connector: Trac
Requires: %{?scl_prefix}eclipse-platform >= 1:4.2.0
Requires: %{name} = %{version}-%{release}
Requires: %{name}-context = %{version}-%{release}
Requires: google-gson

Provides: %{name}-trac = %{version}-%{release}

%description tasks-trac
Provides Task List integration, offline support and rich editing
for the open source Trac issue tracker.

%package  tasks-web
Summary: Mylyn Tasks Connector: Web Templates (Advanced) (Incubation)
Requires: %{?scl_prefix}eclipse-platform >= 1:4.2.0
Requires: %{name} = %{version}-%{release}
Requires: rome >= 0.9-9
Requires: jdom >= 1.1.2-3

Provides: %{name}-webtasks = %{version}-%{release}

%description tasks-web
Provides Task List integration for web-based issue trackers
and templates for example projects.


%package versions
Summary: Eclipse Mylyn Versions
Requires:      %{name} = %{version}-%{release}


%description versions
Provides a framework for accessing team providers for Eclipse Mylyn.


%package versions-git
Summary: Mylyn Versions Connector: Git
Requires: %{?scl_prefix}eclipse-platform >= 1:3.8.0
Requires: %{?scl_prefix}eclipse-egit >= 0.10.1
Requires: %{name}-versions = %{version}-%{release}


%description versions-git
Provides Git integration for Eclipse Mylyn.

%package versions-cvs
Summary: Mylyn Versions Connector: CVS
Requires: %{?scl_prefix}eclipse-platform >= 1:3.8.0
Requires: %{name}-versions = %{version}-%{release}


%description versions-cvs
Provides CVS integration for Eclipse Mylyn.

%package versions-subclipse
Summary: Mylyn Versions Connector: CVS
Requires: %{?scl_prefix}eclipse-platform >= 1:3.8.0
Requires: %{name}-versions = %{version}-%{release}
Requires: %{?scl_prefix}eclipse-subclipse


%description versions-subclipse
Provides CVS integration for Eclipse Mylyn.

%package builds
Summary: Eclipse Mylyn Builds
Requires: %{name} = %{version}-%{release}
Requires: %{name}-context = %{version}-%{release}
Requires: %{?scl_prefix}eclipse-emf
Requires: %{name}-versions = %{version}-%{release}
Requires: xml-commons-apis

%description builds
Provides a common framework to interact with continuous integration
build providers using Eclipse Mylyn.

%package builds-hudson
Summary: Mylyn Builds Connector: Hudson/Jenkins
Requires: java >= 1:1.7.0
Requires: %{?scl_prefix}eclipse-platform >= 1:4.2.0-0.6
Requires: %{name} = %{version}-%{release}
Requires: google-gson >= 1.6.0
Requires: %{name}-builds = %{version}-%{release}


%description builds-hudson
Support for the open source Hudson and Jenkins continuous integration servers.

%package sdk
Summary: Mylyn SDK
Requires: %{name} = %{version}-%{release}
Requires: %{name}-context = %{version}-%{release}
Requires: %{name}-context-java = %{version}-%{release}
Requires: %{name}-context-pde = %{version}-%{release}
Requires: %{name}-context-cdt = %{version}-%{release}
Requires: %{name}-context-team = %{version}-%{release}
Requires: %{name}-ide = %{version}-%{release}
Requires: %{name}-tasks-bugzilla = %{version}-%{release}
Requires: %{name}-docs-wikitext = %{version}-%{release}
Requires: %{name}-docs-htmltext = %{version}-%{release}
Requires: %{name}-tasks-trac = %{version}-%{release}
Requires: %{name}-versions = %{version}-%{release}
Requires: %{name}-versions-git = %{version}-%{release}
Requires: %{name}-versions-cvs = %{version}-%{release}
Requires: %{name}-versions-subclipse = %{version}-%{release}
Requires: %{name}-builds = %{version}-%{release}
Requires: %{name}-builds-hudson = %{version}-%{release}
Requires: guava
Requires: xalan-j2
Requires: hamcrest
Requires: objenesis
Requires: junit
Requires: mockito


%description sdk
Sources for all Mylyn bundles


%prep
%setup -q -n eclipse-mylyn-%{tag}-fetched-src
tar xaf %{SOURCE2} -C org.eclipse.mylyn.commons
cp %{SOURCE4} org.eclipse.mylyn.commons/org.eclipse.core.runtime.compatibility.auth/pom.xml
tar xaf %{SOURCE7} -C org.eclipse.mylyn.tasks --strip-components=1

%patch0
%patch1
%patch2
%patch3
%patch4
%patch5
%patch6
%patch7

#Disable plugins we can live without and for some reason are redundant (unpackaged or causing build failures).
#There must be empty line after each %%pom_* macro invocation.
grep -l -r --include="pom.xml" findbugs-maven-plugin . | ( while read pom_path; do %pom_remove_plugin org.codehaus.mojo:findbugs-maven-plugin $pom_path ; done ) ; 
find . -name feature.xml -exec sed -i -e "s/javax.mail/com.sun.mail.javax.mail/" {} \;
grep -l -r --include="pom.xml" maven-pmd-plugin . | ( while read pom_path; do %pom_remove_plugin org.apache.maven.plugins:maven-pmd-plugin $pom_path ; done ) ; 

#Disable modules we can't build yet
%pom_disable_module org.eclipse.mylyn.reviews .

%pom_disable_module org.eclipse.mylyn.commons.tck-feature org.eclipse.mylyn.commons 

%pom_disable_module org.eclipse.mylyn.tests org.eclipse.mylyn .

%pom_disable_module org.eclipse.mylyn.test-feature org.eclipse.mylyn.tasks .

#Disable all tests (except one that was easier to build than patch dependent bundles.
# grep -v org.eclipse.mylyn.doc
grep -l -r --include="pom.xml" "tests" . | ( while read pom_path; do echo `%pom_xpath_remove "*[local-name() = 'module' and contains(text(),'tests') and not(contains(text(),'tests.'))]" $pom_path` ; done ) ;

#Remove all architectures that do not match current build architecture.
%pom_xpath_remove "*[local-name() = 'environment' and 
       (child::*[local-name() = 'os' and not(text() = 'linux')] 
            or child::*[local-name() = 'ws' and not(text() = 'gtk')] 
            or child::*[local-name() = 'arch' and not(text() = '%{_arch}')]) ]" org.eclipse.mylyn/org.eclipse.mylyn-parent/pom.xml

%pom_remove_plugin :tycho-packaging-plugin org.eclipse.mylyn/org.eclipse.mylyn-parent
%pom_remove_plugin :jacoco-maven-plugin org.eclipse.mylyn/org.eclipse.mylyn.maven-parent/pom.xml
%pom_remove_plugin :jacoco-maven-plugin org.eclipse.mylyn/org.eclipse.mylyn-parent/pom.xml
%pom_set_parent org.eclipse.mylyn.tasks:org.eclipse.mylyn.tasks-parent:3.10.0-SNAPSHOT org.eclipse.mylyn.tasks/org.eclipse.mylyn.trac.wiki/pom.xml
%pom_set_parent org.eclipse.mylyn.tasks:org.eclipse.mylyn.tasks-parent:3.10.0-SNAPSHOT org.eclipse.mylyn.tasks/org.eclipse.mylyn.trac.wiki-feature/pom.xml
%pom_set_parent org.eclipse.mylyn.tasks:org.eclipse.mylyn.tasks-parent:3.10.0-SNAPSHOT org.eclipse.mylyn.tasks/org.eclipse.mylyn.web.tasks/pom.xml
%pom_set_parent org.eclipse.mylyn.tasks:org.eclipse.mylyn.tasks-parent:3.10.0-SNAPSHOT org.eclipse.mylyn.tasks/org.eclipse.mylyn.web.tasks-feature/pom.xml

rm org.eclipse.mylyn.builds/org.eclipse.mylyn.hudson.ui/src/org/eclipse/mylyn/internal/hudson/ui/HudsonStartup.java

#Be more tolerant for guava
sed -i -e "s/compatible/greaterOrEqual/g" org.eclipse.mylyn.versions/org.eclipse.mylyn.versions.sdk-feature/feature.xml
sed -i -e "s/e3.5/e3.6/g" org.eclipse.mylyn.commons/org.eclipse.mylyn.commons-target/pom.xml

%build
%{?scl:%scl_maven_opts}
export MAVEN_OPTS="-XX:CompileCommand=exclude,org/eclipse/tycho/core/osgitools/EquinoxResolver,newState ${MAVEN_OPTS}"
mvn-rpmbuild clean install -Dmaven.test.skip=true

%install
install -d %{buildroot}%{install_loc}/mylyn
install -d %{buildroot}%{install_loc}/mylyn/eclipse
install -d %{buildroot}%{install_loc}/mylyn/eclipse/plugins
install -d %{buildroot}%{install_loc}/mylyn/eclipse/features

cp  org.eclipse.mylyn/org.eclipse.mylyn-site/target/site/plugins/*.jar %{buildroot}%{install_loc}/mylyn/eclipse/plugins/

pushd %{buildroot}%{install_loc}/mylyn/eclipse/plugins/

	rm com.google.gson_*.jar
	ln -s %{_non_scl_javadir}/google-gson.jar

	rm com.sun.syndication_*.jar
	ln -s %{_non_scl_javadir}/rome*.jar

	rm com.sun.mail.javax.mail_*.jar
	ln -s %{_non_scl_javadir}/javamail/mail.jar

	rm javax.wsdl_*.jar
	ln -s %{_non_scl_javadir}/wsdl4j.jar

	rm javax.xml_*.jar
	ln -s %{_non_scl_javadir}/jaxp.jar

	rm javax.xml.rpc_*.jar
 	ln -s %{_non_scl_javadir}/axis/jaxrpc.jar

	rm javax.xml.soap_*.jar
	ln -s %{_non_scl_javadir}/axis/saaj.jar

	rm org.apache.xerces_*.jar
	ln -s %{_non_scl_javadir}/xerces-j2.jar

	rm org.apache.axis_*.jar
	ln -s %{_non_scl_javadir}/axis/axis.jar

	rm org.apache.xml.resolver_*.jar
	ln -s %{_non_scl_javadir}/xml-commons-resolver.jar

	rm org.apache.xml.serializer*.jar
	ln -s %{_non_scl_javadir}/xalan-j2-serializer.jar

	rm org.apache.commons.discovery_*.jar
	ln -s %{_non_scl_javadir}/apache-commons-discovery.jar

	rm org.apache.commons.io_*.jar
	ln -s %{_non_scl_javadir}/apache-commons-io.jar

	rm org.apache.commons.lang_*.jar
	ln -s %{_non_scl_javadir}/apache-commons-lang.jar

	rm org.apache.commons.httpclient_*.jar
	ln -s %{_non_scl_javadir}/commons-httpclient.jar

	rm org.apache.ws.commons.util_*.jar
	ln -s %{_non_scl_javadir}/ws-commons-util.jar
	
	rm org.apache.xmlrpc_*.jar
	ln -s %{_non_scl_javadir}/xmlrpc-client.jar
	ln -s %{_non_scl_javadir}/xmlrpc-common.jar

	rm org.jdom_*.jar
	ln -s %{_non_scl_javadir}/jdom.jar

	rm org.jsoup_*.jar
	ln -s %{_non_scl_javadir}/jsoup.jar

	rm com.google.guava_*.jar
	ln -s %{_non_scl_javadir}/guava.jar

	rm org.apache.lucene.core_*.jar #bundled by platform
	rm org.apache.httpcomponents.httpclient_*.jar #bundled by platform
	rm org.apache.httpcomponents.httpcore_*.jar #bundled by platform
	rm org.apache.commons.logging_*.jar #bundled by platform
	rm org.apache.commons.codec_*.jar #bundled by platform
popd

mkdir -p %{buildroot}%{install_loc}/mylyn/eclipse/features
for f in `ls -1 org.eclipse.mylyn/org.eclipse.mylyn-site/target/site/features/ | grep jar$`; do
    unzip org.eclipse.mylyn/org.eclipse.mylyn-site/target/site/features/$f -d %{buildroot}%{install_loc}/mylyn/eclipse/features/${f/.jar//};
done

install %{SOURCE6} %{buildroot}%{install_loc}/mylyn/eclipse/redhat-bugzilla-custom-transitions.txt

%files
%dir %{install_loc}/mylyn
%dir %{install_loc}/mylyn/eclipse
%dir %{install_loc}/mylyn/eclipse/features/
%dir %{install_loc}/mylyn/eclipse/plugins/
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn_feature_*
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.tasks.ide_*
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.tasks.core_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.tasks.index.core_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.tasks.index.ui_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.tasks.search_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.tasks.ui_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.tasks.bugs_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.help.ui_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.oslc.core_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.oslc.ui_*.jar
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.commons_*
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.commons.soap_feature_*
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.commons.activity_*
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.commons.compatibility_*
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.commons.identity_*
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.commons.notifications_*
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.commons.repositories_*
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.commons.repositories.http_*
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.discovery_*
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.monitor_*
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.commons.activity.ui_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.commons.core_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.commons.identity.core_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.commons.notifications.core_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.commons.notifications.feed_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.commons.notifications.ui_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.commons.repositories.core_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.commons.repositories.http.core_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.commons.repositories.ui_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.commons.screenshots_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.commons.ui_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.commons.workbench_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.discovery.core_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.discovery.ui*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.monitor.core_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.monitor.ui_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.commons.sdk.util_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.commons.soap_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.commons.xmlrpc_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.commons.net_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.core.runtime.compatibility.auth_*.jar
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.context_feature_*
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.context.core_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.context.ui_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.resources.ui_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.context.tasks.ui_*.jar
%{install_loc}/mylyn/eclipse/plugins/apache-commons-lang.jar
%{install_loc}/mylyn/eclipse/plugins/apache-commons-io.jar
%{install_loc}/mylyn/eclipse/plugins/jdom.jar
%{install_loc}/mylyn/eclipse/plugins/rome*.jar
%{install_loc}/mylyn/eclipse/plugins/xmlrpc-client.jar
%{install_loc}/mylyn/eclipse/plugins/xmlrpc-common.jar
%{install_loc}/mylyn/eclipse/plugins/commons-httpclient.jar
%{install_loc}/mylyn/eclipse/plugins/apache-commons-discovery.jar
%{install_loc}/mylyn/eclipse/plugins/ws-commons-util.jar
%{install_loc}/mylyn/eclipse/plugins/jaxp.jar
%{install_loc}/mylyn/eclipse/plugins/google-gson.jar
%{install_loc}/mylyn/eclipse/plugins/axis.jar
%{install_loc}/mylyn/eclipse/plugins/jaxrpc.jar
%{install_loc}/mylyn/eclipse/plugins/saaj.jar
%{install_loc}/mylyn/eclipse/plugins/mail.jar
%{install_loc}/mylyn/eclipse/plugins/guava.jar
%{install_loc}/mylyn/eclipse/plugins/wsdl4j.jar
%doc org.eclipse.mylyn.tasks/org.eclipse.mylyn-feature/epl-v10.html
%doc org.eclipse.mylyn.tasks/org.eclipse.mylyn-feature/license.html

%files context-java
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.java_feature_*
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.java.ui_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.java.tasks_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.ide.ui_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.ide.ant_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.debug.ui_*.jar
%doc org.eclipse.mylyn.context/org.eclipse.mylyn.java-feature/epl-v10.html
%doc org.eclipse.mylyn.context/org.eclipse.mylyn.java-feature/license.html

%files context-pde
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.pde_feature_*
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.pde.ui_*.jar
%doc org.eclipse.mylyn.context/org.eclipse.mylyn.pde-feature/epl-v10.html
%doc org.eclipse.mylyn.context/org.eclipse.mylyn.pde-feature/license.html

%files context-cdt
%{install_loc}/mylyn/eclipse/features/org.eclipse.cdt.mylyn_*
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.cdt.mylyn.ui_*.jar
%doc org.eclipse.mylyn.context/org.eclipse.mylyn.cdt-feature/epl-v10.html
%doc org.eclipse.mylyn.context/org.eclipse.mylyn.cdt-feature/license.html

%files context-team
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.team_feature_*
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.team.ui_*.jar
%doc org.eclipse.mylyn.context/org.eclipse.mylyn.team-feature/epl-v10.html
%doc org.eclipse.mylyn.context/org.eclipse.mylyn.team-feature/license.html

%files ide
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.ide_feature_*
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.team.cvs_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.bugzilla.ide_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.ide.ui_*.jar
%doc org.eclipse.mylyn.tasks/org.eclipse.mylyn.tasks.ide-feature/epl-v10.html
%doc org.eclipse.mylyn.tasks/org.eclipse.mylyn.tasks.ide-feature/license.html

%files tasks-bugzilla
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.bugzilla_feature_*
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.bugzilla.core_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.bugzilla.ui_*.jar
%{install_loc}/mylyn/eclipse/redhat-bugzilla-custom-transitions.txt
%doc org.eclipse.mylyn.tasks/org.eclipse.mylyn.bugzilla-feature/epl-v10.html
%doc org.eclipse.mylyn.tasks/org.eclipse.mylyn.bugzilla-feature/license.html

%files tasks-trac
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.trac_feature_*
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.trac.core_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.trac.ui_*.jar
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.trac.wiki_feature_*
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.trac.wiki_*.jar
%doc org.eclipse.mylyn.tasks/org.eclipse.mylyn.trac-feature/epl-v10.html
%doc org.eclipse.mylyn.tasks/org.eclipse.mylyn.trac-feature/license.html

%files tasks-web
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.web.tasks_feature_*
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.web.tasks_*.jar
%doc org.eclipse.mylyn.tasks/org.eclipse.mylyn.web.tasks-feature/epl-v10.html
%doc org.eclipse.mylyn.tasks/org.eclipse.mylyn.web.tasks-feature/license.html

%files docs-wikitext
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.wikitext_feature_*
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.wikitext.core_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.wikitext.textile.core_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.wikitext.mediawiki.core_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.wikitext.confluence.core_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.wikitext.tracwiki.core_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.wikitext.twiki.core_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.wikitext.ui_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.wikitext.help.ui_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.wikitext.textile.ui_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.wikitext.mediawiki.ui_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.wikitext.confluence.ui_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.wikitext.tracwiki.ui_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.wikitext.twiki.ui_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.wikitext.tasks.ui_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.wikitext.context.ui_*.jar
%{install_loc}/mylyn/eclipse/plugins/jsoup.jar
%doc org.eclipse.mylyn.docs/org.eclipse.mylyn.wikitext-feature/epl-v10.html
%doc org.eclipse.mylyn.docs/org.eclipse.mylyn.wikitext-feature/license.html

%files docs-htmltext
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.htmltext_*
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.htmltext.ui_*.jar
%doc org.eclipse.mylyn.docs/org.eclipse.mylyn.htmltext-feature/epl-v10.html
%doc org.eclipse.mylyn.docs/org.eclipse.mylyn.htmltext-feature/license.html

%files docs-epub
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.docs.epub_*
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.docs.epub.core_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.docs.epub.help_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.docs.epub.ui_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.docs.epub.ant.core_*.jar
%doc org.eclipse.mylyn.docs/org.eclipse.mylyn.docs.epub-feature/epl-v10.html
%doc org.eclipse.mylyn.docs/org.eclipse.mylyn.docs.epub-feature/license.html

%files versions
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.versions_*
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.versions.core_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.versions.ui_*.jar
%doc org.eclipse.mylyn.versions/org.eclipse.mylyn.versions-feature/epl-v10.html
%doc org.eclipse.mylyn.versions/org.eclipse.mylyn.versions-feature/license.html

%files versions-git
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.git_*
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.git.core_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.git.ui_*.jar
%doc org.eclipse.mylyn.versions/org.eclipse.mylyn.git-feature/epl-v10.html
%doc org.eclipse.mylyn.versions/org.eclipse.mylyn.git-feature/license.html

%files versions-cvs
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.cvs_*
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.cvs.core_*.jar
%doc org.eclipse.mylyn.versions/org.eclipse.mylyn.cvs-feature/epl-v10.html
%doc org.eclipse.mylyn.versions/org.eclipse.mylyn.cvs-feature/license.html

%files versions-subclipse
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.subclipse_*
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.subclipse.core_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.subclipse.ui_*.jar
%doc org.eclipse.mylyn.versions/org.eclipse.mylyn.subclipse-feature/epl-v10.html
%doc org.eclipse.mylyn.versions/org.eclipse.mylyn.subclipse-feature/license.html

%files builds
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.builds_*
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.builds.core_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.builds.ui_*.jar
%doc org.eclipse.mylyn.builds/org.eclipse.mylyn.builds-feature/epl-v10.html
%doc org.eclipse.mylyn.builds/org.eclipse.mylyn.builds-feature/license.html

%files builds-hudson
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.hudson_*
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.hudson.core_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.hudson.ui_*.jar
%doc org.eclipse.mylyn.builds/org.eclipse.mylyn.hudson-feature/epl-v10.html
%doc org.eclipse.mylyn.builds/org.eclipse.mylyn.hudson-feature/license.html

%files sdk
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.builds.sdk_*
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.context.sdk_*
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.commons.sdk_*
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.docs.epub.sdk_*
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.docs.sdk_*
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.sdk_feature_*
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.versions.sdk_*
%{install_loc}/mylyn/eclipse/features/org.eclipse.mylyn.wikitext.sdk_*
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.context.sdk.java_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.context.sdk.util_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.wikitext.help.sdk_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.tests.util_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.mylyn.*.source_*.jar
%{install_loc}/mylyn/eclipse/plugins/org.eclipse.cdt.mylyn.ui.source_*.jar
%{install_loc}/mylyn/eclipse/plugins/guava.jar
%{install_loc}/mylyn/eclipse/plugins/xerces-j2.jar
%{install_loc}/mylyn/eclipse/plugins/xalan-j2-serializer.jar
%{install_loc}/mylyn/eclipse/plugins/xml-commons-resolver.jar
%doc org.eclipse.mylyn.commons/org.eclipse.mylyn.commons.sdk-feature/epl-v10.html
%doc org.eclipse.mylyn.commons/org.eclipse.mylyn.commons.sdk-feature/license.html

%changelog
* Tue Nov 12 2013 Alexander Kurtakov <akurtako@redhat.com> 3.10.0-1
- Update to 3.10.
- Drop compat sources and patches as no longer needed.
- Switch to xz for sources.

* Wed Nov 06 2013 Roland Grunberg <rgrunber@redhat.com> 3.9.1-4
- Include fix for Eclipse bug 419869.

* Fri Oct 11 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.9.1-3
- Include fix for Eclipse bug 419133. 

* Thu Oct 3 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.9.1-2
- Add a workaround for a build failing on ARM.

* Thu Oct 3 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.9.1-1
- Update to Kepler SR1.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 12 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.9.0-2
- Adjust the build for the latest javamail.

* Fri Jun 28 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.9.0-1
- Use release tagged upstream.

* Tue Jun 18 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.9.0-0.8.gita6b7cd
- Update to Kepler release.

* Mon Jun 10 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.9.0-0.7.git2ad84d
- Fix for bug 403024.

* Fri Jun 7 2013 Roland Grunberg <rgrunber@redhat.com> 3.9.0-0.6.git2ad84d
- Update to latest upstream.

* Fri May 31 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.9.0-0.5.gita6b7cd
- Don't require jacoco for build.
- Update latest to latest upstream.

* Tue May 14 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.9.0-0.4.git8b0964
- Rebuild to pick up recent dependencies.

* Thu May 2 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.9.0-0.3.git8b0964
- Update to latest upstream.

* Fri Mar 15 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.9.0-0.2.gitf9e1cd
- Make noarch always.

* Fri Mar 1 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.9.0-0.1.gitf9e1cd
- Update to latest upstream.
- Initial SCLization.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 3.8.2-3
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Nov 23 2012 Krzysztof Daniel <kdaniel@redhat.com> 3.8.2-2
- Remove javax.xml.

* Tue Oct 2 2012 Krzysztof Daniel <kdaniel@redhat.com> 3.8.2-1
- Update to 3.8.2 upstream release.

* Tue Sep 18 2012 Krzysztof Daniel <kdaniel@redhat.com> 3.8.1-2
- Replace xmlrpc3 with xmlrpc to fix broken dependencies.

* Mon Aug 20 2012 Krzysztof Daniel <kdaniel@redhat.com> 3.8.1-1
- Update to latest upstream release.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jul 13 2012 Krzysztof Daniel <kdaniel@redhat.com> 3.8.0-5
- Improve obsoletes/conflicts to prevent dissappearing after
  update packages and mixing versions.

* Thu Jul 12 2012 Krzysztof Daniel <kdaniel@redhat.com> 3.8.0-4
- Change the root location of all files.

* Wed Jul 11 2012 Krzysztof Daniel <kdaniel@redhat.com> 3.8.0-3
- Symlink the wsdl jar provided by axis package.

* Tue Jul 10 2012 Krzysztof Daniel <kdaniel@redhat.com> 3.8.0-2
- Add proper BR for jpackage-utils and maven.

* Tue Jul 10 2012 Krzysztof Daniel <kdaniel@redhat.com> 3.8.0-1
- Completely repackaged mylyn.
- Added epub feature.
- Added support for subclipse.

* Mon May 7 2012 Krzysztof Daniel <kdaniel@redhat.com> 3.7.0-5
- Patch for bug 378230 added.

* Mon Apr 30 2012 Krzysztof Daniel <kdaniel@redhat.com> 3.7.0-4
- Include schema description.

* Fri Apr 13 2012 Krzysztof Daniel <kdaniel@redhat.com> 3.7.0-3
- Move to eclipse 4.2.
- Build help.
- Fix the minimum eclipse-rcp requirement

* Mon Apr 2 2012 Krzysztof Daniel <kdaniel@redhat.com> 3.7.0-2
- Bump version to fix upgradepath.

* Mon Mar 26 2012 Krzysztof Daniel <kdaniel@redhat.com> 3.7.0-1
- Update to upstream 3.7.0 release

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec 2 2011 Sami Wagiaalla <swagiaal@redhat.com> 3.6.4-2
- Set noarch conditionally. 

* Tue Nov 29 2011 Sami Wagiaalla <swagiaal@redhat.com> 3.6.4-2
- Add ExclusiveArch: %%{ix86} x86_64 for RHEL.

* Mon Nov 28 2011 Andrew Robinson <arobinso@redhat.com> 3.6.4-1
- Update to upstream 3.6.4 release.

* Mon Oct 31 2011 Andrew Robinson <arobinso@redhat.com> 3.6.3-1
- Update to upstream 3.6.3 release.

* Fri Oct 7 2011 Alexander Kurtakov <akurtako@redhat.com> 3.6.2-1
- Update to upstream 3.6.2 release.

* Thu Jul 14 2011 Severin Gehwolf <sgehwolf@redhat.com> 3.6.0-3
- Mylyn requires Eclipse 3.5 and up. Changed R/BRs
  accordingly.

* Thu Jul 14 2011 Severin Gehwolf <sgehwolf@redhat.com> 3.6.0-2
- Fix qualifier to match upstream.

* Wed Jul 13 2011 Severin Gehwolf <sgehwolf@redhat.com> 3.6.0-1
- Update to upstream's 3.6.0 release.

* Tue Apr 26 2011 Severin Gehwolf <sgehwolf@redhat.com> 3.5.1-1
- Update to upstream 3.5.1.

* Fri Apr 8 2011 Severin Gehwolf <sgehwolf@redhat.com> 3.5.0-1
- Update to upstream 3.5.0 release. This update splits this
  existing SRPM up into about 7 additional ones.
- Now requires new package eclipse-mylyn-commons.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 5 2011 Alexander Kurtakov <akurtako@redhat.com> 3.4.2-4
- Fix symlink to non-existing versioned jar.

* Tue Dec 7 2010 Severin Gehwolf <sgehwolf@redhat.com> 3.4.2-3
- Really fix FTBFS.

* Tue Dec 7 2010 Severin Gehwolf <sgehwolf@redhat.com> 3.4.2-2
- Fix FTBFS RH Bz #660784

* Fri Oct 8 2010 Chris Aniszczyk <zx@redhat.com> 3.4.2-1
- Update to 3.4.2.

* Wed Sep 1 2010 Jeff Johnston <jjohnstn@redhat.com> 3.4.1-3
- Resolves: #605285
- Fix obsoletes/provides for eclipse-cdt-mylyn using an epoch of 2.

* Wed Sep 1 2010 Alexander Kurtakov <akurtako@redhat.com> 3.4.1-2
- Backport patch for wikitext to work with Fedora wiki.

* Tue Aug 31 2010 Alexander Kurtakov <akurtako@redhat.com> 3.4.1-1
- Update to 3.4.1.

* Tue Jul 27 2010 Charley Wang <chwang@redhat.com> 3.4.0-4
- Add Wikitext SDK to eclipse-mylyn

* Wed Jul 21 2010 Charley Wang <chwang@redhat.com> 3.4.0-3
- Relax cdt requires, remove extraneous links, fix xmlrpc split

* Thu Jul 15 2010 Charley Wang <chwang@redhat.com> 3.4.0-2
- Add required jar links to mylyn dropins directory

* Wed Jul 14 2010 Charley Wang <chwang@redhat.com> 3.4.0-1
- Update to 3.4.0. Add mylyn-commons feature, remove commons.soap

* Wed Mar 3 2010 Alexander Kurtakov <akurtako@redhat.com> 3.3.2-4
- Relax bundle version requires for commons-lang.

* Thu Feb 25 2010 Alexander Kurtakov <akurtako@redhat.com> 3.3.2-3
- Really update to 3.3.2.

* Thu Feb 25 2010 Alexander Kurtakov <akurtako@redhat.com> 3.3.2-2
- Bump release.

* Thu Feb 25 2010 Alexander Kurtakov <akurtako@redhat.com> 3.3.2-1
- Update to 3.3.2.

* Wed Feb 17 2010 Alexander Kurtakov <akurtako@redhat.com> 3.3.1-5
- Adapt to commons-lang 2.4.

* Wed Feb 17 2010 Alexander Kurtakov <akurtako@redhat.com> 3.3.1-4
- Fix FTBFS rhbz#564704.

* Thu Jan 07 2010 Andrew Overholt <overholt@redhat.com> 3.3.1-3
- Remove Fedora customizations (adding bugzilla instances).

* Thu Jan 07 2010 Andrew Overholt <overholt@redhat.com> 3.3.1-2
- Update license field to add ASL 2.0 for wikitext.

* Thu Dec 17 2009 Alexander Kurtakov <akurtako@redhat.com> 3.3.1-1
- Update to 3.3.1 version.

* Sun Nov 22 2009 Alexander Kurtakov <akurtako@redhat.com> 3.3.0-4
- Fix build with newer common-codec.

* Wed Oct 28 2009 Alexander Kurtakov <akurtako@redhat.com> 3.3.0-3
- CDT subpackage obsoletes eclipse-cdt-mylyn.

* Tue Oct 27 2009 Alexander Kurtakov <akurtako@redhat.com> 3.3.0-2
- Fix cdt description. Bump qualifier to be newer than Galileo update site.

* Tue Oct 27 2009 Alexander Kurtakov <akurtako@redhat.com> 3.3.0-1
- Update to 3.3.0.
- Add cdt bridge.
- Remove BR/R which are required by eclipse itself now.

* Tue Sep 22 2009 Alexander Kurtakov <akurtako@redhat.com> 3.2.1-2
- Add patch for correct building of o.e.wikitext.help.ui.

* Tue Aug 4 2009 Alexander Kurtakov <akurtako@redhat.com> 3.2.1-1
- Update to 3.2.1.

* Wed Apr 22 2009 Andrew Overholt <overholt@redhat.com> 3.1.1-1
- 3.1.1
- Bug fixes from 3.1.0:  http://tinyurl.com/mylyn-3-1-1bugs
- Remove wikitext build patch that has been merged upstream.

* Wed Mar 25 2009 Alexander Kurtakov <akurtako@redhat.com> 3.1.0-3
- Fix documentation build.

* Mon Mar 23 2009 Alexander Kurtakov <akurtako@redhat.com> 3.1.0-2
- Rebuild to not ship p2 context.xml.

* Tue Mar 17 2009 Andrew Overholt <overholt@redhat.com> 3.1.0-1
- 3.1.0
- Add wikitext sub-package.
- Update to new Fedora customizations plugin.
- Don't repack JARs as it breaks help content.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 9 2009 Andrew Overholt <overholt@redhat.com> 3.0.4-1
- 3.0.4

* Wed Nov 12 2008 Andrew Overholt <overholt@redhat.com> 3.0.3-4
- Add patch for e.o#239435 (rhbz#470356).

* Fri Oct 31 2008 Alexander Kurtakov <akurtako@redhat.com> 3.0.3-3
- Don't apply nojaxb.patch.
- Fix eclipse-mylyn-splitxmlrpc.patch to Import-Package:org.apache.xmlrpc.

* Tue Oct 21 2008 Alexander Kurtakov <akurtako@redhat.com> 3.0.3-2
- BR ws-jaxme.
- Bump xmlrpc3 requires for proper OSGi metadata.
- Fix trac feature.xml to not require different qualifier for the deps.

* Tue Oct 21 2008 Alexander Kurtakov <akurtako@redhat.com> 3.0.3-1
- 3.0.3.
- Rebase addfedoracustomizations.patch.

* Sat Oct 18 2008 Alexander Kurtakov <akurtako@redhat.com> 3.0.1-3
- Add >= for jdom to ensure proper OSGi metadata

* Mon Aug 11 2008 Andrew Overholt <overholt@redhat.com> 3.0.1-2
- Add >= for requirements to ensure proper OSGi metadata

* Fri Aug 08 2008 Andrew Overholt <overholt@redhat.com> 3.0.1-1
- Fix fuzz on adding Fedora customizations patch
- Add patch to make Red Hat bugzilla 3.0

* Thu Aug 07 2008 Andrew Overholt <overholt@redhat.com> 3.0.1-1
- Add webtasks sub-package

* Tue Aug 05 2008 Andrew Overholt <overholt@redhat.com> 3.0.1-1
- Update install locations
- Add qualifier hack for now

* Wed Jul 30 2008 Andrew Overholt <overholt@redhat.com> 3.0.1-1
- 3.0.1
- Add patch to not require jaxb (required by XML-RPC Orbit bundle)
- Fold -ide and -bugzilla into main package
- Add commented-out webtasks sub-package; to be enabled after rome
  review is complete

* Thu Jul 17 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.3.2-6
- fix license tag

* Wed May 14 2008 Andrew Overholt <overholt@redhat.com> 2.3.2-6
- ".qualifier" -> actual release qualifier in build (due to upstream
  build system change (e.o#108291, rh#446468).

* Tue Apr 15 2008 Andrew Overholt <overholt@redhat.com> 2.3.2-5
- Re-build to attempt to fix rhbz#442251 (broken cpio archive).

* Tue Apr 15 2008 Jesse Keating <jkeating@redhat.com> - 2.3.2-4
- Rebuild due to filesystem corruption

* Mon Apr 07 2008 Andrew Overholt <overholt@redhat.com> 2.3.2-3
- Fix commons-lang symlink.

* Mon Apr 07 2008 Andrew Overholt <overholt@redhat.com> 2.3.2-2
- Upload sources.

* Fri Apr 04 2008 Andrew Overholt <overholt@redhat.com> 2.3.2-1
- 2.3.2.
- Add jakarta-commons-lang dependency.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.1.0-2
- Autorebuild for GCC 4.3

* Wed Oct 24 2007 Andrew Overholt <overholt@redhat.com> 2.1.0-1
- 2.1.0
- Enable GNOME bugzilla by default

* Tue Oct 02 2007 Andrew Overholt <overholt@redhat.com> 2.0.0-10
- Add %%post gcj blocks for sub-packages (thanks to David Walluck).
- Rename fetching script (s/mylar/mylyn/).

* Fri Sep 21 2007 Andrew Overholt <overholt@redhat.com> 2.0.0-9
- Really remove all mylar references in mylyn feature - courtesy
  Mandriva package.

* Wed Sep 19 2007 Andrew Overholt <overholt@redhat.com> 2.0.0-8
- Add patch and source to have common bugzilla servers by default.

* Tue Sep 18 2007 Andrew Overholt <overholt@redhat.com> 2.0.0-7
- Fix filename of webcore jar.

* Tue Sep 18 2007 Andrew Overholt <overholt@redhat.com> 2.0.0-6
- Re-add gcj support (accidentally removed the flag).

* Fri Sep 07 2007 Andrew Overholt <overholt@redhat.com> 2.0.0-5
- Make web.core its own jar.
- Unpack web.core so we can symlink to dependencies.
- Symlink to dependencies of web.core.
- Remove rome jar and exports from web.core.
- BR/R all the versions of dependencies that have OSGi manifests.

* Fri Aug 24 2007 Andrew Overholt <overholt@redhat.com> 2.0.0-4
- ExcludeArch ppc64 (no xmlrpc3 on ppc64 due to rh#239123).

* Thu Aug 23 2007 Andrew Overholt <overholt@redhat.com> 2.0.0-3
- Add BR on eclipse-pde.

* Thu Aug 23 2007 Andrew Overholt <overholt@redhat.com> 2.0.0-2
- Add BR and R on eclipse-cvs-client.

* Thu Aug 23 2007 Andrew Overholt <overholt@redhat.com> 2.0.0-1
- Re-name to eclipse-mylyn.

* Fri Aug 10 2007 Ben Konrath <bkonrath@redhat.com> 2.0.0-1
- 2.0.0
- Add -java and -pde sub-packages.

* Wed Apr 25 2007 Andrew Overholt <overholt@redhat.com> 2.0-0.1.M2a.1
- 2.0M2a (a re-tag to fix some tagging issues).

* Wed Apr 18 2007 Andrew Overholt <overholt@redhat.com> 1.0-4
- Add workaround for missing method in GNU Classpath.

* Thu Apr 12 2007 Andrew Overholt <overholt@redhat.com> 1.0-3
- Add Obsoletes and Provides for eclipse-bugzilla on
  eclipse-mylar-bugzilla (comments in bug #222677).  If someone notices
  missing functionality to warrant removing the Provides, please file a
  bug.

* Tue Mar 20 2007 Andrew Overholt <overholt@redhat.com> 1.0-2
- Use xmlrpc3 jars instead of xmlrpc

* Fri Mar 16 2007 Andrew Overholt <overholt@redhat.com> 1.0-1
- Initial build
