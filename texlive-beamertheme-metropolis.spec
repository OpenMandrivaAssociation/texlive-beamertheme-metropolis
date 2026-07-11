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
BuildSystem:	texlive
Requires:	texlive(pgfopts)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a simple, modern Beamer theme for anyone to use. It
tries to minimize noise and maximize space for content.

