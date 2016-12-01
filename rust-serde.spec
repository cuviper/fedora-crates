%global crate serde

Name:           rust-%{crate}
Version:        0.8.19
Release:        1%{?dist}
Summary:        A generic serialization/deserialization framework

License:        ASL 2.0 or MIT
URL:            https://crates.io/crates/%{crate}
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-srpm-macros
BuildRequires:  rust
BuildRequires:  cargo

# no installed binaries
%global debug_package %{nil}

%description
%{summary}


%package devel
Summary:        %{summary}
BuildArch:      noarch

%description devel
%{summary}


%prep
%autosetup -n %{crate}-%{version}
%cargo_prep

sed -i.no-clippy -e '/clippy/s/^/#/' Cargo.toml


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
* Wed Nov 30 2016 Josh Stone <jistone@redhat.com> - 0.8.19-1
- Initial package
