Name:           perl-GRNOC-WebService-Client
Version:        1.3.3
Release:        1%{?dist}
Summary:        GRNOC::WebService::Client Perl module
License:        GRNOC
Group:          Development/Libraries
URL:            http://globalnoc.iu.edu
Source0:        GRNOC-WebService-Client-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  mod_perl
BuildRequires:  httpd-devel
BuildRequires:  ImageMagick-perl
BuildRequires:  perl-GRNOC-WebService >= 1.2.5
BuildRequires:  mod_perl-devel
Requires:       perl >= 5.8.8
Requires:       perl-GRNOC-Config >= 1.0.7
Requires:       perl-JSON >= 2.0
Requires:       perl-JSON-XS >= 2.0
Requires:       perl-libwww-perl
Requires:       perl-IO-Socket-SSL
Requires:       perl-File-MMagic

%description
WebService Client Module

%prep
%setup -q -n GRNOC-WebService-Client-%{version}

%build
%{__perl} Makefile.PL 
make dist

%install
rm -rf $RPM_BUILD_ROOT

%{__install} -d -p %{buildroot}%{perl_sitelib}/GRNOC/WebService/
%{__install} -d -p %{buildroot}%{perl_sitelib}/GRNOC/WebService/Client/
%{__install} -d -p %{buildroot}/usr/bin/globalnoc/webservice/

%{__install} lib/GRNOC/WebService/Client.pm %{buildroot}%{perl_sitelib}/GRNOC/WebService/
%{__install} lib/GRNOC/WebService/Client/Paginator.pm %{buildroot}%{perl_sitelib}/GRNOC/WebService/Client/
%{__install} bin/wsutil.pl %{buildroot}/usr/bin/globalnoc/webservice/

%clean
rm -rf $RPM_BUILD_ROOT

%post

if [ ! -e /usr/bin/wsutil ]
  then 
    ln -s /usr/bin/globalnoc/webservice/wsutil.pl /usr/bin/wsutil
fi

%files
%defattr(-,root,root,-)
%{perl_sitelib}/GRNOC/WebService/Client.pm
%{perl_sitelib}/GRNOC/WebService/Client/Paginator.pm
/usr/bin/globalnoc/webservice/wsutil.pl

%changelog
* Mon Jun 13 2011 mrmccrac 1.1.0-1
- Specfile autogenerated by cpanspec 1.77.
