Name:           wsmancli
Version:        2.6.0
Release:        10
Summary:        Command line interface of open wsman.
License:        BSD
Url:            http://www.openwsman.org/

Source:         https://github.com/Openwsman/wsmancli/archive/v%{version}.tar.gz
Source1:        COPYING
Source2:        README
Source3:        AUTHORS
Patch0:         missing-pthread-symbols.patch

BuildRequires:  openwsman-devel >= 2.1.0 pkgconfig curl-devel
BuildRequires:  autoconf automake libtool
Requires:       openwsman curl

%description
Web Services for Management (WS-MAN) is a specification for managing computer systems using web services standards.
Open wsman is an open source implementation of WS-MAN; enabling the in-band management of Linux/uni* platforms.

%prep
%autosetup -n %{name}-%{version} -p1
cp -fp %SOURCE1 %SOURCE2 %SOURCE3 .;

%build
./bootstrap
%configure --disable-more-warnings 
%make_build

%install
%make_install

%package_help

%files
%{_bindir}/wsman
%{_bindir}/wseventmgr
%license COPYING

%files help
%{_mandir}/man1/wsman*
%{_mandir}/man1/wseventmgr*
%doc README AUTHORS

%changelog
* Mon Sep 14 2020 Ge Wang<wangge20@huawei.com> - 2.6.0-10
- Modify Source0 Url

* Sat Nov 30 2019 jiaxiya<jiaxiyajiaxiya@163.com> - 2.6.0-9
- Package init
