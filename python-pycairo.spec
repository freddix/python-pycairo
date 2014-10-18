%define		pname py2cairo

Summary:	Python Cairo bindings
Name:		python-pycairo
Version:	1.10.0
Release:	3
License:	LGPL v2.1 or MPL v1.1
Group:		Libraries
Source0:	http://cairographics.org/releases/%{pname}-%{version}.tar.bz2
# Source0-md5:	20337132c4ab06c1146ad384d55372c5
URL:		http://cairographics.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cairo-devel
BuildRequires:	libtool
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python Cairo bindings.

%package devel
Summary:	Development files for pycairo
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development files for pycairo.

%prep
%setup -qn %{pname}-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{py_sitedir}/cairo/*.{la,py}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README
%dir %{py_sitedir}/cairo
%attr(755,root,root) %{py_sitedir}/cairo/*.so
%{py_sitedir}/cairo/*.py[oc]

%files devel
%defattr(644,root,root,755)
%{_includedir}/pycairo
%{_pkgconfigdir}/pycairo.pc

