# $Id$

# Authority: dries
# Upstream:

%define real_name File-Tail
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Perl extension for reading from continuosly updated files
Name: perl-File-Tail
Version: 0.98
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-Tail/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/M/MG/MGRABNAR/File-Tail-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
The File::Tail module is designed for reading files which are continously
appended to (the name comes from the tail -f directive). Usualy such files are
logfiles of some description.

The module tries hard not to busy wait on the file, dynamicaly calcultaing 
how long it should wait before it pays to try reading the file again.

The module should handle normal log truncations ("close; move; open"
or "cat /dev/null >file") transparently, without losing any input.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/File/Tail.pm
%{perl_vendorlib}/auto/File/Tail/autosplit.ix
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 0.98-1
- Initial package.
