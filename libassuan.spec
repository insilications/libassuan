#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x249B39D24F25E3B6 (dshaw@jabberwocky.com)
#
Name     : libassuan
Version  : 2.5.1
Release  : 15
URL      : ftp://ftp.gnupg.org/gcrypt/libassuan/libassuan-2.5.1.tar.bz2
Source0  : ftp://ftp.gnupg.org/gcrypt/libassuan/libassuan-2.5.1.tar.bz2
Source99 : ftp://ftp.gnupg.org/gcrypt/libassuan/libassuan-2.5.1.tar.bz2.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0 LGPL-2.1
Requires: libassuan-bin
Requires: libassuan-lib
Requires: libassuan-doc
BuildRequires : libgpg-error-dev

%description
Libassuan
===========
This is a general purpose IPC library which is for example used
GnuPG, GPGME and some other software.

%package bin
Summary: bin components for the libassuan package.
Group: Binaries

%description bin
bin components for the libassuan package.


%package dev
Summary: dev components for the libassuan package.
Group: Development
Requires: libassuan-lib
Requires: libassuan-bin
Provides: libassuan-devel

%description dev
dev components for the libassuan package.


%package doc
Summary: doc components for the libassuan package.
Group: Documentation

%description doc
doc components for the libassuan package.


%package lib
Summary: lib components for the libassuan package.
Group: Libraries

%description lib
lib components for the libassuan package.


%prep
%setup -q -n libassuan-2.5.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1513784013
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1513784013
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/libassuan-config

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libassuan.so
/usr/share/aclocal/*.m4

%files doc
%defattr(-,root,root,-)
%doc /usr/share/info/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libassuan.so.0
/usr/lib64/libassuan.so.0.8.1
