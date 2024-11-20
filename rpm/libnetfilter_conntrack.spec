Name:           libnetfilter_conntrack
Version:        1.1.0
Release:        1
Summary:        Netfilter conntrack userspace library
License:        GPLv2
URL:            https://github.com/sailfishos/libnetfilter_conntrack
Source0:        %{name}-%{version}.tar.bz2

Requires:       libnfnetlink >= 1.0.2

BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  kernel-headers
BuildRequires:  libmnl-devel >= 1.0.3
BuildRequires:  libnfnetlink-devel >= 1.0.1
BuildRequires:  make autoconf automake libtool
BuildRequires:  pkgconfig

%description
libnetfilter_conntrack is a userspace library providing a programming 
interface (API) to the in-kernel connection tracking state table.

%package        devel
Summary:        Netfilter conntrack userspace library
Requires:       %{name} = %{version}-%{release}, libnfnetlink-devel >= 1.0.1
Requires:       kernel-headers

%description    devel
libnetfilter_conntrack is a userspace library providing a programming
interface (API) to the in-kernel connection tracking state table.

%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%build
%autogen
autoreconf -vi
%configure --disable-static --disable-rpath

%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name "*.la" -delete

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%dir %{_includedir}/libnetfilter_conntrack
%{_includedir}/libnetfilter_conntrack/*.h
