[![Telegram](https://img.icons8.com/color/24/telegram-app.png)](https://t.me/maestroofautomation) [Maestro Of Automation's channel in Telegram](https://t.me/maestroofautomation)

# Maestro Antidetect Browser Solution (alpha)

**Maestro Anti Detect Browser Solution** is a tool for managing Chrome browser profiles, rotating proxies, and automatically setting fingerprints.

## Features

- **Profile Management**: Create and store profiles with preserved user data.
- **Opened pages synchronization**: Solution will keep your opened pages between profile usages.
- **Fingerprint Spoofing**: Spoof User-Agent, screen resolution, and other navigator parts by using [BrowserForge Fingerprints](https://github.com/BrowserForge/BrowserForge), like in paid solutions.
- **Proxy support**: Supports proxy & proxy change for profiles. http (with/out auth) & socks5 (WITHOUT auth only)
- **Extension Installation**: Support for extensions. Simply create `extensions` directory in root directory of script, and unpack extension into `extensionName` in `extensions` directory, like `extensions/metamask`

## 🎓 Prerequisites

### Make sure you have `Python 3.10` installed!  

You can download Python [here](https://www.python.org/downloads/).

## Installation

You can download the repository by cloning it to your system and installing the necessary dependencies:

```bash
git clone https://github.com/MaestroOfAutomation/AntidetectBrowserSolution.git
cd AntidetectBrowserSolution
```

## Quick Start 📚
### To quickly install the required libraries and run the solution by those commands:

Open console / terminal and type `run.bat` on Windows or `run.sh` on Linux or `bash run.sh` on MacOS in root script directory.