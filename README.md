## Linux 版微信

**本项目魔改自 [AUR - wechat-universal-bwrap](https://aur.archlinux.org/packages/wechat-universal-bwrap)**，常见问题请先参考这个项目的主页。

目前支持 `x86_64` 和 `aarch64` 两种架构。

## 从源代码构建

- `sudo dnf install @development-tools fedora-packager rpmdevtools`
- `sudo usermod -a -G mock $USER` 然后注销并重新登录用户
- 克隆这个项目并 cd 到项目目录
- `mock --init`
- `mock --buildsrpm --spec wechat-universal-bwrap.spec --sources src`
- `cp /var/lib/mock/fedora-40-aarch64/result/wechat-universal-bwrap-*.src.rpm .`
- `mock --rebuild ./wechat-universal-bwrap-*.src.rpm`
- `sudo dnf install /var/lib/mock/fedora-40-aarch64/result/wechat-universal-bwrap-*.aarch64.rpm`
