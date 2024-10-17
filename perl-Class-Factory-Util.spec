%define upstream_name Class-Factory-Util
%define upstream_version 1.7

Summary:	Provide utility methods for factory classes
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	15
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test)
BuildRequires:	perl(Module::Build)

%description
This module exports a method that is useful for factory classes.

%prep
%autosetup -n %{upstream_name}-%{upstream_version} -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
%make test

%install
%make_install

%files
%doc Changes
%{perl_vendorlib}/Class/*
%doc %{_mandir}/man3/*
