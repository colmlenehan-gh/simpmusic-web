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

## Version 0.2 revision

- Eleven automated tests pass, including read-only OAuth API mocks, pagination, header-only token use, revoked/expired sessions, playlist normalization and invalid configuration.
- Deployed revision loaded the mechanically ported original icons and source-derived layout.
- Avatar navigated to the new account screen. Missing OAuth client configuration was shown explicitly, with the exact deployment origin and no fake account session.
- Existing browser data remained present; the previously imported WAV file started playing after the revision.
- Live Google authorization and real private-library retrieval are not verified and remain blocked by an unprovisioned Google Web OAuth client ID.

- Responsive fixture rendered at 390 CSS pixels (phone) and 1,024 CSS pixels (landscape tablet). Both displayed the detached Search circle, floating Home/Library capsule, native header and four-row scrollable picks. These are browser viewport checks, not tests on a physical iPad.
