Summary:	A libnotify plugin for gmpc
Name:		gmpc-libnotify
Version:	0.20.0
Release:	4
License:	GPLv2+
Group:		Sound
Url:		http://www.sarine.nl/
Source0:	http://download.sarine.nl/Programs/gmpc/%{version}/%{name}-%{version}.tar.gz
Patch0:		gmpc-libnotify-0.20.0-libnotify-0.7.patch
BuildRequires:	libmpd-devel >= 0.14.99
BuildRequires:	libnotify-devel
BuildRequires:	gmpc-devel >= 0.15.4.102
BuildRequires:	gtk+2-devel >= 2.8
BuildRequires:	intltool
Requires:	gmpc

%description
A libnotify plugin for gmpc.

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%defattr(-,root,root)
%{_libdir}/gmpc/plugins/libnotifyplugin.so


%changelog
* Thu Apr 14 2011 Funda Wang <fwang@mandriva.org> 0.20.0-3mdv2011.0
+ Revision: 652902
- fix build with libnotify 0.7

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.20.0-2mdv2011.0
+ Revision: 610905
- rebuild

* Mon Apr 05 2010 Funda Wang <fwang@mandriva.org> 0.20.0-1mdv2010.1
+ Revision: 531608
- update to new version 0.20.0

* Sat Dec 26 2009 Funda Wang <fwang@mandriva.org> 0.19.0-1mdv2010.1
+ Revision: 482401
- BR intltool
- new version 0.19.0

* Mon May 25 2009 Funda Wang <fwang@mandriva.org> 0.18.0-1mdv2010.0
+ Revision: 379388
- New version 0.18.0

* Mon Dec 29 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.17.0-1mdv2009.1
+ Revision: 321125
- update to new version 0.17.0

* Wed Dec 03 2008 Funda Wang <fwang@mandriva.org> 0.16.0-1mdv2009.1
+ Revision: 309575
- move plugins

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - fix file list
    - update to new version 0.16.0

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.15.5.0-3mdv2009.0
+ Revision: 246281
- rebuild

* Wed Jan 30 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.15.5.0-1mdv2008.1
+ Revision: 160366
- add spec file
- add source
- Created package structure for gmpc-libnotify.

