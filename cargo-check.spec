%global crate cargo-check

Name:           %{crate}
Version:        0.2.2
Release:        1%{?dist}
Summary:        wrapper around cargo rustc -- -Zno-trans

License:        ASL 2.0 or MIT
URL:            https://crates.io/crates/%{crate}
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-srpm-macros
BuildRequires:  rust
BuildRequires:  cargo

BuildRequires:  rust-serde_json-devel >= 0.8
BuildRequires:  rust-serde_json-devel < 0.9

Requires:       cargo

%description
This is a wrapper around `cargo rustc -- -Zno-trans`. It can be helpful for
running a faster compile if you only need correctness checks.


%prep
%autosetup -n %{crate}-%{version}
%cargo_prep


%build
%cargo_build


%install
%cargo_install


%check
%cargo_test || :


%files
%doc README.md
%license LICENSE-APACHE LICENSE-MIT
/usr/bin/cargo-check


%changelog
* Wed Nov 30 2016 Josh Stone <jistone@redhat.com> - 0.2.2-1
- Initial package
