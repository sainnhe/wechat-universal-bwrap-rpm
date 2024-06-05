#!/usr/bin/env sh

_version="1.0.0.241"
_arch=${1:-$(uname -m)}

if [ "${_arch}" = "x86_64" ]; then
    curl -fSL -o src/wechat.deb https://home-store-packages.uniontech.com/appstore/pool/appstore/c/com.tencent.wechat/com.tencent.wechat_${_version}_amd64.deb
elif [ "${_arch}" = "aarch64" ]; then
    curl -fSL -o src/wechat.deb https://home-store-packages.uniontech.com/appstore/pool/appstore/c/com.tencent.wechat/com.tencent.wechat_${_version}_arm64.deb
else
    echo "Unsupported architecture: ${_arch}"
    exit 1
fi
