# https://securityaffairs.com/166190/security/bind-updates-high-severity-dos-bugs.html

# CVE-2024-4076 | Assertion Failure When Serving Both Stale Cache Data And Authoritative Zone Content
https://www.cve.org/CVERecord?id=CVE-2024-4076

# CVE-2024-1975 | SIG(0) Can Be Used To Exhaust CPU Resources
https://www.cve.org/CVERecord?id=CVE-2024-1975

# CVE-2024-1737 | BIND's Database Will Be Slow If A Very Large Number Of RRs Exist At The Same Name
https://www.cve.org/CVERecord?id=CVE-2024-1737

# CVE-2024-0760 | A Flood of DNS Messages Over TCP May Make The Server Unstable
https://www.cve.org/CVERecord?id=CVE-2024-0760

The vulnerability CVE-2024-4076 in BIND 9 can cause an assertion failure when serving stale data alongside lookups in local authoritative zone data. This issue affects specific versions, including 9.16.13 through 9.16.50, 9.18.0 through 9.18.27, 9.19.0 through 9.19.24, 9.11.33-S1 through 9.11.37-S1, 9.16.13-S1 through 9.16.50-S1, and 9.18.11-S1 through 9.18.27-S1.

A vulnerability CVE-2024-1975 in BIND 9 allows clients to exhaust CPU resources by sending a stream of SIG(0) signed requests if the server hosts a “KEY” Resource Record or the resolver DNSSEC-validates such a record in cache. The vulnerability impacts BIND 9 versions 9.0.0 through 9.11.37, 9.16.0 through 9.16.50, 9.18.0 through 9.18.27, 9.19.0 through 9.19.24, 9.9.3-S1 through 9.11.37-S1, 9.16.8-S1 through 9.16.49-S1, and 9.18.11-S1 through 9.18.27-S1

A performance issue in BIND 9, tracked as CVE-2024-1737, can occur when resolver caches or authoritative zone databases contain many resource records (RRs) for the same hostname. The flaw affects the addition or updating of content and the handling of client queries. Impacted BIND 9 versions include 9.11.0 through 9.11.37, 9.16.0 through 9.16.50, 9.18.0 through 9.18.27, 9.19.0 through 9.19.24, and certain 9.11.4-S1, 9.16.8-S1, and 9.18.11-S1 series versions.

In BIND 9 versions 9.18.1 through 9.18.27, 9.19.0 through 9.19.24, and 9.18.11-S1 through 9.18.27-S1, a vulnerability tracked as CVE-2024-0760 exists where a malicious client can send numerous DNS messages over TCP, potentially destabilizing the server during the attack. The server may recover once the attack stops. Using Access Control Lists (ACLs) does not mitigate this issue
ISC not aware of public exploits for these flaws or attacks exploiting these vulnerabilities in the wild.  