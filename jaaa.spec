#
# Conditional build:
%bcond_with	tests		# build with tests
%bcond_without	tests		# build without tests
#
Summary:	JACK and ALSA Audio Analyser
Name:		jaaa
Version:	0.8.4
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	2eed043d641788541c15929183ef277f
Patch0:		makefile.patch
URL:		http://kokkinizita.linuxaudio.org/linuxaudio/index.html
BuildRequires:	clthreads-devel
BuildRequires:	clxclient-devel
BuildRequires:	fftw3-single-devel
BuildRequires:	zita-alsa-pcmi-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jaaa (JACK and ALSA Audio Analyser, is an audio signal generator and
spectrum analyser designed to make accurate measurements.

%prep
%setup -q
%patch0 -p1

%build
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
%attr(755,root,root) %{_bindir}/%{name}
