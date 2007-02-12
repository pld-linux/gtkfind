Summary:	A graphical file finding program
Summary(pl.UTF-8):   Graficzny program do szukania plików
Name:		gtkfind
Version:	1.1
Release:	1
License:	GPL
Group:		X11/Applications
# from Mandrake src.rpm
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	6a894f3a798189cf74e7d61ddf1179f6
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gtkfind is a graphical file finding program, written by Matt Grossman
<mattg@oz.net> and distributed under the terms of the GNU GPL. It
requires X and the freely distributable (GPL) GTK+ toolkit to run. GTK+
is available from http://www.gtk.org/ and other places.

%description -l pl.UTF-8
gtkfind jest graficznym programem do znajdowania plików, napisanym
przez Matta Grossmana <mattg@oz.net> i rozpowszechnianym na licencji
GNU GPL. Wymaga X oraz biblioteki GTK+ (którą można uzyskać np. z
http://www.gtk.org/).

%prep
%setup -q

%build
%configure2_13

%{__make} \
	CFLAGS="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_bindir}/gtkfind
%attr(755,root,root) %{_bindir}/mktmp
%{_mandir}/man1/gtkfind.1*
%{_mandir}/man1/mktmp.1*
