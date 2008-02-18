%define gcj_support         1
%define eclipse_base        %{_datadir}/eclipse

Name: eclipse-mylyn 
Summary: Task-focused UI for Eclipse
Version: 2.0.0
Release: %mkrel 0.9.2
License: Eclipse Public License
URL: http://www.eclipse.org/mylyn
BuildRequires:  java-rpmbuild >= 0:1.5, make, gcc

# no xmlrpc3 on ppc64 due to:
# https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=239123
ExcludeArch: ppc64

# mkdir temp && cd temp
# sh fetch-mylyn.sh
# tar cjf org.eclipse.mylyn-R_2_0_0-fetched-src.tar.bz2 org.eclipse.mylyn
Source0: org.eclipse.mylyn-R_2_0_0-fetched-src.tar.bz2
Source1: fetch-mylar.sh
Source2: http://overholt.fedorapeople.org/fedoraeclipse-mylynbugzilla-0.0.1.zip

# SSLSocketFactory#createSocket() is not implemented in GNU Classpath
# http://gcc.gnu.org/bugzilla/show_bug.cgi?id=31626
Patch3: eclipse-mylar-createSocketworkaround.patch
# So we can symlink to dependencies
Patch4: %{name}-unpackwebcore.patch
Patch5: %{name}-webcorejar.patch
Patch6: %{name}-addfedoracustomizations.patch

BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root

%if %{gcj_support}
BuildRequires:    gcc-java
BuildRequires:    java-gcj-compat-devel
%else
BuildRequires:    java-devel >= 1.5.0
%endif

%if ! %{gcj_support}
BuildArch: noarch
%endif
BuildRequires: java-rpmbuild
BuildRequires: eclipse-pde >= 1:3.2.1
BuildRequires: eclipse-cvs-client >= 1:3.2.1
BuildRequires: jakarta-commons-codec >= 0:1.3-8
BuildRequires: jakarta-commons-httpclient >= 1:3.0.1-1.2
BuildRequires: jakarta-commons-logging
BuildRequires: ws-commons-util >= 0:1.0.1-5
BuildRequires: xmlrpc3-client >= 0:3.0-1.3
BuildRequires: xmlrpc3-common >= 0:3.0-1.3
Requires: eclipse-platform >= 1:3.2.1
Requires: eclipse-cvs-client >= 1:3.2.1
Requires: jakarta-commons-codec >= 0:1.3-8.2
Requires: jakarta-commons-httpclient >= 1:3.0.1-1.2
Requires: jakarta-commons-logging
Requires: ws-commons-util >= 0:1.0.1-2
Requires: xmlrpc3-client >= 0:3.0-1.3
Requires: xmlrpc3-common >= 0:3.0-1.3
Provides: eclipse-mylar = 0:2.0.0-1
Obsoletes: eclipse-mylar < 0:2.0.0

Group: Development/Java

%description
Mylyn integrates task support into Eclipse.  It supports offline editing
for certain task repositories and monitors work activity to hide
information that is not relevant to the current task.

%package  bugzilla
Summary:  Mylyn Bugzilla Connector
Requires: %{name} = %{version}-%{release}
Group: Development/Java
Provides: eclipse-bugzilla = 1:0.2.4-4
Obsoletes: eclipse-bugzilla < 1:0.2.5
Provides: eclipse-mylar-bugzilla = 0:2.0.0-1
Obsoletes: eclipse-mylar-bugzilla < 0:2.0.0

%description bugzilla
Bugzilla client integrated with Eclipse and Mylyn; can be used
standalone.

%package  ide
Summary:  Mylyn Focused UI
Requires: %{name} = %{version}-%{release}
Group: Development/Java
Provides: eclipse-mylar-ide = 0:2.0.0-1
Obsoletes: eclipse-mylar-ide < 0:2.0.0

%description ide
Mylyn Focused UI for reducing information overload when working with
tasks. Filters and decorates views and editors to focus on the task
context.

%package  trac
Summary:  Mylyn Trac Connector
Requires: %{name} = %{version}-%{release}
Group: Development/Java
Provides: eclipse-mylar-trac = 0:2.0.0-1
Obsoletes: eclipse-mylar-trac < 0:2.0.0

%description trac
Trac client integrated with Eclipse and Mylyn; can be used standalone.

%package  java
Summary:  Mylyn Focused UI
Requires: eclipse-jdt
Requires: %{name}-ide = %{version}-%{release}
Group: Development/Java

%description java
Mylyn Task-Focused UI extensions for JDT.  Provides focusing of Java
element views and editors.

%package  pde
Summary:  Mylyn Focused UI
Requires: eclipse-pde
Requires: %{name}-java = %{version}-%{release}
Group: Development/Java

%description pde
Mylyn Task-Focused UI extensions for PDE, Ant, Team Support and CVS.

%prep
%setup -q -n org.eclipse.mylyn
unzip -q %{SOURCE2}

# GCJ issue
sed --in-place "s/@Override//" \
   org.eclipse.mylyn.context.ui/src/org/eclipse/mylyn/internal/context/ui/commands/FocusViewHandler.java \
   org.eclipse.mylyn.tasks.ui/src/org/eclipse/mylyn/internal/tasks/ui/commands/AddTaskRepositoryHandler.java

# GCJ issue
pushd org.eclipse.mylyn.web.core
%patch3 -p0
%patch5
popd

# So we can symlink to dependencies
%patch4

/bin/sh -x %{eclipse_base}/buildscripts/copy-platform SDK %{eclipse_base}
mkdir home

# symlink out to jars we built
pushd org.eclipse.mylyn.web.core/lib-httpclient
rm commons-*.jar
ln -s %{_javadir}/commons-codec-1.3.jar
ln -s %{_javadir}/commons-httpclient.jar commons-httpclient-3.0.1.jar
ln -s %{_javadir}/commons-logging-api.jar commons-logging-api-1.0.4.jar
ln -s %{_javadir}/commons-logging.jar commons-logging-1.0.4.jar
popd
pushd org.eclipse.mylyn.web.core/lib-xmlrpc
rm ws-commons-*.jar
rm xmlrpc*.jar
ln -s %{_javadir}/xmlrpc3-client-3.0.jar xmlrpc-client-3.0.jar
ln -s %{_javadir}/xmlrpc3-common-3.0.jar xmlrpc-common-3.0.jar
ln -s %{_javadir}/ws-commons-util-1.0.1.jar
popd
pushd org.eclipse.mylyn.web.core/lib-rome
rm *.jar
ln -s %{_javadir}/jdom-1.0.jar
popd

pushd org.eclipse.mylyn.bugzilla-feature
%patch6
popd

# remove references to mylar in feature
sed --in-place -e "304,456d" org.eclipse.mylyn-feature/feature.xml 
sed --in-place "s/<import.*mylar.*\/>//" org.eclipse.mylyn-feature/feature.xml
%{__grep} mylar org.eclipse.mylyn-feature/feature.xml && exit 1

%build
SDK=$(cd SDK > /dev/null && pwd)

# Eclipse may try to write to the home directory.
homedir=$(cd home > /dev/null && pwd)

# build the main mylyn feature
%{java} -cp $SDK/startup.jar                              \
     -Dosgi.sharedConfiguration.area=%{_libdir}/eclipse/configuration  \
     org.eclipse.core.launcher.Main                    \
     -application org.eclipse.ant.core.antRunner       \
     -DjavacSource=1.5                                 \
     -DjavacTarget=1.5                                 \
     -Dtype=feature                                    \
     -Did=org.eclipse.mylyn_feature                    \
     -DbaseLocation=$SDK                               \
     -DsourceDirectory=$(pwd)                          \
     -DbuildDirectory=$(pwd)/build                     \
     -Dbuilder=%{eclipse_base}/plugins/org.eclipse.pde.build/templates/package-build \
     -f %{eclipse_base}/plugins/org.eclipse.pde.build/scripts/build.xml \
     -vmargs -Duser.home=$homedir                      \
     -DJ2SE-1.5=%{_jvmdir}/java/jre/lib/rt.jar

# build the mylyn bugzilla feature
%{java} -cp $SDK/startup.jar                              \
     -Dosgi.sharedConfiguration.area=%{_libdir}/eclipse/configuration  \
     org.eclipse.core.launcher.Main                    \
     -application org.eclipse.ant.core.antRunner       \
     -DjavacSource=1.5                                 \
     -DjavacTarget=1.5                                 \
     -Dtype=feature                                    \
     -Did=org.eclipse.mylyn.bugzilla_feature           \
     -DbaseLocation=$SDK                               \
     -DsourceDirectory=$(pwd)                          \
     -DbuildDirectory=$(pwd)/build                     \
     -Dbuilder=%{eclipse_base}/plugins/org.eclipse.pde.build/templates/package-build \
     -f %{eclipse_base}/plugins/org.eclipse.pde.build/scripts/build.xml \
     -vmargs -Duser.home=$homedir                      \
     -DJ2SE-1.5=%{_jvmdir}/java/jre/lib/rt.jar

# build the mylyn context feature
%{java} -cp $SDK/startup.jar                              \
     -Dosgi.sharedConfiguration.area=%{_libdir}/eclipse/configuration  \
     org.eclipse.core.launcher.Main                    \
     -application org.eclipse.ant.core.antRunner       \
     -DjavacSource=1.5                                 \
     -DjavacTarget=1.5                                 \
     -Dtype=feature                                    \
     -Did=org.eclipse.mylyn.context_feature            \
     -DbaseLocation=$SDK                               \
     -DsourceDirectory=$(pwd)                          \
     -DbuildDirectory=$(pwd)/build                     \
     -Dbuilder=%{eclipse_base}/plugins/org.eclipse.pde.build/templates/package-build \
     -f %{eclipse_base}/plugins/org.eclipse.pde.build/scripts/build.xml \
     -vmargs -Duser.home=$homedir                      \
     -DJ2SE-1.5=%{_jvmdir}/java/jre/lib/rt.jar

# build the mylyn ide feature
%{java} -cp $SDK/startup.jar                              \
     -Dosgi.sharedConfiguration.area=%{_libdir}/eclipse/configuration  \
     org.eclipse.core.launcher.Main                    \
     -application org.eclipse.ant.core.antRunner       \
     -DjavacSource=1.5                                 \
     -DjavacTarget=1.5                                 \
     -Dtype=feature                                    \
     -Did=org.eclipse.mylyn.ide_feature                \
     -DbaseLocation=$SDK                               \
     -DsourceDirectory=$(pwd)                          \
     -DbuildDirectory=$(pwd)/build                     \
     -Dbuilder=%{eclipse_base}/plugins/org.eclipse.pde.build/templates/package-build \
     -f %{eclipse_base}/plugins/org.eclipse.pde.build/scripts/build.xml \
     -vmargs -Duser.home=$homedir                      \
     -DJ2SE-1.5=%{_jvmdir}/java/jre/lib/rt.jar

# build the mylyn trac feature
%{java} -cp $SDK/startup.jar                              \
     -Dosgi.sharedConfiguration.area=%{_libdir}/eclipse/configuration  \
     org.eclipse.core.launcher.Main                    \
     -application org.eclipse.ant.core.antRunner       \
     -DjavacSource=1.5                                 \
     -DjavacTarget=1.5                                 \
     -Dtype=feature                                    \
     -Did=org.eclipse.mylyn.trac_feature               \
     -DbaseLocation=$SDK                               \
     -DsourceDirectory=$(pwd)                          \
     -DbuildDirectory=$(pwd)/build                     \
     -Dbuilder=%{eclipse_base}/plugins/org.eclipse.pde.build/templates/package-build \
     -f %{eclipse_base}/plugins/org.eclipse.pde.build/scripts/build.xml \
     -vmargs -Duser.home=$homedir                      \
     -DJ2SE-1.5=%{_jvmdir}/java/jre/lib/rt.jar

# build the mylyn java feature
%{java} -cp $SDK/startup.jar                              \
     -Dosgi.sharedConfiguration.area=%{_libdir}/eclipse/configuration  \
     org.eclipse.core.launcher.Main                    \
     -application org.eclipse.ant.core.antRunner       \
     -DjavacSource=1.5                                 \
     -DjavacTarget=1.5                                 \
     -Dtype=feature                                    \
     -Did=org.eclipse.mylyn.java_feature               \
     -DbaseLocation=$SDK                               \
     -DsourceDirectory=$(pwd)                          \
     -DbuildDirectory=$(pwd)/build                     \
     -Dbuilder=%{eclipse_base}/plugins/org.eclipse.pde.build/templates/package-build \
     -f %{eclipse_base}/plugins/org.eclipse.pde.build/scripts/build.xml \
     -vmargs -Duser.home=$homedir                      \
     -DJ2SE-1.5=%{_jvmdir}/java/jre/lib/rt.jar

# build the mylyn pde feature
%{java} -cp $SDK/startup.jar                              \
     -Dosgi.sharedConfiguration.area=%{_libdir}/eclipse/configuration  \
     org.eclipse.core.launcher.Main                    \
     -application org.eclipse.ant.core.antRunner       \
     -DjavacSource=1.5                                 \
     -DjavacTarget=1.5                                 \
     -Dtype=feature                                    \
     -Did=org.eclipse.mylyn.pde_feature               \
     -DbaseLocation=$SDK                               \
     -DsourceDirectory=$(pwd)                          \
     -DbuildDirectory=$(pwd)/build                     \
     -Dbuilder=%{eclipse_base}/plugins/org.eclipse.pde.build/templates/package-build \
     -f %{eclipse_base}/plugins/org.eclipse.pde.build/scripts/build.xml \
     -vmargs -Duser.home=$homedir                      \
     -DJ2SE-1.5=%{_jvmdir}/java/jre/lib/rt.jar


%install
rm -rf %{buildroot}
install -d -m 755 $RPM_BUILD_ROOT%{eclipse_base}
unzip -q -d $RPM_BUILD_ROOT%{eclipse_base}/.. \
 build/rpmBuild/org.eclipse.mylyn_feature.zip
unzip -q -d $RPM_BUILD_ROOT%{eclipse_base}/.. \
 build/rpmBuild/org.eclipse.mylyn.bugzilla_feature.zip
unzip -q -d $RPM_BUILD_ROOT%{eclipse_base}/.. \
 build/rpmBuild/org.eclipse.mylyn.context_feature.zip
unzip -q -d $RPM_BUILD_ROOT%{eclipse_base}/.. \
 build/rpmBuild/org.eclipse.mylyn.ide_feature.zip
unzip -q -d $RPM_BUILD_ROOT%{eclipse_base}/.. \
 build/rpmBuild/org.eclipse.mylyn.trac_feature.zip
unzip -q -d $RPM_BUILD_ROOT%{eclipse_base}/.. \
 build/rpmBuild/org.eclipse.mylyn.java_feature.zip
unzip -q -d $RPM_BUILD_ROOT%{eclipse_base}/.. \
 build/rpmBuild/org.eclipse.mylyn.pde_feature.zip

# symlink
pushd $RPM_BUILD_ROOT%{eclipse_base}/plugins/org.eclipse.mylyn.web.core_*/lib-httpclient
rm commons-*.jar
ln -s %{_javadir}/commons-codec-1.3.jar
ln -s %{_javadir}/commons-httpclient.jar commons-httpclient-3.0.1.jar
ln -s %{_javadir}/commons-logging-api.jar commons-logging-api-1.0.4.jar
ln -s %{_javadir}/commons-logging.jar commons-logging-1.0.4.jar
popd
pushd $RPM_BUILD_ROOT%{eclipse_base}/plugins/org.eclipse.mylyn.web.core_*/lib-xmlrpc
rm ws-commons-*.jar
rm xmlrpc*.jar
ln -s %{_javadir}/xmlrpc3-client-3.0.jar xmlrpc-client-3.0.jar
ln -s %{_javadir}/xmlrpc3-common-3.0.jar xmlrpc-common-3.0.jar
ln -s %{_javadir}/ws-commons-util-1.0.1.jar
popd
pushd $RPM_BUILD_ROOT%{eclipse_base}/plugins/org.eclipse.mylyn.web.core_*/lib-rome
rm -f *.jar
ln -s %{_javadir}/jdom-1.0.jar
popd

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%clean
rm -rf %{buildroot}

%if %{gcj_support}
%post
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi

%postun
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%files bugzilla
%defattr(-,root,root,-)
%{eclipse_base}/plugins/org.eclipse.mylyn.bugzilla.core_*.jar
%{eclipse_base}/plugins/org.eclipse.mylyn.bugzilla.ui_*.jar
%{eclipse_base}/plugins/org.fedoraproject.mylyn.bugzilla_*.jar
%dir %{eclipse_base}/features/org.eclipse.mylyn.bugzilla_feature_*
%doc %{eclipse_base}/features/org.eclipse.mylyn.bugzilla_feature_*/license.html
%doc %{eclipse_base}/features/org.eclipse.mylyn.bugzilla_feature_*/about.html
%doc %{eclipse_base}/features/org.eclipse.mylyn.bugzilla_feature_*/epl-v10.html
%{eclipse_base}/features/org.eclipse.mylyn.bugzilla_feature_*/feature.xml
%if %{gcj_support}
%{_libdir}/gcj/%{name}/org.eclipse.mylyn.bugzilla*
%{_libdir}/gcj/%{name}/org.fedoraproject.mylyn.bugzilla*
%endif

%files ide
%defattr(-,root,root,-)
%{eclipse_base}/plugins/org.eclipse.mylyn.ide.ui_*.jar
%dir %{eclipse_base}/features/org.eclipse.mylyn.ide_feature_*
%doc %{eclipse_base}/features/org.eclipse.mylyn.ide_feature_*/license.html
%doc %{eclipse_base}/features/org.eclipse.mylyn.ide_feature_*/epl-v10.html
%{eclipse_base}/features/org.eclipse.mylyn.ide_feature_*/feature.xml
%if %{gcj_support}
%{_libdir}/gcj/%{name}/org.eclipse.mylyn.ide.ui_*
%endif

%files trac
%defattr(-,root,root,-)
%{eclipse_base}/plugins/org.eclipse.mylyn.trac.core_*.jar
%{eclipse_base}/plugins/org.eclipse.mylyn.trac.ui_*.jar
%dir %{eclipse_base}/features/org.eclipse.mylyn.trac_feature_*
%{eclipse_base}/features/org.eclipse.mylyn.trac_feature_*/feature.xml
%if %{gcj_support}
%{_libdir}/gcj/%{name}/org.eclipse.mylyn.trac*
%endif

%files java
%defattr(-,root,root,-)
%{eclipse_base}/plugins/org.eclipse.mylyn.java.ui_*.jar
%dir %{eclipse_base}/features/org.eclipse.mylyn.java_feature_*
%doc %{eclipse_base}/features/org.eclipse.mylyn.java_feature_*/license.html
%doc %{eclipse_base}/features/org.eclipse.mylyn.java_feature_*/epl-v10.html
%{eclipse_base}/features/org.eclipse.mylyn.java_feature_*/feature.xml
%if %{gcj_support}
%{_libdir}/gcj/%{name}/org.eclipse.mylyn.java*
%endif

%files pde
%defattr(-,root,root,-)
%{eclipse_base}/plugins/org.eclipse.mylyn.team.ui_*.jar
%{eclipse_base}/plugins/org.eclipse.mylyn.team.cvs_*.jar
%{eclipse_base}/plugins/org.eclipse.mylyn.bugzilla.ide_*.jar
%{eclipse_base}/plugins/org.eclipse.mylyn.ide.ant_*.jar
%{eclipse_base}/plugins/org.eclipse.mylyn.pde.ui_*.jar
%dir %{eclipse_base}/features/org.eclipse.mylyn.pde_feature_*
%doc %{eclipse_base}/features/org.eclipse.mylyn.pde_feature_*/license.html
%doc %{eclipse_base}/features/org.eclipse.mylyn.pde_feature_*/epl-v10.html
%{eclipse_base}/features/org.eclipse.mylyn.pde_feature_*/feature.xml
%if %{gcj_support}
%{_libdir}/gcj/%{name}/org.eclipse.mylyn.pde.ui*
%{_libdir}/gcj/%{name}/org.eclipse.mylyn.team.ui*
%{_libdir}/gcj/%{name}/org.eclipse.mylyn.team.cvs*
%{_libdir}/gcj/%{name}/org.eclipse.mylyn.bugzilla.ide*
%{_libdir}/gcj/%{name}/org.eclipse.mylyn.ide.ant*
%endif

%files
%defattr(-,root,root,-)
%{eclipse_base}/plugins/org.eclipse.mylyn.help.ui_*.jar
%{eclipse_base}/plugins/org.eclipse.mylyn.web.core_*
%{eclipse_base}/plugins/org.eclipse.mylyn.context.core_*.jar
%{eclipse_base}/plugins/org.eclipse.mylyn.tasks.ui_*.jar
%{eclipse_base}/plugins/org.eclipse.mylyn.tasks.core_*.jar
%{eclipse_base}/plugins/org.eclipse.mylyn_*.jar
%{eclipse_base}/plugins/org.eclipse.mylyn.monitor.core_*.jar
%{eclipse_base}/plugins/org.eclipse.mylyn.monitor.ui_*.jar
%doc %{eclipse_base}/features/org.eclipse.mylyn_feature_*/license.html
%doc %{eclipse_base}/features/org.eclipse.mylyn_feature_*/epl-v10.html
%{eclipse_base}/features/org.eclipse.mylyn_feature_*/feature.xml
%doc %{eclipse_base}/features/org.eclipse.mylyn.context_feature_*/license.html
%doc %{eclipse_base}/features/org.eclipse.mylyn.context_feature_*/epl-v10.html
%{eclipse_base}/features/org.eclipse.mylyn.context_feature_*/feature.xml
%{eclipse_base}/plugins/org.eclipse.mylyn.context.ui_*.jar
%{eclipse_base}/plugins/org.eclipse.mylyn.web.ui_*.jar
%{eclipse_base}/plugins/org.eclipse.mylyn.resources.ui_*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/org.eclipse.mylyn.help.ui_*
%{_libdir}/gcj/%{name}/mylyn-webcore*
%{_libdir}/gcj/%{name}/org.eclipse.mylyn.context.core_*
%{_libdir}/gcj/%{name}/org.eclipse.mylyn.tasks.ui_*
%{_libdir}/gcj/%{name}/org.eclipse.mylyn.tasks.core_*
%{_libdir}/gcj/%{name}/org.eclipse.mylyn.monitor.core_*
%{_libdir}/gcj/%{name}/org.eclipse.mylyn.monitor.ui_*
%{_libdir}/gcj/%{name}/org.eclipse.mylyn.context.ui_*
%{_libdir}/gcj/%{name}/org.eclipse.mylyn.resources.ui_*
%{_libdir}/gcj/%{name}/org.eclipse.mylyn.web.ui_*
%dir %{_libdir}/gcj/%{name}
%endif
