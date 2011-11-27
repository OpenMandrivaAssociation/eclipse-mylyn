%global eclipse_base        %{_libdir}/eclipse
%global install_loc         %{_datadir}/eclipse/dropins
# Taken from update site so we match upstream
#  http://download.eclipse.org/mylyn/archive/3.5.1/v20110422-0200/
%global qualifier           v20110422-0200

Name: eclipse-mylyn
Summary: Eclipse Mylyn main feature
Version: 3.5.1
Release: 3
License: EPL
URL: http://www.eclipse.org/mylyn

# bash fetch-eclipse-mylyn.sh
Source0: eclipse-mylyn-R_3_5_1-fetched-src.tar.bz2
Source1: fetch-eclipse-mylyn.sh

BuildArch: noarch

BuildRequires: java-devel >= 1.5.0
BuildRequires: eclipse-platform >= 0:3.4.0
BuildRequires: eclipse-pde >= 0:3.4.0
BuildRequires: eclipse-mylyn-commons >= 3.5.0

Requires: eclipse-platform >= 0:3.4.0
Requires: eclipse-mylyn-commons >= 3.5.0

Group: Development/Java

%description
Mylyn integrates task support into Eclipse. It supports offline editing
for certain task repositories and monitors work activity to hide
information that is not relevant to the current task.

%prep
%setup -c

%build
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.mylyn_feature \
 -a "-DjavacSource=1.5 -DjavacTarget=1.5 -DforceContextQualifier=%{qualifier} -DmylynQualifier=%{qualifier}" \
 -d "mylyn-commons"

%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_datadir}/eclipse
install -d -m 755 %{buildroot}%{install_loc}/mylyn

unzip -q -o -d %{buildroot}%{install_loc}/mylyn \
 build/rpmBuild/org.eclipse.mylyn_feature.zip

%files
%defattr(-,root,root,-)
%{install_loc}/mylyn
%doc org.eclipse.mylyn.tasks/org.eclipse.mylyn-feature/epl-v10.html
%doc org.eclipse.mylyn.tasks/org.eclipse.mylyn-feature/license.html

