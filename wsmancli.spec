Name:           wsmancli
Version:        2.6.0
Release:        1
Summary:        Command line interface of Web Services for Management (WS-MAN).
License:        BSD
Url:            http://www.openwsman.org/

Source:         wsmancli-%{version}.tar.gz
Source1:        COPYING
Source2:        README
Source3:        AUTHORS
Patch0:         missing-pthread-symbols.patch

BuildRequires:  openwsman-devel >= 2.1.0 pkgconfig curl-devel
BuildRequires:  autoconf automake libtool
Requires:       openwsman curl

%description
Web Services for Management (WS-MAN) is a specification for managing computer systems using web services standards.
This project is an open source implementation of WS-MAN; enabling the in-band management of Linux/uni* platforms.

%prep
%autosetup -n wsmancli-%{version} -p1
cp -fp %SOURCE1 %SOURCE2 %SOURCE3 .;

%build
./bootstrap
%configure --disable-more-warnings 
make %{?_smp_flags}

%install
make DESTDIR=%{buildroot} install

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
* Sat Nov 30 2019 openEuler Buildteam <buildteam@openeuler.org> - 2.6.0-1
- Package init
