# ToDo:
# - fix pl description [?]
%define		_modname	vld
%define		_status		beta
Summary:	%{_modname} - provides functionality to dump the internal representation of PHP scripts
Summary(pl):	%{_modname} - dostarcza funkcjonalno¶ci do zrzutu wewnêtrzenej reprezentacji skryptów PHP
Name:		php-pecl-%{_modname}
Version:	0.7.0
Release:	1
License:	BSD style
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	d074260535f5f685517b1dff200f4a67
URL:		http://pecl.php.net/package/vld/
BuildRequires:	libtool
BuildRequires:	php-devel
Requires:	php-common
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/php
%define		extensionsdir	%{_libdir}/php

%description
The Vulcan Logic Disassembler hooks into the Zend Engine and
dumps all the opcodes (execution units) of a script.

This extension has in PEAR status: %{_status}.

%description -l pl
Vulcan Logic Disassembler przyczepia siê do Silnika Zend i
zwraca wszystkie opcody (jednostki wykonawcze) skryptu.

To rozszerzenie ma w PEAR status: %{_status}.

%prep
%setup -q -c

%build
cd %{_modname}-%{version}
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{extensionsdir}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{extensionsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/php-module-install install %{_modname} %{_sysconfdir}/php-cgi.ini

%preun
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove %{_modname} %{_sysconfdir}/php-cgi.ini
fi

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/%{_modname}.so
%doc %{_modname}-%{version}/{Changelog,CREDITS}
