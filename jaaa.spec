Summary:	JACK and ALSA Audio Analyser
Summary(pl.UTF-8):	Analizator dźwięku JACK i ALSA
Name:		jaaa
Version:	0.9.2
Release:	1
License:	GPL v2
Group:		Applications/Sound
Source0:	http://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	02ceeda017e57635c64302e6271ad094
Patch0:		makefile.patch
URL:		http://kokkinizita.linuxaudio.org/linuxaudio/index.html
BuildRequires:	clthreads-devel >= 2.4.0
BuildRequires:	clxclient-devel >= 3.9.0
BuildRequires:	fftw3-single-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	zita-alsa-pcmi-devel >= 0.3.0
Requires:	clthreads >= 2.4.0
Requires:	clxclient >= 3.9.0
Requires:	zita-alsa-pcmi >= 0.3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jaaa (JACK and ALSA Audio Analyser), is an audio signal generator and
spectrum analyser designed to make accurate measurements.

%description -l pl.UTF-8
Jaaa (JACK and ALSA Audio Analyser) to generator i analizator widma
sygnałów dźwiękowych, zaprojektowany z myślą o dokładnych pomiarach.

%prep
%setup -q
%patch0 -p1

%build
CXX="%{__cxx}" \
CXXFLAGS="%{rpmcxxflags}" \
CPPFLAGS="%{rpmcppflags}" \
LDFLAGS="%{rpmldflags}" \
%{__make} -C source

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C source install \
	PREFIX="%{_prefix}" \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/jaaa
