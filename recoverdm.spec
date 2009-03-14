Summary:	recoverdm - recover files/disks with damaged sectors
Summary(pl.UTF-8):	recoverdm - odzyskuje pliki/dyski z uszkodzonymi sektorami
Name:		recoverdm
Version:	0.20
Release:	1
License:	distributable
Group:		Applications/System
Source0:	http://www.vanheusden.com/recoverdm/%{name}-%{version}.tgz
# Source0-md5:	9da9ea7d44f8f94984715eb2ff1ecab4
Patch0:		%{name}-VERSION.patch
URL:		http://www.vanheusden.com/recoverdm/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program will help you recover disks with bad sectors. You can
recover files as well as complete devices.

%description -l pl.UTF-8
Ten program pomoże Ci odzyskać dyski ze złymi sektorami. Możesz
odzyskać zarówno pliki jak i całe urządzenia.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	LDFLAGS="%{rpmldflags}" \
	CFLAGS="%{rpmcflags} -Wall -Wshadow -Wwrite-strings -Wconversion -Winline"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install recoverdm $RPM_BUILD_ROOT%{_bindir}
install mergebad  $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
