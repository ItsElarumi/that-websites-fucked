# VirusTotal Repository URL Analysis

**Repository:** `ItsElarumi/that-websites-fucked`
**Scanned URL:** https://github.com/ItsElarumi/that-websites-fucked
**Analysis service:** VirusTotal
**Analysis section:** GTI Summary
**Observed scan transaction:** 23 November 2026, 07:47:07 UTC
**Purpose:** Record the public URL reputation and page-technology observations for the Elarumi investigation repository.

**VirusTotal report:**
https://www.virustotal.com/gui/url/5e7d76133596a728ff973d5cf24624d29c1dae2cfaa8ba9ae3aff50dcf32b551/gti-summary

---

## 1. Security vendor analysis

The supplied VirusTotal vendor analysis showed no malicious or suspicious verdicts among the entries provided.

The repository-page HTTP transaction showed:

- **Detections:** 0 / 93
- **HTTP status:** 200
- **Final URL:** `https://github.com/ItsElarumi/that-websites-fucked`

The vendor list supplied for review contained entries marked `Clean` and `Unrated`. An `Unrated` result is not a clean verdict. These results represent the scan at the recorded time and may change.

This is a URL reputation result. It is not a source-code audit, a guarantee of safety, or proof that every file in the repository is free of malicious content.

## 2. Page and technology observations

VirusTotal reported the following web technologies:

- GitHub Pages
- HSTS
- Amazon S3
- lit-html
- Turbo
- React
- Amazon Web Services

These are technologies associated with the scanned page and its hosting environment. Their appearance does not establish that the repository itself directly uses or operates each technology.

Other reported page statistics:

| Observation | Reported result |
|---|---:|
| Page stats | 116 |
| Associated domains | 3 |
| Associated IP addresses | 4 |
| Countries | 1 |
| Reported transfer size | 7.92 MB |
| Cookies observed | 6 |
| Trackers | Not found |

These are scanner observations, not proof that the repository communicates with malicious infrastructure.

## 3. JavaScript global-variable inventory

VirusTotal reported **96 JavaScript global variables** on the scanned GitHub page.

Examples included:

| Variable or component | Observed type | Context |
|---|---|---|
| `Turbo` | Object | GitHub page navigation framework |
| `litHtmlVersions` | Object | Lit HTML version information |
| `__reactRouterVersion` | String | React Router version metadata |
| `__TANSTACK_QUERY_CLIENT__` | Object | TanStack Query client reference |
| `ActionBarElement` | Function | GitHub interface component |
| `ModalDialogElement` | Function | GitHub interface component |
| `MarkdownToolbarElement` | Function | Markdown editing interface |
| `ClipboardCopyElement` | Function | Clipboard interface component |
| `ImageCropElement` | Function | Image interface component |
| `onpagereveal` | Object | Browser lifecycle event property |
| `onpageswap` | Object | Browser lifecycle event property |

The inventory also included short, minified names such as `t_`, `tK` and `iM`.

### Interpretation

A count of 96 global variables is not a vulnerability score. Globally accessible functions, framework objects and browser event properties are not inherently exploitable.

The names and types are consistent with a modern, JavaScript-based GitHub frontend. The inventory does not demonstrate that the repository's Markdown documents or scripts expose these globals, nor does it establish that any secret or credential was disclosed.

No vulnerability is established by this inventory alone.

## 4. Cookies and privacy handling

VirusTotal reported six cookies associated with GitHub domains, including cookie names such as:

- `tz`
- `_octo`
- `_gh_sess`
- `logged_in`
- `preferred_color_mode`
- `cpu_bucket`

**Cookie values and visitor identifiers are deliberately excluded from this public record.** The supplied scan output contained session-related and visitor-identification values. They are unnecessary for the security conclusions and should not be reproduced in public documentation.

The reported `logged_in` cookie value was `no`, indicating that the scanned page reported a logged-out state at that time. This does not establish the state of every browser session or account.

## 5. Network requests and external resources

The supplied scan displayed 10 of 116 network-request records.

The repository page transaction returned:

- HTTP status `200`
- 0 detections out of 93
- HTML content type
- Final URL on `github.com`

The displayed supporting resources were predominantly hosted on `github.githubassets.com`, including JavaScript bundles, stylesheets and images.

The scan also reported GitHub page metadata, including the repository's public status and canonical repository URL.

These observations are consistent with the page being served through GitHub's own infrastructure. They do not establish that GitHub operates or endorses the subject of the separate website investigation.

## 6. HTTP response security headers

The supplied response included the following headers:

| Header | Observed value | General purpose |
|---|---|---|
| `strict-transport-security` | `max-age=31536000; includeSubdomains; preload` | Enforces HTTPS |
| `content-security-policy` | Present | Restricts permitted resource sources |
| `x-frame-options` | `deny` | Prevents framing |
| `x-content-type-options` | `nosniff` | Prevents MIME-type sniffing |
| `referrer-policy` | `no-referrer-when-downgrade` | Controls referrer disclosure |

These are headers observed on GitHub's response. They should not be represented as security settings configured by Elarumi in the repository.

## 7. Assessment and limitations

The supplied VirusTotal results are encouraging:

1. No security vendor detections were shown for the recorded repository-page transaction.
2. The page returned HTTP 200.
3. The tracker analysis reported no trackers found.
4. The observed JavaScript globals and technologies are consistent with GitHub's frontend.
5. No vulnerability is demonstrated by the JavaScript inventory, cookie count or technology fingerprint.

Limitations:

- This is a point-in-time URL scan, not a continuous monitoring result.
- The scan primarily assesses the public GitHub page and its associated resources.
- The result does not constitute a complete audit of repository contents, commit history, dependencies or account security.
- `Unrated` vendor results must not be interpreted as clean verdicts.
- The analysis does not guarantee future safety or prevent later changes to the repository or hosting platform.

**Conclusion:** The supplied VirusTotal URL analysis showed no vendor detections in the recorded repository-page transaction. The additional page metadata does not establish a security issue with the repository.

---

*Prepared as a separate repository reputation record on 23 November 2026. Raw session values, visitor identifiers, request identifiers and other unnecessary tracking data have been excluded.*
