#global _internal_version  3906358 
#global	 debug_package     %{nil}
%global  _trans_version    2014.05.25
#global  date              20141123

Name:           cinnamon-translations
Version:        2.4.2
Release:        %mkrel 1
Summary:        Translations for Cinnamon and Nemo

License:        GPLv2+
URL:            http://cinnamon.linuxmint.com
Source0:        %{name}-%{version}.tar.gz
#SourceGet0: https://github.com/linuxmint/cinnamon-translations/archive/%{version}.tar.gz
#Source0:        %{name}-%{version}.git%{_internal_version}.tar.gz
##SourceGet0: https://github.com/linuxmint/cinnamon-translations/tarball/%{_internal_version}
Source1:        http://packages.linuxmint.com/pool/main/m/mint-translations/mint-translations_%{_trans_version}.tar.gz
Requires:       cinnamon
BuildArch:      noarch
Group:   Graphical desktop/Cinnamon
      

%description
Translations for Cinnamon and Nemo

%prep
%setup -q -n %{name}-%{version}
tar -xf %{SOURCE1}

%build
make

%install
# install mint translations for mintlocale
find mint-translations-%{_trans_version}/ -not -name 'mintlocale.mo' -type f -exec rm -f {} ';'
cp -r mint-translations-%{_trans_version}/%{_datadir}/linuxmint/locale/* usr/share/locale/

install -m 0755 -d $RPM_BUILD_ROOT%{_datadir}/locale/
cp -Rp usr/share/locale/* $RPM_BUILD_ROOT%{_datadir}/locale/

%find_lang cinnamon
%find_lang mintlocale
%find_lang nemo
%find_lang cinnamon-control-center
%find_lang cinnamon-screensaver
%find_lang cinnamon-session
%find_lang cinnamon-bluetooth

%files -f cinnamon.lang -f nemo.lang -f cinnamon-control-center.lang -f cinnamon-screensaver.lang -f cinnamon-session.lang -f mintlocale.lang -f cinnamon-bluetooth.lang
%doc COPYING




%changelog
* Thu Nov 27 2014 joequant <joequant> 2.4.2-1.mga5
+ Revision: 799546
- 2.4.2

* Sun Nov 23 2014 joequant <joequant> 2.4.1-1.mga5
+ Revision: 798401
- upgrade to 2.4

* Wed Oct 15 2014 umeabot <umeabot> 2.2.4-4.mga5
+ Revision: 746675
- Second Mageia 5 Mass Rebuild

* Thu Sep 18 2014 umeabot <umeabot> 2.2.4-3.mga5
+ Revision: 693612
- Rebuild to fix library dependencies

* Tue Sep 16 2014 umeabot <umeabot> 2.2.4-2.mga5
+ Revision: 678402
- Mageia 5 Mass Rebuild

* Sat Aug 30 2014 joequant <joequant> 2.2.4-1.mga5
+ Revision: 669420
- update to 2.2.4

* Tue Jun 10 2014 joequant <joequant> 2.2.3-1.mga5
+ Revision: 635324
- upgrade to 2.2.3

* Thu May 15 2014 joequant <joequant> 2.2.2-1.mga5
+ Revision: 622869
- upgrade to 2.2.2

* Fri Apr 18 2014 joequant <joequant> 2.2.0-1.mga5
+ Revision: 616811
- upgrade to 2.2

* Thu Jan 09 2014 joequant <joequant> 2.0.3-2.mga4
+ Revision: 565910
- fix missing 2.0.3
- push to core/release

* Mon Oct 21 2013 umeabot <umeabot> 2.0.1-2.mga4
+ Revision: 541271
- Mageia 4 Mass Rebuild

* Fri Oct 11 2013 joequant <joequant> 2.0.1-1.mga4
+ Revision: 495433
- update to 2.0.1

* Mon Oct 07 2013 joequant <joequant> 2.0.0-1.mga4
+ Revision: 492468
- update to 2.0.0

* Wed Sep 11 2013 joequant <joequant> 1.9.2-0.20130826git6091a38.5.mga4
+ Revision: 477505
- fix translations

* Wed Sep 11 2013 joequant <joequant> 1.9.2-0.20130826git6091a38.4.mga4
+ Revision: 477501
- remove cinnamon-screensaver
- remove screensaver

* Wed Sep 11 2013 joequant <joequant> 1.9.2-0.20130826git6091a38.2.mga4
+ Revision: 477496
- move translations into standard location

* Tue Sep 10 2013 joequant <joequant> 1.9.2-0.20130826git6091a38.1.mga4
+ Revision: 477244
- update to git

* Mon Sep 02 2013 joequant <joequant> 1.9.2-0.1.git444eac5.mga4
+ Revision: 474256
- imported package cinnamon-translations

