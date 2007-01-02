# ToDo:
# - fix pl description [?]
%define		_modname	vld
%define		_status		beta
Summary:	%{_modname} - provides functionality to dump the internal representation of PHP scripts
Summary(pl):	%{_modname} - dostarcza funkcjonalno¶ci do zrzutu wewnêtrznej reprezentacji skryptów PHP
Name:		php-pecl-%{_modname}
Version:	0.8.0
Release:	7
License:	BSD style
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	00351344ed03a6eea6219e1db25aa660
Patch0:		%{name}-php51.patch
URL:		http://pecl.php.net/package/vld/
BuildRequires:	php-devel >= 3:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.344
%{?requires_php_extension}
Requires:	php-common >= 4:5.0.4
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Vulcan Logic Disassembler hooks into the Zend Engine and dumps all
the opcodes (execution units) of a script.

In PECL status of this package is: %{_status}.

%description -l pl
Vulcan Logic Disassembler przyczepia siê do Silnika Zend i zwraca
wszystkie opcody (jednostki wykonawcze) skryptu.

To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c
%patch0 -p1

%build
cd %{_modname}-%{version}
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir}}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{_modname}.ini
; Enable %{_modname} extension module
extension=%{_modname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%php_webserver_restart

%postun
if [ "$1" = 0 ]; then
	%php_webserver_restart
fi

%files
%defattr(644,root,root,755)
%doc %{_modname}-%{version}/{Changelog,CREDITS}
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{_modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{_modname}.so
