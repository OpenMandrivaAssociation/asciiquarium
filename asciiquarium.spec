%define name    asciiquarium
%define version 1.0
%define release %mkrel 5

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        An aquarium/sea animation in ASCII art
License:        GPL
Group:          Toys
URL:            http://www.robobunny.com/projects/asciiquarium/
Source0:        http://www.robobunny.com/projects/asciiquarium/%{name}_%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}
Requires:	perl-Term-Animation
BuildArch:      noarch

%description
Asciiquarium is an aquarium/sea animation in ASCII art.

%prep
%setup -q -n %{name}_%{version}

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_bindir}
install -m 755 asciiquarium %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES  README gpl.txt
%{_bindir}/*


