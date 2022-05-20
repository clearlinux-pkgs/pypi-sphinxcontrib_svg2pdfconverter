#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-sphinxcontrib_svg2pdfconverter
Version  : 1.2.0
Release  : 5
URL      : https://files.pythonhosted.org/packages/59/3a/202cfc55f35118e9b2f3d78a5376b38a050f835e30ea9ab6f88828733a47/sphinxcontrib-svg2pdfconverter-1.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/59/3a/202cfc55f35118e9b2f3d78a5376b38a050f835e30ea9ab6f88828733a47/sphinxcontrib-svg2pdfconverter-1.2.0.tar.gz
Summary  : Sphinx SVG to PDF converter extension
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-sphinxcontrib_svg2pdfconverter-license = %{version}-%{release}
Requires: pypi-sphinxcontrib_svg2pdfconverter-python = %{version}-%{release}
Requires: pypi-sphinxcontrib_svg2pdfconverter-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(sphinx)

%description
*************************************
Sphinx SVG to PDF Converter Extension
*************************************

%package license
Summary: license components for the pypi-sphinxcontrib_svg2pdfconverter package.
Group: Default

%description license
license components for the pypi-sphinxcontrib_svg2pdfconverter package.


%package python
Summary: python components for the pypi-sphinxcontrib_svg2pdfconverter package.
Group: Default
Requires: pypi-sphinxcontrib_svg2pdfconverter-python3 = %{version}-%{release}

%description python
python components for the pypi-sphinxcontrib_svg2pdfconverter package.


%package python3
Summary: python3 components for the pypi-sphinxcontrib_svg2pdfconverter package.
Group: Default
Requires: python3-core
Provides: pypi(sphinxcontrib_svg2pdfconverter)
Requires: pypi(sphinx)

%description python3
python3 components for the pypi-sphinxcontrib_svg2pdfconverter package.


%prep
%setup -q -n sphinxcontrib-svg2pdfconverter-1.2.0
cd %{_builddir}/sphinxcontrib-svg2pdfconverter-1.2.0
pushd ..
cp -a sphinxcontrib-svg2pdfconverter-1.2.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1653060407
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-sphinxcontrib_svg2pdfconverter
cp %{_builddir}/sphinxcontrib-svg2pdfconverter-1.2.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-sphinxcontrib_svg2pdfconverter/edb6d4112e8d9c10aa748beafecc30e8f3fc4fdf
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-sphinxcontrib_svg2pdfconverter/edb6d4112e8d9c10aa748beafecc30e8f3fc4fdf

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
