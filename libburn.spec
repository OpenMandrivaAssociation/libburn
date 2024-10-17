%define major 4
%define libname %mklibname burn %{major}
%define devname %mklibname burn -d

Summary:	Library for reading, mastering and writing optical discs
Name:		libburn
Version:	1.5.6
Release:	1
License:	GPLv2+
Group:		System/Libraries
Url:		https://libburnia-project.org/
Source0:	https://dev.lovelyhq.com/libburnia/libburn/archive/release-%{version}.tar.gz
BuildRequires:	doxygen
BuildRequires:	graphviz

%description
Libburn is an open-source library for reading, mastering and writing
optical discs.

%package -n %{libname}
Group:		System/Libraries
Summary:	An open-source library for optical discs

%description -n %{libname}
An open-source library for reading, mastering and writing optical discs.

%package -n %{devname}
Summary:	Header files for development with %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}burn6-devel < 1.2.4
Obsoletes:	%{_lib}burn-static-devel < 1.2.8-2

%description -n %{devname}
This package includes the header files for the %{name} package.

%package -n cdrskin
Summary:	Limited cdrecord compatibility wrapper for libburn
Group:		Archiving/Cd burning

%description -n cdrskin
A limited cdrecord compatibility wrapper which allows to use some
libburn features from the command line. 

%prep
%autosetup -p1 -n %{name}
%configure

%build
%make_build

%install
%make_install

# build documentation
doxygen -u doc/doxygen.conf
doxygen doc/doxygen.conf

%files -n %{libname}
%{_libdir}/libburn.so.%{major}*

%files -n %{devname}
%doc README AUTHORS COPYRIGHT
%{_libdir}/libburn.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/%{name}

%files -n cdrskin
%doc cdrskin/README
%{_bindir}/cdrskin
%doc %{_mandir}/man1/cdrskin.1*
