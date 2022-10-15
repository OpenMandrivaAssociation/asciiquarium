Name:		asciiquarium
Version:	1.1
Release:	3
Summary:	An aquarium/sea animation in ASCII art
License:	GPL
Group:		Toys
URL:		http://www.robobunny.com/projects/asciiquarium/
Source0:	http://www.robobunny.com/projects/asciiquarium/%{name}_%{version}.tar.gz
BuildArch:	noarch

%description
Asciiquarium is an aquarium/sea animation in ASCII art.

%files
%doc CHANGES README gpl.txt
%{_bindir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}_%{version}

%build
# nothing to do here

%install
install -dm 755 %{buildroot}%{_bindir}
install -pm 755 %{name} %{buildroot}%{_bindir}

