%global tl_name beamertheme-metropolis
%global tl_revision 78281

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	A modern LaTeX beamer theme
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/themes/metropolis
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-metropolis.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-metropolis.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-metropolis.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Requires:	texlive(pgfopts)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a simple, modern Beamer theme for anyone to use. It
tries to minimize noise and maximize space for content.

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
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/beamertheme-metropolis
%dir %{_datadir}/texmf-dist/source/latex/beamertheme-metropolis
%dir %{_datadir}/texmf-dist/tex/latex/beamertheme-metropolis
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-metropolis/README.md
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-metropolis/demo.bib
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-metropolis/demo.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-metropolis/demo.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-metropolis/metropolistheme.pdf
%doc %{_datadir}/texmf-dist/source/latex/beamertheme-metropolis/beamercolorthememetropolis-highcontrast.dtx
%doc %{_datadir}/texmf-dist/source/latex/beamertheme-metropolis/beamercolorthememetropolis.dtx
%doc %{_datadir}/texmf-dist/source/latex/beamertheme-metropolis/beamerfontthememetropolis.dtx
%doc %{_datadir}/texmf-dist/source/latex/beamertheme-metropolis/beamerinnerthememetropolis.dtx
%doc %{_datadir}/texmf-dist/source/latex/beamertheme-metropolis/beamerouterthememetropolis.dtx
%doc %{_datadir}/texmf-dist/source/latex/beamertheme-metropolis/beamerthememetropolis.dtx
%doc %{_datadir}/texmf-dist/source/latex/beamertheme-metropolis/beamerthememetropolis.ins
%doc %{_datadir}/texmf-dist/source/latex/beamertheme-metropolis/metropolistheme.dtx
%doc %{_datadir}/texmf-dist/source/latex/beamertheme-metropolis/pgfplotsthemetol.dtx
%{_datadir}/texmf-dist/tex/latex/beamertheme-metropolis/beamercolorthememetropolis-highcontrast.sty
%{_datadir}/texmf-dist/tex/latex/beamertheme-metropolis/beamercolorthememetropolis.sty
%{_datadir}/texmf-dist/tex/latex/beamertheme-metropolis/beamerfontthememetropolis.sty
%{_datadir}/texmf-dist/tex/latex/beamertheme-metropolis/beamerinnerthememetropolis.sty
%{_datadir}/texmf-dist/tex/latex/beamertheme-metropolis/beamerouterthememetropolis.sty
%{_datadir}/texmf-dist/tex/latex/beamertheme-metropolis/beamerthememetropolis.sty
%{_datadir}/texmf-dist/tex/latex/beamertheme-metropolis/pgfplotsthemetol.sty
