Name:		texlive-beamertheme-metropolis
Version:	43031
Release:	2
Summary:	A modern LaTeX beamer theme
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/beamertheme-metropolis
License:	other-free
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-metropolis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-metropolis.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-metropolis.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a simple, modern Beamer theme for anyone
to use. It tries to minimize noise and maximize space for
content.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/beamertheme-metropolis
%{_texmfdistdir}/tex/latex/beamertheme-metropolis
%doc %{_texmfdistdir}/doc/latex/beamertheme-metropolis

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
