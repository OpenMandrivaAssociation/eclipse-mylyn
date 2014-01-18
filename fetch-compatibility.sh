#!/bin/sh
TAG=20110110

rm -rf eclipse.platform.runtime-${TAG}.tar.bz2
rm -rf eclipse.platform.runtime-${TAG}

wget -O eclipse.platform.runtime-${TAG}.tar.bz2 http://git.eclipse.org/c/platform/eclipse.platform.runtime.git/snapshot/eclipse.platform.runtime-${TAG}.tar.bz2

tar xjf eclipse.platform.runtime-${TAG}.tar.bz2

pushd eclipse.platform.runtime-${TAG}
  cd bundles/
  tar caf org.eclipse.core.runtime.compatibility.auth.tar.xz org.eclipse.core.runtime.compatibility.auth
  mv org.eclipse.core.runtime.compatibility.auth.tar.xz ../../
popd

rm -rf eclipse.platform.runtime-${TAG}.tar.xz
rm -rf eclipse.platform.runtime-${TAG}