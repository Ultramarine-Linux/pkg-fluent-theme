%undefine _disable_source_fetch

Name:           fluent-theme
Version:        031021
Release:        2%{?dist}
Summary:        Fluent is a Fluent design theme for GNOME/GTK based desktop environments.

License:        GPLv3
URL:            https://github.com/vinceliuice/Fluent-gtk-theme
Source0:        %{url}/archive/refs/tags/2021-10-03.tar.gz

BuildRequires:  sassc
Requires:       gtk-murrine-engine

%description
Qogir is a flat Design theme for GTK 3, GTK 2 and Gnome-Shell which supports GTK 3 and GTK 2 based desktop environments like Gnome, Unity, Budgie, Cinnamon Pantheon, XFCE, Mate, etc.

%prep
%autosetup -n Fluent-gtk-theme-2021-10-03


#%build
#./parse-sass.sh



%install
./parse-sass.sh
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_datadir}/themes
./install.sh --tweaks round -d %{buildroot}%{_datadir}/themes

%files
%license COPYING
%doc README.md

%{_datadir}/themes/Fluent*/

%changelog
* Tue Feb 22 2022 Ultramarine Release Tracking Service - 031021-2
- Mass rebuild for release um36

* Sat Nov 13 2021 korewaChino <cappy@cappuchino.xyz>
- initial release
