#!/usr/bin/tclsh

set arch "noarch"
set base "csp-0.1.0_git20151118"

set var2 [list git clone https://github.com/securitykiss-com/csp.git $base]
exec >@stdout 2>@stderr {*}$var2

cd $base

set var2 [list git checkout c224a4b46ea55e813941c8ee4a1f70f32cebe75b]
exec >@stdout 2>@stderr {*}$var2

set var2 [list git reset --hard]
exec >@stdout 2>@stderr {*}$var2

file delete -force .git

cd ..

set var2 [list tar czvf ${base}.tar.gz $base]
exec >@stdout 2>@stderr {*}$var2

if {[file exists build]} {
    file delete -force build
}

file mkdir build/BUILD build/RPMS build/SOURCES build/SPECS build/SRPMS
file copy -force $base.tar.gz build/SOURCES

set buildit [list rpmbuild --target $arch --define "_topdir [pwd]/build" -bb csp.spec]
exec >@stdout 2>@stderr {*}$buildit

# Remove our source code
file delete -force $base
file delete -force $base.tar.gz
