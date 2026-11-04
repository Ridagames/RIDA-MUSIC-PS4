# RIDA MUSIC — PS4 Homebrew

RIDA MUSIC is an independent PS4 homebrew music-player project for GoldHEN-compatible consoles.

## Current milestone

This first commit establishes the OpenOrbis build pipeline and package identity. It is a **native PS4 bootstrap**, not yet the finished Spotify-style interface or a working streaming client.

Planned milestones:
- [x] OpenOrbis PS4 project structure
- [x] GitHub Actions PKG build pipeline
- [ ] Native graphical interface and DualShock 4 navigation
- [ ] Legal music catalogue/search provider
- [ ] Network streaming and playback controls
- [ ] Playlists, favourites and persistence

## Build

Push to the default branch or run **Actions → Build RIDA MUSIC PS4 → Run workflow**. The workflow uses the OpenOrbis toolchain and publishes the generated `.pkg` as a downloadable Actions artifact.

## Important

RIDA MUSIC will only use audio streams and catalogue APIs that are permitted by their providers. It will not extract or bypass DRM from Spotify, YouTube Music, or other subscription services.

Target: PS4 homebrew / GoldHEN  
Toolchain: OpenOrbis PS4 Toolchain  
Title ID: `RIDA00001`
