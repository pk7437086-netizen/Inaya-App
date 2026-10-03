[app]

# Application information
title = Inaya
package.name = inayaapp
package.domain = org.test

# Source code location
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,gif,mp3,wav

# Version
version = 0.1

# Requirements
requirements = python3,kivy

# App display settings
orientation = portrait
fullscreen = 0

# Permissions
android.permissions = INTERNET,RECORD_AUDIO

# Android SDK / NDK settings
android.api = 31
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

[buildozer]

log_level = 2
warn_on_root = 1
