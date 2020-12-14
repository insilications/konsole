#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : konsole
Version  : 20.12.0
Release  : 39
URL      : https://download.kde.org/stable/release-service/20.12.0/src/konsole-20.12.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/20.12.0/src/konsole-20.12.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/20.12.0/src/konsole-20.12.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0 LGPL-2.0
Requires: konsole-bin = %{version}-%{release}
Requires: konsole-data = %{version}-%{release}
Requires: konsole-lib = %{version}-%{release}
Requires: konsole-license = %{version}-%{release}
Requires: konsole-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : buildreq-qmake
BuildRequires : extra-cmake-modules-data
BuildRequires : kdoctools-dev
BuildRequires : kglobalaccel-dev
BuildRequires : knotifyconfig-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86misc-dev libXxf86vm-dev
BuildRequires : qtbase-dev
BuildRequires : qtbase-dev mesa-dev
Patch1: 0001-Fix-build-with-LTO-enabled.patch

%description
Use CheckXML to verify the file is valid XML
Use meinproc5 to create an HTML version for local viewing.

%package bin
Summary: bin components for the konsole package.
Group: Binaries
Requires: konsole-data = %{version}-%{release}
Requires: konsole-license = %{version}-%{release}

%description bin
bin components for the konsole package.


%package data
Summary: data components for the konsole package.
Group: Data

%description data
data components for the konsole package.


%package doc
Summary: doc components for the konsole package.
Group: Documentation

%description doc
doc components for the konsole package.


%package lib
Summary: lib components for the konsole package.
Group: Libraries
Requires: konsole-data = %{version}-%{release}
Requires: konsole-license = %{version}-%{release}

%description lib
lib components for the konsole package.


%package license
Summary: license components for the konsole package.
Group: Default

%description license
license components for the konsole package.


%package locales
Summary: locales components for the konsole package.
Group: Default

%description locales
locales components for the konsole package.


%prep
%setup -q -n konsole-20.12.0
cd %{_builddir}/konsole-20.12.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1607914967
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1607914967
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/konsole
cp %{_builddir}/konsole-20.12.0/COPYING %{buildroot}/usr/share/package-licenses/konsole/7c203dee3a03037da436df03c4b25b659c073976
cp %{_builddir}/konsole-20.12.0/COPYING.DOC %{buildroot}/usr/share/package-licenses/konsole/0c4be15f5177aafffe980ca09c0f4ca6ed741f43
cp %{_builddir}/konsole-20.12.0/COPYING.LIB %{buildroot}/usr/share/package-licenses/konsole/ba8966e2473a9969bdcab3dc82274c817cfd98a1
pushd clr-build
%make_install
popd
%find_lang konsole

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/konsole
/usr/bin/konsoleprofile

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.konsole.desktop
/usr/share/khotkeys/konsole.khotkeys
/usr/share/knotifications5/konsole.notifyrc
/usr/share/knsrcfiles/konsole.knsrc
/usr/share/konsole/BlackOnLightYellow.colorscheme
/usr/share/konsole/BlackOnRandomLight.colorscheme
/usr/share/konsole/BlackOnWhite.colorscheme
/usr/share/konsole/BlueOnBlack.colorscheme
/usr/share/konsole/Breeze.colorscheme
/usr/share/konsole/DarkPastels.colorscheme
/usr/share/konsole/GreenOnBlack.colorscheme
/usr/share/konsole/Linux.colorscheme
/usr/share/konsole/RedOnBlack.colorscheme
/usr/share/konsole/Solarized.colorscheme
/usr/share/konsole/SolarizedLight.colorscheme
/usr/share/konsole/WhiteOnBlack.colorscheme
/usr/share/konsole/default.keytab
/usr/share/konsole/linux.keytab
/usr/share/konsole/macos.keytab
/usr/share/konsole/solaris.keytab
/usr/share/kservices5/ServiceMenus/konsolehere.desktop
/usr/share/kservices5/ServiceMenus/konsolerun.desktop
/usr/share/kservices5/konsolepart.desktop
/usr/share/kservicetypes5/terminalemulator.desktop
/usr/share/metainfo/org.kde.konsole.appdata.xml
/usr/share/qlogging-categories5/konsole.categories

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/konsole/draganddrop-contextmenu.png
/usr/share/doc/HTML/ca/konsole/index.cache.bz2
/usr/share/doc/HTML/ca/konsole/index.docbook
/usr/share/doc/HTML/de/konsole/index.cache.bz2
/usr/share/doc/HTML/de/konsole/index.docbook
/usr/share/doc/HTML/en/konsole/draganddrop-contextmenu.png
/usr/share/doc/HTML/en/konsole/index.cache.bz2
/usr/share/doc/HTML/en/konsole/index.docbook
/usr/share/doc/HTML/it/konsole/draganddrop-contextmenu.png
/usr/share/doc/HTML/it/konsole/index.cache.bz2
/usr/share/doc/HTML/it/konsole/index.docbook
/usr/share/doc/HTML/nl/konsole/index.cache.bz2
/usr/share/doc/HTML/nl/konsole/index.docbook
/usr/share/doc/HTML/pt/konsole/index.cache.bz2
/usr/share/doc/HTML/pt/konsole/index.docbook
/usr/share/doc/HTML/pt_BR/konsole/draganddrop-contextmenu.png
/usr/share/doc/HTML/pt_BR/konsole/index.cache.bz2
/usr/share/doc/HTML/pt_BR/konsole/index.docbook
/usr/share/doc/HTML/sr/konsole/index.cache.bz2
/usr/share/doc/HTML/sr/konsole/index.docbook
/usr/share/doc/HTML/sv/konsole/index.cache.bz2
/usr/share/doc/HTML/sv/konsole/index.docbook
/usr/share/doc/HTML/uk/konsole/draganddrop-contextmenu.png
/usr/share/doc/HTML/uk/konsole/index.cache.bz2
/usr/share/doc/HTML/uk/konsole/index.docbook
/usr/share/doc/HTML/zh_CN/konsole/index.cache.bz2
/usr/share/doc/HTML/zh_CN/konsole/index.docbook

%files lib
%defattr(-,root,root,-)
/usr/lib64/libkdeinit5_konsole.so
/usr/lib64/libkonsoleprivate.so.20
/usr/lib64/libkonsoleprivate.so.20.12.0
/usr/lib64/qt5/plugins/konsolepart.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/konsole/0c4be15f5177aafffe980ca09c0f4ca6ed741f43
/usr/share/package-licenses/konsole/7c203dee3a03037da436df03c4b25b659c073976
/usr/share/package-licenses/konsole/ba8966e2473a9969bdcab3dc82274c817cfd98a1

%files locales -f konsole.lang
%defattr(-,root,root,-)

