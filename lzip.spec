Summary:	LZMA file compressor
Summary(pl.UTF-8):	Kompresor plików oparty na algorytmie LZMA
Name:		lzip
Version:	1.25
Release:	2
License:	GPL v3+
Group:		Applications/Archiving
Source0:	https://download.savannah.gnu.org/releases/lzip/%{name}-%{version}.tar.gz
# Source0-md5:	1ee31ca9e80af55f7a3d738e7a861dcc
Patch0:		%{name}-info.patch
URL:		http://savannah.nongnu.org/projects/lzip/
BuildRequires:	libstdc++-devel
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lzip is a lossless file compressor based on the LZMA
(Lempel-Ziv-Markov chain-Algorithm) algorithm designed by Igor Pavlov.
The high compression of LZMA comes from combining two basic,
well-proven compression ideas: sliding dictionaries (i.e. LZ77/78),
and Markov models (i.e. the thing used by every compression algorithm
that uses a range encoder or similar order-0 entropy coder as its last
stage) with segregation of contexts according to what the bits are
used for.

%description -l pl.UTF-8
lzip to bezstratny kompresor plików oparty na algorytmie LZMA
(Lempel-Ziv-Markov chain-Algorithm) opracowanym przez Igora Pawłowa.
Wysoki stopień kompresji LZMA wywodzi się z połączenia dwóch
podstawowych, dobrze sprawdzonych idei kompresji: przesuwnych
słowników (LZ77/78) i modeli Markowa (używanych przez każdy algorytm
kompresji wykorzystujący w ostatnim stadium kodowanie zakresów lub
podobne kodowanie entropii rzędu 0) z podziałem kontekstów w
zależności od wykorzystania bitów.

%prep
%setup -q
%patch -P0 -p1

%build
%configure \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcxxflags}" \
	CPPFLAGS="%{rpmcppflags}" \
	LDFLAGS="%{rpmldflags}"

%{__make} all info

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install-man \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/lzip
%{_mandir}/man1/lzip.1*
%{_infodir}/lzip.info*
