#
# Conditional build:
%bcond_without	tests		# perform "make test"
#
%define	pdir	MozRepl
Summary:	MozRepl - Perl interface of MozRepl
Summary(pl.UTF-8):	MozRepl - interfejs Perla do MozRepl
Name:		perl-MozRepl
Version:	0.06
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://cpan.metacpan.org/authors/id/Z/ZI/ZIGOROU/%{pdir}-%{version}.tar.gz
# Source0-md5:	0c7637b6cb5e3d3f1e8aca4cc24c8634
URL:		http://search.cpan.org/dist/MozRepl-RemoteObject/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl(Carp::Clan)
BuildRequires:	perl(Class::Accessor::Fast)
BuildRequires:	perl(Class::Data::Inheritable)
BuildRequires:	perl(Data::Dump)
BuildRequires:	perl(Data::JavaScript::Anon)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Module::Pluggable::Fast)
BuildRequires:	perl(Net::Telnet)
BuildRequires:	perl(Template)
BuildRequires:	perl(Template::Provider::FromDATA)
BuildRequires:	perl(Text::SimpleTable)
BuildRequires:	perl(UNIVERSAL::require)
BuildRequires:	perl(URI)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MozRepl is accessing and control Firefox using telnet.
This module is perl interface of MozRepl.

%description -l pl.UTF-8
MozRepl jest mechanizmem sterowania Firefoksem za pomocą telneta.
Ten moduł jest interfejsem Perla do MozRepl.

%prep
%setup -q -n %{pdir}-%{version}

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
%doc Changes README
%{perl_vendorlib}/MozRepl.pm
%{perl_vendorlib}/MozRepl
#{perl_vendorlib}/MozRepl/Plugin
#{perl_vendorlib}/MozRepl/Plugin/Repl
#{perl_vendorlib}/MozRepl/Plugin/Repl/Util
%{_mandir}/man?/*
