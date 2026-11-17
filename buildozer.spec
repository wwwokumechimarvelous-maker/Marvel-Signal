ini
[app]
title = Marvel AT Signal
package.name = marvelatsignal
package.domain = com.marvel.atsignal
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
android.api = 33
android.minapi = 21
android.ndk = 25
android.accept_sdk_license_agreements = True
