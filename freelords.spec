Summary:	Strategy game
Summary(pl):	Gra strategiczna
Name:		freelords
Version:	0.1.6
Release:	2
License:	GPL
Group:		X11/Applications/Games/Strategy
Source0:	http://download.freelords.org/sources/%{name}-%{version}.tar.gz
Patch0:		%{name}-make.patch
Patch1:		%{name}-path.patch
URL:		http://www.freelords.org/
BuildRequires:	SDL_image-devel
BuildRequires:	libstdc++-devel
BuildRequires:	paragui-devel
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
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
find . -type d -name 'CVS'| xargs rm -rf

%build
%{__make} CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_bindir},%{_libdir}}

install src/%{name} $RPM_BUILD_ROOT%{_bindir}
install src/{common,graphic}/lib*so.*.* $RPM_BUILD_ROOT%{_libdir}

cp -a pic/* $RPM_BUILD_ROOT%{_datadir}/%{name}
install src/*.py $RPM_BUILD_ROOT%{_datadir}/%{name}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/* AUTHORS ChangeLog TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_datadir}/%{name}
