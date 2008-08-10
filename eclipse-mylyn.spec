%define eclipse_base        %{_libdir}/eclipse
%define install_loc         %{_datadir}/eclipse/dropins
# Taken from update site so we match upstream
# http://download.eclipse.org/tools/mylyn/update/e3.4/
%define qualifier           v20080716-2300-e3x

Name: eclipse-mylyn 
Summary: Mylyn is a task-focused UI for Eclipse
Version: 3.0.1
Release: %mkrel 0.1.1
License: Eclipse Public License
URL: http://www.eclipse.org/mylyn

# mkdir temp && cd temp
# sh fetch-mylyn.sh
# tar cjf org.eclipse.mylyn-R_3_0_1-fetched-src.tar.bz2 org.eclipse.mylyn
Source0: org.eclipse.mylyn-R_3_0_1-fetched-src.tar.bz2
Source1: fetch-mylyn.sh
Source2: http://overholt.fedorapeople.org/fedoraeclipse-mylynbugzilla-0.0.2.zip

Patch6: %{name}-addfedoracustomizations.patch
# This is a dependency declared by the Orbit xmlrpc JAR.  We don't use
# their JAR and the part of Mylyn using xmlrpc isn't using the
# javax.xml.bind-using part(s) of xmlrpc.
Patch7: %{name}-nojaxb.patch
# Our xmlrpc packages are split into JARs differently than Orbit
Patch8: %{name}-splitxmlrpc.patch
# Red Hat Bugzilla is 3.0 now
Patch9: %{name}-rhbz30.patch

BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:    java-devel >= 1.5.0


BuildArch: noarch

BuildRequires: java-rpmbuild
BuildRequires: eclipse-pde >= 1:3.4.0
BuildRequires: eclipse-cvs-client >= 1:3.4.0
BuildRequires: jakarta-commons-codec >= 1.3-8jpp.2
BuildRequires: jakarta-commons-httpclient >= 1:3.1
BuildRequires: jakarta-commons-logging
BuildRequires: jakarta-commons-lang >= 2.1
BuildRequires: ws-commons-util >= 1.0.1-5
BuildRequires: xmlrpc3-client >= 3.0-1jpp.3
BuildRequires: xmlrpc3-common >= 3.0-1jpp.3
BuildRequires: rome
BuildRequires: jdom
Requires: eclipse-platform >= 1:3.4.0
Requires: eclipse-cvs-client >= 1:3.4.0
Requires: jakarta-commons-codec >= 1.3-8jpp.2
Requires: jakarta-commons-httpclient >= 1:3.1
Requires: jakarta-commons-logging
Requires: jakarta-commons-lang >= 2.1
Requires: ws-commons-util >= 1.0.1-2
Requires: xmlrpc3-client >= 3.0-1jpp.3
Requires: xmlrpc3-common >= 3.0-1jpp.3
Provides: eclipse-mylar = 2.0.0-1.fc7
Obsoletes: eclipse-mylar < 2.0.0
Provides: eclipse-mylyn-ide = %{version}-%{release}
Obsoletes: eclipse-mylyn-ide < 3.0.0
Provides: eclipse-bugzilla = 1:0.2.4-4.fc6
Obsoletes: eclipse-bugzilla < 1:0.2.5
Provides: eclipse-mylar-bugzilla = 2.0.0-1.fc7
Obsoletes: eclipse-mylar-bugzilla < 2.0.0
Provides: eclipse-mylyn-bugzilla = %{version}-%{release}
Obsoletes: eclipse-mylyn-bugzilla < 3.0.0

Group: Development/Java

%description
Mylyn integrates task support into Eclipse.  It supports offline editing
for certain task repositories and monitors work activity to hide
information that is not relevant to the current task.  Also included is
the Mylyn Focused UI for reducing information overload when working with
tasks and the Bugzilla task connector.

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

%package  webtasks
Summary:  Mylyn Focused UI
Requires: %{name} = %{version}-%{release}
Requires: rome
Requires: jdom
Group: Development/Tools

%description webtasks
Provides Task List integration for several web-based issue trackers
and templates for example projects.

%prep
%setup -q -n org.eclipse.mylyn
unzip -q %{SOURCE2}

# The tests have dependencies we don't need/want/have
rm -rf *tests*

mkdir orbitDeps
pushd orbitDeps
ln -s %{_javadir}/commons-codec-1.3.jar org.apache.commons.codec_1.3.0.jar
ln -s %{_javadir}/commons-httpclient.jar org.apache.commons.httpclient_3.1.0.jar
ln -s %{_javadir}/commons-lang.jar org.apache.commons.lang_2.3.0.jar
ln -s %{_javadir}/commons-logging-api.jar org.apache.commons.logging.api_1.0.4.jar
ln -s %{_javadir}/commons-logging.jar org.apache.commons.logging_1.0.4.jar
ln -s %{_javadir}/xmlrpc3-client-3.0.jar org.apache.xmlrpc.client_3.0.0.v20080530-1550.jar
ln -s %{_javadir}/xmlrpc3-common-3.0.jar org.apache.xmlrpc.common_3.0.0.v20080530-1550.jar
ln -s %{_javadir}/ws-commons-util-1.0.1.jar org.apache.ws.commons.util_1.0.0.v20080530-1550.jar
ln -s %{_javadir}/jdom-1.0.jar org.jdom_1.0.0.v200806100616.jar
ln -s %{_javadir}/rome-0.9.jar com.sun.syndication_0.9.0.v200803061811.jar
popd

#javax.activation_1.1.0.v200806101325.jar
#javax.xml.bind_2.0.0.v20080604-1500.jar
#javax.mail_1.4.0.v200804091730.jar
#javax.servlet_2.4.0.v200806031604.jar
#org.apache.ant_1.7.0.v200803061910.zip,unpack=true
#javax.xml.rpc_1.1.0.v200806030420.zip,unpack=true
#javax.wsdl_1.5.1.v200806030408.jar
#javax.xml.soap_1.2.0.v200806030421.zip,unpack=true
#org.apache.axis_1.4.0.v200806030120.zip,unpack=true
#org.apache.commons.discovery_0.2.0.v200806030120.zip,unpack=true

%patch6 -p0
pushd org.fedoraproject.mylyn.bugzilla
%patch9
popd
%patch7
%patch8

find -name feature.xml |
  while read f; do
      sed -i "s/qualifier/%{qualifier}/g" $f
  done

%build
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.mylyn_feature \
 -a "-DjavacSource=1.5 -DjavacTarget=1.5 -DforceContextQualifier=%{qualifier} -DmylynQualifier=%{qualifier}" \
 -j -DJ2SE-1.5=%{_jvmdir}/java-rpmbuild/jre/lib/rt.jar \
 -o `pwd`/orbitDeps
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.mylyn.context_feature \
 -a "-DjavacSource=1.5 -DjavacTarget=1.5 -DforceContextQualifier=%{qualifier} -DmylynQualifier=%{qualifier}" \
 -j -DJ2SE-1.5=%{_jvmdir}/java-rpmbuild/jre/lib/rt.jar \
 -o `pwd`/orbitDeps
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.mylyn.team_feature \
 -a "-DjavacSource=1.5 -DjavacTarget=1.5 -DforceContextQualifier=%{qualifier} -DmylynQualifier=%{qualifier}" \
 -j -DJ2SE-1.5=%{_jvmdir}/java-rpmbuild/jre/lib/rt.jar \
 -o `pwd`/orbitDeps
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.mylyn.bugzilla_feature \
 -a "-DjavacSource=1.5 -DjavacTarget=1.5 -DforceContextQualifier=%{qualifier} -DmylynQualifier=%{qualifier}" \
 -j -DJ2SE-1.5=%{_jvmdir}/java-rpmbuild/jre/lib/rt.jar \
 -o `pwd`/orbitDeps
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.mylyn.ide_feature \
 -a "-DjavacSource=1.5 -DjavacTarget=1.5 -DforceContextQualifier=%{qualifier} -DmylynQualifier=%{qualifier}" \
 -j -DJ2SE-1.5=%{_jvmdir}/java-rpmbuild/jre/lib/rt.jar \
 -o `pwd`/orbitDeps
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.mylyn.trac_feature \
 -a "-DjavacSource=1.5 -DjavacTarget=1.5 -DforceContextQualifier=%{qualifier} -DmylynQualifier=%{qualifier}" \
 -j -DJ2SE-1.5=%{_jvmdir}/java-rpmbuild/jre/lib/rt.jar \
 -o `pwd`/orbitDeps
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.mylyn.java_feature \
 -a "-DjavacSource=1.5 -DjavacTarget=1.5 -DforceContextQualifier=%{qualifier} -DmylynQualifier=%{qualifier}" \
 -j -DJ2SE-1.5=%{_jvmdir}/java-rpmbuild/jre/lib/rt.jar \
 -o `pwd`/orbitDeps
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.mylyn.pde_feature \
 -a "-DjavacSource=1.5 -DjavacTarget=1.5 -DforceContextQualifier=%{qualifier} -DmylynQualifier=%{qualifier}" \
 -j -DJ2SE-1.5=%{_jvmdir}/java-rpmbuild/jre/lib/rt.jar \
 -o `pwd`/orbitDeps
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.mylyn.web.tasks_feature \
 -a "-DjavacSource=1.5 -DjavacTarget=1.5 -DforceContextQualifier=%{qualifier} -DmylynQualifier=%{qualifier}" \
 -j -DJ2SE-1.5=%{_jvmdir}/java-rpmbuild/jre/lib/rt.jar \
 -o `pwd`/orbitDeps

%install
rm -rf %{buildroot}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/eclipse
install -d -m 755 $RPM_BUILD_ROOT%{install_loc}/mylyn
install -d -m 755 $RPM_BUILD_ROOT%{install_loc}/mylyn-java
install -d -m 755 $RPM_BUILD_ROOT%{install_loc}/mylyn-pde
install -d -m 755 $RPM_BUILD_ROOT%{install_loc}/mylyn-trac
install -d -m 755 $RPM_BUILD_ROOT%{install_loc}/mylyn-webtasks

unzip -q -o -d $RPM_BUILD_ROOT%{install_loc}/mylyn \
 build/rpmBuild/org.eclipse.mylyn_feature.zip
unzip -q -o -d $RPM_BUILD_ROOT%{install_loc}/mylyn \
 build/rpmBuild/org.eclipse.mylyn.bugzilla_feature.zip
unzip -q -o -d $RPM_BUILD_ROOT%{install_loc}/mylyn \
 build/rpmBuild/org.eclipse.mylyn.context_feature.zip
unzip -q -o -d $RPM_BUILD_ROOT%{install_loc}/mylyn \
 build/rpmBuild/org.eclipse.mylyn.team_feature.zip
unzip -q -o -d $RPM_BUILD_ROOT%{install_loc}/mylyn \
 build/rpmBuild/org.eclipse.mylyn.ide_feature.zip
unzip -q -o -d $RPM_BUILD_ROOT%{install_loc}/mylyn-trac \
 build/rpmBuild/org.eclipse.mylyn.trac_feature.zip
unzip -q -o -d $RPM_BUILD_ROOT%{install_loc}/mylyn-java \
 build/rpmBuild/org.eclipse.mylyn.java_feature.zip
unzip -q -o -d $RPM_BUILD_ROOT%{install_loc}/mylyn-pde \
 build/rpmBuild/org.eclipse.mylyn.pde_feature.zip
unzip -q -o -d $RPM_BUILD_ROOT%{install_loc}/mylyn-webtasks \
 build/rpmBuild/org.eclipse.mylyn.web.tasks_feature.zip

pushd $RPM_BUILD_ROOT%{install_loc}/mylyn/eclipse/plugins
rm org.apache.commons.codec_1.3.0.v20080530-1600.jar
rm org.apache.commons.httpclient_3.1.0.v20080605-1935.jar
rm org.apache.commons.lang_2.3.0.v200803061910.jar
rm org.apache.commons.logging_1.0.4.v20080605-1930.jar
ln -s %{_javadir}/commons-codec-1.3.jar org.apache.commons.codec_1.3.0.jar
ln -s %{_javadir}/commons-httpclient.jar org.apache.commons.httpclient_3.1.0.jar
ln -s %{_javadir}/commons-lang.jar org.apache.commons.lang_2.3.0.jar
ln -s %{_javadir}/commons-logging-api.jar org.apache.commons.logging.api_1.0.4.jar
ln -s %{_javadir}/commons-logging.jar org.apache.commons.logging_1.0.4.jar
popd

pushd $RPM_BUILD_ROOT%{install_loc}/mylyn-trac/eclipse/plugins
rm org.apache.ws.commons.util_1.0.0.v20080716-2300-e3x.jar
rm org.apache.xmlrpc_3.0.0.v20080716-2300-e3x.jar
ln -s %{_javadir}/xmlrpc3-client-3.0.jar org.apache.xmlrpc.client_3.0.0.v20080530-1550.jar
ln -s %{_javadir}/xmlrpc3-common-3.0.jar org.apache.xmlrpc.common_3.0.0.v20080530-1550.jar
ln -s %{_javadir}/ws-commons-util-1.0.1.jar org.apache.ws.commons.util_1.0.0.v20080530-1550.jar
popd

pushd $RPM_BUILD_ROOT%{install_loc}/mylyn-webtasks/eclipse/plugins
rm org.jdom_1.0.0.v200806100616.jar
rm com.sun.syndication_0.9.0.v200803061811.jar
ln -s %{_javadir}/jdom-1.0.jar org.jdom_1.0.0.v200806100616.jar
ln -s %{_javadir}/rome-0.9.jar com.sun.syndication_0.9.0.v200803061811.jar
popd

%clean
rm -rf %{buildroot}

%files webtasks
%defattr(-,root,root,-)
#%{install_loc}/plugins/com.sun.syndication_*.jar
#%{install_loc}/plugins/org.jdom_*.jar
#%{install_loc}/plugins/org.eclipse.mylyn.web.tasks_*.jar
#%dir %{install_loc}/features/org.eclipse.mylyn.web.tasks_feature_*
#%doc %{install_loc}/features/org.eclipse.mylyn.web.tasks_feature_*/license.html
#%doc %{install_loc}/features/org.eclipse.mylyn.web.tasks_feature_*/about.html
#%doc %{install_loc}/features/org.eclipse.mylyn.web.tasks_feature_*/epl-v10.html
#%{install_loc}/features/org.eclipse.mylyn.web.tasks_feature_*/feature.xml
%{install_loc}/mylyn-webtasks

%files trac
%defattr(-,root,root,-)
%{install_loc}/mylyn-trac
# FIXME:  add the doc files back
#%doc %{install_loc}/features/org.eclipse.mylyn.trac_feature_*/license.html
#%doc %{install_loc}/features/org.eclipse.mylyn.trac_feature_*/epl-v10.html
#%doc %{install_loc}/features/org.eclipse.mylyn.trac_feature_*/about.html

%files java
%defattr(-,root,root,-)
%{install_loc}/mylyn-java
# FIXME:  add the doc files back
#%doc %{install_loc}/features/org.eclipse.mylyn.java_feature_*/license.html
#%doc %{install_loc}/features/org.eclipse.mylyn.java_feature_*/epl-v10.html
#%doc %{install_loc}/features/org.eclipse.mylyn.java_feature_*/about.html

%files pde
%defattr(-,root,root,-)
%{install_loc}/mylyn-pde
# FIXME:  add the doc files back
#%doc %{install_loc}/features/org.eclipse.mylyn.pde_feature_*/license.html
#%doc %{install_loc}/features/org.eclipse.mylyn.pde_feature_*/epl-v10.html
#%doc %{install_loc}/features/org.eclipse.mylyn.pde_feature_*/about.html

%files
%defattr(-,root,root,-)
%{install_loc}/mylyn
# FIXME:  add the doc files back

