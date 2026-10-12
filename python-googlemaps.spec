Name:		python-googlemaps
Version:	4.10.0
Release:	2
Summary:	Python client library for Google Maps Platform
License:	Apache-2.0
Group:		Development/Python
URL:		https://pypi.org/project/googlemaps/
Source0:	googlemaps-4.10.0.tar.gz
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(requests)
BuildArch:	noarch
%description
Python client library for Google Maps Platform.

%files
%{py_sitedir}/*
