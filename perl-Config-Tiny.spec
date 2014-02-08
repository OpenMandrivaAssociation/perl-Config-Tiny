%define upstream_name    Config-Tiny
%define upstream_version 2.14

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	Read/Write .ini style files with as little code as possible
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Config/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

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
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Config
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 2.140.0-4mdv2012.0
+ Revision: 765107
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 2.140.0-3
+ Revision: 763564
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 2.140.0-2
+ Revision: 676621
- rebuild

* Sat Mar 26 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.140.0-1
+ Revision: 648567
- update to new version 2.14

* Fri Sep 03 2010 Jérôme Quelin <jquelin@mandriva.org> 2.130.0-1mdv2011.0
+ Revision: 575590
- update to 2.13

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 2.120.0-1mdv2011.0
+ Revision: 406914
- rebuild using %%perl_convert_version

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 2.12-3mdv2009.0
+ Revision: 256130
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Nov 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.12-1mdv2008.1
+ Revision: 105301
- update to new version 2.12


* Sat Nov 18 2006 Olivier Thauvin <nanardon@mandriva.org> 2.10-1mdv2007.0
+ Revision: 85433
- 2.10
- Import perl-Config-Tiny

* Thu Aug 03 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.08-1mdv2007.0
- New version 2.08

* Wed May 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.07-1mdv2007.0
- New release 2.07
- spec cleanup
- fix directory ownership

* Thu Apr 27 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.06-1mdk
- New release 2.06

* Mon Feb 27 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.05-1mdk
- 2.05

* Tue Feb 07 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.04-1mdk
- 2.04

* Fri Jul 15 2005 Oden Eriksson <oeriksson@mandriva.com> 2.02-1mdk
- initial Mandriva package

