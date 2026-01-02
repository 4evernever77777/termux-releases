# Contributing to Termux Releases

Thank you for your interest in contributing to the Termux Releases repository!

## About This Repository

This repository is an **archive** of Termux APK releases. It is not the official Termux project. For contributing to Termux development itself, please visit:

- [Official Termux App Repository](https://github.com/termux/termux-app)
- [Termux Packages Repository](https://github.com/termux/termux-packages)

## How to Contribute to This Archive

### Adding New Releases

If you'd like to contribute new Termux releases to this archive:

1. **Fork this repository**
   ```bash
   # Click "Fork" on GitHub, then clone your fork
   git clone https://github.com/YOUR_USERNAME/termux-releases.git
   cd termux-releases
   ```

2. **Create a new branch**
   ```bash
   git checkout -b add-termux-version-XXX
   ```

3. **Add the new release**
   - Create a new directory: `Releases/Termux_XXX/`
   - Add the APK file: `Releases/Termux_XXX/com.termux_XXX.apk`
   - Ensure the file is from an official source

4. **Update documentation**
   - Update `README.md` with the new version in the version table
   - Update `CHANGELOG.md` with release information
   - Update `CHECKSUMS.md` with the SHA256 checksum:
     ```bash
     sha256sum Releases/Termux_XXX/com.termux_XXX.apk
     ```

5. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add Termux version 0.XXX"
   ```

6. **Push and create a pull request**
   ```bash
   git push origin add-termux-version-XXX
   # Then create a pull request on GitHub
   ```

### Reporting Issues

If you find any problems with:
- Corrupted APK files
- Incorrect checksums
- Outdated documentation

Please open an issue with:
- Clear description of the problem
- Steps to reproduce (if applicable)
- Expected vs actual behavior

### Improving Documentation

Documentation improvements are always welcome! This includes:
- Fixing typos
- Clarifying instructions
- Adding helpful examples
- Updating links

For documentation changes:
1. Fork the repository
2. Make your changes to the relevant `.md` files
3. Submit a pull request with a clear description

## Code of Conduct

Please be respectful and constructive in all interactions. This is a community project to help preserve and share Termux releases.

## Questions?

If you have questions:
- Check the [README.md](README.md) first
- Review existing issues
- Open a new issue if your question hasn't been answered

## License

By contributing to this repository, you agree that your contributions will be licensed under the same terms as the Termux project (GPLv3).

---

**Remember**: This is an archive repository. For feature requests and development contributions to Termux itself, please visit the [official Termux repository](https://github.com/termux/termux-app).
