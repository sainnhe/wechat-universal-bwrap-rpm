%global __brp_check_rpaths %{nil}
%global _pkgname wechat-universal
%global _lib_uos libuosdevicea
%global _wechat_root %{buildroot}%{_datadir}/%{_pkgname}

Name:           wechat-universal-bwrap
Version:        1.0.0.241
Release:        1%{?dist}
Summary:        WeChat (Universal) with bwrap sandbox

License:        Proprietary and GPLv3
URL:            https://weixin.qq.com
Source0:        wechat-universal.sh
Source1:        wechat-universal.desktop
Source2:        libuosdevicea.c
Source3:        fake_dde-file-manager
Source4:        wechat-x86_64.deb
Source5:        wechat-aarch64.deb

BuildRequires:  gcc
BuildRequires:  bsdtar
BuildRequires:  alsa-lib-devel
BuildRequires:  at-spi2-core-devel
BuildRequires:  libXcomposite-devel
BuildRequires:  libxkbcommon-x11-devel
BuildRequires:  libXrandr-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  nss-devel
BuildRequires:  pango-devel
BuildRequires:  xcb-util-image-devel
BuildRequires:  xcb-util-keysyms-devel
BuildRequires:  xcb-util-renderutil-devel
BuildRequires:  xcb-util-wm-devel
BuildRequires:  xdg-desktop-portal-devel
Requires:       alsa-lib
Requires:       at-spi2-core
Requires:       bubblewrap
Requires:       flatpak-xdg-utils
Requires:       libXcomposite
Requires:       libxkbcommon-x11
Requires:       libXrandr
Requires:       mesa-libGL
Requires:       nss
Requires:       pango
Requires:       xcb-util-image
Requires:       xcb-util-keysyms
Requires:       xcb-util-renderutil
Requires:       xcb-util-wm
Requires:       xdg-desktop-portal
Requires:       xdg-user-dirs

%description
WeChat (Universal) wrapped in a sandbox environment using bubblewrap for enhanced security.

%prep
cp %{_sourcedir}/* .

%build
gcc %{optflags} -fPIC -shared %{_lib_uos}.c -o %{_lib_uos}.so

%install
echo 'Popupating pkgdir with data from wechat-universal deb file...'
mkdir tmp
cd tmp
bsdtar -xf ../wechat-$(uname -m).deb
tar xvf data.tar.xz
mkdir -p %{buildroot}/opt
mv opt/apps/com.tencent.wechat/files %{buildroot}/opt/%{_pkgname}
rm %{buildroot}/opt/%{_pkgname}/%{_lib_uos}.so
cd ..

echo 'Installing icons...'
for res in 16 32 48 64 128 256; do
    install -Dpm 644 \
        tmp/opt/apps/com.tencent.wechat/entries/icons/hicolor/${res}x${res}/apps/com.tencent.wechat.png \
        %{buildroot}%{_datadir}/icons/hicolor/${res}x${res}/apps/%{_pkgname}.png
done
rm -rf %{buildroot}/opt/apps

echo 'Fixing licenses...'
# This is needed if /usr/lib/license/${_lib_uos}.so needs to be mounted in sandbox
mkdir -p %{buildroot}/usr/lib/license
chmod 755 %{buildroot}/usr/lib/license
mkdir -p %{_wechat_root}/usr/lib/license
chmod 755 %{_wechat_root}/usr/lib/license
install -Dm755 %{_lib_uos}.so %{_wechat_root}/usr/lib/license/%{_lib_uos}.so
echo 'DISTRIB_ID=uos' |
    install -Dm755 /dev/stdin %{_wechat_root}%{_sysconfdir}/lsb-release

echo 'Installing fake deepin file manager...'
install -Dm755 fake_dde-file-manager %{_wechat_root}%{_bindir}/dde-file-manager

echo 'Installing desktop files...'
install -Dm 644 %{_pkgname}.desktop %{buildroot}%{_datadir}/applications/%{_pkgname}.desktop
install -Dm 755 %{_pkgname}.sh %{buildroot}%{_bindir}/%{_pkgname}

%files
/opt/%{_pkgname}
%{_bindir}/%{_pkgname}
/usr/lib/license
%{_datadir}/applications/%{_pkgname}.desktop
%{_datadir}/icons/hicolor/128x128/apps/wechat-universal.png
%{_datadir}/icons/hicolor/16x16/apps/wechat-universal.png
%{_datadir}/icons/hicolor/256x256/apps/wechat-universal.png
%{_datadir}/icons/hicolor/32x32/apps/wechat-universal.png
%{_datadir}/icons/hicolor/48x48/apps/wechat-universal.png
%{_datadir}/icons/hicolor/64x64/apps/wechat-universal.png
%{_datadir}/%{_pkgname}

%changelog
* Wed Jun 05 2024 Sainnhe Park <i@sainnhe.dev> - 1.0.0.241-1
- First build of wechat-universal-bwrap for Fedora
