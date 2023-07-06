#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
#
Name     : R-rgl
Version  : 1.2.1
Release  : 78
URL      : https://cran.r-project.org/src/contrib/rgl_1.2.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rgl_1.2.1.tar.gz
Summary  : 3D Visualization Using OpenGL
Group    : Development/Tools
License  : GL2PS GPL-2.0
Requires: R-rgl-lib = %{version}-%{release}
Requires: R-rgl-license = %{version}-%{release}
Requires: R-R6
Requires: R-base64enc
Requires: R-htmltools
Requires: R-htmlwidgets
Requires: R-jsonlite
Requires: R-knitr
Requires: R-magrittr
Requires: R-mime
BuildRequires : R-R6
BuildRequires : R-base64enc
BuildRequires : R-htmltools
BuildRequires : R-htmlwidgets
BuildRequires : R-jsonlite
BuildRequires : R-knitr
BuildRequires : R-magrittr
BuildRequires : R-mime
BuildRequires : R-webshot
BuildRequires : buildreq-R
BuildRequires : freetype-dev
BuildRequires : glu-dev
BuildRequires : mesa-dev
BuildRequires : pkgconfig(freetype2)
BuildRequires : pkgconfig(libpng)
BuildRequires : pkgconfig(x11)

%description
functions modelled on base graphics (plot3d(), etc.) as well as functions for
    constructing representations of geometric objects (cube3d(), etc.).  Output
    may be on screen using OpenGL, or to various standard 3D file formats including
    WebGL, PLY, OBJ, STL as well as 2D image formats, including PNG, Postscript, SVG, PGF.

%package lib
Summary: lib components for the R-rgl package.
Group: Libraries
Requires: R-rgl-license = %{version}-%{release}

%description lib
lib components for the R-rgl package.


%package license
Summary: license components for the R-rgl package.
Group: Default

%description license
license components for the R-rgl package.


%prep
%setup -q -n rgl
pushd ..
cp -a rgl buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1688665217

%install
export SOURCE_DATE_EPOCH=1688665217
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/R-rgl
cp %{_builddir}/rgl/COPYING %{buildroot}/usr/share/package-licenses/R-rgl/4223014cc138a542580deb3408eb736830bf3543 || :
cp %{_builddir}/rgl/src/COPYING.GL2PS %{buildroot}/usr/share/package-licenses/R-rgl/faad94114418f45f4537f08f56abaaeb33f32e8e || :
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
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
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

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/lib64/R/library/rgl/NEWS.md
/usr/lib64/R/library/rgl/R/rgl
/usr/lib64/R/library/rgl/R/rgl.rdb
/usr/lib64/R/library/rgl/R/rgl.rdx
/usr/lib64/R/library/rgl/WORDLIST
/usr/lib64/R/library/rgl/WebGL/template.html
/usr/lib64/R/library/rgl/demo/flag.R
/usr/lib64/R/library/rgl/demo/mouseCallbacks.R
/usr/lib64/R/library/rgl/demo/rgl.r
/usr/lib64/R/library/rgl/demo/shinyDemo.R
/usr/lib64/R/library/rgl/demo/shinyMouse.R
/usr/lib64/R/library/rgl/demo/shinyTabs.R
/usr/lib64/R/library/rgl/demo/shinyToggle.R
/usr/lib64/R/library/rgl/demo/simpleShinyRgl.R
/usr/lib64/R/library/rgl/demo/stereo.R
/usr/lib64/R/library/rgl/demodata/population.dat
/usr/lib64/R/library/rgl/demodata/region.dat
/usr/lib64/R/library/rgl/doc/WebGL.R
/usr/lib64/R/library/rgl/doc/WebGL.Rmd
/usr/lib64/R/library/rgl/doc/WebGL.html
/usr/lib64/R/library/rgl/doc/demos.R
/usr/lib64/R/library/rgl/doc/demos.Rmd
/usr/lib64/R/library/rgl/doc/demos.html
/usr/lib64/R/library/rgl/doc/deprecation.R
/usr/lib64/R/library/rgl/doc/deprecation.Rmd
/usr/lib64/R/library/rgl/doc/deprecation.html
/usr/lib64/R/library/rgl/doc/index.html
/usr/lib64/R/library/rgl/doc/pkgdown.R
/usr/lib64/R/library/rgl/doc/pkgdown.Rmd
/usr/lib64/R/library/rgl/doc/pkgdown.html
/usr/lib64/R/library/rgl/doc/rgl.R
/usr/lib64/R/library/rgl/doc/rgl.Rmd
/usr/lib64/R/library/rgl/doc/rgl.html
/usr/lib64/R/library/rgl/doc/transparency.R
/usr/lib64/R/library/rgl/doc/transparency.Rmd
/usr/lib64/R/library/rgl/doc/transparency.html
/usr/lib64/R/library/rgl/fonts/FreeMono.ttf
/usr/lib64/R/library/rgl/fonts/FreeSans.ttf
/usr/lib64/R/library/rgl/fonts/FreeSerif.ttf
/usr/lib64/R/library/rgl/help/AnIndex
/usr/lib64/R/library/rgl/help/aliases.rds
/usr/lib64/R/library/rgl/help/figures/READMEpolyhedra-1-rgl.png
/usr/lib64/R/library/rgl/help/paths.rds
/usr/lib64/R/library/rgl/help/rgl.rdb
/usr/lib64/R/library/rgl/help/rgl.rdx
/usr/lib64/R/library/rgl/html/00Index.html
/usr/lib64/R/library/rgl/html/R.css
/usr/lib64/R/library/rgl/htmlwidgets/lib/CanvasMatrix/CanvasMatrix.min.js
/usr/lib64/R/library/rgl/htmlwidgets/lib/CanvasMatrix/CanvasMatrix.src.js
/usr/lib64/R/library/rgl/htmlwidgets/lib/rglClass/JSDoc.json
/usr/lib64/R/library/rgl/htmlwidgets/lib/rglClass/animation.src.js
/usr/lib64/R/library/rgl/htmlwidgets/lib/rglClass/axes.src.js
/usr/lib64/R/library/rgl/htmlwidgets/lib/rglClass/buffer.src.js
/usr/lib64/R/library/rgl/htmlwidgets/lib/rglClass/controls.src.js
/usr/lib64/R/library/rgl/htmlwidgets/lib/rglClass/draw.src.js
/usr/lib64/R/library/rgl/htmlwidgets/lib/rglClass/init.src.js
/usr/lib64/R/library/rgl/htmlwidgets/lib/rglClass/mouse.src.js
/usr/lib64/R/library/rgl/htmlwidgets/lib/rglClass/pieces.src.js
/usr/lib64/R/library/rgl/htmlwidgets/lib/rglClass/pretty.src.js
/usr/lib64/R/library/rgl/htmlwidgets/lib/rglClass/projection.src.js
/usr/lib64/R/library/rgl/htmlwidgets/lib/rglClass/rgl.css
/usr/lib64/R/library/rgl/htmlwidgets/lib/rglClass/rglClass.min.js
/usr/lib64/R/library/rgl/htmlwidgets/lib/rglClass/rglClass.src.js
/usr/lib64/R/library/rgl/htmlwidgets/lib/rglClass/rglTimer.src.js
/usr/lib64/R/library/rgl/htmlwidgets/lib/rglClass/selection.src.js
/usr/lib64/R/library/rgl/htmlwidgets/lib/rglClass/shaders.src.js
/usr/lib64/R/library/rgl/htmlwidgets/lib/rglClass/shaders/rgl_fragment.glsl
/usr/lib64/R/library/rgl/htmlwidgets/lib/rglClass/shaders/rgl_vertex.glsl
/usr/lib64/R/library/rgl/htmlwidgets/lib/rglClass/shadersrc.src.js
/usr/lib64/R/library/rgl/htmlwidgets/lib/rglClass/subscenes.src.js
/usr/lib64/R/library/rgl/htmlwidgets/lib/rglClass/textures.src.js
/usr/lib64/R/library/rgl/htmlwidgets/lib/rglClass/utils.src.js
/usr/lib64/R/library/rgl/htmlwidgets/rglPlayer.js
/usr/lib64/R/library/rgl/htmlwidgets/rglWebGL.js
/usr/lib64/R/library/rgl/pkgdown/templates/after-head.html
/usr/lib64/R/library/rgl/slowTests/demos.R
/usr/lib64/R/library/rgl/tests/bbox3dtests.R
/usr/lib64/R/library/rgl/tests/boundary.R
/usr/lib64/R/library/rgl/tests/indices.R
/usr/lib64/R/library/rgl/tests/testthat.R
/usr/lib64/R/library/rgl/tests/testthat/conversions.R
/usr/lib64/R/library/rgl/tests/testthat/test-as.mesh3d.R
/usr/lib64/R/library/rgl/tests/testthat/test-getShaders.R
/usr/lib64/R/library/rgl/tests/testthat/test-mesh3d.R
/usr/lib64/R/library/rgl/tests/testthat/test-obj.R
/usr/lib64/R/library/rgl/tests/testthat/test-r3d.R
/usr/lib64/R/library/rgl/tests/testthat/test-subscenes.R
/usr/lib64/R/library/rgl/tests/testthat/test-surfaces.R
/usr/lib64/R/library/rgl/tests/testthat/test-tags.R
/usr/lib64/R/library/rgl/tests/testthat/test-user2window.R
/usr/lib64/R/library/rgl/tests/testthat/testdata/mergeVertices.rds
/usr/lib64/R/library/rgl/tests/testthat/testdata/obj.rds
/usr/lib64/R/library/rgl/tests/testthat/testdata/qmesh3d.rds
/usr/lib64/R/library/rgl/tests/testthat/testdata/r3d.rds
/usr/lib64/R/library/rgl/tests/testthat/testdata/shade3detc.rds
/usr/lib64/R/library/rgl/tests/testthat/testdata/subscenes.rds
/usr/lib64/R/library/rgl/tests/testthat/testdata/tmesh3d.rds
/usr/lib64/R/library/rgl/tests/testthat/testdata/transformations.rds
/usr/lib64/R/library/rgl/tests/unfixed.R
/usr/lib64/R/library/rgl/tests/userTexture.R
/usr/lib64/R/library/rgl/tests/widgetlighting.R
/usr/lib64/R/library/rgl/textures/bump_dust.png
/usr/lib64/R/library/rgl/textures/nightfire.png
/usr/lib64/R/library/rgl/textures/particle.png
/usr/lib64/R/library/rgl/textures/refmap.png
/usr/lib64/R/library/rgl/textures/rgl2.png
/usr/lib64/R/library/rgl/textures/sunsleep.png
/usr/lib64/R/library/rgl/textures/world.png
/usr/lib64/R/library/rgl/textures/worldsmall.png
/usr/lib64/R/library/rgl/useNULL/README.txt

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/rgl/libs/rgl.so
/usr/lib64/R/library/rgl/libs/rgl.so.avx2
/usr/lib64/R/library/rgl/libs/rgl.so.avx512
/usr/lib64/R/library/rgl/useNULL/rgl.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/R-rgl/4223014cc138a542580deb3408eb736830bf3543
/usr/share/package-licenses/R-rgl/faad94114418f45f4537f08f56abaaeb33f32e8e
