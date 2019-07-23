#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-guice-servlet
Version  : 3.0
Release  : 1
URL      : https://repo1.maven.org/maven2/com/google/inject/extensions/guice-servlet/3.0/guice-servlet-3.0.jar
Source0  : https://repo1.maven.org/maven2/com/google/inject/extensions/guice-servlet/3.0/guice-servlet-3.0.jar
Source1  : https://repo1.maven.org/maven2/com/google/inject/extensions/guice-servlet/3.0/guice-servlet-3.0.pom
Source2  : https://repo1.maven.org/maven2/com/google/inject/extensions/guice-servlet/4.0/guice-servlet-4.0.jar
Source3  : https://repo1.maven.org/maven2/com/google/inject/extensions/guice-servlet/4.0/guice-servlet-4.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-guice-servlet-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-guice-servlet package.
Group: Data

%description data
data components for the mvn-guice-servlet package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/google/inject/extensions/guice-servlet/3.0
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/com/google/inject/extensions/guice-servlet/3.0/guice-servlet-3.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/google/inject/extensions/guice-servlet/3.0
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/com/google/inject/extensions/guice-servlet/3.0/guice-servlet-3.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/google/inject/extensions/guice-servlet/4.0
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/com/google/inject/extensions/guice-servlet/4.0/guice-servlet-4.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/google/inject/extensions/guice-servlet/4.0
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/com/google/inject/extensions/guice-servlet/4.0/guice-servlet-4.0.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/com/google/inject/extensions/guice-servlet/3.0/guice-servlet-3.0.jar
/usr/share/java/.m2/repository/com/google/inject/extensions/guice-servlet/3.0/guice-servlet-3.0.pom
/usr/share/java/.m2/repository/com/google/inject/extensions/guice-servlet/4.0/guice-servlet-4.0.jar
/usr/share/java/.m2/repository/com/google/inject/extensions/guice-servlet/4.0/guice-servlet-4.0.pom
