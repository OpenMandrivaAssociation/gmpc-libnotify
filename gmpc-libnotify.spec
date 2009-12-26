Summary:	A libnotify plugin for gmpc
Name:		gmpc-libnotify
Version:	0.19.0
Release:	%mkrel 1
License:	GPLv2+
Group:		Sound
Url:		http://www.sarine.nl/
Source0:	http://download.sarine.nl/Programs/gmpc/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	libmpd-devel >= 0.14.99
BuildRequires:	libnotify-devel
BuildRequires:	gmpc-devel >= 0.15.4.102
BuildRequires:	gtk+2-devel >= 2.8
Requires:	gmpc
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
A libnotify plugin for gmpc.

%prep
%setup -q

%build
%configure2_5x
%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/gmpc/plugins/libnotifyplugin.la
%{_libdir}/gmpc/plugins/libnotifyplugin.so
