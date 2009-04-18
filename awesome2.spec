Summary:	Awesome Window Manager
Summary(hu.UTF-8):	awesome ablakkezelő
Summary(pl.UTF-8):	Zarządca okien X - Awesome
Name:		awesome2
Version:	2.3.6
Release:	0.1
License:	GPL v2
Group:		X11/Window Managers
Source0:	http://awesome.naquadah.org/download/awesome-%{version}.tar.bz2
# Source0-md5:	29b07dbb801b0907514844b88f9bca6e
Source1:	%{name}-xsession.desktop
URL:		http://awesome.naquadah.org/
BuildRequires:	asciidoc
BuildRequires:	cairo-devel
BuildRequires:	doxygen
BuildRequires:	imlib2-devel
BuildRequires:	libconfuse-devel
BuildRequires:	pango-devel
BuildRequires:	pkgconfig >= 0.9.0
BuildRequires:	sed >= 4.0
BuildRequires:	xmlto
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXrandr-devel
Conflicts:	awesome < 3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%{expand:%%define	_sysconfdir	%{_sysconfdir}/X11}

%description
awesome is a floating and tiling window manager initialy based on a
dwm code rewriting. It's extremely fast, small, dynamic and awesome.
This is the old stable 2.x branch (without lua).

%description -l pl.UTF-8
awesome to zarządca okien o zachowaniu pływającym i kaflowym,
początkowo oparty na przepisaniu kodu zarządcy dwm. Jest bardzo
szybki, mały, dynamiczny i przeraźliwy.

%description -l hu.UTF-8
awesome egy floating és tiling típusú ablakkezelő, amely kezdetben a
dwm-en alapult. Extrém gyors, kicsi, dinamikus és... félelmetes. Ez a
régi, stabil 2.x-es sorozat tagja (ebben még nincs lua).

%prep
%setup -q -n awesome-%{version}

%build
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xsessions

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_datadir}/awesome{,2}

for i in $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man{1,5}}/*; do
	mv $i $(dirname $i)/$(echo $(basename $i) | sed "s|awesome|awesome2|");
done

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/xsessions/%{name}.desktop

rm -rf $RPM_BUILD_ROOT%{_docdir}/awesome

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE README STYLE awesomerc
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/%{name}-client
%attr(755,root,root) %{_bindir}/%{name}-menu
%attr(755,root,root) %{_bindir}/%{name}-message
%{_datadir}/%{name}
%{_datadir}/xsessions/%{name}.desktop
%{_mandir}/man1/%{name}*
%{_mandir}/man5/%{name}*
