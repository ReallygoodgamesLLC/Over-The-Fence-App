# Over the Fence for iPhone and iPad (TestFlight)

This folder is the iOS app. It is the game page wrapped in a small native app that runs fully offline:
three.js and the fonts are bundled inside, and saved progress (levels, stars, toys) stays on the device.
It builds with Codemagic exactly like Witch's Greenhouse, and uploads to TestFlight for your internal testers.

- App name under the icon: **Over the Fence**
- Bundle ID: **com.reallygoodgame.overthefence**
- iPhone and iPad, landscape only, full screen, iOS 15 or newer

## One-time setup

1. **Register the bundle ID.** developer.apple.com → Certificates, Identifiers & Profiles → Identifiers → + → App IDs → App.
   Description "Over the Fence", Bundle ID (Explicit) `com.reallygoodgame.overthefence`. No extra capabilities needed.
2. **Create the app in App Store Connect.** appstoreconnect.apple.com → Apps → + → New App.
   Platform iOS, name "Over the Fence" (if it's taken, add something like "Over the Fence Game"; the name under the icon can stay "Over the Fence"),
   language English, bundle ID `com.reallygoodgame.overthefence`, SKU `overthefence`.
3. **Copy the app's Apple ID.** In the new app: App Information → General Information → **Apple ID** (a long number).
   Paste it into `codemagic.yaml` in place of `0000000000`.
4. **Use your existing Codemagic API key.** In `codemagic.yaml`, change `CODEMAGIC_ASC_KEY` to the name of the
   App Store Connect integration you already use for Witch's Greenhouse (Codemagic → Team settings → Integrations).
5. **Put this folder in a new GitHub repo** (for example `over-the-fence-ios`) and push it.
6. **Add the repo in Codemagic.** Codemagic → Add application → pick the repo → it finds `codemagic.yaml`.
7. **Internal testers.** App Store Connect → the app → TestFlight → Internal Testing → + to make a group, add your testers.
   Turn on automatic distribution for the group so every new build reaches them.

## Every new build

1. Copy the newest game into `game-source.html` (download it from the artifact, or ask me for the file).
2. Commit and push. In Codemagic, start the **Over the Fence → TestFlight** workflow.
3. Codemagic runs `build_web.py`, makes the Xcode project, signs, numbers the build and uploads it.
   After Apple finishes processing (usually 10–30 minutes) testers get it in the TestFlight app.

## Notes

- `build_web.py` swaps the internet-only parts of the game (three.js CDN, Google Fonts) for the bundled copies and
  refuses to build if the page still has test hooks in it.
- Export compliance is answered in Info.plist (no non-exempt encryption), so TestFlight won't ask each time.
- The icon is `OverTheFence/Assets.xcassets/AppIcon.appiconset/icon-1024.png`. Swap it any time with another 1024×1024 PNG (no transparency).
- To debug on a test device: Safari on a Mac → Develop → your iPhone → Over the Fence.
