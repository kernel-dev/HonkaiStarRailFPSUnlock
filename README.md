# Honkai: Star Rail 60 FPS Cap Unlocker

This is a small script that merely changes the `FPS` value in the Windows Registry for Honkai: SR.

For anyone interested, the path to it (in the Registry Editor) is: `HKEY_CURRENT_USER\SOFTWARE\Cognosphere\Star Rail`, and the value itself is `GraphicsSettings_Model_hXXXXXXXXXX`. You simply double click on it to alter the value, and edit the binary data of the value `60` (in hex: `0x36 0x30`) whose parent key is `FPS`, so that it is `120`. It's easier to preview the hex representation of `120` with a HexEditor, but for those lazy ones, it's `0x31 0x32 0x30`.

## Why only 120FPS?

For reasons unknown to me, raising this threshold above 120FPS through the Windows Registry simply defaults back to rendering at 60FPS. It's highly plausible that a RAM patch is necessary to raise it above that.