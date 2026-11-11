# SimpMusic Web

An **unofficial, partial browser reimplementation** of [SimpMusic](https://github.com/maxrave-dev/SimpMusic), using its Poppins typography, app icon, dark panel layout, cyan brand colour, and library/player structure. GPL-3.0-or-later. This is not an official release, a Kotlin-to-web compilation, or a feature-identical conversion.

## Run

No build, npm dependencies, accounts, or paid services are required for local audio playback.

1. Extract the ZIP.
2. Serve this folder with any static HTTPS host, or run `python3 -m http.server 8000` inside it.
3. Open `http://localhost:8000`.

Do not open `index.html` as a `file://` URL: JavaScript modules, persistent storage, and service workers need an HTTP origin. GitHub Pages provides HTTPS. On iPad, use the hosted site; importing audio works through the Files picker. Where supported, install through the browser’s Add to Home Screen option.

## Features

- Responsive desktop three-panel layout and mobile navigation.
- Home quick picks, mix, library search, and mood search shortcuts.
- Import multiple audio files into IndexedDB. SHA-256 IDs deduplicate content and reconnect files restored from metadata backups.
- Native browser audio playback, seek, previous/next, shuffle, repeat, volume, and Media Session controls where available.
- YouTube video URLs, featured videos, official visible embeds, and optional YouTube Data API search.
- Persistent favourites, named playlists, queue, song metadata editing, history, and listening statistics based on observed playback time.
- Timed LRC import and highlighting; opt-in exact-match lyrics lookup through LRCLIB.
- Local-audio ten-band Web Audio equalizer, sleep timer, dark/light/system themes.
- Metadata/playlist/lyrics backup export and merge import. API keys and audio bytes are excluded.
- Offline application shell after the first successful online load; imported audio can play offline.
- HTML escaping, restricted artwork hosts, strict YouTube URL parsing, and validated backup structure.

The initial featured YouTube selection is curated starter content, not personalized recommendations or a live chart. Moods search by text; they do not classify local audio automatically. The mix is a shuffled local library, not YouTube radio. Local file labels are inferred from `Artist - Title.ext`; embedded ID3 tags are not parsed. Edit labels through the song menu.

## YouTube search

Video URLs and starter embeds need no developer key. For online search, enable YouTube Data API v3 in your own Google Cloud project and enter a **browser-restricted key** in Settings. Restrict the key to your actual site origin/referrer and to YouTube Data API v3. The key is kept only in this browser’s local storage and sent to Google when searching; it is excluded from exports. Client-side keys cannot be hidden. Quota, authorization, network, embed, and regional failures are displayed rather than replaced with fake results.

Without a key, search covers the library and accepts YouTube links. There is no bundled shared credential and no proxy pretending to be YouTube Music.

## Compatibility and deliberate limitations

| Original capability | Web implementation |
| --- | --- |
| Native UI | Reimplemented in HTML/CSS; not pixel-identical or generated from Compose |
| Local playback | Browser-decoded formats, IndexedDB storage |
| YouTube playback | Official visible iframe, controlled by YouTube availability and advertising |
| YouTube Music home/search/account | Curated home; optional public YouTube search; no Music account sync |
| Background/ad-free playback | Not guaranteed for YouTube; browser/OS policies apply |
| Downloads | User-imported audio only; no YouTube extraction or offline downloads |
| Lyrics | Local LRC and opt-in LRCLIB; no other provider integrations or translation |
| Equalizer | Ten bands on local audio, with fixed -6 dB headroom; no AutoEq, delay, reverb, or iframe audio processing |
| Playlists/favourites | Local device storage; no Google/Spotify synchronization |
| Analytics | Local playback observations while page runs; suspended browser time is not estimated |
| Cast/Android Auto/widgets/device routing | Not implemented |
| Shared rooms/Discord/Last.fm/SponsorBlock/AI | Not implemented |
| Recognition/comments/account transfer | Not implemented |

GitHub Pages hosts static files, not the JVM playback engine, an extraction service, or a credential-handling backend. Browsers cannot reproduce arbitrary native networking or intercept third-party iframe audio. Open-source licensing permits adaptation; it does not remove these platform differences. Feature parity would require a separately hosted backend, native integrations where applicable, substantial further engineering, and continued verification against upstream.

Playback must start from a user gesture. YouTube may require a second tap inside its player, show ads, reject embedding, require sign-in, or return region and age restrictions. The player remains visible and no restriction bypass is included. Media Session, Web Audio, service workers, installation, codecs, and background behaviour vary by browser.

## Privacy and storage

No application server, telemetry, or external font CDN is used. Artwork requests go to YouTube, YouTube embeds contact Google, optional search sends the query/key to Google, and opting into lyric search sends the song/artist to LRCLIB. Your playlists and local audio are not uploaded by the app. Browser storage is not a durable backup: private browsing, storage eviction, or clearing site data can remove it. Keep original audio files. Library exports are unencrypted files containing your song titles, playlists, and lyrics.

## GitHub Pages

Publish the root of `main` under repository **Settings → Pages → Deploy from a branch**. All asset URLs are relative, and hash routing supports project subpaths. `.nojekyll` avoids unnecessary Jekyll processing. No build workflow or secrets are required. Publish only this web folder, not upstream Android build files.

## Development and checks

```sh
npm run check
npm test
npm start
```

Tests use Node’s built-in test runner; Node 20+ is recommended. Runtime itself has no npm dependencies. Core tests cover unsafe URLs, markup escaping, timed lyrics, backup validation, and invalid duration handling. Real-device audio, YouTube regional availability, restricted-key search, and mobile background behaviour need testing in their respective environments.

## Source and attribution

Inspected upstream revision: `c11ee6a38102b6065dd27b71cb12b0afef61f54a` from `maxrave-dev/SimpMusic` (default `dev` branch at inspection). Upstream source provides Android and JVM targets, not a ready browser target.

See [NOTICE.md](NOTICE.md), [LICENSE](LICENSE), and [Poppins font licence](assets/OFL-Poppins.txt). The browser code is newly written; the upstream Android/JVM code is not included in this ZIP. Reused assets are included with attribution and applicable licence terms. No affiliation or endorsement is claimed. Music, video, lyrics, and artwork retain their respective owners’ rights.
