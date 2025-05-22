# DREAD | Damage, Reproducability, Exploitability, Affected users, Discoverability
- https://en.wikipedia.org/wiki/DREAD_(risk_assessment_model)
- https://learn.microsoft.com/en-us/archive/blogs/david_leblanc/dreadful


# Damage
- How bad would an attack be?
- Is it a vulnerability, a flaw, or an error, and is it exploitable?

# Reproducibilty / Reliability
- How easy is it to reproduce the attack?
- How likely is it to occur?

# Exploitability
- How much work is it to launch the attack
- Does the exploit work every time?
- Does it require special configuration
- Does it require an information link?

# Affected Users
- How many people will be impacted?

# Discoverability
- How easy is it to discover the threat?
- Is it publicly known?
- Is it publicly disclosed?

# Scoring with DREAD
```
Severity = f(Damage, Reproducability, Affected Users)

Base severity (1-5) = Damage + f(R, A)

If R + A > 4 (both high, or one high and the other at least medium), add 2
else if R + A > 3 (one high, or both medium) add 1
else add 0

If E = high, Di = high, add 4
else if one is high, other medium, add 3
else if one is high, other low, add 2
else if both medium, add 1
else add 0
```