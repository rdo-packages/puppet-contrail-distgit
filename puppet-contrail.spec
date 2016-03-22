Name:			puppet-contrail
Version:		XXX
Release:		XXX
Summary:		Puppet module for Juniper OpenContrail
License:		Apache-2.0

URL:			https://github.com/redhat-cip/puppet-contrail

Source0:		https://github.com/redhat-cip/puppet-contrail/archive/%{version}.tar.gz

BuildArch:		noarch

Requires:		puppet-inifile
Requires:		puppet-stdlib
Requires:		puppet >= 2.7.0

%description
Puppet module for Juniper OpenContrail

%prep
%setup -q -n %{name}-%{version}

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

