Summary:	GPL Arcade Volleyball
Summary(pl):	Gra zr�czno�ciowa w siatk�wk�
Name:		gav
Version:	0.8.0
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	4972fae26f2d0c0df8a0ce32560b1f5f
Patch0:		%{name}-desktop.patch
URL:		http://gav.sourceforge.net/
BuildRequires:	SDL_net-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GAV stands for GPL Arcade Volleyball, and is a remake of the old dos
game Arcade Volleyball.

%description -l pl
GAV oznacza GPL Arcade Volleyball i jest "od�wie�on�" wersj� starej
dosowej gry Arcade Voleyball.

%prep
%setup -q
%patch0 -p1

%build
./build_linux.sh
%{__make} \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcflags} `sdl-config --cflags` -Wall -I`pwd`/menu -I`pwd`/automa -I`pwd`/net -I`pwd`"

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
