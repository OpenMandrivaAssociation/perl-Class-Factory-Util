%define upstream_name	 Class-Factory-Util
%define upstream_version 1.7

Summary:	Provide utility methods for factory classes
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	9
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl(Module::Build)

%description
This module exports a method that is useful for factory classes.

%prep
%setup -qn %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes
%{perl_vendorlib}/Class/*
%{_mandir}/man3/*

