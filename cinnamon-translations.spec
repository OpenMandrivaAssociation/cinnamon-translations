#global _internal_version  3906358 
#global	 debug_package     %{nil}
%global  _trans_version    2014.05.25
#global  date              20141123

Name:           cinnamon-translations
Version:        2.4.2
Release:        1
Summary:        Translations for Cinnamon and Nemo

License:        GPLv2+
URL:            http://cinnamon.linuxmint.com
Source0:        %{name}-%{version}.tar.gz
#SourceGet0: https://github.com/linuxmint/cinnamon-translations/archive/%{version}.tar.gz
#Source0:        %{name}-%{version}.git%{_internal_version}.tar.gz
##SourceGet0: https://github.com/linuxmint/cinnamon-translations/tarball/%{_internal_version}
Source1:        http://packages.linuxmint.com/pool/main/m/mint-translations/mint-translations_%{_trans_version}.tar.gz
BuildArch:      noarch
Group:   Graphical desktop/Other
      

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

cat *.lang > %{name}.lang

%files -f %{name}.lang
%doc COPYING



