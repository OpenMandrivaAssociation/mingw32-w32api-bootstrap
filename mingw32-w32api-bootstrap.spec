# NOTE: NOT a Mandriva package. This contains binaries which are needed
# just to bootstrap the whole system if you build everything from scratch.

%define __os_install_post /usr/lib/rpm/brp-compress %{nil}

%define w32api_version 3.11

Name: mingw32-w32api-bootstrap
Version: 1
Release: %mkrel 1
Summary: MinGW Windows bootstrap (binary package)

Group: Development/Other
License: Public Domain
URL: http://www.mingw.org/

Source0: http://dl.sourceforge.net/sourceforge/mingw/w32api-%{w32api_version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildArch: noarch

Provides: mingw32-w32api = %{w32api_version}
Provides: mingw-w32api = %{w32api_version}


%description
MinGW bootstrap (binary package).


%prep
%setup -q -c

%build
rm -rf i586-pc-mingw32

# Setup sys-root.
mkdir -p i586-pc-mingw32/sys-root/mingw
cp -a include lib i586-pc-mingw32/sys-root/mingw


%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_prefix}
cp -a i586-pc-mingw32 $RPM_BUILD_ROOT%{_prefix}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%dir %{_prefix}/i586-pc-mingw32
%{_prefix}/i586-pc-mingw32/sys-root
