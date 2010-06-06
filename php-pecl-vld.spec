%define		modname	vld
%define		status	beta
Summary:	%{modname} - provides functionality to dump the internal representation of PHP scripts
Summary(pl.UTF-8):	%{modname} - dostarcza funkcjonalności do zrzutu wewnętrznej reprezentacji skryptów PHP
Name:		php-pecl-%{modname}
Version:	0.10.1
Release:	1
License:	BSD style
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{modname}-%{version}.tgz
# Source0-md5:	c050c9aae5aeb83f012635619c568ddb
URL:		http://pecl.php.net/package/vld/
BuildRequires:	php-devel >= 3:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.344
%{?requires_php_extension}
Requires:	php-common >= 4:5.0.4
Obsoletes:	php-pear-%{modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Vulcan Logic Disassembler hooks into the Zend Engine and dumps all
the opcodes (execution units) of a script.

In PECL status of this package is: %{status}.

%description -l pl.UTF-8
Vulcan Logic Disassembler podłącza się do silnika Zend i zwraca
wszystkie jednostki wykonawcze (tzw. opcody) danego skryptu.

To rozszerzenie ma w PECL status: %{status}.

%prep
%setup -qc
mv %{modname}-%{version}/* .

%build
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir}}
install -p modules/%{modname}.so $RPM_BUILD_ROOT%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{modname}.ini
; Enable %{modname} extension module
extension=%{modname}.so
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
%doc Changelog CREDITS
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{modname}.so
