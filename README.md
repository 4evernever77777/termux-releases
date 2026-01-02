# Termux Releases

This repository contains Termux APK releases and installation scripts for running AI models on Android devices.

## What is Termux?

Termux is a powerful Android terminal emulator and Linux environment app that works directly with no rooting or setup required. It allows you to run a Linux distribution on your Android device.

## Available Releases

- **Termux v118** - Latest version (`Releases/Termux_118/com.termux_118.apk`)
- **Termux v117** - Previous version (`Releases/Termux_117/com.termux_117.apk`)

## Installing Termux

1. Download the desired APK from the `Releases` folder
2. Enable "Install from Unknown Sources" in your Android settings
3. Install the APK on your device
4. Open Termux and update packages:
   ```bash
   pkg update && pkg upgrade
   ```

## Installing DeepSeek on Termux

DeepSeek is a powerful AI language model that can run locally on your device. Follow these steps to install it:

### Quick Installation

```bash
# Download and run the installation script
curl -o install-deepseek.sh https://raw.githubusercontent.com/4evernever77777/termux-releases/main/install-deepseek.sh
chmod +x install-deepseek.sh
./install-deepseek.sh
```

### Manual Installation

If you prefer to install manually, follow the [DeepSeek Installation Guide](DEEPSEEK_GUIDE.md).

## Requirements

- Android device with at least 4GB RAM (8GB+ recommended)
- At least 10GB of free storage space
- Termux installed and updated
- Stable internet connection for initial setup

## Support

For issues or questions:
- Check the [DeepSeek Guide](DEEPSEEK_GUIDE.md)
- Open an issue on this repository
- Review Termux documentation at [termux.dev](https://termux.dev)

## License

This repository provides APK files and scripts for educational purposes. Please refer to individual projects for their respective licenses:
- Termux: [GPLv3](https://github.com/termux/termux-app/blob/master/LICENSE.md)
- DeepSeek: Check [DeepSeek official repository](https://github.com/deepseek-ai)
