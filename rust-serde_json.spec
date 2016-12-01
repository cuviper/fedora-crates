%global crate serde_json

Name:           rust-%{crate}
Version:        0.8.3
Release:        1%{?dist}
Summary:        Raw bindings to platform APIs for Rust 

License:        ASL 2.0 or MIT
URL:            https://crates.io/crates/%{crate}
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-srpm-macros
BuildRequires:  rust
BuildRequires:  cargo

BuildRequires:  rust-serde-devel >= 0.8.13
BuildRequires:  rust-serde-devel < 0.9

BuildRequires:  rust-dtoa-devel >= 0.2
BuildRequires:  rust-dtoa-devel < 0.3

BuildRequires:  rust-itoa-devel >= 0.1
BuildRequires:  rust-itoa-devel < 0.2

BuildRequires:  rust-num-traits-devel >= 0.1.32
BuildRequires:  rust-num-traits-devel < 0.2

# no installed binaries
%global debug_package %{nil}

%description
A library for types and bindings to native C functions often found in libc or
other common platform libraries.


%package devel
Summary:        %{summary}
BuildArch:      noarch

Requires:       rust-serde-devel >= 0.8.13
Requires:       rust-serde-devel < 0.9

Requires:       rust-dtoa-devel >= 0.2
Requires:       rust-dtoa-devel < 0.3

Requires:       rust-itoa-devel >= 0.1
Requires:       rust-itoa-devel < 0.2

Requires:       rust-num-traits-devel >= 0.1.32
Requires:       rust-num-traits-devel < 0.2

%description devel
A library for types and bindings to native C functions often found in libc or
other common platform libraries.


%prep
%autosetup -n %{crate}-%{version}
%cargo_prep

sed -i.no-clippy -e '/clippy/s/^/#/' Cargo.toml
sed -i.no-linked-hash-map -e '/linked-hash-map/s/^/#/' Cargo.toml


%build
%cargo_build


%install
%cargo_install_crate %{crate}-%{version}


%check
%cargo_test


%files devel
%license
%{cargo_registry}/%{crate}-%{version}/


%changelog
* Wed Nov 30 2016 Josh Stone <jistone@redhat.com> - 0.8.3-1
- Initial package
