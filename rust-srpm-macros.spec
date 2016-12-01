Name:           rust-srpm-macros
Version:        1
Release:        1%{?dist}
Summary:        RPM macros for building Rust packages
BuildArch:      noarch

License:        ASL 2.0 or MIT
Source0:        macros.rust

%description
The package provides macros for building projects in Rust.


%prep
# nothing to prep


%build
# nothing to build


%install
install -D -p -m 0644 -t %{buildroot}%{rpmmacrodir} %{SOURCE0}
mkdir -p %{buildroot}%{_usrsrc}/rust


%files
%{rpmmacrodir}/macros.rust
%dir %{_usrsrc}/rust


%changelog
* Wed Nov 30 2016 Josh Stone <jistone@redhat.com> - 1-1
- Initial package.

