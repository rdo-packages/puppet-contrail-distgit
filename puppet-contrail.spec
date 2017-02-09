%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-contrail
%global commit 9a890f368bee58efa4ea9f94fcfe6bdc3d82c592
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-contrail
Version:        1.0.0
Release:        2%{?alphatag}%{?dist}
Summary:        Puppet module for Juniper OpenContrail
License:        ASL 2.0

URL:            https://github.com/Juniper/puppet-contrail

Source0:        https://github.com/Juniper/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:      noarch

Requires:       puppet-inifile
Requires:       puppet-stdlib
Requires:       puppet >= 2.7.0

%description
Puppet module for Juniper OpenContrail

%prep
%setup -q -n %{name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/contrail/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/contrail/



%files
%{_datadir}/openstack-puppet/modules/contrail/


%changelog
* Thu Feb 09 2017 Alfredo Moralejo <amoralej@redhat.com> 1.0.0-2.9a890f3git
- Ocata update 1.0.0 (9a890f368bee58efa4ea9f94fcfe6bdc3d82c592)

