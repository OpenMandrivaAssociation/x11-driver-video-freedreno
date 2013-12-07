%define _disable_ld_no_undefined 1

Summary:	X.org driver for freedreno
Name:		x11-driver-video-freedreno
Version:	1.0.0
Release:	4
Group:		System/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-freedreno-%{version}.tar.bz2

BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(libdrm_freedreno)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xproto)
BuildRequires:	pkgconfig(udev)
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-freedreno is the X.org driver for Freedreno.

%prep
%setup -qn xf86-video-freedreno-%{version}
%apply_patches

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%{_libdir}/xorg/modules/drivers/freedreno_drv.so
