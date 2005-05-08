%define		module	pyid3lib
Summary:	A Python module for editing ID3v2 tags of MP3 audio files
Name:		python-%{module}
Version:	0.5.1
Release:	1
License:	LGPL
Group:		Libraries/Python
#Source0Download: http://www.andrewchatham.com/pyogg/
Source0:	http://dl.sourceforge.net/pyid3lib/pyid3lib-%{version}.tar.gz
# Source0-md5:	45a4ecc4d0600661199e4040a81ea3fe
URL:		http://pyid3lib.sourceforge.net/
BuildRequires:	id3lib-devel
BuildRequires:	rpmbuild(macros) >= 1.174
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pyid3lib is a Python module for editing ID3v2 tags of MP3 audio files.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--optimize=2 \
	--root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{py_sitedir}/*.so
