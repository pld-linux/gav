Summary:	GPL Arcade Volleyball
Summary(pl):	Gra zrêczno¶ciowa w siatkówkê
Name:		gav
Version:	0.8.0
Release:	2
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	4972fae26f2d0c0df8a0ce32560b1f5f
Source1:	http://gav.sourceforge.net/themes/tgz/fabeach.tgz
# Source1-md5:	3d1c461befc84ca91fc4a10a91296289
Source2:	http://gav.sourceforge.net/themes/tgz/inverted.tgz
# Source2-md5:	282e27c9bf5b4743a10ca2af1977883e
Source3:	http://gav.sourceforge.net/themes/tgz/unnamed.tgz
# Source3-md5:	3c109c0f229ba16e3062fc8b249d4492
Source4:	http://gav.sourceforge.net/themes/tgz/yisus.tgz
# Source4-md5:	bd7981c2308d07635fe0738dd88d7369
Source5:	http://gav.sourceforge.net/themes/tgz/yisus2.tgz
# Source5-md5:	21ff7420f3670aa1d565f4c89efd44b9
Source6:	http://gav.sourceforge.net/themes/tgz/naive.tgz
# Source6-md5:	330f63e5d781e382637eeec3f683b5cf
Source7:	http://gav.sourceforge.net/themes/tgz/florindo.tgz
# Source7-md5:	51817c29099a8bc6bc2e9a92f64f5c5b
Patch0:		%{name}-desktop.patch
URL:		http://gav.sourceforge.net/
BuildRequires:	SDL_net-devel
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

cd themes/
tar xzvf %{SOURCE1}
tar xzvf %{SOURCE2}
tar xzvf %{SOURCE3}
tar xzvf %{SOURCE4}
tar xzvf %{SOURCE5}
tar xzvf %{SOURCE6}
tar xzvf %{SOURCE7}

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
