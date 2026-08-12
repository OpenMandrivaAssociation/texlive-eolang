%global tl_name eolang
%global tl_revision 79939
%global tl_version 0.24.0
%global tl_bin_links eolang:%{_texmfdistdir}/scripts/eolang/eolang.pl

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	Formulas and graphs for the EO programming language
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/eolang
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/eolang.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/eolang.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/eolang.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(adjustbox)
Requires:	texlive(amsfonts)
Requires:	texlive(amsmath)
Requires:	texlive(eolang.bin)
Requires:	texlive(everyshi)
Requires:	texlive(fancyvrb)
Requires:	texlive(hyperref)
Requires:	texlive(iexec)
Requires:	texlive(pdftexcmds)
Requires:	texlive(pgf)
Requires:	texlive(pgfopts)
Requires:	texlive(stmaryrd)
Requires:	texlive(xstring)
Provides:	texlive(%{tl_name}) = %{version}
Provides:	texlive(%{tl_name}.bin) = %{version}
Provides:	texlive-%{tl_name}.bin = %{EVRD}

%description
This package helps you format expressions of [?] -calculus and draw SODG
graphs for the EO programming language.

