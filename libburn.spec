%define name    libburn
%define version 0.3.8
%define rel 	1

%define major 	4
%define libname %mklibname burn %major
%define develname %mklibname burn -d

Summary: 	Library for reading, mastering and writing optical discs
Name: 		%name
Version: 	%version
Release: 	%mkrel %rel
Url: 		http://libburnia.pykix.org/
License: 	GPL
Group: 		System/Libraries
Source: 	http://libburnia-download.pykix.org/releases/%{name}-%{version}.tar.gz
BuildRequires:	doxygen
BuildRequires:	graphviz

%description
Libburn is an open-source library for reading, mastering and writing
optical discs.

%package -n	%{libname}
Group:		System/Libraries
Summary:	An open-source library for optical discs

%description -n %{libname}
An open-source library for reading, mastering and writing optical discs.

################

%package -n %{develname}
Group:          Development/C
Summary:        Header files for development with %name
Provides:       %{name}-devel = %{version}
Requires:       %{libname} = %{version}
Obsoletes:	%{_lib}burn6-devel

%description -n %{develname}
This package includes the header files for the %{name} package.

#################

%package -n cdrskin
Summary: Limited cdrecord compatibility wrapper for libburn
Group: Archiving/Cd burning

%description -n cdrskin
A limited cdrecord compatibility wrapper which allows to use some
libburn features from the command line.

%prep
%setup -q

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

# build documentation
doxygen doc/doxygen.conf

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %{libname}
%defattr(-,root,root)
%doc README AUTHORS COPYING COPYRIGHT
%_libdir/libburn.so.*

%files -n %{develname}
%defattr(-,root,root)
%_libdir/libburn.so
%_libdir/libburn.la
%_libdir/libburn.a
%_libdir/pkgconfig/*.pc
%_includedir/%name/

%files -n cdrskin
%defattr(-,root,root)
%doc cdrskin/README
%{_bindir}/cdrskin
%{_mandir}/man1/cdrskin.1.*

