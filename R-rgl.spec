#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-rgl
Version  : 0.100.26
Release  : 28
URL      : https://cran.r-project.org/src/contrib/rgl_0.100.26.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rgl_0.100.26.tar.gz
Summary  : 3D Visualization Using OpenGL
Group    : Development/Tools
License  : GL2PS GPL-2.0
Requires: R-rgl-lib = %{version}-%{release}
Requires: R-crosstalk
Requires: R-htmltools
Requires: R-htmlwidgets
Requires: R-jsonlite
Requires: R-knitr
Requires: R-magrittr
Requires: R-manipulateWidget
Requires: R-rmarkdown
Requires: R-shiny
BuildRequires : R-crosstalk
BuildRequires : R-htmltools
BuildRequires : R-htmlwidgets
BuildRequires : R-jsonlite
BuildRequires : R-knitr
BuildRequires : R-magrittr
BuildRequires : R-manipulateWidget
BuildRequires : R-rmarkdown
BuildRequires : R-shiny
BuildRequires : R-webshot
BuildRequires : buildreq-R
BuildRequires : glu-dev
BuildRequires : mesa-dev
BuildRequires : pkgconfig(freetype2)
BuildRequires : pkgconfig(libpng)
BuildRequires : pkgconfig(x11)

%description
The currently shipping OpenGL32.DLL from Microsoft only has entry points
for OpenGL 1.1. If an application wants to use OpenGL {1.2, 1.3, 1.4, 1.5}
functions, it has to use wglGetProcAddress() in order to obtain the entry
points from the driver. The files in this distribution enable the application
pretend that there is full support for OpenGL {1.2/1.3/1.4/1.5} if the
underlying implementation supports OpenGL {1.2/1.3/1.4/1.5}.

%package lib
Summary: lib components for the R-rgl package.
Group: Libraries

%description lib
lib components for the R-rgl package.


%prep
%setup -q -c -n rgl

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1562650809

%install
export SOURCE_DATE_EPOCH=1562650809
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rgl
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rgl
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rgl
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc rgl || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/rgl/DESCRIPTION
/usr/lib64/R/library/rgl/INDEX
/usr/lib64/R/library/rgl/Meta/Rd.rds
/usr/lib64/R/library/rgl/Meta/demo.rds
/usr/lib64/R/library/rgl/Meta/features.rds
/usr/lib64/R/library/rgl/Meta/hsearch.rds
/usr/lib64/R/library/rgl/Meta/links.rds
/usr/lib64/R/library/rgl/Meta/nsInfo.rds
/usr/lib64/R/library/rgl/Meta/package.rds
/usr/lib64/R/library/rgl/Meta/vignette.rds
/usr/lib64/R/library/rgl/NAMESPACE
/usr/lib64/R/library/rgl/NEWS
/usr/lib64/R/library/rgl/R/rgl
/usr/lib64/R/library/rgl/R/rgl.rdb
/usr/lib64/R/library/rgl/R/rgl.rdx
/usr/lib64/R/library/rgl/WebGL/template.html
/usr/lib64/R/library/rgl/demo/abundance.r
/usr/lib64/R/library/rgl/demo/bivar.r
/usr/lib64/R/library/rgl/demo/envmap.r
/usr/lib64/R/library/rgl/demo/flag.R
/usr/lib64/R/library/rgl/demo/hist3d.r
/usr/lib64/R/library/rgl/demo/lollipop3d.R
/usr/lib64/R/library/rgl/demo/lsystem.r
/usr/lib64/R/library/rgl/demo/mouseCallbacks.R
/usr/lib64/R/library/rgl/demo/regression.r
/usr/lib64/R/library/rgl/demo/rgl.r
/usr/lib64/R/library/rgl/demo/rglExamples.R
/usr/lib64/R/library/rgl/demo/shapes3d.R
/usr/lib64/R/library/rgl/demo/shinyDemo.R
/usr/lib64/R/library/rgl/demo/shinyToggle.R
/usr/lib64/R/library/rgl/demo/simpleShinyRgl.R
/usr/lib64/R/library/rgl/demo/stereo.R
/usr/lib64/R/library/rgl/demo/subdivision.r
/usr/lib64/R/library/rgl/demodata/population.dat
/usr/lib64/R/library/rgl/demodata/region.dat
/usr/lib64/R/library/rgl/doc/WebGL.R
/usr/lib64/R/library/rgl/doc/WebGL.Rmd
/usr/lib64/R/library/rgl/doc/WebGL.html
/usr/lib64/R/library/rgl/doc/index.html
/usr/lib64/R/library/rgl/doc/legacyWebGL.R
/usr/lib64/R/library/rgl/doc/legacyWebGL.Rmd
/usr/lib64/R/library/rgl/doc/legacyWebGL.html
/usr/lib64/R/library/rgl/doc/rgl.R
/usr/lib64/R/library/rgl/doc/rgl.Rmd
/usr/lib64/R/library/rgl/doc/rgl.html
/usr/lib64/R/library/rgl/fonts/FreeMono.ttf
/usr/lib64/R/library/rgl/fonts/FreeSans.ttf
/usr/lib64/R/library/rgl/fonts/FreeSerif.ttf
/usr/lib64/R/library/rgl/help/AnIndex
/usr/lib64/R/library/rgl/help/aliases.rds
/usr/lib64/R/library/rgl/help/paths.rds
/usr/lib64/R/library/rgl/help/rgl.rdb
/usr/lib64/R/library/rgl/help/rgl.rdx
/usr/lib64/R/library/rgl/html/00Index.html
/usr/lib64/R/library/rgl/html/R.css
/usr/lib64/R/library/rgl/htmlwidgets/lib/CanvasMatrix/CanvasMatrix.src.js
/usr/lib64/R/library/rgl/htmlwidgets/lib/rglClass/rgl.css
/usr/lib64/R/library/rgl/htmlwidgets/lib/rglClass/rglClass.src.js
/usr/lib64/R/library/rgl/htmlwidgets/rglPlayer.js
/usr/lib64/R/library/rgl/htmlwidgets/rglPlayer.yaml
/usr/lib64/R/library/rgl/htmlwidgets/rglWebGL.js
/usr/lib64/R/library/rgl/htmlwidgets/rglWebGL.yaml
/usr/lib64/R/library/rgl/shinyDemo/server.R
/usr/lib64/R/library/rgl/shinyDemo/ui.R
/usr/lib64/R/library/rgl/shinySimple/server.R
/usr/lib64/R/library/rgl/shinySimple/ui.R
/usr/lib64/R/library/rgl/tests/demos.R
/usr/lib64/R/library/rgl/textures/bump_dust.png
/usr/lib64/R/library/rgl/textures/nightfire.png
/usr/lib64/R/library/rgl/textures/particle.png
/usr/lib64/R/library/rgl/textures/refmap.png
/usr/lib64/R/library/rgl/textures/rgl2.png
/usr/lib64/R/library/rgl/textures/sunsleep.png
/usr/lib64/R/library/rgl/textures/world.png
/usr/lib64/R/library/rgl/textures/worldsmall.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/rgl/libs/rgl.so
/usr/lib64/R/library/rgl/libs/rgl.so.avx2
/usr/lib64/R/library/rgl/libs/rgl.so.avx512
