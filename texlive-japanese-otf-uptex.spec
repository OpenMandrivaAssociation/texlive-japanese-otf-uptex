# revision 25293
# category Package
# catalog-ctan /language/japanese/japanese-otf-uptex
# catalog-date 2012-02-02 11:15:04 +0100
# catalog-license other-free
# catalog-version undef
Name:		texlive-japanese-otf-uptex
Version:	20120202
Release:	1
Summary:	Support for Japanese OTF files in upLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/japanese/japanese-otf-uptex
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/japanese-otf-uptex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/japanese-otf-uptex.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/japanese-otf-uptex.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-japanese-otf

%description
The bundle offers support of the fonts in the japanese-otf
package, for use with the UpTeX distribution (version 0.20 or
later).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/map/dvipdfmx/japanese-otf-uptex/otf-up-noEmbed.map
%{_texmfdistdir}/fonts/tfm/public/japanese-otf-uptex/hmgothr-h.tfm
%{_texmfdistdir}/fonts/tfm/public/japanese-otf-uptex/hmgothr-v.tfm
%{_texmfdistdir}/fonts/tfm/public/japanese-otf-uptex/upexpgothb-h.tfm
%{_texmfdistdir}/fonts/tfm/public/japanese-otf-uptex/upexpgothb-v.tfm
%{_texmfdistdir}/fonts/tfm/public/japanese-otf-uptex/upexpgothr-h.tfm
%{_texmfdistdir}/fonts/tfm/public/japanese-otf-uptex/upexpgothr-v.tfm
%{_texmfdistdir}/fonts/tfm/public/japanese-otf-uptex/upexpmgothr-h.tfm
%{_texmfdistdir}/fonts/tfm/public/japanese-otf-uptex/upexpmgothr-v.tfm
%{_texmfdistdir}/fonts/tfm/public/japanese-otf-uptex/upexpminb-h.tfm
%{_texmfdistdir}/fonts/tfm/public/japanese-otf-uptex/upexpminb-v.tfm
%{_texmfdistdir}/fonts/tfm/public/japanese-otf-uptex/upexpminl-h.tfm
%{_texmfdistdir}/fonts/tfm/public/japanese-otf-uptex/upexpminl-v.tfm
%{_texmfdistdir}/fonts/tfm/public/japanese-otf-uptex/upexpminr-h.tfm
%{_texmfdistdir}/fonts/tfm/public/japanese-otf-uptex/upexpminr-v.tfm
%{_texmfdistdir}/fonts/tfm/public/japanese-otf-uptex/uphgothb-h.tfm
%{_texmfdistdir}/fonts/tfm/public/japanese-otf-uptex/uphgothb-v.tfm
%{_texmfdistdir}/fonts/tfm/public/japanese-otf-uptex/uphgotheb-h.tfm
%{_texmfdistdir}/fonts/tfm/public/japanese-otf-uptex/uphgotheb-v.tfm
%{_texmfdistdir}/fonts/tfm/public/japanese-otf-uptex/uphgothr-h.tfm
%{_texmfdistdir}/fonts/tfm/public/japanese-otf-uptex/uphgothr-v.tfm
%{_texmfdistdir}/fonts/tfm/public/japanese-otf-uptex/uphmgothr-h.tfm
%{_texmfdistdir}/fonts/tfm/public/japanese-otf-uptex/uphmgothr-v.tfm
%{_texmfdistdir}/fonts/tfm/public/japanese-otf-uptex/uphminb-h.tfm
%{_texmfdistdir}/fonts/tfm/public/japanese-otf-uptex/uphminb-v.tfm
%{_texmfdistdir}/fonts/tfm/public/japanese-otf-uptex/uphminl-h.tfm
%{_texmfdistdir}/fonts/tfm/public/japanese-otf-uptex/uphminl-v.tfm
%{_texmfdistdir}/fonts/tfm/public/japanese-otf-uptex/uphminr-h.tfm
%{_texmfdistdir}/fonts/tfm/public/japanese-otf-uptex/uphminr-v.tfm
%{_texmfdistdir}/fonts/tfm/public/japanese-otf-uptex/upnmlgothb-h.tfm
%{_texmfdistdir}/fonts/tfm/public/japanese-otf-uptex/upnmlgothb-v.tfm
%{_texmfdistdir}/fonts/tfm/public/japanese-otf-uptex/upnmlgotheb-h.tfm
%{_texmfdistdir}/fonts/tfm/public/japanese-otf-uptex/upnmlgotheb-v.tfm
%{_texmfdistdir}/fonts/tfm/public/japanese-otf-uptex/upnmlgothr-h.tfm
%{_texmfdistdir}/fonts/tfm/public/japanese-otf-uptex/upnmlgothr-v.tfm
%{_texmfdistdir}/fonts/tfm/public/japanese-otf-uptex/upnmlmgothr-h.tfm
%{_texmfdistdir}/fonts/tfm/public/japanese-otf-uptex/upnmlmgothr-v.tfm
%{_texmfdistdir}/fonts/tfm/public/japanese-otf-uptex/upnmlminb-h.tfm
%{_texmfdistdir}/fonts/tfm/public/japanese-otf-uptex/upnmlminb-v.tfm
%{_texmfdistdir}/fonts/tfm/public/japanese-otf-uptex/upnmlminl-h.tfm
%{_texmfdistdir}/fonts/tfm/public/japanese-otf-uptex/upnmlminl-v.tfm
%{_texmfdistdir}/fonts/tfm/public/japanese-otf-uptex/upnmlminr-h.tfm
%{_texmfdistdir}/fonts/tfm/public/japanese-otf-uptex/upnmlminr-v.tfm
%{_texmfdistdir}/fonts/tfm/public/japanese-otf-uptex/uprubygothb-h.tfm
%{_texmfdistdir}/fonts/tfm/public/japanese-otf-uptex/uprubygothb-v.tfm
%{_texmfdistdir}/fonts/tfm/public/japanese-otf-uptex/uprubygothr-h.tfm
%{_texmfdistdir}/fonts/tfm/public/japanese-otf-uptex/uprubygothr-v.tfm
%{_texmfdistdir}/fonts/tfm/public/japanese-otf-uptex/uprubymgothr-h.tfm
%{_texmfdistdir}/fonts/tfm/public/japanese-otf-uptex/uprubymgothr-v.tfm
%{_texmfdistdir}/fonts/tfm/public/japanese-otf-uptex/uprubyminb-h.tfm
%{_texmfdistdir}/fonts/tfm/public/japanese-otf-uptex/uprubyminb-v.tfm
%{_texmfdistdir}/fonts/tfm/public/japanese-otf-uptex/uprubyminl-h.tfm
%{_texmfdistdir}/fonts/tfm/public/japanese-otf-uptex/uprubyminl-v.tfm
%{_texmfdistdir}/fonts/tfm/public/japanese-otf-uptex/uprubyminr-h.tfm
%{_texmfdistdir}/fonts/tfm/public/japanese-otf-uptex/uprubyminr-v.tfm
%{_texmfdistdir}/fonts/vf/public/japanese-otf-uptex/upexpgothb-h.vf
%{_texmfdistdir}/fonts/vf/public/japanese-otf-uptex/upexpgothb-v.vf
%{_texmfdistdir}/fonts/vf/public/japanese-otf-uptex/upexpgothr-h.vf
%{_texmfdistdir}/fonts/vf/public/japanese-otf-uptex/upexpgothr-v.vf
%{_texmfdistdir}/fonts/vf/public/japanese-otf-uptex/upexpmgothr-h.vf
%{_texmfdistdir}/fonts/vf/public/japanese-otf-uptex/upexpmgothr-v.vf
%{_texmfdistdir}/fonts/vf/public/japanese-otf-uptex/upexpminb-h.vf
%{_texmfdistdir}/fonts/vf/public/japanese-otf-uptex/upexpminb-v.vf
%{_texmfdistdir}/fonts/vf/public/japanese-otf-uptex/upexpminl-h.vf
%{_texmfdistdir}/fonts/vf/public/japanese-otf-uptex/upexpminl-v.vf
%{_texmfdistdir}/fonts/vf/public/japanese-otf-uptex/upexpminr-h.vf
%{_texmfdistdir}/fonts/vf/public/japanese-otf-uptex/upexpminr-v.vf
%{_texmfdistdir}/fonts/vf/public/japanese-otf-uptex/upnmlgothb-h.vf
%{_texmfdistdir}/fonts/vf/public/japanese-otf-uptex/upnmlgothb-v.vf
%{_texmfdistdir}/fonts/vf/public/japanese-otf-uptex/upnmlgotheb-h.vf
%{_texmfdistdir}/fonts/vf/public/japanese-otf-uptex/upnmlgotheb-v.vf
%{_texmfdistdir}/fonts/vf/public/japanese-otf-uptex/upnmlgothr-h.vf
%{_texmfdistdir}/fonts/vf/public/japanese-otf-uptex/upnmlgothr-v.vf
%{_texmfdistdir}/fonts/vf/public/japanese-otf-uptex/upnmlmgothr-h.vf
%{_texmfdistdir}/fonts/vf/public/japanese-otf-uptex/upnmlmgothr-v.vf
%{_texmfdistdir}/fonts/vf/public/japanese-otf-uptex/upnmlminb-h.vf
%{_texmfdistdir}/fonts/vf/public/japanese-otf-uptex/upnmlminb-v.vf
%{_texmfdistdir}/fonts/vf/public/japanese-otf-uptex/upnmlminl-h.vf
%{_texmfdistdir}/fonts/vf/public/japanese-otf-uptex/upnmlminl-v.vf
%{_texmfdistdir}/fonts/vf/public/japanese-otf-uptex/upnmlminr-h.vf
%{_texmfdistdir}/fonts/vf/public/japanese-otf-uptex/upnmlminr-v.vf
%{_texmfdistdir}/fonts/vf/public/japanese-otf-uptex/uprubygothb-h.vf
%{_texmfdistdir}/fonts/vf/public/japanese-otf-uptex/uprubygothb-v.vf
%{_texmfdistdir}/fonts/vf/public/japanese-otf-uptex/uprubygothr-h.vf
%{_texmfdistdir}/fonts/vf/public/japanese-otf-uptex/uprubygothr-v.vf
%{_texmfdistdir}/fonts/vf/public/japanese-otf-uptex/uprubymgothr-h.vf
%{_texmfdistdir}/fonts/vf/public/japanese-otf-uptex/uprubymgothr-v.vf
%{_texmfdistdir}/fonts/vf/public/japanese-otf-uptex/uprubyminb-h.vf
%{_texmfdistdir}/fonts/vf/public/japanese-otf-uptex/uprubyminb-v.vf
%{_texmfdistdir}/fonts/vf/public/japanese-otf-uptex/uprubyminl-h.vf
%{_texmfdistdir}/fonts/vf/public/japanese-otf-uptex/uprubyminl-v.vf
%{_texmfdistdir}/fonts/vf/public/japanese-otf-uptex/uprubyminr-h.vf
%{_texmfdistdir}/fonts/vf/public/japanese-otf-uptex/uprubyminr-v.vf
%doc %{_texmfdistdir}/doc/fonts/japanese-otf-uptex/00otf-uptex.txt
%doc %{_texmfdistdir}/doc/fonts/japanese-otf-uptex/COPYRIGHT
%doc %{_texmfdistdir}/doc/fonts/japanese-otf-uptex/README
#- source
%doc %{_texmfdistdir}/source/fonts/japanese-otf-uptex/basepl/ubase-h.pl
%doc %{_texmfdistdir}/source/fonts/japanese-otf-uptex/basepl/ubase-v.pl
%doc %{_texmfdistdir}/source/fonts/japanese-otf-uptex/fontmap/ckt.map?for?udvips?
%doc %{_texmfdistdir}/source/fonts/japanese-otf-uptex/fontmap/cktx.map?for?dvipdfmx?
%doc %{_texmfdistdir}/source/fonts/japanese-otf-uptex/fontmap/hiragino.map?for?udvips?
%doc %{_texmfdistdir}/source/fonts/japanese-otf-uptex/fontmap/hiraginox.map?for?dvipdfmx?
%doc %{_texmfdistdir}/source/fonts/japanese-otf-uptex/fontmap/kozuka.map
%doc %{_texmfdistdir}/source/fonts/japanese-otf-uptex/fontmap/kozukax.map
%doc %{_texmfdistdir}/source/fonts/japanese-otf-uptex/fontmap/morisawa.map?for?udvips?
%doc %{_texmfdistdir}/source/fonts/japanese-otf-uptex/fontmap/morisawax.map?for?dvipdfmx?
%doc %{_texmfdistdir}/source/fonts/japanese-otf-uptex/fontmap/vfontmap.txt
%doc %{_texmfdistdir}/source/fonts/japanese-otf-uptex/patch/otfbeta_uptex-0.07.patch
%doc %{_texmfdistdir}/source/fonts/japanese-otf-uptex/test/uplatex/Makefile
%doc %{_texmfdistdir}/source/fonts/japanese-otf-uptex/test/uplatex/uotftest-utf8.tex
%doc %{_texmfdistdir}/source/fonts/japanese-otf-uptex/test/uplatex/uotftest.tex
%doc %{_texmfdistdir}/source/fonts/japanese-otf-uptex/umakeotf
%doc %{_texmfdistdir}/source/fonts/japanese-otf-uptex/umkjvf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc source %{buildroot}%{_texmfdistdir}
