Summary  : A graphical file finding program
Name     : gtkfind
Version  : 1.0
Release  : 1
Copyright: GPL
Group    : X11/Utilities
Source0  : http://www.oz.net/~mattg/gtkfind-1.0.tar.gz
URL      : http://www.oz.net/~mattg/download.html
Vendor   : Matt Grossman <mattg@oz.net>
Packager : Tom Weber <x@4t2.com>
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gtkfind is a graphical file finding program, written by Matt Grossman
<mattg@oz.net> and distributed under the terms of the GNU GPL.  It
requires X and the freely distributable (GPL) gtk toolkit to run.  gtk
is available from www.gtk.org and other places.

%prep
%setup 

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr
make

%install
XBD=$RPM_BUILD_ROOT/usr/X11R6/bin
XMD=$RPM_BUILD_ROOT/usr/X11R6/man/man1
BD=$RPM_BUILD_ROOT/usr/bin
MD=$RPM_BUILD_ROOT/usr/man/man1
test -d $XBD || mkdir -p $XBD
test -d $XMD || mkdir -p $XMD
test -d $BD || mkdir -p $BD
test -d $MD || mkdir -p $MD
install -s -m 555 gtkfind $XBD
install -m 444 gtkfind.1 $XMD
install -s -m 555 mktmp $BD
install -m 444 mktmp.1 $MD

%clean
rm -fr $RPM_BUILD_ROOT

%files
%attr(-, root, root) %doc README TODO
%attr(555, root, root) /usr/X11R6/bin/gtkfind
%attr(444, root, root) /usr/X11R6/man/man1/gtkfind.1
%attr(555, root, root) /usr/bin/mktmp
%attr(444, root, root) /usr/man/man1/mktmp.1
