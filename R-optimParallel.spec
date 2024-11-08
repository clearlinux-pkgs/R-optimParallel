#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-optimParallel
Version  : 1.0.2
Release  : 9
URL      : https://cran.r-project.org/src/contrib/optimParallel_1.0-2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/optimParallel_1.0-2.tar.gz
Summary  : Parallel Version of the L-BFGS-B Optimization Method
Group    : Development/Tools
License  : GPL-2.0+
BuildRequires : R-numDeriv
BuildRequires : buildreq-R

%description
The R package optimParallel
===========================
The package provides a parallel versions of the L-BFGS-B optim method.
If the evaluation of the function fn takes more than 0.1 seconds,
optimParallel can significantly reduce the optimization time. For a p-parameter optimization,
the speed increase is about factor 1+2p when no analytic gradient is specified and
1+2p processor cores are available.

%prep
%setup -q -n optimParallel
cd %{_builddir}/optimParallel

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1662079379

%install
export SOURCE_DATE_EPOCH=1662079379
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/optimParallel/CITATION
/usr/lib64/R/library/optimParallel/DESCRIPTION
/usr/lib64/R/library/optimParallel/INDEX
/usr/lib64/R/library/optimParallel/Meta/Rd.rds
/usr/lib64/R/library/optimParallel/Meta/features.rds
/usr/lib64/R/library/optimParallel/Meta/hsearch.rds
/usr/lib64/R/library/optimParallel/Meta/links.rds
/usr/lib64/R/library/optimParallel/Meta/nsInfo.rds
/usr/lib64/R/library/optimParallel/Meta/package.rds
/usr/lib64/R/library/optimParallel/Meta/vignette.rds
/usr/lib64/R/library/optimParallel/NAMESPACE
/usr/lib64/R/library/optimParallel/NEWS
/usr/lib64/R/library/optimParallel/R/optimParallel
/usr/lib64/R/library/optimParallel/R/optimParallel.rdb
/usr/lib64/R/library/optimParallel/R/optimParallel.rdx
/usr/lib64/R/library/optimParallel/doc/index.html
/usr/lib64/R/library/optimParallel/doc/optimParallel.pdf
/usr/lib64/R/library/optimParallel/doc/optimParallel.pdf.asis
/usr/lib64/R/library/optimParallel/help/AnIndex
/usr/lib64/R/library/optimParallel/help/aliases.rds
/usr/lib64/R/library/optimParallel/help/optimParallel.rdb
/usr/lib64/R/library/optimParallel/help/optimParallel.rdx
/usr/lib64/R/library/optimParallel/help/paths.rds
/usr/lib64/R/library/optimParallel/html/00Index.html
/usr/lib64/R/library/optimParallel/html/R.css
/usr/lib64/R/library/optimParallel/tests/run-all.R
/usr/lib64/R/library/optimParallel/tests/testthat/test-issues.R
/usr/lib64/R/library/optimParallel/tests/testthat/test-object.R
/usr/lib64/R/library/optimParallel/tests/testthat/test-optimParallel.R
/usr/lib64/R/library/optimParallel/tests/testthat/test-spam.R
/usr/lib64/R/library/optimParallel/tests/testthat/testsetup.R
