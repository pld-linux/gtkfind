Summary:	A graphical file finding program
Summary(pl):	Graficzny program do szukania plików
Name:		gtkfind
Version:	1.0.2
Release:	1
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	http://www.oz.net/~mattg/%{name}-%{version}.tar.gz
URL:		http://www.oz.net/~mattg/download.html
Vendor:		Matt Grossman <mattg@oz.net>
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
gtkfind is a graphical file finding program, written by Matt Grossman
<mattg@oz.net> and distributed under the terms of the GNU GPL. It
requires X and the freely distributable (GPL) gtk toolkit to run. gtk
is available from www.gtk.org and other places.

%description -l pl
gtkfind jest graficznym programem do znajdowania plików, napisanym
przez Matta Grossmana <mattg@oz.net> i rozpowszechnianym na licencji
GNU GPL. Wymaga X oraz biblioteki gtk (któr± mo¿na uzyskaæ np. z
www.gtk.org).

%prep
%setup -q 

%build
CFLAGS="%{rpmcflags}" ./configure --prefix=/usr
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
XBD=$RPM_BUILD_ROOT%{_bindir}
XMD=$RPM_BUILD_ROOT%{_mandir}/man1
BD=$RPM_BUILD_ROOT/usr/bin
MD=$RPM_BUILD_ROOT/usr/share/man/man1
test -d $XBD || install -d $XBD
test -d $XMD || install -d $XMD
test -d $BD || install -d $BD
test -d $MD || install -d $MD
install -m 555 gtkfind $XBD
install -m 444 gtkfind.1 $XMD
install -m 555 mktmp $BD
install -m 444 mktmp.1 $MD

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(-, root, root) %doc README TODO
%attr(555, root, root) %{_bindir}/gtkfind
%attr(444, root, root) %{_mandir}/man1/gtkfind.1
%attr(555, root, root) /usr/bin/mktmp
%attr(444, root, root) /usr/share/man/man1/mktmp.1
