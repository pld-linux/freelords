Summary:	Turn-based strategy game
Summary(pl.UTF-8):	Turowa gra strategiczna
Name:		freelords
Version:	0.3.8
Release:	2
License:	GPL v2+
Group:		X11/Applications/Games/Strategy
Source0:	http://dl.sourceforge.net/freelords/%{name}-%{version}.tar.bz2
# Source0-md5:	e8b0047cd9410d0b33607a206e816c50
Source1:	%{name}rc.conf
Patch0:		%{name}-configure_in.patch
Patch1:		%{name}-types.patch
Patch2:		%{name}-undefined_macros.patch
Patch3:		%{name}-desktop.patch
Patch4:		%{name}-mkinstalldirs.patch
Patch5:		%{name}-makefileam.patch
URL:		http://freelords.sourceforge.net/
BuildRequires:	SDL_image-devel >= 1.2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libsigc++12-devel >= 1.2.1
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	paragui-devel >= 1.1.8
BuildRequires:	pkgconfig
BuildRequires:	qt-devel >= 2.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FreeLords is a turn-based strategy game. There can be various goals to
achieve like e.g.: destroying all enemies, gathering a specific amount
of money, occupying a certain city, ...

%description -l pl.UTF-8
FreeLords to turowa gra strategiczna wzorowana na klasycznej grze
Warlords. Cele gry mogą być różne np. zniszczenie wszystkich
przeciwników, zebranie określonej sumy pieniędzy, okupacja określonego
miasta i inne.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/freelordsrc
install dat/various/%{name}.png $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc doc/* AUTHORS ChangeLog NEWS TODO
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/freelordsrc
%attr(755,root,root) %{_bindir}/freelords
%attr(755,root,root) %{_bindir}/freelords_editor
%attr(755,root,root) %{_bindir}/freelords_server
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
