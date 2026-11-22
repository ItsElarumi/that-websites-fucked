# THAT WEBSITE'S FUCKED

## Independent security investigation

**Case ID:** ELARUMI-EPIC-2026-001
**Prepared by:** Elarumi
**Investigation date:** 22 November 2026
**Classification:** Suspected phishing / possible brand impersonation
**Status:** Reports submitted to some relevant parties; outcomes unconfirmed.

---

## 1. Executive summary

This investigation began after a suspicious Fortnite tournament invitation was shared through Discord.

The invitation promoted a tournament described as "FNCS PRO-LEAGUE" and encouraged the recipient to join a team called "Falcons". The message included a website presenting itself as a Fortnite competitive or esports destination.

The website domain observed during the investigation was:

`fortnitecompetitive[.]fun`

The invitation and website presentation raised concerns about possible brand impersonation and phishing.

The available evidence does not establish that credentials were stolen, that the website successfully collected credentials, or that the website was operated by any particular person or organisation.

## 2. What was observed

The Discord invitation included the following message:

> register in 'FNCS PRO-LEAGUE' and join in my team 'Falcons'

The associated website paths observed were:

- `fortnitecompetitive[.]fun/tournaments/falcons`
- `fortnitecompetitive[.]fun/tournaments/falcons/login`

The website preview presented Fortnite-related branding and described itself as a Fortnite competitive or esports destination.

These observations raised a concern that visitors could mistake the site for an official Fortnite service.

A screenshot was supplied by another person and subsequently downloaded for evidence preservation. The screenshot is not included in this public repository.

## 3. Technical observations

### Domain registration

The RDAP information collected during the investigation indicated:

- Registration date: 17 November 2026
- Last changed: 22 November 2026
- Expiration date: 17 November 2027
- Registrar: REG.RU LLC

Registration information identifies a registrar, not necessarily the website operator or the person responsible for the content.

### DNS observations

The DNS lookup returned the following records:

**A records (IPv4):**
- `104.21.96.131`
- `172.67.180.252`

**AAAA records (IPv6):**
- `2606:4700:3035::6815:6083`
- `2606:4700:3036::ac43:b4fc`

**NS records (nameservers):**
- `ignat.ns.cloudflare.com`
- `ara.ns.cloudflare.com`

**SOA record:**
- Primary nameserver (MNAME): `ara.ns.cloudflare.com.`
- Responsible party field (RNAME): `dns.cloudflare.com.`

**MX records:** No records found in the lookup.

**TXT records:** No records found in the lookup.

The returned IP addresses and nameservers are consistent with Cloudflare infrastructure. This does not establish that Cloudflare operates the website's origin server, owns the domain, or is responsible for its content. The origin server and website operator were not identified.

The absence of MX or TXT records in this lookup does not prove that the operator has no email service or that no other DNS configuration exists.

### Certificate transparency

The crt.sh lookup returned an HTTP 502 error during collection.

This result was inconclusive. It does not establish that the domain had no certificates or that HTTPS was absent.

## 4. Investigation boundaries

The investigation was limited to passive observation and responsible reporting.

The following actions were not performed:

- No credentials were entered or submitted.
- No credential transmission was tested.
- No unauthorised access was attempted.
- No exploitation was performed.
- No service disruption or denial-of-service activity was performed.
- No attempt was made to identify or expose a private individual behind the website.

Accordingly, this report does not claim confirmed credential theft, confirmed compromise, or confirmed malicious backend activity.

## 5. Reporting and disclosure history

### Epic Games

An incident report and evidence archive were sent to Epic Games security on 22 November 2026.

The automated response directed vulnerability reports to HackerOne.

The Epic Games HackerOne programme information reviewed during this investigation described a closed scope and excluded social engineering, including phishing, as well as third-party assets not owned by Epic Games.

The suspicious domain was not established to be an Epic-owned asset. No bounty eligibility or Epic investigation is claimed.

### REG.RU

An abuse report and evidence archive were sent to REG.RU on 22 November 2026.

A response or remediation outcome had not been confirmed when this document was prepared.

### Discord

The person who originally received the invitation reported the Discord message.

The report reference and outcome were not independently confirmed for this investigation.

### Cloudflare

Attempts to access the Cloudflare abuse portal resulted in access-block pages.

No Cloudflare abuse report was successfully submitted during this investigation.

An access-support enquiry was drafted but had not been sent when this document was prepared.

No Cloudflare investigation or action is claimed.

## 6. Evidence handling and privacy

The original investigation files are maintained separately from this public repository.

This public version intentionally excludes:

- The original screenshot supplied by another person.
- Discord usernames, account IDs, and message IDs.
- Private messages and correspondence.
- The original evidence ZIP archive.
- Private or identifying information about any suspected individual.

The screenshot's authenticity and original capture date were not independently verified.

The technical observations represent the results of checks performed during this investigation. They should not be interpreted as a guarantee of the website's current state.

## 7. Current conclusion

The combination of a Fortnite-themed tournament invitation, Fortnite-related website presentation, and the observed domain justified raising a phishing and possible impersonation concern.

However, the available evidence is insufficient to establish:

- Who operates the website.
- Whether the operator is intentionally impersonating Epic Games.
- Whether credentials or other information were collected.
- Whether any visitor was compromised.
- Whether Epic Games, Discord, REG.RU, or Cloudflare took action.
- Whether the website has since been disabled or changed.

The appropriate conclusion is therefore **suspected phishing / possible brand impersonation**, pending confirmation by the relevant service providers.

## 8. Responsible disclosure

If you believe you have encountered this website or a similar invitation, avoid entering passwords or personal information. Use official service-provider reporting channels and preserve relevant evidence without interacting with suspicious login pages.

This report is intended to document observations and encourage responsible handling, not to facilitate retaliation, harassment, or unauthorised access.

---

**FUCK SCAMMERS. GO GET A LIFE. XD <3**
