#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : siege
Version  : 2.78
Release  : 2
URL      : http://pkgs.fedoraproject.org/repo/pkgs/siege/siege-2.78.tar.gz/e165dcab18ae27026f09c2b23dcca322/siege-2.78.tar.gz
Source0  : http://pkgs.fedoraproject.org/repo/pkgs/siege/siege-2.78.tar.gz/e165dcab18ae27026f09c2b23dcca322/siege-2.78.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: siege-bin
BuildRequires : openssl-dev
BuildRequires : zlib-dev

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

%description bin
bin components for the siege package.


%prep
%setup -q -n siege-2.78

%build
export LANG=C
export SOURCE_DATE_EPOCH=1487203910
%reconfigure --disable-static ; sed -i 's/doc //' Makefile.am; autoreconf -vif; libtoolize -c -f; %configure; rm -f libtool; cp /usr/bin/libtool .
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1487203910
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
