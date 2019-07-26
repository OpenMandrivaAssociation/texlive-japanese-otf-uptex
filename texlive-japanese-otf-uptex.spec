%global __requires_exclude perl\\((script::MakeSPList)\\)

Name:		texlive-japanese-otf-uptex
Epoch:		1
Version:	0.18
Release:	3
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
%{_texmfdistdir}/fonts/ovp/public/japanese-otf-uptex
%{_texmfdistdir}/fonts/tfm/public/japanese-otf-uptex
%{_texmfdistdir}/fonts/vf/public/japanese-otf-uptex
%{_texmfdistdir}/tex/platex/japanese-otf-uptex
%doc %{_texmfdistdir}/doc/fonts/japanese-otf-uptex
#- source
%doc %{_texmfdistdir}/source/fonts/japanese-otf-uptex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
