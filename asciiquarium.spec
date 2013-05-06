%define name    asciiquarium
%define version 1.1
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        An aquarium/sea animation in ASCII art
License:        GPL
Group:          Toys
URL:            http://www.robobunny.com/projects/asciiquarium/
Source0:        http://www.robobunny.com/projects/asciiquarium/%{name}_%{version}.tar.gz
Requires:	perl-Term-Animation
BuildArch:      noarch

%description
Asciiquarium is an aquarium/sea animation in ASCII art.

%prep
%setup -q -n %{name}_%{version}

%install
install -d -m 755 %{buildroot}%{_bindir}
install -m 755 asciiquarium %{buildroot}%{_bindir}

%files
%doc CHANGES  README gpl.txt
%{_bindir}/*




%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-6mdv2011.0
+ Revision: 616606
- the mass rebuild of 2010.0 packages

* Tue Sep 01 2009 Thierry Vignaud <tv@mandriva.org> 1.0-5mdv2010.0
+ Revision: 423961
- rebuild

* Thu Jun 19 2008 Thierry Vignaud <tv@mandriva.org> 1.0-4mdv2009.0
+ Revision: 226178
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 18 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.0-3mdv2008.1
+ Revision: 132386
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Nov 24 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.0-2mdv2007.0
+ Revision: 86968
- rebuild
- Import asciiquarium

* Thu Sep 08 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.0-1mdk
- first mdk release

