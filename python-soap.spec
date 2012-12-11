Name:            python-soap
Summary:         A SOAP library for python
Version:         0.12.0
Release:         %mkrel 9
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




%changelog
* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0:0.12.0-9mdv2010.0
+ Revision: 442486
- rebuild

* Sun Dec 28 2008 Funda Wang <fwang@mandriva.org> 0:0.12.0-8mdv2009.1
+ Revision: 320163
- rebuild for new python

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0:0.12.0-7mdv2009.0
+ Revision: 259808
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 0:0.12.0-6mdv2009.0
+ Revision: 247639
- rebuild

* Sat Dec 29 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0:0.12.0-4mdv2008.1
+ Revision: 139214
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Dec 09 2006 David Walluck <walluck@mandriva.org> 0.12.0-3mdv2007.0
+ Revision: 93953
- rebuild for new python
- Import python-soap

* Sun Sep 03 2006 David Walluck <walluck@mandriva.org> 0:0.12.0-2mdv2007.0
- remove %%pyver from Requires

* Sun Sep 03 2006 David Walluck <walluck@mandriva.org> 0:0.12.0-1mdv2007.0
- 0.12.0
- provide SOAPpy
- add Source0 URL
- use python macros

* Sat May 21 2005 Lenny Cartier <lenny@mandriva.com> 0.11.6-1mdk
- 0.11.6
- get complete pyver

* Sun Dec 05 2004 Michael Scherer <misc@mandrake.org> 0.11.3-2mdk
- Rebuild for new  python

* Sun Feb 22 2004 Austin Acton <austin@mandrake.org> 0.11.3-1mdk
- first release

