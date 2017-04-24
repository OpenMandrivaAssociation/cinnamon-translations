Name:           cinnamon-translations
Version:        3.2.2
Release:        1
Summary:        Translations for Cinnamon and Nemo

License:        GPLv2+
URL:            http://cinnamon.linuxmint.com
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
Group:   Graphical desktop/Other
      

%description
Translations for Cinnamon and Nemo

%prep
%setup -q -n %{name}-%{version}

%build
make

%install
install -m 0755 -d $RPM_BUILD_ROOT%{_datadir}/locale/
cp -Rp usr/share/locale/* $RPM_BUILD_ROOT%{_datadir}/locale/

%find_lang cinnamon
%find_lang nemo
%find_lang cinnamon-control-center
%find_lang cinnamon-screensaver
%find_lang cinnamon-bluetooth

cat *.lang > %{name}.lang

%files -f %{name}.lang
%doc COPYING



