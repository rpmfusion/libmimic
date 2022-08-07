Name:           libmimic
Version:        1.0.4
Release:        21%{?dist}
Summary:        Encoding/decoding library for Mimic V2.x
License:        LGPLv2+
URL:            http://farsight.sourceforge.net/
Source0:        http://downloads.sourceforge.net/farsight/%{name}-%{version}.tar.gz
BuildRequires:  doxygen glib2-devel gcc-c++

%description
libmimic is an open source video encoding/decoding library for Mimic V2.x-
encoded content (fourCC: ML20), which is the encoding used by MSN Messenger
for webcam conversations.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}, pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
%configure --disable-static
%make_build libmimic_la_LIBADD="-lglib-2.0 -lm"


%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%ldconfig_scriptlets


%files
%doc AUTHORS README
%license COPYING
%{_libdir}/*.so.*

%files devel
%doc doc/api/html
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libmimic.pc


%changelog
* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.0.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.0.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.0.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.0.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.0.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.0.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.0.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 27 2019 Nicolas Chauvet <kwizart@gmail.com> - 1.0.4-14
- Spec file clean-up

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.0.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.0.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.0.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 19 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep 01 2014 Sérgio Basto <sergio@serjux.com> - 1.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Mar 02 2014 Hans de Goede <j.w.r.degoede@gmail.com> - 1.0.4-7
- Stop using pre-built docs (rf3114)

* Sun Mar 03 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.0.4-6
- Mass rebuilt for Fedora 19 Features

* Wed Feb 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Nov  7 2009 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0.4-4
- Fix multilib conflict in -devel package (rf858)

* Fri Aug  7 2009 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0.4-3
- Actually link to glib-2.0 not the ancient glib (issue
  caused by the undefined-non-weak-symbol fix) (rf487)

* Thu Aug  6 2009 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0.4-2
- Fix undefined-non-weak-symbol in libmimic.so.0 (rf487)

* Sun Mar 29 2009 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0.4-1
- First version of the RPM Fusion package
