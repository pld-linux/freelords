Summary:	Strategy game
Summary(pl):	Gra strategiczna
Name:		freelords
Version:	0.0.6
Release:	1
License:	GPL
Group:		X11/Applications/Games/Strategy
Group(de):	X11/Applikationen/Spiele/Strategie
Group(pl):	X11/Aplikacje/Gry/Strategiczne
Source0:	http://download.freelords.org/sources/%{name}-%{version}.tar.gz
Patch0:		%{name}-make.patch
Patch1:		%{name}-path.patch
URL:		http://www.freelords.org/
BuildRequires:	qt-devel >= 2.2.0
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

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
OPT_FLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"
export OPT_FLAGS
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_bindir}}

install src/%{name} $RPM_BUILD_ROOT%{_bindir}
cp -a pic/* $RPM_BUILD_ROOT%{_datadir}/%{name}
install src/*.py $RPM_BUILD_ROOT%{_datadir}/%{name}

gzip -9nf doc/* AUTHORS README ChangeLog NEWS TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/*.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
