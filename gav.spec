Summary:	GPL Arcade Volleyball
Summary(pl):	Gra zrêczno¶ciowa w siatkówkê
Name:		gav
Version:	0.7.3
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	938c8cd9e7eef6842f931620377fe6b4
Patch0:		%{name}-desktop.patch
URL:		http://gav.sourceforge.net/
Buildrequires:	SDL-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GAV stands for GPL Arcade Volleyball, and is a remake of the old dos
game Arcade Volleyball.

%description -l pl
GAV oznacza GPL Arcade Volleyball i jest "od¶wie¿on±" wersj± starej
dosowej gry Arcade Voleyball.

%prep
%setup -q
%patch0 -p1

%build
./build_linux.sh
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	ROOT=$RPM_BUILD_ROOT

install package/%{name}.desktop $RPM_BUILD_ROOT%{_desktopdir}
install package/%{name}.png $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/games/%{name}
%{_desktopdir}/*
%{_pixmapsdir}/*
