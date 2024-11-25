<h1 align="center">
  Opera GX Widevine Updater
</h1>

<p align="center">
  <a href="https://github.com/KeyErrorFinn/opera-gx-widevine-updater/commits/main/"><img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/KeyErrorFinn/opera-gx-widevine-updater" /></a>
  <a href="https://github.com/KeyErrorFinn/opera-gx-widevine-updater/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues-raw/KeyErrorFinn/opera-gx-widevine-updater" /></a>
</p>
<p align="center">
  <a href="#"><img alt="Python" src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff" /></a>
</p>

This project updates the `WidevineCdm` folder for Opera GX, ensuring that the latest Widevine version is available for use. The script automatically identifies the highest version folder of Opera GX and copies the `WidevineCdm` folder into it, then restarts the browser.

## Table of Contents
- [Table of Contents](#table-of-contents)
- [About The Project](#about-the-project)
  - [How the program works](#how-the-program-works)
  - [Usage](#usage)
  - [Requirements](#requirements)
  - [TO-DO](#to-do)

## About the Project
This project allows you to automatically update the `WidevineCdm` folder for Opera GX by copying it into the folder corresponding to the highest installed version of Opera GX. It also ensures that Opera GX is restarted after the update.

### How the program works:
1) The script checks the installed versions of Opera GX in the `%localappdata%\Programs\Opera GX` directory.
2) It identifies the highest version folder of Opera GX.
3) It copies the `WidevineCdm` folder from the repository into the highest version folder.
4) It closes any running instance of Opera GX.
5) After a short delay, it reopens Opera GX with the updated `WidevineCdm` folder.

### Usage:
1) Clone the repository or download the script files.
2) Ensure that the `WidevineCdm` folder is already included in the repository, as this will be used for the update.
3) Run the script to automatically update the `WidevineCdm` folder for the latest Opera GX version.

```bash
python opera-gx-widevine-updater.py
```

4) Or use the batch file provided. 

### Requirements:
To install the necessary dependencies, you can use the provided `requirements.txt` file. Run the following command to install all required libraries:

```bash
pip install -r requirements.txt
```

### TO-DO:
- [x] <s>Implement the folder scanning mechanism</s>
- [x] <s>Automatically close and restart Opera GX</s>
- [ ] Add error handling for specific Opera GX folder issues
