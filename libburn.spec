%define major 4
%define libname %mklibname burn %{major}
%define develname %mklibname burn -d

Summary:	Library for reading, mastering and writing optical discs
Name:		libburn
Version:	1.1.8
Release:	%mkrel 2
License:	GPLv2+
Group:		System/Libraries
URL:		http://libburnia-project.org/
Source0:	http://files.libburnia-project.org/releases/%{name}-%{version}.tar.gz
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

%package -n %{develname}
Summary:	Header files for development with %{name}
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	%{_lib}burn6-devel
Provides:	burn-devel = %{version}-%{release}

%description -n %{develname}
This package includes the header files for the %{name} package.

%package -n cdrskin
Summary:	Limited cdrecord compatibility wrapper for libburn
Group:		Archiving/Cd burning

%description -n cdrskin
A limited cdrecord compatibility wrapper which allows to use some
libburn features from the command line.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

# build documentation
pushd doc
doxygen -u doxygen.conf
doxygen doxygen.conf
popd

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libburn.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc README AUTHORS COPYRIGHT
%{_libdir}/libburn.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/%{name}

%files -n cdrskin
%defattr(-,root,root)
%doc cdrskin/README
%{_bindir}/cdrskin
%{_mandir}/man1/cdrskin.1.*
