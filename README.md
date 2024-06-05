## Fedora Linux 版微信

**本项目魔改自 [AUR - wechat-universal-bwrap](https://aur.archlinux.org/packages/wechat-universal-bwrap)**，常见问题请先参考这个项目的主页。

目前支持 `x86_64` 和 `aarch64` 两种架构。

## 从源代码构建

- `sudo dnf install @development-tools fedora-packager rpmdevtools`
- `sudo usermod -a -G mock $USER` 然后注销并重新登录用户
- 克隆这个项目并 cd 到项目目录
- `./download-deb.sh`
- `mock --init`
- `mock --buildsrpm --spec wechat-universal-bwrap.spec --sources src`
- `cp /var/lib/mock/[YOUR_OS]/result/wechat-universal-bwrap-*.src.rpm .`
- `mock --rebuild ./wechat-universal-bwrap-*.src.rpm`
- 生成的 rpm 文件在 `/var/lib/mock/[YOUR_OS]/result/` 目录下，可直接通过 `sudo dnf install` 安装，如：
  - `sudo dnf install /var/lib/mock/fedora-40-aarch64/result/wechat-universal-bwrap-*.aarch64.rpm`
