# $Id$

# Authority: dries
# Upstream: 
# Screenshot: http://kgeography.berlios.de/screen1.png
# ScreenshotURL: http://kgeography.berlios.de/screenshots.html

Summary: Geography learning tool
Name: kgeography
Version: 0.1
Release: 1
License: GPL
Group: Amusements/Games
URL: http://kgeography.berlios.de/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://download.berlios.de/kgeography/kgeography-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gettext, libart_lgpl-devel
BuildRequires: libjpeg-devel, libpng-devel
BuildRequires: arts-devel, zlib-devel, gcc
BuildRequires: kdelibs-devel, make, gcc-c++
BuildRequires:  XFree86-devel, qt-devel


%description
KGeography is a geography learning tool. Right now it has three usage modes: 
* Browse the maps clicking in a map division to see it's name
* The game tells you a map division name and you have to click on it
* The game shows you a map division flag and you have to guess its name

%prep
%setup

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=KGeography
Comment=Geography learning tool
Exec=kgeography
Terminal=false
Type=Application
StartupNotify=true
Encoding=UTF-8
Categories=Application;Games;X-Red-Hat-Extra;
EOF

%build
. /etc/profile.d/qt.sh
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
. /etc/profile.d/qt.sh
%makeinstall

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor net                  \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING INSTALL README TODO
%{_bindir}/*
%{_datadir}/applications/*.desktop

%changelog
* Tue May 4 2004 Dries Verachtert <dries@ulyssis.org> - 0.1-1 
- Initial package.
