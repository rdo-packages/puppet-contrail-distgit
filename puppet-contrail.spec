%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-contrail
%global commit ecf700b52054ffb9d73768dc4ae31d87dc66fc98
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-contrail
Version:        1.0.0
Release:        4%{?alphatag}%{?dist}
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
* Thu Feb 15 2018 RDO <dev@lists.rdoproject.org> 1.0.0-4.ecf700bgit
- Update to post 1.0.0 (ecf700b52054ffb9d73768dc4ae31d87dc66fc98)



