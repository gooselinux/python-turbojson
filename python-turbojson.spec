%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?pyver: %define pyver %(%{__python} -c "import sys ; print sys.version[:3]")}

%define module turbojson

Name:           python-turbojson
Version:        1.2.1
Release:        8.1%{?dist}
Summary:        Python template plugin that supports json

Group:          Development/Languages
License:        MIT
URL:            http://cheeseshop.python.org/pypi/TurboJson
Source0:        http://pypi.python.org/packages/source/T/TurboJson/TurboJson-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires: python-devel
BuildRequires: python-setuptools-devel
BuildRequires: python-prioritized-methods > 0.2
BuildRequires: python-peak-rules >= 0.5a1.dev-0.2555
BuildRequires: python-simplejson >= 1.9.1
BuildRequires: python-nose

Requires:      python-peak-rules >= 0.5a1.dev-0.2555
Requires:      python-simplejson >= 1.9.1
Requires:      python-prioritized-methods > 0.2

%description
This package provides a template engine plugin, allowing you
to easily use Json with TurboGears, Buffet or other systems
that support python.templating.engines.


%prep
%setup -q -n TurboJson-%{version}

%build
%{__python} setup.py build


%install
rm -rf %{buildroot}
%{__python} setup.py install --skip-build --root=%{buildroot}

%check
python setup.py test

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{python_sitelib}/%{module}/
%{python_sitelib}/TurboJson-%{version}-py%{pyver}.egg-info/


%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.2.1-8.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 3 2009 Toshio Kuratomi <toshio@fedoraproject.org> - 1.2.1-7
- And nose

* Tue Mar 3 2009 Toshio Kuratomi <toshio@fedoraproject.org> - 1.2.1-6
- Add BR on simplejson so testsuite will run.

* Tue Mar 3 2009 Toshio Kuratomi <toshio@fedoraproject.org> - 1.2.1-5
- Enable test suite.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.2.1-3
- Rebuild for Python 2.6

* Wed Sep 17 2008 Luke Macken <lmacken@redhat.com> 1.2.1-2
- Require python-prioritized-methods > 0.2

* Tue Sep 16 2008 Luke Macken <lmacken@redhat.com> 1.2.1-1
- Latest release of the 1.2.x series
- Require python-peak-rules (#459157, #459117)

* Sun Jun 22 2008 Luke Macken <lmacken@redhat.com> 1.2-1
- Latest upstream release, intended to be used with the upcoming TurboGears 1.1 version.
- Remove python-turbojson-SAfix-r3749.patch

* Sat Feb 2 2008 Toshio Kuratomi <tkuratom@redhat.com> 1.1.2-3
- ...and remember to include the patch in cvs.

* Sat Feb 2 2008 Toshio Kuratomi <tkuratom@redhat.com> 1.1.2-2
- Backport fix for 1.1.2's SQLAlchemy breakage.

* Tue Nov 27 2007 Luke Macken <lmacken@redhat.com> 1.1.2-1
- 1.1.2

* Wed Oct  3 2007 Toshio Kuratomi <a.badger@gmail.com> 1.1-2
- BuildRequire python-devel and setuptools-devel
- Use the setup.py script to build and install

* Wed Oct  3 2007 Luke Macken <lmacken@redhat.com> 1.1-1
- 1.1
- Update URL and Source

* Fri Dec  8 2006 Luke Macken <lmacken@redhat.com> 0.9.9-3
- Rebuild for new python

* Fri Oct  6 2006 Luke Macken <lmacken@redhat.com> 0.9.9-2
- Update source url

* Mon Sep 25 2006 Luke Macken <lmacken@redhat.com> 0.9.9-1
- 0.9.9
- Rename to python-turbojson
- Own the %%{python_sitelib/turbojson directory
- Install the EGG-INFO

* Sat Sep 16 2006 Luke Macken <lmacken@redhat.com> 0.9.8-1
- Initial creation
