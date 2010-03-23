%define lib_name %mklibname %{name} %{version}
%define lib_name_devel %mklibname %{name} -d

Name:           yate
Version:        2.2
Release:        %mkrel 1
Epoch:          0
Summary:        Yet Another Telephony Engine
License:        GPLv2+
Group:          Networking/Instant messaging
URL:            http://yate.null.ro/
Source0:        http://yate.null.ro/tarballs/yate2/yate2.tar.gz
# Converted from <http://yate.null.ro/favicon.ico>
Source1:        yate-16.png
Source2:        yate-32.png
Patch0:         yate-fhs.patch
Patch1:         yate-link-cxx.patch
Patch2:         yate-linking-order.patch

Patch3:         yate-fix_format_string.patch 
Patch4:         yate-fix_qt_detection.diff

Requires(post): rpm-helper
Requires(preun): rpm-helper
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  imagemagick
BuildRequires:  alsa-lib-devel
BuildRequires:  coredumper-devel
BuildRequires:  gsm-devel
BuildRequires:  qt4-devel
BuildRequires:  xulrunner-devel
BuildRequires:  mysql-devel
BuildRequires:  openssl-devel
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

%package openssl
Summary:        OpenSSL based encryption support for Yate
Group:          Networking/Instant messaging
Provides:       %{name}-ssl = %{epoch}:%{version}-%{release}
Provides:       %{name}-crypto = %{epoch}:%{version}-%{release}

%description openssl
This package provides SSL/TLS encrypted communication support for Yate as
well as cryptographic routines used for other purposes.

%package pgsql
Summary:        PostgreSQL database driver for Yate
Group:          Networking/Instant messaging
Provides:       yate-database = %{epoch}:%{version}-%{release}

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

%package client-common
Summary:        Common files for all Yate clients
Group:          Networking/Instant messaging

%description client-common
This package includes the common files needed to use Yate as a VoIP client.

%package qt4
Summary:        Qt-4 client package for Yate
Group:          Networking/Instant messaging
Provides:       %{name}-client = %{epoch}:%{version}-%{release}
Requires:       %{name}-client-common = %{epoch}:%{version}-%{release}

%description qt4
The yate-qt4 package includes the files needed to use Yate as a VoIP client
with a Qt version 4 graphical interface.

%package scripts
Summary:        External scripting package for Yate
Group:          Networking/Instant messaging
Requires:       %{name} = %{epoch}:%{version}-%{release}

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
Requires:       %{lib_name} = %{epoch}:%{version}-%{release}
Provides:       %{name}-devel = %{epoch}:%{version}-%{release}
Provides:       lib%{name}-devel = %{epoch}:%{version}-%{release}
Provides:       %{_lib}%{name}-devel = %{epoch}:%{version}-%{release}
Obsoletes:	%mklibname -d %{name} 1.2.0

%description -n %{lib_name_devel}
This package includes the libraries and header files for Yate that can 
be used to build and install new modules.

%package all
Summary:        Metapackage for Yate
Group:          Networking/Instant messaging
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-alsa = %{epoch}:%{version}-%{release}
Requires:       %{name}-gsm = %{epoch}:%{version}-%{release}
Requires:       %{name}-h323 = %{epoch}:%{version}-%{release}
Requires:       %{name}-isdn = %{epoch}:%{version}-%{release}
Requires:       %{name}-openssl = %{epoch}:%{version}-%{release}
Requires:       %{name}-mysql = %{epoch}:%{version}-%{release}
Requires:       %{name}-pgsql = %{epoch}:%{version}-%{release}
Requires:       %{name}-qt4 = %{epoch}:%{version}-%{release}
Requires:       %{name}-scripts = %{epoch}:%{version}-%{release}

%description all
Metapackage for Yate allowing to fetch and install all components at 
once. It contains no files, just dependencies to all other packages.

%prep
%setup -q -n %{name}
#%%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p0
%patch4 -p0

# fix openh323 detection
%{__perl} -pi -e 's|/lib/|/%{_lib}/|g' configure.in
# fix CFLAGS
%{__perl} -pi -e 's|^CFLAGS := (.*)|CFLAGS := %{optflags} \1|g;' \
              -e 's|^CXXFLAGS := (.*)|CXXFLAGS := %{optflags} \1|g;' \
              -e 's|^CPPFLAGS := (.*)|CPPFLAGS := %{optflags} \1|g;' \
  `%{_bindir}/find . -type f -name Makefile.in`
# fix caps and logdir
%{__perl} -pi -e 's|YATE|yate|g;' \
              -e 's|/var/log|%{_logdir}|g;' \
  packing/yate.init

%build
#export CXXFLAGS="%{optflags} `pkg-config --cflags QtCore QtGui QtXml QtNetwork`"
#export LDFLAGS="-lpthread `pkg-config --libs QtCore QtGui QtXml QtNetwork`"
./autogen.sh
%{configure2_5x} --with-archlib=%{_lib}
%{__make} 
%{__make} apidocs-everything 

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}

%{__mkdir_p} %{buildroot}%{_initrddir}
%{__cp} -a packing/yate.init %{buildroot}%{_initrddir}/yate

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

%{_bindir}/find %{buildroot} -type f -name '*.menu' | %{_bindir}/xargs -t %{__rm}
%{__mkdir_p} %{buildroot}%{_datadir}/icons/hicolor/16x16/apps
%{__cp} -a %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}-qt4.png
%{__mkdir_p} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
%{__cp} -a %{SOURCE2} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}-qt4.png
%{__mkdir_p} %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
%{_bindir}/convert -resize 48x48 %{SOURCE2} %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}-qt4.png
%{__mkdir_p} %{buildroot}%{_datadir}/pixmaps
%{__cp} -a %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/%{name}-qt4.png

mkdir -p %{buildroot}%{_datadir}/applications/
/bin/echo 'Icon=%{name}-qt4' >> %{buildroot}%{_datadir}/applications/yate-qt4.desktop
%{_bindir}/desktop-file-install --vendor ""             \
        --dir %{buildroot}%{_datadir}/applications \
        --add-category X-MandrivaLinux-Internet-InstantMessaging \
        --remove-category Application                   \
        %{buildroot}%{_datadir}/applications/yate-qt4.desktop

# fix wrong location doc files
%{__rm} -rf __doc
%{__mkdir_p} __doc
mv %{buildroot}%{_datadir}/doc/%{name}*/* __doc/
rm -r __doc/api __doc/*.html

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

%post qt4
%{update_desktop_database}
%update_icon_cache hicolor

%postun qt4
%{update_desktop_database}
%update_icon_cache hicolor

%files
%defattr(-, root, root)
%doc __doc/*
%attr(0755,root,root) %{_bindir}/yate
%attr(0755,root,root) %{_initrddir}/yate
%dir %{_libdir}/yate
%dir %{_libdir}/yate/client
%dir %{_libdir}/yate/server
%dir %{_sysconfdir}/yate
%{_libdir}/yate/analyzer.yate
%{_libdir}/yate/callfork.yate
%{_libdir}/yate/callgen.yate
%{_libdir}/yate/cdrbuild.yate
%{_libdir}/yate/cdrfile.yate
%{_libdir}/yate/client/osschan.yate
%{_libdir}/yate/conference.yate
%{_libdir}/yate/dumbchan.yate
%{_libdir}/yate/enumroute.yate
%{_libdir}/yate/extmodule.yate
%{_libdir}/yate/ilbccodec.yate
%{_libdir}/yate/moh.yate
%{_libdir}/yate/msgsniff.yate
%{_libdir}/yate/mux.yate
%{_libdir}/yate/pbx.yate
%{_libdir}/yate/regexroute.yate
%{_libdir}/yate/rmanager.yate
%{_libdir}/yate/server/accfile.yate
%{_libdir}/yate/server/analog.yate
%{_libdir}/yate/server/analogdetect.yate
%{_libdir}/yate/server/clustering.yate
%{_libdir}/yate/server/dbpbx.yate
%{_libdir}/yate/server/heartbeat.yate
%{_libdir}/yate/server/lateroute.yate
%{_libdir}/yate/server/mgcpca.yate
%{_libdir}/yate/server/mgcpgw.yate
%{_libdir}/yate/server/mrcpspeech.yate
%{_libdir}/yate/server/park.yate
%{_libdir}/yate/server/pbxassist.yate
%{_libdir}/yate/server/queues.yate
%{_libdir}/yate/server/regfile.yate
%{_libdir}/yate/server/register.yate
%{_libdir}/yate/server/sipfeatures.yate
%{_libdir}/yate/server/yradius.yate
%{_libdir}/yate/server/ysigchan.yate
%{_libdir}/yate/speexcodec.yate
%{_libdir}/yate/tonedetect.yate
%{_libdir}/yate/tonegen.yate
%{_libdir}/yate/wavefile.yate
%{_libdir}/yate/yiaxchan.yate
%{_libdir}/yate/yjinglechan.yate
%{_libdir}/yate/yrtpchan.yate
%{_libdir}/yate/ysipchan.yate
%{_libdir}/yate/ystunchan.yate
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
%config(noreplace) %{_sysconfdir}/yate/analog.conf
%config(noreplace) %{_sysconfdir}/yate/clustering.conf
%config(noreplace) %{_sysconfdir}/yate/heartbeat.conf
%config(noreplace) %{_sysconfdir}/yate/lateroute.conf
%config(noreplace) %{_sysconfdir}/yate/mgcpca.conf
%config(noreplace) %{_sysconfdir}/yate/mgcpgw.conf
%config(noreplace) %{_sysconfdir}/yate/mux.conf
%config(noreplace) %{_sysconfdir}/yate/queues.conf
%config(noreplace) %{_sysconfdir}/yate/ysigchan.conf

%files alsa
%defattr(-, root, root)
%{_libdir}/yate/client/alsachan.yate

%files gsm
%defattr(-, root, root)
%{_libdir}/yate/gsmcodec.yate

%files h323
%defattr(-, root, root)
%{_libdir}/yate/h323chan.yate
%config(noreplace) %{_sysconfdir}/yate/h323chan.conf

%files isdn
%defattr(-, root, root)
%if 0
%{_libdir}/yate/server/wpchan.yate
%endif
#%{_libdir}/yate/server/zapcard.yate
#%{_libdir}/yate/zapcard.yate
%config(noreplace) %{_sysconfdir}/yate/wpcard.conf
%config(noreplace) %{_sysconfdir}/yate/zapcard.conf

%files openssl
%defattr(-, root, root)
%{_libdir}/yate/openssl.yate

%files mysql
%defattr(-, root, root)
%{_libdir}/yate/server/mysqldb.yate
%config(noreplace) %{_sysconfdir}/yate/mysqldb.conf

%files pgsql
%defattr(-, root, root)
%{_libdir}/yate/server/pgsqldb.yate
%config(noreplace) %{_sysconfdir}/yate/pgsqldb.conf

%files client-common
%defattr(-, root, root)
%{_datadir}/pixmaps/null_team-*.png
%dir %{_datadir}/yate/skins
%{_datadir}/yate/skins/*
%dir %{_datadir}/yate/sounds
%{_datadir}/yate/sounds/*
%dir %{_datadir}/yate/help
%{_datadir}/yate/help/*
%config(noreplace) %{_sysconfdir}/yate/providers.conf

%files qt4
%defattr(-, root, root)
%{_bindir}/yate-qt4
%{_datadir}/applications/yate-qt4.desktop
%config(noreplace) %{_sysconfdir}/yate/yate-qt4.conf
%{_datadir}/icons/hicolor/16x16/apps/%{name}-qt4.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}-qt4.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}-qt4.png
%{_datadir}/pixmaps/%{name}-qt4.png

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
