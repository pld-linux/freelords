Summary:	Strategy game
Summary(pl):	Gra strategiczna
Name:		freelords
Version:	0.2.3
Release:	1
License:	GPL
Group:		X11/Applications/Games/Strategy
Source0:	http://dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	b87f3b506c6567a1932e333459a5b9bb
Source1:	%{name}rc.conf
URL:		http://www.freelords.org/
BuildRequires:	SDL_image-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libsigc++-devel >= 1.2.1
BuildRequires:	libtool
BuildRequires:	paragui-devel
BuildRequires:	qt-devel >= 2.2.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FreeLords is a turn-based strategy game. There can be various goals to
achieve like e.g.: destroying all enemies, gathering a specific amount
of money, occupying a certain city, ...

%description -l pl
FreeLords to gra strategiczna z podzia�em na tury. Cele gry mog� by�
r�ne np. zniszczenie wszystkich przeciwnik�w, zebranie okre�lonej
sumy pieni�dzy, okupacja okre�lonego miasta i inne.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}

%configure \
	--disable-paraguitest
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc

install %{SOURCE1} $RPM_BUILD_ROOT/etc/freelordsrc
%{__make} DESTDIR=$RPM_BUILD_ROOT install


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/* AUTHORS ChangeLog TODO
%attr(644,root,root) %config(noreplace) %verify(not size mtime md5) /etc/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
