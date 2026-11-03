# Opera GX Widevine Updater

<p align="center">
  <img src="assets/logo.png" alt="opera-gx-widevine-updater logo" width="180" />
</p>

<p align="center">
  <img alt="Windows" src="https://img.shields.io/badge/Windows-0078D4?logo=windows&logoColor=fff" />
  <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff" />
  <img alt="Opera GX" src="https://img.shields.io/badge/Opera%20GX-EE2950?logo=opera&logoColor=fff" />
</p>

A Windows repair utility that replaces Opera GX's bundled `WidevineCdm` directory with the copy stored in this repository, closes Opera, and starts it again.

> [!CAUTION]
> The script permanently deletes the selected Opera version's existing `WidevineCdm` folder before copying the replacement. It does not create a backup.

## Bundled component

The committed manifest reports Widevine version `4.10.2710.0`. The repository only includes the Windows x64 binary, even though the upstream manifest lists other architectures.

Use this only on a Windows x64 Opera GX installation. The bundled component can become older than the version Opera expects.

## Target location

The script searches:

~~~text
%LOCALAPPDATA%\Programs\Opera GX
~~~

It treats numeric directory names as Opera versions, selects the highest one, and replaces:

~~~text
%LOCALAPPDATA%\Programs\Opera GX\<version>\WidevineCdm
~~~

## Before running

1. Close sensitive browser sessions.
2. Find the target version folder.
3. Copy its `WidevineCdm` directory somewhere safe.
4. Confirm this repository's `WidevineCdm` folder is present.
5. Make sure the installation is Windows x64.

## Install and run

~~~powershell
python -m pip install -r requirements.txt
python main.py
~~~

You can also run `Fix Opera.bat`.

The script copies the files first, terminates every process named `opera.exe`, waits five seconds, and launches `launcher.exe`.

## Verify

1. Open `opera://components`.
2. Find Widevine Content Decryption Module.
3. Check its status.
4. Test protected media on a legitimate service.

## Recovery

If Opera or protected playback stops working:

1. Close Opera GX.
2. Delete the replacement `WidevineCdm` directory.
3. Restore your backup.
4. If no backup exists, repair or reinstall Opera GX with the official installer.

## Limitations

- Only the default per-user Opera GX path is supported.
- Only Windows x64 files are included.
- Version comparison assumes dot-separated numeric folder names.
- Every `opera.exe` process is terminated.
- There is no dry-run mode, backup, rollback, or integrity check.
- The project does not download a current Widevine release.

## Files

- `main.py`, version selection, replacement, process termination, and restart.
- `Fix Opera.bat`, Windows launcher.
- `WidevineCdm/`, the bundled replacement component and its licence.
- `requirements.txt`, the pinned `psutil` dependency.

## Licence

The bundled Widevine directory includes its own `LICENSE` file. No separate project-level licence is currently included.
