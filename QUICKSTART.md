# DeepSeek Quick Start Guide

## 🚀 Fast Installation

### Step 1: Install Termux
Download and install Termux APK from `Releases/Termux_118/com.termux_118.apk`

### Step 2: Update Termux
```bash
pkg update && pkg upgrade -y
```

### Step 3: Install DeepSeek
```bash
# Download installer
curl -o install-deepseek.sh https://raw.githubusercontent.com/4evernever77777/termux-releases/main/install-deepseek.sh

# Run installer
chmod +x install-deepseek.sh
./install-deepseek.sh
```

## 🔑 Setup API (Recommended)

1. Get API key from [platform.deepseek.com](https://platform.deepseek.com)
2. Configure:
```bash
cd ~/deepseek
./setup_api.sh
```

## 💬 Start Using

### Test API:
```bash
cd ~/deepseek
./example_api_call.sh
```

### Interactive Chat:
```bash
cd ~/deepseek
python chat.py
```

## 📖 Need More Help?

Read the comprehensive guide: [DEEPSEEK_GUIDE.md](DEEPSEEK_GUIDE.md)

## ⚡ Quick Commands

```bash
# Check installation
python --version
pip --version

# Update packages
pkg update && pkg upgrade

# Reinstall DeepSeek dependencies
pip install --upgrade transformers torch tiktoken

# Check API key
echo $DEEPSEEK_API_KEY
```

## 🆘 Common Issues

**API not working?**
```bash
# Set API key manually
export DEEPSEEK_API_KEY='your-key-here'
```

**Out of storage?**
```bash
# Clean caches
pkg clean
pip cache purge
```

**Package install fails?**
```bash
# Install build tools
pkg install -y clang cmake
```

---

For detailed documentation, see [DEEPSEEK_GUIDE.md](DEEPSEEK_GUIDE.md)
