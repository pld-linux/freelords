Summary:	Strategy game
Summary(pl):	Gra strategiczna
Name:		freelords
Version:	0.3.5
Release:	1
License:	GPL
Group:		X11/Applications/Games/Strategy
Source0:	http://dl.sourceforge.net/freelords/%{name}-%{version}.tar.bz2
# Source0-md5:	263887334afa2df5a34cc9ce9163bfe3
Source1:	%{name}rc.conf
Patch0:		%{name}-configure_in.patch
Patch1:		%{name}-types.patch
URL:		http://www.freelords.org/
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

%description -l pl
FreeLords to gra strategiczna z podzia³em na tury. Cele gry mog± byæ
ró¿ne np. zniszczenie wszystkich przeciwników, zebranie okre¶lonej
sumy pieniêdzy, okupacja okre¶lonego miasta i inne.

%prep
%setup -q
%patch0 -p0
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/freelordsrc

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc doc/* AUTHORS ChangeLog TODO
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
