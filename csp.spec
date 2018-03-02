#
# openSUSE RPM spec for tcl-csp package
#

%define buildroot %{_tmppath}/%{name}
%define tarname csp

Name:          tcl-csp
Summary:       Tcl library for Golang style concurrency
Version:       0.1.0_git20151118
Release:       0
License:       MIT
Group:         Development/Libraries/Tcl
Source:        %{tarname}-%{version}.tar.gz
URL:           https://github.com/securitykiss-com/csp
Requires:      tcl >= 8.6
BuildArch:     noarch
BuildRoot:     %{buildroot}

%description
The csp package for Tcl is a concurrency library based on Communicating
Sequential Processes and provides two primitives namely coroutines and
channels which allow concurrent programming in the style of Golang.

%prep
%setup -q -n %{tarname}-%{version}

%build

%install
mkdir -p %{buildroot}%_datadir/tcl/%{tarname}%{version}
cp pkgIndex.tcl %{buildroot}%_datadir/tcl/%{tarname}%{version}
cp csp.tcl %{buildroot}%_datadir/tcl/%{tarname}%{version}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc LICENSE.txt README.md csp.html
%_datadir/tcl/%{tarname}%{version}

