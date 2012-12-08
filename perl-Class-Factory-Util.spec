%define upstream_name	 Class-Factory-Util
%define upstream_version 1.7

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:	Provide utility methods for factory classes
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:  perl(Module::Build)

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module exports a method that is useful for factory classes.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/Class/*
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.700.0-2mdv2011.0
+ Revision: 680820
- mass rebuild

* Sat Feb 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.700.0-1mdv2011.0
+ Revision: 505428
- rebuild using %%perl_convert_version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.7-4mdv2010.0
+ Revision: 430328
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.7-3mdv2009.0
+ Revision: 241185
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Apr 29 2007 Olivier Thauvin <nanardon@mandriva.org> 1.7-1mdv2008.0
+ Revision: 19314
- 1.7


* Fri Mar 31 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.6-2mdk
- Rebuild

* Wed Aug 25 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.6-1mdk
- Initial MDK release.

