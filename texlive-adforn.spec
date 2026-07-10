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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle provides the Ornements ADF font in PostScript type 1 format
with TeX/LaTeX support files. The font is licensed under GPL v2 or later
with font exception. (See NOTICE, COPYING, README.) The TeX/LaTeX
support is licensed under LPPL. (See README, manifest.txt.)

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/fonts
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/fonts
%dir %{_datadir}/texmf-dist/fonts/afm
%dir %{_datadir}/texmf-dist/fonts/enc
%dir %{_datadir}/texmf-dist/fonts/map
%dir %{_datadir}/texmf-dist/fonts/tfm
%dir %{_datadir}/texmf-dist/fonts/type1
%dir %{_datadir}/texmf-dist/source/fonts
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/fonts/adforn
%dir %{_datadir}/texmf-dist/fonts/afm/arkandis
%dir %{_datadir}/texmf-dist/fonts/enc/dvips
%dir %{_datadir}/texmf-dist/fonts/map/dvips
%dir %{_datadir}/texmf-dist/fonts/tfm/arkandis
%dir %{_datadir}/texmf-dist/fonts/type1/arkandis
%dir %{_datadir}/texmf-dist/source/fonts/adforn
%dir %{_datadir}/texmf-dist/tex/latex/adforn
%dir %{_datadir}/texmf-dist/fonts/afm/arkandis/adforn
%dir %{_datadir}/texmf-dist/fonts/enc/dvips/adforn
%dir %{_datadir}/texmf-dist/fonts/map/dvips/adforn
%dir %{_datadir}/texmf-dist/fonts/tfm/arkandis/adforn
%dir %{_datadir}/texmf-dist/fonts/type1/arkandis/adforn
%doc %{_datadir}/texmf-dist/doc/fonts/adforn/COPYING
%doc %{_datadir}/texmf-dist/doc/fonts/adforn/NOTICE
%doc %{_datadir}/texmf-dist/doc/fonts/adforn/README.md
%doc %{_datadir}/texmf-dist/doc/fonts/adforn/adforn-tables.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/adforn/adforn-tables.tex
%doc %{_datadir}/texmf-dist/doc/fonts/adforn/adforn.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/adforn/manifest.txt
%{_datadir}/texmf-dist/fonts/afm/arkandis/adforn/OrnementsADF.afm
%{_datadir}/texmf-dist/fonts/enc/dvips/adforn/OrnementsADF.enc
%{_datadir}/texmf-dist/fonts/map/dvips/adforn/adforn.map
%{_datadir}/texmf-dist/fonts/tfm/arkandis/adforn/OrnementsADF.tfm
%{_datadir}/texmf-dist/fonts/type1/arkandis/adforn/OrnementsADF.pfb
%doc %{_datadir}/texmf-dist/source/fonts/adforn/adforn.dtx
%doc %{_datadir}/texmf-dist/source/fonts/adforn/adforn.ins
%{_datadir}/texmf-dist/tex/latex/adforn/adforn.sty
%{_datadir}/texmf-dist/tex/latex/adforn/uornementsadf.fd
