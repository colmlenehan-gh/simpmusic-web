# Google account connection

The account page now implements Google Identity Services OAuth authorization and read-only YouTube Data API access. It is not a fake login, a password form, or a link that claims to share your existing YouTube cookies.

**Current deployment status:** no Google OAuth client has been provisioned. The application cannot open a functional account chooser until the website owner registers one. A client ID cannot be invented, copied from a different app, or produced from SimpMusic’s source.

## One-time owner setup

1. Open https://console.cloud.google.com/ and create or select a project you control.
2. Enable **YouTube Data API v3** for that project.
3. Configure **Google Auth Platform** branding, audience and data access. Request only `https://www.googleapis.com/auth/youtube.readonly`. Supply the app information and privacy disclosures Google requires.
4. If the application is in testing, add the Google account(s) that should be allowed to connect as test users. Follow Google’s testing, publishing and verification requirements; do not bypass warnings or restrictions.
5. Create an OAuth client with application type **Web application**. Add the exact authorized JavaScript origin:

   `https://colmlenehan-gh.github.io`

   Origins have no repository path and no trailing slash. For local testing, separately register `http://localhost:8000`. The GIS popup token flow used here does not require a redirect page in this repository.
6. Copy the public `…apps.googleusercontent.com` client ID. Do **not** put a client secret in this site.
7. To enable sign-in for everyone visiting the deployment, set `googleClientId` in `auth-config.js`, commit, and let GitHub Pages deploy. Alternatively, enter the ID under **avatar → Account setup** to test only in your own browser. A Google Cloud project is not automatically configured by entering an ID.
8. Click **Continue with Google**, choose your account/channel, and grant read-only YouTube access on Google’s page. The application loads owned playlists. Import one or all playlists and optionally import liked videos.

Signing in is not yet verified against a real configured client. Automated tests mock the authorization and API responses. A live account test remains necessary after provisioning.

## What is retrieved

- Owned playlists exposed through `playlists.list(mine=true)`.
- Available playlist videos using `playlistItems.list`, with pagination.
- Liked videos using `videos.list(myRating=like)`. Google limits this collection to the most recent 1,000 videos.
- YouTube search results using the connected account’s access token.

These are YouTube Data API resources. They are **not a complete YouTube Music account export**. Music-only saved albums, uploaded music files, personal mixes, recommendations, and some Music-only playlists are not available through this implementation. Private/deleted/unavailable video entries are skipped. Imported playlist order is preserved. Refreshing an imported playlist updates the local snapshot, not YouTube.

An empty owned-playlist result can mean the selected channel has none. Saved playlists owned by other channels are not automatically returned by `mine=true`. Select the intended account/channel in Google’s chooser.

## Why the original native login cannot simply be pasted into a webpage

In upstream `LogInScreen.kt`, Android opens a native WebView, detects the YouTube Music URL and reads its session cookie through a platform cookie manager. The desktop implementation can import browser profiles through native APIs. That capability is not part of ordinary web JavaScript. Browser same-origin rules prevent this site from reading Google or YouTube cookies, even when the user is already signed in elsewhere.

Reusing those functions would require native code or a different deployment architecture. The current upstream Gradle project has Android and JVM targets and numerous native `expect`/`actual` platform implementations. Copying Kotlin source into an HTML file would not supply those runtime capabilities.

## Security and data lifecycle

- Read-only YouTube scope; no write operations or account modification.
- Google password and sign-in remain on Google’s own UI.
- Access token is held only in JavaScript module memory. It is never put in localStorage, IndexedDB, exports, URLs, the repository or the ZIP.
- API calls use an Authorization header and `cache: no-store`; the service worker ignores Google requests.
- Reloads and token expiry require reconnecting through a user action.
- Disconnect revokes current Google consent and clears the in-memory token. Imported local copies remain until removed by the user.
- Playlist names, imported tracks, channel display name/ID and import timestamps are kept in this browser. Library exports may include imported private playlist titles and track metadata, so treat exports accordingly.
- Public client IDs are not secrets. OAuth projects still need proper origin restriction, consent configuration, quota monitoring, and Google verification where required.

## Primary references

- https://developers.google.com/identity/oauth2/web/guides/use-token-model
- https://developers.google.com/youtube/data/guides/authentication
- https://developers.google.com/youtube/data/reference/rest/v3/playlists/list
- https://developers.google.com/youtube/data/reference/rest/v3/playlistItems/list
- https://developers.google.com/youtube/data/reference/rest/v3/videos/list
