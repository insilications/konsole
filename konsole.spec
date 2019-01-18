#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : konsole
Version  : 18.12.1
Release  : 15
URL      : https://github.com/KDE/konsole/archive/v18.12.1.tar.gz
Source0  : https://github.com/KDE/konsole/archive/v18.12.1.tar.gz
Summary  : KDE's terminal emulator
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0 LGPL-2.0
Requires: konsole-bin = %{version}-%{release}
Requires: konsole-data = %{version}-%{release}
Requires: konsole-lib = %{version}-%{release}
Requires: konsole-license = %{version}-%{release}
BuildRequires : attica-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : buildreq-qmake
BuildRequires : kbookmarks-dev
BuildRequires : kcodecs-dev
BuildRequires : kcompletion-dev
BuildRequires : kconfigwidgets-dev
BuildRequires : kcrash-dev
BuildRequires : kdbusaddons-dev
BuildRequires : kglobalaccel-dev
BuildRequires : kguiaddons-dev
BuildRequires : kiconthemes-dev
BuildRequires : kinit-dev
BuildRequires : kio-dev
BuildRequires : kitemviews-dev
BuildRequires : kjobwidgets-dev
BuildRequires : knewstuff-dev
BuildRequires : knotifications-dev
BuildRequires : knotifyconfig-dev
BuildRequires : kparts-dev
BuildRequires : kpty-dev
BuildRequires : ktextwidgets-dev
BuildRequires : kwidgetsaddons-dev
BuildRequires : kwindowsystem-dev
BuildRequires : kxmlgui-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86misc-dev libXxf86vm-dev
BuildRequires : qtbase-dev mesa-dev
BuildRequires : solid-dev
BuildRequires : sonnet-dev

%description
> Konsole is a *great* program, but is designed for the end user to have a
> lot of control over their session--which in our environment would be
> very bad.  The users have no clue what emulation to pick, how many
> columns and rows they need.
> What would really help is some command line arguments that would take
> configure certain items, and then disable them from the pulldowns along
> the top.
> For instance, if the command --noscrollbar was issued, it would turn off
> the scroll bar and then now allow them to turn it back on again via the
> pulldowns.
> The more things that I could configure via the command line, the better.

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


%prep
%setup -q -n konsole-18.12.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1547423176
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1547423176
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/konsole
cp COPYING %{buildroot}/usr/share/package-licenses/konsole/COPYING
cp COPYING.DOC %{buildroot}/usr/share/package-licenses/konsole/COPYING.DOC
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/konsole/COPYING.LIB
pushd clr-build
%make_install
popd

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
/usr/share/konsole/solaris.keytab
/usr/share/kservices5/ServiceMenus/konsolehere.desktop
/usr/share/kservices5/ServiceMenus/konsolerun.desktop
/usr/share/kservices5/konsolepart.desktop
/usr/share/kservicetypes5/terminalemulator.desktop
/usr/share/metainfo/org.kde.konsole.appdata.xml
/usr/share/xdg/konsole.categories
/usr/share/xdg/konsole.knsrc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/en/konsole/draganddrop-contextmenu.png
/usr/share/doc/HTML/en/konsole/index.cache.bz2
/usr/share/doc/HTML/en/konsole/index.docbook

%files lib
%defattr(-,root,root,-)
/usr/lib64/libkdeinit5_konsole.so
/usr/lib64/libkonsoleprivate.so.18
/usr/lib64/libkonsoleprivate.so.18.12.1
/usr/lib64/qt5/plugins/konsolepart.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/konsole/COPYING
/usr/share/package-licenses/konsole/COPYING.DOC
/usr/share/package-licenses/konsole/COPYING.LIB
