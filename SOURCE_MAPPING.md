# Native source porting map

Pinned upstream: maxrave-dev/SimpMusic, c11ee6a38102b6065dd27b71cb12b0afef61f54a.

| Browser implementation | Original implementation used |
| --- | --- |
| `icons.js` | 26 original `SimpIcons` Kotlin ImageVector definitions; path commands mechanically converted to SVG |
| `scripts/port-icons.py` | Reproducible converter retaining original curves, relative coordinates and winding |
| `upstream-reference/icons/*.kt` | Exact original source for the ported icons |
| `native.css` header | `HomeScreen.kt`: 56dp row, 16dp avatar inset, 4dp chip spacing, pinned Create/actions on wide screens |
| `native.css` quick-pick rail | `QuickPicks` in `HomeScreen.kt` and `QuickPicksItem` in `AdapterItems.kt`: four 64dp rows, 256dp rail, 44dp artwork, 16dp title gap, 10dp row padding |
| `native.css` touch navigation | `AppBottomNavigationBar.kt`: 64dp capsule, 56dp selection indicator and detached Search circle, 6dp internal inset, 12dp inter-control gap, up to 96dp tabs |
| `native.css` fonts/type | `Typo.kt`: Poppins Medium family, 13sp titles, 11sp metadata, 20sp section headers |
| Theme and artwork | `Color.kt`: #8ECAE6 seed, #FF4081 favourite, #121212 desktop panels; original app icon |
| Account implementation | Native `LogInScreen.kt` reviewed; native cookie-manager functions are replaced with GIS OAuth rather than misrepresented as web-compatible |

`upstream-reference/Typo.kt` and `Color.kt` retain the native definitions used. All borrowed code/assets retain GPL and font notices. The CSS converts Compose dp/sp values to CSS px at normal browser scaling; platform rendering, dynamic Material palette generation, and native glass refraction still differ. Dynamic server recommendations are not fabricated when no account data is available.

The UI now selects a touch-native shell on phones and tablets, including iPad landscape. Fine-pointer desktop windows retain the native desktop sidebar and optional now-playing column. Empty player surfaces are hidden until a song is selected. Source-derived icons replace generic glyph/emoji controls.
