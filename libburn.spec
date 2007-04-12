%define name    libburn
%define version 0.2.6.3
%define rel 1

%define major 	6
%define lib_name %mklibname burn %major

Summary: 	Library for reading, mastering and writing optical discs
Name: 		%name
Version: 	%version
Release: 	%mkrel %rel
Url: 		http://libburnia.pykix.org/
License: 	GPL
Group: 		System/Libraries
Source: 	http://libburnia-download.pykix.org/releases/%{name}-%{version}.tar.bz2
Buildroot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: doxygen
BuildRequires: graphviz

%description
Libburn is an open-source library for reading, mastering and writing
optical discs. For now this means only CD-R and CD-RW.

%package -n	%{lib_name}
Group:		System/Libraries
Summary:	An open-source library for optical discs

%description -n %{lib_name}
An open-source library for reading, mastering and writing optical discs.

################

%package -n %{lib_name}-devel
Group:          Development/C
Summary:        Header files for development with %name
Provides:       %{name}-devel = %{version}
Requires:       %{lib_name} = %{version}

%description -n %{lib_name}-devel
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

%post -n %{lib_name} -p /sbin/ldconfig
%postun -n %{lib_name} -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %{lib_name}
%defattr(-,root,root)
%doc README AUTHORS COPYING COPYRIGHT
%_libdir/libburn.so.*

%files -n %{lib_name}-devel
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


