# Alerting and Detection Strategy Framework


- https://github.com/palantir/alerting-detection-strategy-framework
- https://github.com/palantir/alerting-detection-strategy-framework/blob/master/ADS-Framework.md

1. Goal - Determine what needs to be detected
2. Categorization - Mapping the MITRE ATT&CK frameowrk TTPs and areas of the kill chain where ADS will be used
3. Strategy Abstract - top-level description of implementation functions
4. Technical Context - Technical environment of the detection being used
5. Blind Spots and Assumptions - Potential pitfalls in detection engineering
6. False Positives - Outlining where false-positives or false-negatives may occur
7. Validation - Where detection is verified, true-positives validated
8. Priority - alert levels shown through an SIEM or information collection platform
9. Response - triage of detection alerts, SOAR, incident response, XDR