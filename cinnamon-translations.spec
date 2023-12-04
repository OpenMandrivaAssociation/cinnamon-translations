Name:           cinnamon-translations
Version:        6.0.1
Release:        1
Summary:        Translations for Cinnamon and Nemo

License:        GPLv2+
URL:            http://cinnamon.linuxmint.com
Source0:        https://github.com/linuxmint/cinnamon-translations/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Group:   Graphical desktop/Other
      
%description
Translations for Cinnamon and Nemo

%prep
%setup -q -n %{name}-%{version}

%build
%make_build

%install
install -m 0755 -d $RPM_BUILD_ROOT%{_datadir}/locale/
cp -Rp usr/share/locale/* $RPM_BUILD_ROOT%{_datadir}/locale/

%find_lang cinnamon
%find_lang nemo
%find_lang nemo-extensions
%find_lang cinnamon-control-center
%find_lang cinnamon-screensaver
%find_lang cinnamon-session
%find_lang cinnamon-settings-daemon

cat *.lang > %{name}.lang

%files -f %{name}.lang
%doc COPYING
