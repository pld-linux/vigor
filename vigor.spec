Summary:	vigor - vi-compatible editor with extra something thrown in
Summary(pl):	vigor - edytor podobny do vi z Panem Spinaczem
Name:		vigor
Version:	0.016
Release:	2
License:	BSD
Group:		Applications/Editors
Source0:	http://www.red-bean.com/~joelh/vigor/%{name}-%{version}.tar.gz
Patch0:		%{name}-ncurses.patch
URL:		http://www.red-bean.com/~joelh/vigor/
BuildRequires:	autoconf
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	tk-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Vigor is designed as a vi-compatible editor, with a little (*ahem*)
extra something thrown in. It was inspired by the January 4, 2000
storyline in the User Friendly comic. If you haven't seen it yet,
check it out at http://www.userfriendly.org/ (and do so in a place you
can freely laugh). Go ahead, I'll wait.

%description -l pl
Vigor jest edytorem kompatybilnym z vi z wbudowanym Panem Spinaczem,
zainspirowany historyjk± User Friendly z 4 stycznia 2000.

%prep
%setup -q
%patch0 -p1

%build
cd build
%{__autoconf}
OPTFLAG=" "; export OPTFLAG
CFLAGS="%{rpmcflags} -I/usr/include/ncurses"
%configure \
	--disable-curses \
	--enable-re \
	--enable-db

# <regex.h> doesn't have REG_STARTEND
# <db.h> from db3 is incompatible too

#cat >>config.h <<EOF
##define recno_t db_recno_t
##define MAX_REC_NUMBER DB_MAX_RECORDS
#EOF

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}}

(cd build
%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	exec_prefix=$RPM_BUILD_ROOT%{_exec_prefix} \
	datadir=$RPM_BUILD_ROOT%{_datadir} \
	bindir=$RPM_BUILD_ROOT%{_bindir}
)


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.vigor
%attr(755,root,root) %{_bindir}/vigor
%dir %{_datadir}/vigor
%{_datadir}/vigor/perl
%{_datadir}/vigor/tcl
%dir %{_datadir}/vigor/catalog
%{_datadir}/vigor/catalog/english
%lang(nl) %{_datadir}/vigor/catalog/dutch
%lang(fr) %{_datadir}/vigor/catalog/french
%lang(de) %{_datadir}/vigor/catalog/german
%lang(ru) %{_datadir}/vigor/catalog/ru_SU.KOI8-R
%lang(es) %{_datadir}/vigor/catalog/spanish
%lang(sv) %{_datadir}/vigor/catalog/swedish
