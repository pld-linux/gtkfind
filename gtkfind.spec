Summary:	A graphical file finding program
Name:		gtkfind
Version:	1.0.2
Release:	1
License:	GPL
Group:		X11/Utilities
Group(pl):	X11/Narzêdzia
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
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
XBD=$RPM_BUILD_ROOT%{_prefix}/bin
XMD=$RPM_BUILD_ROOT%{_prefix}/man/man1
BD=$RPM_BUILD_ROOT%{_bindir}
MD=$RPM_BUILD_ROOT/usr/man/man1
test -d $XBD || install -d $XBD
test -d $XMD || install -d $XMD
test -d $BD || install -d $BD
test -d $MD || install -d $MD
install -s -m 555 gtkfind $XBD
install -m 444 gtkfind.1 $XMD
install -s -m 555 mktmp $BD
install -m 444 mktmp.1 $MD

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(-, root, root) %doc README TODO
%attr(555, root, root) %{_prefix}/bin/gtkfind
%attr(444, root, root) %{_prefix}/man/man1/gtkfind.1
%attr(555, root, root) %{_bindir}/mktmp
%attr(444, root, root) /usr/man/man1/mktmp.1
