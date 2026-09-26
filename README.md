# Opera GX Widevine Updater

A Windows utility that replaces Opera GX's bundled `WidevineCdm` directory with the copy stored in this repository, then restarts the browser.

> [!CAUTION]
> This removes an existing Widevine directory inside the selected Opera version before copying the bundled replacement. Close sensitive browser sessions and back up the target directory first.

## How it works

`main.py`:

1. Scans `%LOCALAPPDATA%\Programs\Opera GX` for version-number directories.
2. Chooses the highest version.
3. Deletes that version's existing `WidevineCdm` folder, if present.
4. Copies the repository's `WidevineCdm` folder into the version directory.
5. terminates processes named `opera.exe`.
6. waits five seconds and launches Opera GX through `launcher.exe`.

This is a file-replacement helper, not an online updater: it installs the Widevine files already committed in this repository.

## Requirements

- Windows
- Opera GX installed in its standard per-user location
- Python 3
- `psutil==6.0.0`

```powershell
python -m pip install -r requirements.txt
```

## Running

Use the provided batch file:

```text
Fix Opera.bat
```

or run the actual Python entry point:

```powershell
python main.py
```

Keep `WidevineCdm/` beside `main.py`.

## Verification and recovery

After running, open `opera://components` and check the Widevine component status, then test protected media on a legitimate service.

If Opera stops working:

1. Close Opera GX.
2. Restore the backed-up `WidevineCdm` directory, or reinstall/update Opera GX through its official installer.
3. Restart the browser.

## Limitations

- Only the default Windows installation path is supported.
- Version-folder comparison assumes numeric dot-separated folder names.
- The bundled Widevine files can become outdated or incompatible.
- The script has limited error handling and forcefully closes every `opera.exe` process.
