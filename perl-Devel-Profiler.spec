#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	Devel
%define	pnam	Profiler
Summary:	Devel::Profiler - a Perl profiler compatible with dprofpp
Summary(pl):	Devel::Profiler - profiler dla Perla kompatybilny z dprofpp
Name:		perl-Devel-Profiler
Version:	0.04
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-Time-HiRes
%endif
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements a Perl profiler that outputs profiling data in
a format compatible with dprofpp, Devel::DProf's profile analysis
tool. It is meant to be a drop-in replacement for Devel::DProf.

%description -l pl
Ten modu³ jest implementacj± perlowego profilera, który zapisuje dane
profiluj±ce w formacie kompatybilnym z dprofpp, czyli narzêdziem
analizuj±cym z Devel::DProf. Ma byæ zastepnikiem Devel::DProf.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{perl_sitelib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
