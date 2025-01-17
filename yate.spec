%define major 4
%define lib_name %mklibname %{name} %{major}
%define lib_name_devel %mklibname %{name} -d
%define uprel	2

Name:           yate
Version:        4.2.0
Release:        2
Summary:        Yet Another Telephony Engine
License:        GPLv2+
Group:          Networking/Instant messaging
URL:            https://yate.null.ro/
Source0:        http://yate.null.ro/tarballs/yate%{major}/%{name}-%{version}-%{uprel}.tar.gz
# Converted from <http://yate.null.ro/favicon.ico>
Source1:        yate-16.png
Source2:        yate-32.png
Patch0:		yate-4.1.0-mdv-dont_break_cflags.patch

Requires(post): rpm-helper
Requires(preun): rpm-helper
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  imagemagick
BuildRequires:  pkgconfig(alsa)
BuildRequires:  coredumper-devel
BuildRequires:  gsm-devel
BuildRequires:  qt4-devel
BuildRequires:  xulrunner-devel
BuildRequires:  mysql-devel
BuildRequires:  openssl-devel
BuildRequires:  pq-devel
BuildRequires:  pri-devel
#BuildRequires:  pkgconfig(ptlib)
BuildRequires:	pkgconfig(spandsp)
BuildRequires:  speex-devel
BuildRequires:  tonezone-devel
#BuildRequires:  pkgconfig(opal)
BuildRequires:  postgresql-devel

%description
Yate is a telephony engine designed to implement PBX and IVR solutions 
for small to large scale projects.

%files
%dir %{_defaultdocdir}/%{name}
%doc %{_defaultdocdir}/%{name}/README
%doc %{_defaultdocdir}/%{name}/COPYING
%doc %{_defaultdocdir}/%{name}/ChangeLog
%{_bindir}/yate
%{_mandir}/*/yate.*
%{_initrddir}/yate
%dir %{_datadir}/yate/data
%{_datadir}/yate/data/*
%dir %{_libdir}/yate
%dir %{_libdir}/yate/client
%dir %{_libdir}/yate/jabber
%dir %{_libdir}/yate/server
%dir %{_libdir}/yate/sig
%dir %{_libdir}/yate/sip
%{_libdir}/yate/cdrbuild.yate
%{_libdir}/yate/cdrfile.yate
%{_libdir}/yate/regexroute.yate
%{_libdir}/yate/javascript.yate
%{_libdir}/yate/gvoice.yate
%{_libdir}/yate/isaccodec.yate
%{_libdir}/yate/server/regfile.yate
%{_libdir}/yate/server/accfile.yate
%{_libdir}/yate/server/register.yate
%{_libdir}/yate/tonegen.yate
%{_libdir}/yate/tonedetect.yate
%{_libdir}/yate/wavefile.yate
%{_libdir}/yate/conference.yate
%{_libdir}/yate/moh.yate
%{_libdir}/yate/callgen.yate
%{_libdir}/yate/analyzer.yate
%{_libdir}/yate/rmanager.yate
%{_libdir}/yate/msgsniff.yate
%{_libdir}/yate/mux.yate
%{_libdir}/yate/pbx.yate
%{_libdir}/yate/dumbchan.yate
%{_libdir}/yate/callfork.yate
%{_libdir}/yate/extmodule.yate
%{_libdir}/yate/filetransfer.yate
%{_libdir}/yate/ysipchan.yate
%{_libdir}/yate/yrtpchan.yate
%{_libdir}/yate/ystunchan.yate
%{_libdir}/yate/ysockschan.yate
%{_libdir}/yate/yiaxchan.yate
%{_libdir}/yate/yjinglechan.yate
%{_libdir}/yate/enumroute.yate
%{_libdir}/yate/faxchan.yate
%{_libdir}/yate/ilbcwebrtc.yate
%{_libdir}/yate/ilbccodec.yate
%{_libdir}/yate/server/dbwave.yate
%{_libdir}/yate/server/dbpbx.yate
%{_libdir}/yate/server/pbxassist.yate
%{_libdir}/yate/server/park.yate
%{_libdir}/yate/server/queues.yate
%{_libdir}/yate/server/lateroute.yate
%{_libdir}/yate/server/callcounters.yate
%{_libdir}/yate/server/yradius.yate
%{_libdir}/yate/server/sipfeatures.yate
%{_libdir}/yate/server/queuesnotify.yate
%{_libdir}/yate/server/heartbeat.yate
%{_libdir}/yate/server/clustering.yate
%{_libdir}/yate/server/mgcpca.yate
%{_libdir}/yate/server/mgcpgw.yate
%{_libdir}/yate/server/mrcpspeech.yate
%{_libdir}/yate/server/ysigchan.yate
%{_libdir}/yate/server/ciscosm.yate
%{_libdir}/yate/server/sigtransport.yate
%{_libdir}/yate/server/analog.yate
%{_libdir}/yate/server/analogdetect.yate
%{_libdir}/yate/server/users.yate
%{_libdir}/yate/server/presence.yate
%{_libdir}/yate/server/subscription.yate
%{_libdir}/yate/server/cpuload.yate
%{_libdir}/yate/server/ccongestion.yate
%{_libdir}/yate/server/monitoring.yate
%{_libdir}/yate/server/ysnmpagent.yate
%{_libdir}/yate/server/cache.yate
%{_libdir}/yate/server/eventlogs.yate
%{_libdir}/yate/client/osschan.yate
%{_libdir}/yate/client/jabberclient.yate
%{_libdir}/yate/jabber/jabberserver.yate
%{_libdir}/yate/jabber/jbfeatures.yate
%{_libdir}/yate/sig/isupmangler.yate
%{_libdir}/yate/sig/ss7_lnp_ansi.yate
%{_libdir}/yate/sig/camel_map.yate
%{_libdir}/yate/sip/sip_cnam_lnp.yate
%dir %{_sysconfdir}/yate
%config(noreplace) %{_sysconfdir}/yate/accfile.conf
%config(noreplace) %{_sysconfdir}/yate/cdrbuild.conf
%config(noreplace) %{_sysconfdir}/yate/cdrfile.conf
%config(noreplace) %{_sysconfdir}/yate/callcounters.conf
%config(noreplace) %{_sysconfdir}/yate/dbpbx.conf
%config(noreplace) %{_sysconfdir}/yate/dsoundchan.conf
%config(noreplace) %{_sysconfdir}/yate/enumroute.conf
%config(noreplace) %{_sysconfdir}/yate/sipfeatures.conf
%config(noreplace) %{_sysconfdir}/yate/callfork.conf
%config(noreplace) %{_sysconfdir}/yate/extmodule.conf
%config(noreplace) %{_sysconfdir}/yate/filetransfer.conf
%config(noreplace) %{_sysconfdir}/yate/moh.conf
%config(noreplace) %{_sysconfdir}/yate/mux.conf
%config(noreplace) %{_sysconfdir}/yate/pbxassist.conf
%config(noreplace) %{_sysconfdir}/yate/queues.conf
%config(noreplace) %{_sysconfdir}/yate/queuesnotify.conf
%config(noreplace) %{_sysconfdir}/yate/lateroute.conf
%config(noreplace) %{_sysconfdir}/yate/regexroute.conf
%config(noreplace) %{_sysconfdir}/yate/javascript.conf
%config(noreplace) %{_sysconfdir}/yate/regfile.conf
%config(noreplace) %{_sysconfdir}/yate/register.conf
%config(noreplace) %{_sysconfdir}/yate/tonegen.conf
%config(noreplace) %{_sysconfdir}/yate/rmanager.conf
%config(noreplace) %{_sysconfdir}/yate/yate.conf
%config(noreplace) %{_sysconfdir}/yate/yiaxchan.conf
%config(noreplace) %{_sysconfdir}/yate/yradius.conf
%config(noreplace) %{_sysconfdir}/yate/yrtpchan.conf
%config(noreplace) %{_sysconfdir}/yate/ysockschan.conf
%config(noreplace) %{_sysconfdir}/yate/ystunchan.conf
%config(noreplace) %{_sysconfdir}/yate/ysipchan.conf
%config(noreplace) %{_sysconfdir}/yate/yjinglechan.conf
%config(noreplace) %{_sysconfdir}/yate/heartbeat.conf
%config(noreplace) %{_sysconfdir}/yate/clustering.conf
%config(noreplace) %{_sysconfdir}/yate/mgcpca.conf
%config(noreplace) %{_sysconfdir}/yate/mgcpgw.conf
%config(noreplace) %{_sysconfdir}/yate/analog.conf
%config(noreplace) %{_sysconfdir}/yate/ysigchan.conf
%config(noreplace) %{_sysconfdir}/yate/ciscosm.conf
%config(noreplace) %{_sysconfdir}/yate/sigtransport.conf
%config(noreplace) %{_sysconfdir}/yate/cpuload.conf
%config(noreplace) %{_sysconfdir}/yate/ccongestion.conf
%config(noreplace) %{_sysconfdir}/yate/monitoring.conf
%config(noreplace) %{_sysconfdir}/yate/ysnmpagent.conf
%config(noreplace) %{_sysconfdir}/yate/cache.conf
%config(noreplace) %{_sysconfdir}/yate/users.conf
%config(noreplace) %{_sysconfdir}/yate/presence.conf
%config(noreplace) %{_sysconfdir}/yate/subscription.conf
%config(noreplace) %{_sysconfdir}/yate/jabberclient.conf
%config(noreplace) %{_sysconfdir}/yate/jabberserver.conf
%config(noreplace) %{_sysconfdir}/yate/jbfeatures.conf
%config(noreplace) %{_sysconfdir}/yate/isupmangler.conf
%config(noreplace) %{_sysconfdir}/yate/ss7_lnp_ansi.conf
%config(noreplace) %{_sysconfdir}/yate/camel_map.conf
%config(noreplace) %{_sysconfdir}/yate/sip_cnam_lnp.conf
%config(noreplace) %{_sysconfdir}/yate/gvoice.conf
%config(noreplace) %{_sysconfdir}/yate/eventlogs.conf
%config(noreplace) %{_sysconfdir}/yate/lksctp.conf

%config %{_sysconfdir}/logrotate.d/yate

%post
%_post_service %{name}

%preun
%_preun_service %{name}

#------------------------------------------------------------------------------

%package alsa
Summary:        ALSA sound driver for Yate
Group:          Networking/Instant messaging

%description alsa
Advanced Linux Sound Architecture audio driver for Yate. This is the 
recommended audio interface for using the client under Linux.

%files alsa
%{_libdir}/yate/client/alsachan.yate

#------------------------------------------------------------------------------

%package gsm
Summary:        GSM audio codec for Yate
Group:          Networking/Instant messaging

%description gsm
European GSM 06.10 audio codec for Yate. This is a low CPU usage codec 
that provides moderate compression and good voice quality.

%files gsm
%{_libdir}/yate/gsmcodec.yate

#------------------------------------------------------------------------------

%package speex
Summary:        Speex audio codec for Yate
Group:          Networking/Instant messaging

%description speex
Speex audio codec for Yate. Speex is based on CELP  and is designed to
compress voice at bitrates ranging from 2 to 44 kbps.

%files speex
%{_libdir}/yate/speexcodec.yate

#------------------------------------------------------------------------------

%package h323
Summary:        H.323 protocol driver for Yate
Group:          Networking/Instant messaging

%description h323
Yate driver for the ITU-T H.323 VoIP protocol based on the OpenH323 
library.

%files h323
#%{_libdir}/yate/h323chan.yate
%config(noreplace) %{_sysconfdir}/yate/h323chan.conf

#------------------------------------------------------------------------------

%package isdn
Summary:        ISDN PRI card and protocol drivers for Yate
Group:          Networking/Instant messaging

%description isdn
Yate drivers for ISDN PRI cards supported by the Zaptel or Wanpipe 
kernel interfaces.

%files isdn
#%{_libdir}/yate/server/wpcard.yate
%config(noreplace) %{_sysconfdir}/yate/wpcard.conf
%{_libdir}/yate/server/zapcard.yate
%config(noreplace) %{_sysconfdir}/yate/zapcard.conf
#%{_libdir}/yate/server/tdmcard.yate
%config(noreplace) %{_sysconfdir}/yate/tdmcard.conf

#------------------------------------------------------------------------------

#%package lksctp
#Summary:        Linux Kernel based SCTP support for Yate
#Group:          Networking/Instant messaging
#Provides:       %{name}-sctp = %{EVRD}
#
#%description lksctp
#This package provides SCTP sockets support for Yate based on the Linux Kernel
#implementation. These are needed for standard SIGTRAN interfaces.
#
#%files lksctp
#%{_libdir}/yate/server/lksctp.yate

#------------------------------------------------------------------------------

%package openssl
Summary:        OpenSSL based encryption support for Yate
Group:          Networking/Instant messaging
Provides:       %{name}-ssl = %{EVRD}
Provides:       %{name}-crypto = %{EVRD}

%description openssl
This package provides SSL/TLS encrypted communication support for Yate as
well as cryptographic routines used for other purposes.

%files openssl
%{_libdir}/yate/openssl.yate
%config(noreplace) %{_sysconfdir}/yate/openssl.conf

#------------------------------------------------------------------------------

%package zlib
Summary:        Zlib compression support for Yate
Group:          Networking/Instant messaging
Provides:       %{name}-compression = %{EVRD}

%description zlib
This package provides Zlib data compression for Yate.

%files zlib
%{_libdir}/yate/zlibcompress.yate
%config(noreplace) %{_sysconfdir}/yate/zlibcompress.conf

#------------------------------------------------------------------------------

%package pgsql
Summary:        PostgreSQL database driver for Yate
Group:          Networking/Instant messaging
Provides:       %{name}-database = %{EVRD}

%description pgsql
This package allows Yate to connect to a PostgreSQL database server. 
All modules that support database access will be able to use 
PostgreSQL.

%files pgsql
%{_libdir}/yate/server/pgsqldb.yate
%config(noreplace) %{_sysconfdir}/yate/pgsqldb.conf

#------------------------------------------------------------------------------

%package mysql
Summary:        MySQL database driver for Yate
Group:          Networking/Instant messaging
Provides:       %{name}-database = %{EVRD}

%description mysql
This package allows Yate to connect to a MySQL database server. All 
modules that support database access will be able to use MySQL.

%files mysql
%{_libdir}/yate/server/mysqldb.yate
%config(noreplace) %{_sysconfdir}/yate/mysqldb.conf

#------------------------------------------------------------------------------

%package client-common
Summary:        Common files for all Yate clients
Group:          Networking/Instant messaging

%description client-common
This package includes the common files needed to use Yate as a VoIP client.

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

#------------------------------------------------------------------------------

%package qt4
Summary:        Qt-4 client package for Yate
Group:          Networking/Instant messaging
Provides:       %{name}-client = %{EVRD}
Requires:       %{name}-client-common = %{EVRD}

%description qt4
The yate-qt4 package includes the files needed to use Yate as a VoIP client
with a Qt version 4 graphical interface.

%files qt4
%defattr(-, root, root)
%{_bindir}/yate-qt4
%{_libdir}/libyateqt4.so.*
%{_libdir}/yate/qt4/*.yate
%{_datadir}/applications/yate-qt4.desktop
%config(noreplace) %{_sysconfdir}/yate/yate-qt4.conf

#------------------------------------------------------------------------------

%package scripts
Summary:        External scripting package for Yate
Group:          Networking/Instant messaging
Requires:       %{name} = %{EVRD}

%description scripts
The yate-scripts package includes libraries for using external scripts 
with Yate.

%files scripts
%dir %{_datadir}/yate/scripts
%{_datadir}/yate/scripts/*.*

#------------------------------------------------------------------------------

%package -n %{lib_name}
Summary:        Library for Yate
Group:          System/Libraries

%description -n %{lib_name}
Library for Yate.

%files -n %{lib_name}
%{_libdir}/libyate.so.*
%{_libdir}/libyatescript.so.*
%{_libdir}/libyatejabber.so.*
%{_libdir}/libyatesig.so.*
%{_libdir}/libyatemgcp.so.*

#------------------------------------------------------------------------------

%package -n %{lib_name_devel}
Summary:        Development package for Yate
Group:          Development/C++
Requires:       %{lib_name} = %{EVRD}
Provides:       %{name}-devel = %{EVRD}
Provides:       lib%{name}-devel = %{EVRD}
Obsoletes:	%mklibname -d %{name} 1.2.0

%description -n %{lib_name_devel}
This package includes the libraries and header files for Yate that can 
be used to build and install new modules.

%files -n %{lib_name_devel}
%defattr(-, root, root)
%doc %{_datadir}/doc/%{lib_name_devel}/*.html
%doc %{_datadir}/doc/%{lib_name_devel}/api/*
/usr/include/*
%{_libdir}/lib*.so
%{_bindir}/yate-config
%{_mandir}/*/yate-config.*
%{_libdir}/pkgconfig/yate.pc

#------------------------------------------------------------------------------

%package all
Summary:        Metapackage for Yate
Group:          Networking/Instant messaging
Requires:       %{name} = %{EVRD}
Requires:       %{name}-alsa = %{EVRD}
Requires:       %{name}-gsm = %{EVRD}
Requires:       %{name}-speex = %{EVRD}
#Requires:       %{name}-h323 = %{EVRD}
Requires:       %{name}-isdn = %{EVRD}
#Requires:       %{name}-lksctp = %{EVRD}
Requires:       %{name}-openssl = %{EVRD}
Requires:       %{name}-zlib = %{EVRD}
Requires:       %{name}-mysql = %{EVRD}
Requires:       %{name}-pgsql = %{EVRD}
Requires:       %{name}-qt4 = %{EVRD}
Requires:       %{name}-scripts = %{EVRD}

%description all
Metapackage for Yate allowing to fetch and install all components at 
once. It contains no files, just dependencies to all other packages.

#------------------------------------------------------------------------------

%prep
%setup -q -n %{name}
%patch0 -p1

# fix openh323 detection
%{__perl} -pi -e 's|/lib/|/%{_lib}/|g' configure.in
# fix CFLAGS
#%{__perl} -pi -e 's|^CFLAGS := (.*)|CFLAGS := %{optflags} \1|g;' \
#              -e 's|^CXXFLAGS := (.*)|CXXFLAGS := %{optflags} \1|g;' \
#              -e 's|^CPPFLAGS := (.*)|CPPFLAGS := %{optflags} \1|g;' \
#  `%{_bindir}/find . -type f -name Makefile.in`
# fix caps and logdir
%{__perl} -pi -e 's|YATE|yate|g;' \
              -e 's|/var/log|%{_logdir}|g;' \
  packing/rpm/yate.init

autoreconf

%build
%{configure2_5x} --with-archlib=%{_lib}
make 
%make apidocs-everything 

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}

%{__mkdir_p} %{buildroot}%{_initrddir}
%{__cp} -a packing/rpm/yate.init %{buildroot}%{_initrddir}/yate

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
#%{__mkdir_p} %{buildroot}%{_datadir}/icons/hicolor/16x16/apps
#%{__cp} -a %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}-qt4.png
#%{__mkdir_p} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
#%{__cp} -a %{SOURCE2} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}-qt4.png
#%{__mkdir_p} %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
#%{_bindir}/convert -resize 48x48 %{SOURCE2} %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}-qt4.png
#%{__mkdir_p} %{buildroot}%{_datadir}/pixmaps
#%{__cp} -a %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/%{name}-qt4.png

mkdir -p %{buildroot}%{_datadir}/applications/
#/bin/echo 'Icon=%{name}-qt4' >> %{buildroot}%{_datadir}/applications/yate-qt4.desktop
%{_bindir}/desktop-file-install --vendor ""             \
        --dir %{buildroot}%{_datadir}/applications \
        --add-category X-MandrivaLinux-Internet-InstantMessaging \
        --remove-category Application                   \
        %{buildroot}%{_datadir}/applications/yate-qt4.desktop

# fix wrong location doc files
mv %{buildroot}%{_docdir}/%{name}-%{version} %{buildroot}%{_docdir}/%{name}

install -d -m 755 %{buildroot}/%{_docdir}/%{lib_name_devel}
mv %{buildroot}%{_docdir}/%{name}/*.html %{buildroot}%{_docdir}/%{name}/api/ %{buildroot}/%{_docdir}/%{lib_name_devel}


%changelog
* Wed Apr 25 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 4.1.0-1mdv2011.0
+ Revision: 793322
- update to 4.1.0
- update to 4.0.0

  + Sergey Zhemoitel <serg@mandriva.org>
    - resource for new version
    - update to new version 3.3.2

* Thu Mar 17 2011 Oden Eriksson <oeriksson@mandriva.com> 0:2.2.0-6
+ Revision: 645907
- relink against libmysqlclient.so.18

* Sat Jan 01 2011 Oden Eriksson <oeriksson@mandriva.com> 0:2.2.0-5mdv2011.0
+ Revision: 627292
- rebuilt against mysql-5.5.8 libs, again

* Thu Dec 30 2010 Oden Eriksson <oeriksson@mandriva.com> 0:2.2.0-4mdv2011.0
+ Revision: 626566
- rebuilt against mysql-5.5.8 libs

* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 0:2.2.0-3mdv2011.0
+ Revision: 615758
- the mass rebuild of 2010.1 packages

* Thu Apr 08 2010 Michael Scherer <misc@mandriva.org> 0:2.2.0-2mdv2010.1
+ Revision: 533138
- Rebuild for new libopenssl
- remove patch0, not applied and it seems that yate respect fhs already

* Tue Mar 23 2010 Michael Scherer <misc@mandriva.org> 0:2.2.0-1mdv2010.1
+ Revision: 526776
- drop patch1, applied upstream
- drop patch2, splitted and rediffed in 3 patch
- rediff patchs for version 2.2
- really update to 2.2, and no longer hardcode the tarball version, thus leading to mdvsys update failure
- add patch to fix qt detection
- complete patch for linking order
- add patch for format string detection
- update to 2.2
- fix various problems

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild
    - lowercase ImageMagick

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Mon Dec 08 2008 Funda Wang <fwang@mandriva.org> 0:2.0.0-2mdv2009.1
+ Revision: 311718
- rebuild for new mysql

* Mon Aug 11 2008 David Walluck <walluck@mandriva.org> 0:2.0.0-1mdv2009.0
+ Revision: 270884
- fix menu removal
- 2.0.0

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0:1.3.0-3mdv2009.0
+ Revision: 243000
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Sep 04 2007 Funda Wang <fwang@mandriva.org> 0:1.3.0-1mdv2008.0
+ Revision: 79276
- fix file list
- remove unexist file
- spandsp is not stable (yate bug#84)
- rename BR spandsp
- New version 1.3.0

  + David Walluck <walluck@mandriva.org>
    - update BuildRequires

* Wed Apr 18 2007 David Walluck <walluck@mandriva.org> 0:1.2.0-2mdv2008.0
+ Revision: 14289
- BuildRequires: libspeex-devel
- 1.2.0


* Sun Jan 07 2007 David Walluck <walluck@mandriva.org> 1.1.0-5mdv2007.0
+ Revision: 105034
- rebuild for new libpq-devel

* Sun Dec 17 2006 David Walluck <walluck@mandriva.org> 0:1.1.0-4mdv2007.1
+ Revision: 98246
- bumo release
- fix initscript
  create logdir and add logrotate file

* Sun Dec 17 2006 David Walluck <walluck@mandriva.org> 0:1.1.0-3mdv2007.1
+ Revision: 98234
- try non-parallel make
- menu icons
  Makefile fixes and better FHS compliance
  yate-all no longer requires yate-devel

* Sat Dec 16 2006 David Walluck <walluck@mandriva.org> 0:1.1.0-1mdv2007.1
+ Revision: 98054
- BuildRequires: postgresql-devel
- Import yate

* Fri Dec 15 2006 David Walluck <walluck@mandriva.org> 0:1.1.0-1mdv2007.1
- release

