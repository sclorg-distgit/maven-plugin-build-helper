%global pkg_name maven-plugin-build-helper
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

Name:           %{?scl_prefix}%{pkg_name}
Version:        1.5
Release:        13.12%{?dist}
Summary:        Build Helper Maven Plugin

License:        MIT and ASL 2.0
URL:            http://mojo.codehaus.org/build-helper-maven-plugin/
# The source tarball has been generated from upstream VCS:
# svn export https://svn.codehaus.org/mojo/tags/build-helper-maven-plugin-%{version} 
#            %{pkg_name}-%{version}
# tar caf %{pkg_name}-%{version}.tar.xz %{pkg_name}-%{version}
Source0:        %{pkg_name}-%{version}.tar.xz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

Patch0:         add-junit-dependency.patch
Patch1:         %{pkg_name}-core.patch

BuildArch: noarch

BuildRequires: %{?scl_prefix_java_common}javapackages-tools
BuildRequires: %{?scl_prefix}plexus-utils
BuildRequires: %{?scl_prefix_java_common}maven-local
BuildRequires: %{?scl_prefix}maven-plugin-plugin
BuildRequires: %{?scl_prefix}maven-resources-plugin
BuildRequires: %{?scl_prefix}maven-compiler-plugin
BuildRequires: %{?scl_prefix}maven-install-plugin
BuildRequires: %{?scl_prefix}maven-jar-plugin
BuildRequires: %{?scl_prefix}maven-javadoc-plugin
BuildRequires: %{?scl_prefix}maven-enforcer-plugin
BuildRequires: %{?scl_prefix}maven-surefire-plugin
BuildRequires: %{?scl_prefix}maven-doxia-sitetools
BuildRequires: %{?scl_prefix}mojo-parent
BuildRequires: %{?scl_prefix_java_common}junit

%description
This plugin contains various small independent goals to assist with
Maven build lifecycle.

%package javadoc
Summary:        Javadoc for %{pkg_name}

%description javadoc
API documentation for %{pkg_name}.

%prep
%setup -q -n %{pkg_name}-%{version}
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%patch0
%patch1 -p1
cp %{SOURCE1} LICENSE-2.0.txt
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc header.txt LICENSE-2.0.txt
%dir %{_mavenpomdir}/%{pkg_name}
%dir %{_javadir}/%{pkg_name}

%files javadoc -f .mfiles-javadoc
%doc header.txt LICENSE-2.0.txt

%changelog
* Mon Jan 11 2016 Michal Srb <msrb@redhat.com> - 1.5-13.12
- maven33 rebuild #2

* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 1.5-13.11
- maven33 rebuild

* Thu Jan 15 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.5-13.10
- Add directory ownership on %%{_mavenpomdir} subdir

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 1.5-13.9
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 1.5-13.8
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.5-13.7
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.5-13.6
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.5-13.5
- Mass rebuild 2014-02-18

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.5-13.4
- Rebuild to fix incorrect auto-requires

* Fri Feb 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.5-13.3
- SCL-ize requires and build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.5-13.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.5-13.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.5-13
- Mass rebuild 2013-12-27

* Fri Aug 23 2013 Michal Srb <msrb@redhat.com> - 1.5-12
- Migrate away from mvn-rpmbuild (Resolves: #997496)

* Mon Jul 29 2013 Michal Srb <msrb@redhat.com> - 1.5-11
- Install MIT license text

* Fri Jul 26 2013 Tomas Radej <tradej@redhat.com> - 1.5-10
- Add missing ASL license text and installed all license files

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.5-9
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

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
