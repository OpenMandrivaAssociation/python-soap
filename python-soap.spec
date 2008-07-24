Name:            python-soap
Summary:         A SOAP library for python
Version:         0.12.0
Release:         %mkrel 6
Epoch:           0
Source0:         http://ovh.dl.sourceforge.net/sourceforge/pywebsvcs/SOAPpy-%{version}.tar.bz2
Patch0:          SOAPpy-0.12.0-future.patch
URL:             http://pywebsvcs.sourceforge.net/
License:         BSD
Group:           Development/Python
BuildRoot:       %{_tmppath}/%{name}-buildroot
BuildArch:       noarch
Requires:        python-fpconst
BuildRequires:   python-fpconst
BuildRequires:   python-devel
Provides:        SOAPpy = %{epoch}:%{version}-%{release}

%description
Web services for Python programmers, both client and servers. This
includes SOAP, WSDL, UDDI, etc.

%prep
%setup -q -n SOAPpy-%{version}
%patch0 -p1

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --root=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc docs/* validate tests tools contrib bid
%{python_sitelib}/*


