#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Devel
%define		pnam	Profiler
Summary:	Devel::Profiler - a Perl profiler compatible with dprofpp
Summary(pl.UTF-8):	Devel::Profiler - profiler dla Perla kompatybilny z dprofpp
Name:		perl-Devel-Profiler
Version:	0.04
Release:	4
# same as perl 5
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c52d615e3083defd2c71726f21b2127a
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-tools-devel
%if %{with tests}
BuildRequires:	perl-Test-Simple
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements a Perl profiler that outputs profiling data in
a format compatible with dprofpp, Devel::DProf's profile analysis
tool. It is meant to be a drop-in replacement for Devel::DProf.

%description -l pl.UTF-8
Ten moduł jest implementacją perlowego profilera, który zapisuje dane
profilujące w formacie kompatybilnym z dprofpp, czyli narzędziem
analizującym z Devel::DProf. Ma być zastepnikiem Devel::DProf.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
