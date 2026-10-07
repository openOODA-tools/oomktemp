Name:           oomktemp
Version:        0.1.0
Release:        1%{?dist}
Summary:        Creates temporary files and directories under systemd-tmpfiles paths securely.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oomktemp
Source0:        oomktemp-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oomktemp is a sovereign, capability-bounded TEMP CREATOR written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oomktemp
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oomktemp-uninstall

%files
/usr/bin/oomktemp
/usr/bin/oomktemp-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
