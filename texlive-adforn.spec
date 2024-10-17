Name:		texlive-adforn
Version:	54512
Release:	2
Summary:	OrnementsADF font with TeX/LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/adforn
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/adforn.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/adforn.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle provides the Ornements ADF font in PostScript type 1
format with TeX/LaTeX support files. The font is licensed under
GPL v2 or later with font exception. (See NOTICE, COPYING,
README.) The TeX/LaTeX support is licensed under LPPL. (See
README, manifest.txt.).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/arkandis/adforn/OrnementsADF.afm
%{_texmfdistdir}/fonts/enc/dvips/adforn/OrnementsADF.enc
%{_texmfdistdir}/fonts/map/dvips/adforn/OrnementsADF.map
%{_texmfdistdir}/fonts/tfm/arkandis/adforn/OrnementsADF.tfm
%{_texmfdistdir}/fonts/type1/arkandis/adforn/OrnementsADF.pfb
%{_texmfdistdir}/tex/latex/adforn/adforn.sty
%{_texmfdistdir}/tex/latex/adforn/uornementsadf.fd
%doc %{_texmfdistdir}/doc/fonts/adforn/COPYING
%doc %{_texmfdistdir}/doc/fonts/adforn/NOTICE
%doc %{_texmfdistdir}/doc/fonts/adforn/README
%doc %{_texmfdistdir}/doc/fonts/adforn/adforn.pdf
%doc %{_texmfdistdir}/doc/fonts/adforn/adforn.tex
%doc %{_texmfdistdir}/doc/fonts/adforn/manifest.txt

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
