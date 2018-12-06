# Run tests in check section
%bcond_without check

%global goipath         github.com/bitly/go-simplejson
Version:                0.5.0

%global common_description %{expand:
Go package to interact with arbitrary JSON.}

%gometa

Name:    %{goname}
Release: 6%{?dist}
Summary: Go package to interact with arbitrary JSON
License: MIT
URL:     %{gourl}
Source:  %{gosource}

%if %{with check}
BuildRequires: golang(github.com/stretchr/testify/assert)
BuildRequires: golang(github.com/bmizerany/assert)
%endif

%description
%{common_description}


%package    devel
Summary:    %{summary}
BuildArch:  noarch

Provides: golang-github-bitly-go-simplejson-devel = %{version}-%{release}
Obsoletes: golang-github-bitly-go-simplejson-devel < 0.5.0-3
 
%description devel
%{common_description}
 
This package contains the source code needed for building packages that import
the %{goipath} Go namespace.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Mon Nov 12 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.5.0-6
- SPEC refresh

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0.5.0-5
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 08 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.5.0-3
- Update with the new Go packaging

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Nov 25 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0.5.0-1
- First package for Fedora

