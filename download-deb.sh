#!/usr/bin/env sh

_version="1.0.0.241"

curl -fSL -o src/wechat-x86_64.deb https://home-store-packages.uniontech.com/appstore/pool/appstore/c/com.tencent.wechat/com.tencent.wechat_${_version}_amd64.deb
curl -fSL -o src/wechat-aarch64.deb https://home-store-packages.uniontech.com/appstore/pool/appstore/c/com.tencent.wechat/com.tencent.wechat_${_version}_arm64.deb
