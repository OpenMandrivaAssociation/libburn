%define major 4
%define libname %mklibname burn %{major}
%define develname %mklibname burn -d
%define sdevellibname %mklibname -s -d burn

Summary:	Library for reading, mastering and writing optical discs
Name:		libburn
Version:	1.2.4
Release:	1
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
Obsoletes:	%{_lib}burn6-devel < 1.2.4
Provides:	burn-devel = %{version}-%{release}

%description -n %{develname}
This package includes the header files for the %{name} package.

%package -n cdrskin
Summary:	Limited cdrecord compatibility wrapper for libburn
Group:		Archiving/Cd burning

%description -n cdrskin
A limited cdrecord compatibility wrapper which allows to use some
libburn features from the command line.


%package -n %{sdevellibname}
Summary:	Static development files for %{name}
Group:		Development/C
Requires:	%{develname} = %{version}-%{release}
Provides:	burn-static-devel = %{version}-%{release}
Obsoletes:	%{_lib}burn-static-devel < 1.1.8-2

%description -n %{sdevellibname}
This package contains static libraries to develop applications that use
%{name}.


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
%{_libdir}/libburn.so.%{major}*

%files -n %{develname}
%doc README AUTHORS COPYRIGHT
%{_libdir}/libburn.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/%{name}

%files -n %sdevellibname
%{_libdir}/*.a

%files -n cdrskin
%doc cdrskin/README
%{_bindir}/cdrskin
%{_mandir}/man1/cdrskin.1.*


%changelog
* Mon Jul 30 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.2.4-1
+ Revision: 811451
- version update  1.2.4

* Sat Apr 07 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 1.2.2-1
+ Revision: 789762
- update to new version 1.2.2

* Thu Feb 02 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.2.0-2
+ Revision: 770643
- bump for 2011
- removed la files
- version update 1.2.0

* Fri Jan 20 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.1.8-2
+ Revision: 762937
- added static package
- removed la files
- removed old macroses and now package provides burn-devel

* Wed Nov 23 2011 Alexander Khrukin <akhrukin@mandriva.org> 1.1.8-1
+ Revision: 732826
- version update to 1.1.8

* Tue Oct 04 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.1.6-1
+ Revision: 702994
- update to new version 1.1.6

* Mon Aug 29 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.1.4-1
+ Revision: 697345
- update to new version 1.1.4
- corretc url for source

* Sat Sep 18 2010 Funda Wang <fwang@mandriva.org> 0.8.6-1mdv2011.0
+ Revision: 579314
- new version 0.8.6

* Sun Jul 11 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.8.4-1mdv2011.0
+ Revision: 550912
- update to new version 0.8.4

* Sat Apr 10 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.8.0-1mdv2010.1
+ Revision: 533560
- update to new version 0.8.0

* Sun Jan 24 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.7.6-1mdv2010.1
+ Revision: 495604
- update to new version 0.7.6

* Sat Nov 07 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.7.2-1mdv2010.1
+ Revision: 462502
- update to new version 0.7.2

* Fri Aug 28 2009 Frederik Himpe <fhimpe@mandriva.org> 0.7.0-1mdv2010.0
+ Revision: 422032
- update to new version 0.7.0

* Tue Jul 14 2009 Frederik Himpe <fhimpe@mandriva.org> 0.6.8-1mdv2010.0
+ Revision: 396040
- update to new version 0.6.8

* Sat Jun 06 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.6-1mdv2010.0
+ Revision: 383235
- update to new version 0.6.6

* Sat Feb 21 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.2-1mdv2009.1
+ Revision: 343629
- update to new version 0.6.2

* Tue Jan 13 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.0-1mdv2009.1
+ Revision: 328813
- fix doxygen call
- update to new version 0.6.0

* Mon Dec 08 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.8-1mdv2009.1
+ Revision: 311922
- update to new version 0.5.8

* Fri Nov 28 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.6-1mdv2009.1
+ Revision: 307473
- update to new version 0.5.6
- fix urls
- spec file clean

* Tue Oct 14 2008 Funda Wang <fwang@mandriva.org> 0.5.4-1mdv2009.1
+ Revision: 293511
- New version 0.5.4
- no need to provide libburn-5 now

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.4.6-2mdv2009.0
+ Revision: 267804
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue May 13 2008 Adam Williamson <awilliamson@mandriva.org> 0.4.6-1mdv2009.0
+ Revision: 206525
- new release 0.4.6

* Thu Apr 17 2008 Adam Williamson <awilliamson@mandriva.org> 0.4.4-1mdv2009.0
+ Revision: 195306
- symlink libburn-1.pc to libburn-5.pc (brasero expects the latter)
- new release 0.4.4

* Thu Feb 28 2008 Adam Williamson <awilliamson@mandriva.org> 0.4.2-1mdv2008.1
+ Revision: 176471
- new release 0.4.2

* Tue Jan 15 2008 Adam Williamson <awilliamson@mandriva.org> 0.4.0-1mdv2008.1
+ Revision: 152997
- move docs out of lib package
- spec clean
- new license policy
- new release 0.4.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Jul 31 2007 Adam Williamson <awilliamson@mandriva.org> 0.3.8-1mdv2008.0
+ Revision: 57132
- new release 0.3.8

* Sun Jul 01 2007 Adam Williamson <awilliamson@mandriva.org> 0.3.6-1mdv2008.0
+ Revision: 46846
- new release 0.3.6, new devel policy

