
# conditional build:
# _without_dist_kernel    without kernel from distribution

Summary:	recoverdm - recover files/disks with damaged sectors
Summary(pl):	recoverdm - odzyskuje pliki/dyski z uszkodzonymi sektorami
Name:		recoverdm
Version:	0.14
Release:	1
License:	distributable
Group:		Applications/System
Source0:	http://www.vanheusden.com/recoverdm/%{name}-%{version}.tgz
URL:		http://www.vanheusden.com/recoverdm/
BuildRequires:	fvhlib-devel >= 2.0
%{!?_without_dist_kernel:BuildRequires: kernel-headers}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program will help you recover disks with bad sectors. You can
recover files as well as complete devices.

%description -l pl
Ten program pomo¿e Ci odzyskaæ dyski ze z³ymi sektorami. Mo¿esz
odzyskaæ zarówno pliki jak i ca³e urz±dzenia.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install recoverdm $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
