# Termux Releases

Welcome to the **Termux Releases** repository! This repository contains archived copies of various Termux App releases for Android.

## About Termux

Termux is a powerful terminal emulator and Linux environment app for Android. It provides access to a full Linux command-line environment without requiring root access.

## Repository Structure

```
termux-releases/
├── Releases/
│   ├── Termux_117/
│   │   └── com.termux_117.apk (82M)
│   └── Termux_118/
│       └── com.termux_118.apk (98M)
├── CHANGELOG.md
├── CHECKSUMS.md
├── CONTRIBUTING.md
├── Termux (text file)
└── README.md
```

## Available Versions

| Version | File Size | Location |
|---------|-----------|----------|
| 0.117 | 82 MB | `Releases/Termux_117/com.termux_117.apk` |
| 0.118 | 98 MB | `Releases/Termux_118/com.termux_118.apk` |

### Verifying Downloads

For security, always verify the integrity of downloaded APK files using SHA256 checksums. See [CHECKSUMS.md](CHECKSUMS.md) for verification instructions and checksums for all releases.

## Download Instructions

### Option 1: Direct Download from GitHub

1. Navigate to the [Releases](./Releases) directory
2. Choose the version you want to download
3. Click on the APK file
4. Click the "Download" button

### Option 2: Using Git Clone

```bash
# Clone this repository
git clone https://github.com/4evernever77777/termux-releases.git
cd termux-releases/Releases

# Or if you forked this repo, use your username instead
# git clone https://github.com/YOUR_USERNAME/termux-releases.git
```

### Option 3: Direct Download Links

You can download the APK files directly using these links (or use the corresponding links from your fork):

- **Termux 0.117**: [com.termux_117.apk](https://github.com/4evernever77777/termux-releases/raw/main/Releases/Termux_117/com.termux_117.apk)
- **Termux 0.118**: [com.termux_118.apk](https://github.com/4evernever77777/termux-releases/raw/main/Releases/Termux_118/com.termux_118.apk)

## Installation Instructions

### Prerequisites

Before installing Termux, you need to enable installation from unknown sources on your Android device:

1. Go to **Settings** > **Security** (or **Privacy**)
2. Enable **Unknown Sources** or **Install from Unknown Sources**
3. Allow your browser or file manager to install apps

### Installing the APK

1. Download the desired Termux APK version from this repository
2. Open your file manager and navigate to the Downloads folder
3. Tap on the downloaded APK file
4. Follow the on-screen prompts to install
5. Once installed, open Termux from your app drawer

### First Launch

When you first launch Termux, it will:
- Set up the environment
- Download necessary base packages
- Create the home directory structure

This initial setup may take a few minutes.

## Important Notes

⚠️ **Security Notice**: Always verify the source of APK files before installing them on your device. This repository provides archived copies of Termux releases.

⚠️ **Version Compatibility**: Make sure to check which version is compatible with your Android version:
- Termux 0.117 and above require Android 7.0 (API 24) or higher
- Older Android versions may need earlier Termux releases

⚠️ **Updates**: These are archived releases. For the latest official Termux versions, visit:
- [F-Droid](https://f-droid.org/packages/com.termux/)
- [Official Termux GitHub](https://github.com/termux/termux-app)

## Usage

After installing Termux, you can:

- Run Linux commands
- Install packages using `pkg install <package-name>`
- Set up development environments
- Run scripts and programs
- Access remote servers via SSH
- And much more!

### Basic Commands

```bash
# Update package lists
pkg update

# Upgrade installed packages
pkg upgrade

# Install a package
pkg install git

# List installed packages
pkg list-installed

# Search for packages
pkg search <keyword>
```

## Useful Resources

- [Termux Official Website](https://termux.com/)
- [Termux Wiki](https://wiki.termux.com/)
- [Termux GitHub Repository](https://github.com/termux/termux-app)
- [Termux Community](https://gitter.im/termux/termux)
- [Package List](https://github.com/termux/termux-packages)
- [CHANGELOG.md](CHANGELOG.md) - Release notes and version history
- [CHECKSUMS.md](CHECKSUMS.md) - SHA256 checksums for security verification

## Contributing

Interested in contributing to this archive? Check out [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on adding new releases or improving documentation.

For contributing to Termux development itself, please visit the [official Termux repository](https://github.com/termux/termux-app).

## License

Termux is licensed under the GPLv3 license. For more information, see the [Termux License](https://github.com/termux/termux-app/blob/master/LICENSE.md).

## Disclaimer

This repository is a fork that archives Termux releases. We are not affiliated with the official Termux project. All rights and credits go to the original Termux developers and contributors.

For official releases and support, please visit the [official Termux GitHub repository](https://github.com/termux/termux-app).
