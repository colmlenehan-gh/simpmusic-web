# Validation record

Date: 11 November 2026.

## Passed

- JavaScript syntax checks for application, core utilities and service worker.
- Five Node test cases: YouTube URL validation, timed lyrics parsing, escaping and artwork URL restrictions, malformed backup rejection, invalid duration handling.
- Public GitHub repository confirmed; GitHub Pages enabled for `main` at repository root.
- Deployed site loaded with navigation, bundled fonts, artwork, library and player UI.
- Browser: created a playlist; it remained after a reload.
- Browser: added a favourite; the saved count remained after a reload.
- Browser: searched the local library for Coldplay and obtained Yellow.
- Browser: selecting the result loaded an official YouTube embed with the correct title and duration.
- Browser: imported a generated WAV test file into IndexedDB. On-device library count became one; selecting it changed the player to Pause, confirming native audio playback started.

## Not established

- YouTube video playback did not visibly advance in the testing browser. The official player loaded metadata and duration, but this is not evidence that sound played. Browser/network restrictions, autoplay and YouTube availability remain external dependencies.
- Restricted-key online search was not tested because no user key was supplied.
- LRCLIB service response, real-device codec support, mobile layouts on physical devices, background playback, audio output, and storage eviction were not verified.
- Offline playback is implemented through IndexedDB and shell caching; a complete offline browser session was not tested.

No claim of complete parity with the native SimpMusic app is made. See README.md for the feature matrix and native-only limitations.
