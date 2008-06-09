%define lib_name %mklibname %{name} %{version}
%define lib_name_devel %mklibname %{name} -d

Name:           yate
Version:        1.3.0
Release:        %mkrel 1
Epoch:          0
Summary:        Yet Another Telephony Engine
License:        GPL
Group:          Networking/Instant messaging
URL:            http://yate.null.ro/
Source0:        http://yate.null.ro/tarballs/yate1/yate-%{version}-1.tar.gz
# Converted from <http://yate.null.ro/favicon.ico>
Source1:        yate-16.png
Source2:        yate-32.png
Patch0:         yate-fhs.patch
Requires(post): rpm-helper
Requires(preun): rpm-helper
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  ImageMagick
BuildRequires:  alsa-lib-devel
BuildRequires:  coredumper-devel
BuildRequires:  gsm-devel
BuildRequires:  gtk+2-devel
BuildRequires:  mozilla-firefox-devel
BuildRequires:  mysql-devel
BuildRequires:  pq-devel
BuildRequires:  pri-devel
BuildRequires:  pwlib-devel
BuildRequires:  speex-devel
BuildRequires:  tonezone-devel
BuildRequires:  openh323-devel
BuildRequires:  postgresql-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Yate is a telephony engine designed to implement PBX and IVR solutions 
for small to large scale projects.

%package alsa
Summary:        ALSA sound driver for Yate
Group:          Networking/Instant messaging

%description alsa
Advanced Linux Sound Architecture audio driver for Yate. This is the 
recommended audio interface for using the client under Linux.

%package gsm
Summary:        GSM audio codec for Yate
Group:          Networking/Instant messaging

%description gsm
European GSM 06.10 audio codec for Yate. This is a low CPU usage codec 
that provides moderate compression and good voice quality.

%package h323
Summary:        H.323 protocol driver for Yate
Group:          Networking/Instant messaging

%description h323
Yate driver for the ITU-T H.323 VoIP protocol based on the OpenH323 
library.

%package isdn
Summary:        ISDN PRI card and protocol drivers for Yate
Group:          Networking/Instant messaging

%description isdn
Yate drivers for ISDN PRI cards supported by the Zaptel or Wanpipe 
kernel interfaces.

%package pgsql
Summary:        PostgreSQL database driver for Yate
Group:          Networking/Instant messaging
Provides:       yate-database

%description pgsql
This package allows Yate to connect to a PostgreSQL database server. 
All modules that support database access will be able to use 
PostgreSQL.

%package mysql
Summary:        MySQL database driver for Yate
Group:          Networking/Instant messaging
Provides:       yate-database

%description mysql
This package allows Yate to connect to a MySQL database server. All 
modules that support database access will be able to use MySQL.

%package gtk2
Summary:        Gtk2 client package for Yate
Group:          Networking/Instant messaging
Provides:       yate-client
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description gtk2
The yate-gtk2 package includes the files needed to use Yate as a VoIP 
client with a Gtk2 graphical interface.

%package mozilla
Summary:        Mozilla embedding in Yate
Group:          Networking/Instant messaging
Requires:       yate-gtk2 = %{epoch}:%{version}
Provides:       yate-browser

%description mozilla
This package adds a Mozilla widget that can be embedded in a Yate 
client window.

%package scripts
Summary:        External scripting package for Yate
Group:          Networking/Instant messaging
Requires:       %{name}

%description scripts
The yate-scripts package includes libraries for using external scripts 
with Yate.

%package -n %{lib_name}
Summary:        Library for Yate
Group:          System/Libraries

%description -n %{lib_name}
Library for Yate.

%package -n %{lib_name_devel}
Summary:        Development package for Yate
Group:          Development/C++
Requires:       %{lib_name} = %{epoch}:%{version}
Provides:       %{name}-devel = %{epoch}:%{version}
Provides:       lib%{name}-devel = %{epoch}:%{version}
Provides:       %{_lib}%{name}-devel = %{epoch}:%{version}
Obsoletes:	%mklibname -d %{name} 1.2.0

%description -n %{lib_name_devel}
This package includes the libraries and header files for Yate that can 
be used to build and install new modules.

%package all
Summary:        Metapackage for Yate
Group:          Networking/Instant messaging
Requires:       %{name} = %{epoch}:%{version}
Requires:       %{name}-alsa = %{epoch}:%{version}
Requires:       %{name}-gsm = %{epoch}:%{version}
Requires:       %{name}-h323 = %{epoch}:%{version}
Requires:       %{name}-isdn = %{epoch}:%{version}
Requires:       %{name}-mysql = %{epoch}:%{version}
Requires:       %{name}-pgsql = %{epoch}:%{version}
Requires:       %{name}-gtk2 = %{epoch}:%{version}
Requires:       %{name}-mozilla = %{epoch}:%{version}
Requires:       %{name}-scripts = %{epoch}:%{version}

%description all
Metapackage for Yate allowing to fetch and install all components at 
once. It contains no files, just dependencies to all other packages.

%prep
%setup -q -n %{name}
%patch0 -p1
# fix gtkmozembed detection
%{__perl} -pi -e 's/mozilla-gtkmozembed/firefox-gtkmozembed/g' configure.in
# fix openh323 detection
%{__perl} -pi -e 's|/lib/|/%{_lib}/|g' configure.in
# fix zaptel detection
%{__perl} -pi -e 's|linux/zaptel.h|zaptel/zaptel.h|g' configure.in modules/zapchan.cpp
# fix wanpipe detection
# XXX: there's still an error in the wanpipe headers
%{__perl} -pi -e 's|linux/(wanpipe.*\.h)|wanpipe/\1|g;' \
              -e 's|linux/sdla_aft_te1\.h|wanpipe/sdla_aft_te1\.h|g;' \
  configure.in modules/wpchan.cpp
# fix CFLAGS
%{__perl} -pi -e 's|^CFLAGS := (.*)|CFLAGS := %{optflags} \1|g;' \
              -e 's|^CXXFLAGS := (.*)|CXXFLAGS := %{optflags} \1|g;' \
              -e 's|^CPPFLAGS := (.*)|CPPFLAGS := %{optflags} \1|g;' \
  `%{_bindir}/find . -type f -name Makefile.in`
# fix caps and logdir
%{__perl} -pi -e 's|YATE|yate|g;' \
              -e 's|/var/log|%{_logdir}|g;' \
  yate.init
%{__autoconf}

%build
%{configure2_5x} --without-kdoc --without-wphwec --without-spandsp
%{__make}
%{__make} apidocs

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}

%{__mkdir_p} %{buildroot}%{_initrddir}
%{__cp} -a yate.init %{buildroot}%{_initrddir}/yate

%{__mkdir_p} %{buildroot}%{_logdir}/yate

%{__mkdir_p} %{buildroot}%{_sysconfdir}/logrotate.d
%{__cat} > %{buildroot}%{_sysconfdir}/logrotate.d/yate << EOF
%{_logdir}/yate {
    notifempty
    missingok
    rotate 7
    daily
    compress
    create 644 root root
    postrotate
         /sbin/service yate reload 2>/dev/null || true
    endscript
}
EOF

%{__rm} %{buildroot}%{_libdir}/menu/yate-gtk2.menu

%{__mkdir_p} %{buildroot}%{_datadir}/icons/hicolor/16x16/apps
%{__cp} -a %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}-gtk2.png
%{__mkdir_p} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
%{__cp} -a %{SOURCE2} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}-gtk2.png
%{__mkdir_p} %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
%{_bindir}/convert -resize 48x48 %{SOURCE2} %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}-gtk2.png
%{__mkdir_p} %{buildroot}%{_datadir}/pixmaps
%{__cp} -a %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/%{name}-gtk2.png

/bin/echo 'Icon=%{name}-gtk2' >> %{buildroot}%{_datadir}/applications/yate-gtk2.desktop
%{_bindir}/desktop-file-install --vendor ""             \
        --dir %{buildroot}%{_datadir}/applications \
        --add-category X-MandrivaLinux-Internet-InstantMessaging \
        --remove-category Application                   \
        %{buildroot}%{_datadir}/applications/yate-gtk2.desktop

# remove wrong location doc files
rm -fr %{buildroot}%{_datadir}/doc/%{name}-%{version}

%clean
%{__rm} -rf %{buildroot}

%post
%_post_service %{name}

%preun
%_preun_service %{name}

%if %mdkversion < 200900
%post -n %{lib_name} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{lib_name} -p /sbin/ldconfig
%endif

%post gtk2
%{update_desktop_database}
%update_icon_cache hicolor

%postun gtk2
%{update_desktop_database}
%update_icon_cache hicolor

%files
%defattr(-, root, root)
%doc ChangeLog COPYING README
%attr(0755,root,root) %{_bindir}/yate
%attr(0755,root,root) %{_initrddir}/yate
%dir %{_libdir}/yate
%dir %{_libdir}/yate/modules
%dir %{_sysconfdir}/yate
%{_libdir}/yate/modules/cdrbuild.yate
%{_libdir}/yate/modules/cdrfile.yate
%{_libdir}/yate/modules/regexroute.yate
%{_libdir}/yate/modules/regfile.yate
%{_libdir}/yate/modules/accfile.yate
%{_libdir}/yate/modules/register.yate
%{_libdir}/yate/modules/tonegen.yate
%{_libdir}/yate/modules/tonedetect.yate
%{_libdir}/yate/modules/wavefile.yate
%{_libdir}/yate/modules/conference.yate
%{_libdir}/yate/modules/moh.yate
%{_libdir}/yate/modules/callgen.yate
%{_libdir}/yate/modules/analyzer.yate
%{_libdir}/yate/modules/rmanager.yate
%{_libdir}/yate/modules/msgsniff.yate
%{_libdir}/yate/modules/pbx.yate
%{_libdir}/yate/modules/dbpbx.yate
%{_libdir}/yate/modules/pbxassist.yate
%{_libdir}/yate/modules/dumbchan.yate
%{_libdir}/yate/modules/callfork.yate
%{_libdir}/yate/modules/extmodule.yate
%{_libdir}/yate/modules/yradius.yate
%{_libdir}/yate/modules/ysipchan.yate
%{_libdir}/yate/modules/yrtpchan.yate
%{_libdir}/yate/modules/yiaxchan.yate
%{_libdir}/yate/modules/enumroute.yate
%{_libdir}/yate/modules/osschan.yate
%{_libdir}/yate/modules/ilbccodec.yate
%{_libdir}/yate/modules/speexcodec.yate
%{_libdir}/yate/modules/yjinglechan.yate
%{_libdir}/yate/modules/ystunchan.yate
%{_libdir}/yate/modules/park.yate
%{_libdir}/yate/modules/queues.yate
%{_libdir}/yate/modules/sipfeatures.yate
%dir %{_logdir}/yate
%{_mandir}/man8/yate.8*
%config(noreplace) %{_sysconfdir}/logrotate.d/yate
%config(noreplace) %{_sysconfdir}/yate/accfile.conf
%config(noreplace) %{_sysconfdir}/yate/cdrbuild.conf
%config(noreplace) %{_sysconfdir}/yate/cdrfile.conf
%config(noreplace) %{_sysconfdir}/yate/dbpbx.conf
%config(noreplace) %{_sysconfdir}/yate/dsoundchan.conf
%config(noreplace) %{_sysconfdir}/yate/enumroute.conf
%config(noreplace) %{_sysconfdir}/yate/extmodule.conf
%config(noreplace) %{_sysconfdir}/yate/moh.conf
%config(noreplace) %{_sysconfdir}/yate/pbxassist.conf
%config(noreplace) %{_sysconfdir}/yate/regexroute.conf
%config(noreplace) %{_sysconfdir}/yate/regfile.conf
%config(noreplace) %{_sysconfdir}/yate/register.conf
%config(noreplace) %{_sysconfdir}/yate/rmanager.conf
%config(noreplace) %{_sysconfdir}/yate/yate.conf
%config(noreplace) %{_sysconfdir}/yate/yiaxchan.conf
%config(noreplace) %{_sysconfdir}/yate/yjinglechan.conf
%config(noreplace) %{_sysconfdir}/yate/yradius.conf
%config(noreplace) %{_sysconfdir}/yate/yrtpchan.conf
%config(noreplace) %{_sysconfdir}/yate/ysipchan.conf
%config(noreplace) %{_sysconfdir}/yate/ystunchan.conf
%config(noreplace) %{_sysconfdir}/yate/sipfeatures.conf

%files alsa
%defattr(-, root, root)
%{_libdir}/yate/modules/alsachan.yate

%files gsm
%defattr(-, root, root)
%{_libdir}/yate/modules/gsmcodec.yate

%files h323
%defattr(-, root, root)
%{_libdir}/yate/modules/h323chan.yate
%config(noreplace) %{_sysconfdir}/yate/h323chan.conf

%files isdn
%defattr(-, root, root)
%if 0
%{_libdir}/yate/modules/wpchan.yate
%endif
%{_libdir}/yate/modules/zapchan.yate
%config(noreplace) %{_sysconfdir}/yate/wpchan.conf
%config(noreplace) %{_sysconfdir}/yate/zapchan.conf

%files mysql
%defattr(-, root, root)
%{_libdir}/yate/modules/mysqldb.yate
%config(noreplace) %{_sysconfdir}/yate/mysqldb.conf

%files pgsql
%defattr(-, root, root)
%{_libdir}/yate/modules/pgsqldb.yate
%config(noreplace) %{_sysconfdir}/yate/pgsqldb.conf

%files gtk2
%defattr(-, root, root)
%{_bindir}/yate-gtk2
%{_datadir}/applications/yate-gtk2.desktop
%dir %{_datadir}/yate/skin
%{_datadir}/yate/skin/*
%dir %{_datadir}/yate/help
%{_datadir}/yate/help/*
%config(noreplace) %{_sysconfdir}/yate/yate-gtk2.conf
%config(noreplace) %{_sysconfdir}/yate/providers.conf
%{_datadir}/icons/hicolor/16x16/apps/%{name}-gtk2.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}-gtk2.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}-gtk2.png
%{_datadir}/pixmaps/%{name}-gtk2.png

%files mozilla
%defattr(-, root, root)
%dir %{_libdir}/yate/modules/gtk2
%{_libdir}/yate/modules/gtk2/*

%files scripts
%defattr(-, root, root)
%dir %{_datadir}/yate/scripts
%{_datadir}/yate/scripts/*.*

%files -n %{lib_name}
%defattr(-, root, root)
%{_libdir}/lib*.so.*

%files -n %{lib_name_devel}
%defattr(-, root, root)
%doc docs/*.html docs/api
%{_bindir}/yate-config
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/yate.pc
%{_mandir}/*/yate-config.*

%files all
%defattr(-,root,root)
