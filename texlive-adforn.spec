%global tl_name adforn
%global tl_revision 78315

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.4
Release:	%{tl_revision}.1
Summary:	OrnementsADF font with TeX/LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/adforn
License:	lppl1.3c gpl2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/adforn.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/adforn.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/adforn.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle provides the Ornements ADF font in PostScript type 1 format
with TeX/LaTeX support files. The font is licensed under GPL v2 or later
with font exception. (See NOTICE, COPYING, README.) The TeX/LaTeX
support is licensed under LPPL. (See README, manifest.txt.)

