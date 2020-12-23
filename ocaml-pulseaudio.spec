Name:     ocaml-pulseaudio
Version:  0.1.4
Release:  0.1%{?dist}
Summary:  OCAML pulseaudio

%global libname %(echo %{name} | sed -e 's/^ocaml-//')

License:  GPLv2+
URL:      https://github.com/savonet/ocaml-pulseaudio
Source0:  https://github.com/savonet/ocaml-pulseaudio/archive/v%{version}.tar.gz?#/ocaml-pulseaudio-%{version}.tag.gz

BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: ocaml-dune
BuildRequires: ocaml-dune-devel
BuildRequires: pulseaudio-libs-devel


%description
OCaml bindings for pulseaudio.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{version}

%build
dune build

%install
dune install \
  --prefix %{buildroot} \
  --libdir %{buildroot}$(ocamlfind printconf destdir)
rm -rf %{buildroot}/doc


%files
%doc README.md CHANGES.md
%license COPYING
%{_libdir}/ocaml/%{libname}
%{_libdir}/ocaml/stublibs/dll%{libname}_stubs.so
%ifarch %{ocaml_native_compiler}
%exclude %{_libdir}/ocaml/%{libname}/*.a
%exclude %{_libdir}/ocaml/%{libname}/*.cmxa
%exclude %{_libdir}/ocaml/%{libname}/*.cmx
%exclude %{_libdir}/ocaml/%{libname}/*.mli
%endif

%files devel
%license COPYING
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{libname}/*.a
%{_libdir}/ocaml/%{libname}/*.cmxa
%{_libdir}/ocaml/%{libname}/*.cmx
%{_libdir}/ocaml/%{libname}/*.mli
%endif

%changelog
* Tue Dec 22 2020 Lucas Bickel <hairmare@rabe.ch> - 0.1.4-0.1
- initial package
