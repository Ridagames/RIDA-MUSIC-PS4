# RIDA MUSIC — PS4 Homebrew

RIDA MUSIC is an independent PS4 homebrew music-player project for GoldHEN-compatible consoles.

## Current milestone

The project now includes a native 1080p interface rendered with the OpenOrbis VideoOut sample graphics layer, plus DualShock 4 navigation (D-pad, L1/R1, Cross, Circle and Options). The visible library is currently a demonstration UI; it does not yet fetch real tracks or play streamed music.

- [x] OpenOrbis PS4 project structure and PKG build pipeline
- [x] Native graphical interface
- [x] DualShock 4 menu navigation
- [ ] Legal music catalogue/search provider
- [ ] Network audio streaming and decoding
- [ ] Playlists, favourites and persistence

## Controls

- D-pad: move through the library
- L1 / R1 or Left / Right: change section
- Cross: queue / unqueue the highlighted demo item
- Circle: clear the queue state
- Options: return to Home

## Build

Push to the default branch or run **Actions → Build RIDA MUSIC PS4 → Run workflow**. The workflow uses the OpenOrbis toolchain and publishes the generated PKG as a downloadable Actions artifact.

## Important

RIDA MUSIC will only use audio streams and catalogue APIs that are permitted by their providers. It will not extract or bypass DRM from Spotify, YouTube Music, or other subscription services.

Target: PS4 homebrew / GoldHEN  
Toolchain: OpenOrbis PS4 Toolchain  
Title ID: RIDA00001
