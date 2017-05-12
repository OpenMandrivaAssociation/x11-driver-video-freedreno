%define _disable_ld_no_undefined 1

Summary:	X.org driver for freedreno
Name:		x11-driver-video-freedreno
Version:	1.4.0.20170512
Release:	1
Group:		System/X11
License:	MIT
URL:		http://xorg.freedesktop.org
# From git@github.com:freedreno/xf86-video-freedreno.git
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-freedreno-%{version}.tar.xz
Buildrequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(libdrm_freedreno)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xproto)
BuildRequires:	pkgconfig(udev)
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)
ExclusiveArch:	%armx

%description
x11-driver-video-freedreno is the X.org driver for Adreno graphics chips

%prep
%setup -qn xf86-video-freedreno-%{version}
%apply_patches
[ -e configure ] || ./autogen.sh

%build
# CFLAGS need some fixes
# error: unknown attribute 'error' ignored
#export CC=gcc
%configure
%make

%install
%makeinstall_std

%files
%{_libdir}/xorg/modules/drivers/freedreno_drv.so
%{_datadir}/X11/xorg.conf.d/42-freedreno.conf
%{_mandir}/man4/*
