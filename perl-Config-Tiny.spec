%define upstream_name    Config-Tiny
%define upstream_version 2.14

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Read/Write .ini style files with as little code as possible
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Config/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
"Config::Tiny" is a perl class to read and write .ini style
configuration files with as little code as possible, reducing load time
and memory overhead. Most of the time it is accepted that Perl
applications use a lot of memory and modules. The "::Tiny" family of
modules is specifically intended to provide an ultralight alternative to
the standard modules.

This module is primarily for reading human written files, and anything
we write shouldn't need to have documentation/comments. If you need
something with more power move up to Config::Simple, Config::General or
one of the many other "Config::" modules. To rephrase, Config::Tiny does
not preserve your comments, whitespace, or the order of your config
file.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
chmod 644 Changes lib/Config/Tiny.pm
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Config
%{_mandir}/*/*
