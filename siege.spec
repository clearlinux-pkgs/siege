#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : siege
Version  : 2.78
Release  : 6
URL      : http://pkgs.fedoraproject.org/repo/pkgs/siege/siege-2.78.tar.gz/e165dcab18ae27026f09c2b23dcca322/siege-2.78.tar.gz
Source0  : http://pkgs.fedoraproject.org/repo/pkgs/siege/siege-2.78.tar.gz/e165dcab18ae27026f09c2b23dcca322/siege-2.78.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: siege-bin
Requires: siege-data
Requires: siege-doc
BuildRequires : openssl-dev
BuildRequires : zlib-dev
Patch1: 0001-Better-file-locations.patch

%description
WHAT IS IT?
-----------
Siege is an open source regression  test and  benchmark utility.
It can stress test a single URL  with a user  defined  number of
simulated  users, or  it can  read  many  URLs into  memory  and
stress  them  simultaneously.  The  program  reports  the  total
number  of  hits  recorded,  bytes  transferred,  response time,
concurrency, and return status.  Siege supports HTTP/1.0 and 1.1
protocols, the  GET and POST  directives,  cookies,  transaction
logging, and basic authentication. Its features are configurable
on a per user basis.

%package bin
Summary: bin components for the siege package.
Group: Binaries
Requires: siege-data

%description bin
bin components for the siege package.


%package data
Summary: data components for the siege package.
Group: Data

%description data
data components for the siege package.


%package doc
Summary: doc components for the siege package.
Group: Documentation

%description doc
doc components for the siege package.


%prep
%setup -q -n siege-2.78
%patch1 -p1

%build
export LANG=C
export SOURCE_DATE_EPOCH=1487273757
%reconfigure --disable-static ; autoreconf -vif; %configure; cp /usr/bin/libtool .
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1487273757
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/bombardment
/usr/bin/siege
/usr/bin/siege.config
/usr/bin/siege2csv.pl

%files data
%defattr(-,root,root,-)
/usr/share/defaults/siege/siegerc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man5/*
%doc /usr/share/man/man7/*
