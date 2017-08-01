%{?scl:%scl_package maven-plugin-build-helper}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}maven-plugin-build-helper
Version:        1.9.1
Release:        4.1%{?dist}
Summary:        Build Helper Maven Plugin
Group:          Development/Libraries
License:        MIT and ASL 2.0
URL:            http://mojo.codehaus.org/build-helper-maven-plugin/
BuildArch: noarch

# The source tarball has been generated from upstream VCS:
# svn export https://svn.codehaus.org/mojo/tags/build-helper-maven-plugin-%{version} %{pkg_name}-%{version}
# tar caf %{pkg_name}-%{version}.tar.xz %{pkg_name}-%{version}
Source0:        %{pkg_name}-%{version}.tar.xz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires:  %{?scl_prefix}maven-local
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-artifact)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-compat)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-core)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-model)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-project)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.plugins:maven-invoker-plugin)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  %{?scl_prefix}mvn(org.beanshell:bsh)
BuildRequires:  %{?scl_prefix}mvn(org.codehaus.mojo:mojo-parent:pom:)
BuildRequires:  %{?scl_prefix}mvn(org.codehaus.plexus:plexus-utils)

%description
This plugin contains various small independent goals to assist with
Maven build lifecycle.

%package javadoc
Summary:        API documentation for %{pkg_name}

%description javadoc
This package provides %{summary}.

%prep
%setup -n %{pkg_name}-%{version} -q 
cp %{SOURCE1} LICENSE-2.0.txt
%pom_add_dep org.apache.maven:maven-compat

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc header.txt LICENSE-2.0.txt
%dir %{_javadir}/%{pkg_name}

%files javadoc -f .mfiles-javadoc
%doc header.txt LICENSE-2.0.txt

%changelog
* Wed Jun 21 2017 Java Maintainers <java-maint@redhat.com> - 1.9.1-4.1
- Automated package import and SCL-ization

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Sep 04 2014 Michal Srb <msrb@redhat.com> - 1.9.1-1
- Update to upstream version 1.9.1

* Mon Jun 09 2014 Michal Srb <msrb@redhat.com> - 1.9-2
- Regenerate BR

* Mon Jun  9 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.9-1
- Update to upstream version 1.9

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.8-3
- Use Requires: java-headless rebuild (#1067528)

* Fri Jul 26 2013 Tomas Radej <tradej@redhat.com> - 1.8-2
- Add missing ASL license text and installed all license files

* Mon Jul 22 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8-1
- Add missing BR: maven-invoker-plugin

* Fri Jul 19 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8-1
- Update to upstream version 1.8

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.5-7
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Tomas Radej <tradej@redhat.com> - 1.5-4
- Update to current guidelines
- Fix build

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct 28 2010 Alexander Kurtakov <akurtako@redhat.com> 1.5-2
- Maven plugins should require parent poms because they are totally unusable without them.

* Thu Sep 16 2010 Alexander Kurtakov <akurtako@redhat.com> 1.5-1
- Update to 1.5.
- Use newer maven packages' names.

* Thu Sep 10 2009 Alexander Kurtakov <akurtako@gmail.com> 1.4-1
- Initial package.
