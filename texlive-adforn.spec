Name:		texlive-adforn
Version:	1.001.b.2
Release:	1
Summary:	OrnementsADF font with TeX/LaTeX support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/adforn
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/adforn.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/adforn.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The bundle provides the Ornements ADF font in PostScript type 1
format with TeX/LaTeX support files. The font is licensed under
GPL v2 or later with font exception. (See NOTICE, COPYING,
README.) The TeX/LaTeX support is licensed under LPPL. (See
README, manifest.txt.).

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/arkandis/adforn/OrnementsADF.afm
%{_texmfdistdir}/fonts/enc/dvips/adforn/OrnementsADF.enc
%{_texmfdistdir}/fonts/map/dvips/adforn/OrnementsADF.map
%{_texmfdistdir}/fonts/tfm/arkandis/adforn/OrnementsADF.tfm
%{_texmfdistdir}/fonts/type1/arkandis/adforn/OrnementsADF.pfb
%{_texmfdistdir}/fonts/type1/arkandis/adforn/OrnementsADF.pfm
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
