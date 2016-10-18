Summary:	Yamaha DX7 modeling software synthesizer for DSSI
Summary(pl.UTF-8):	Syntezator programowy dla DSSI modelujący urządzenie Yamaha DX7
Name:		hexter
Version:	1.0.3
Release:	2
License:	GPL v2+
Group:		Applications/Sound
Source0:	http://downloads.sourceforge.net/dssi/%{name}-%{version}.tar.bz2
# Source0-md5:	4c3ffd27eecb7eabf1ffc3fe334937bb
URL:		http://dssi.sourceforge.net/hexter.html
BuildRequires:	alsa-lib-devel
BuildRequires:	dssi-devel >= 0.4
BuildRequires:	gtk+2-devel >= 2:2.4
BuildRequires:	ladspa-devel
BuildRequires:	liblo-devel >= 0.23
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
Requires:	dssi >= 0.4
Requires:	liblo >= 0.23
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Yamaha DX7 modeling software synthesizer for the DSSI Soft Synth
Interface.

%description -l pl.UTF-8
Syntezator programowy modelujący urządzenie Yamaha DX7, przeznaczony
dla środowiska DSSI (DSSI Soft Synth Interface).

%prep
%setup -q

%build
%configure \
	--with-textui
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/dssi/hexter.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_libdir}/dssi/hexter.so
%dir %{_libdir}/dssi/hexter
%attr(755,root,root) %{_libdir}/dssi/hexter/hexter_gtk
%attr(755,root,root) %{_libdir}/dssi/hexter/hexter_text
%{_datadir}/hexter
