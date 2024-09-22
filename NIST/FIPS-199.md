# FIPS PUB 199 | Federal Information Processing Standard 199

# Documents 
- [E-Government Act of 2014 (Public Law 113-283) FISMA](https://www.govinfo.gov/app/details/PLAW-113publ283/) (16 Pages)
- [E-Government Act of 2002 (Public Law 107-347) FISMA ](https://www.congress.gov/107/plaws/publ347/PLAW-107publ347.pdf) (72 Pages) 
- [NIST FISMA](https://csrc.nist.gov/topics/laws-and-regulations/laws/fisma) 
- [44 USC 3542 (b)(2)](https://www.govinfo.gov/content/pkg/USCODE-2011-title44/html/USCODE-2011-title44-chap35-subchapIII-sec3542.htm) (1 Page)

# Purpose summary
FISMA tasks NIST to develop standards, guidelines, associatead methods and techniques for information systems, and other information related to computer systems used between contractors, agencies, and other agencies within the Federal government. The standards upheld by NIST are set by FISMA as well.

```
• Standards to be used by all federal agencies to categorize all information and information systems collected or maintained by or on behalf of each agency based on the objectives of providing appropriate levels of information security according to a range of risk levels;
• Guidelines recommending the types of information and information systems to be included in each category; and
• Minimum information security requirements (i.e., management, operational, and technical
controls), for information and information systems in each such category.
```

# Applicability
```
(i) All information within the federal government other than that information that has been determined pursuant to Executive Order 12958, as amended by Executive Order 13292, or any predecessor order, or by the Atomic Energy Act of 1954, as amended, to require protection against unauthorized disclosure and is marked to indicate its classified status and
```
```
(ii) all federal information systeams other than those information systems designated as national security systems as defined in 44 United States Code Section 3542(b)(2).
```
```
Agency officials shall use the security categorizations described in FIPS Publication 199 whenever there is a federal requirement to provide such a categorization of information or information systems. Additional security designators may be developed and used at agency discretion. State, local, and tribal governments as well as private sector organizations comprising the critical infrastructure of the United States may consider the use of these standards as appropriate. These standards are effective upon approval by the Secretary of Commerce.
```

### Sub note 44 United States Code Section 3542 (b)(2)
```
(2)(A) The term ‘‘national security system’’ means any information system (including any telecommunications system) used or operated by an agency or by a contractor of an agency, or other organization on behalf of an agency—

    (i) the function, operation, or use of which—
        (I) involves intelligence activities;
        (II) involves cryptologic activities related to national security;
        (III) involves command and control of military forces;
        (IV) involves equipment that is an integral part of a weapon or weapons system; or
        (V) subject to subparagraph (B), is critical to the direct fulfillment of military or intelligence missions; or
    (ii) is protected at all times by procedures established for information that have been specifically authorized under criteria established by an Executive order or an Act of Congress to be kept classified in the interest of national defense or foreign policy.
(B) Subparagraph (A)(i)(V) does not include a system that is to be used for routine administrative and business applications (including payroll, finance, logistics, and personnel management applications).
```

# Categorization of Information and Information Systems
- The definition for Confidentiality, Integrity, and Availability are all defined within [44 U.S.C., Sec. 3542](https://www.govinfo.gov/content/pkg/USCODE-2011-title44/html/USCODE-2011-title44-chap35-subchapIII-sec3542.htm)

### Confidentiality
as defined in FISMA
```
(B) confidentiality, which means preserving author-
ized restrictions on access and disclosure, including means
for protecting personal privacy and proprietary information;
```
A loss of confidentiality is the unauthorized disclosure of information.

### Integrity
as defined in FISMA
```
(A) integrity, which means guarding against improper
information modification or destruction, and includes
ensuring information nonrepudiation and authenticity;
```
A loss of integrity is the unauthorized modification or destruction of information.
### Availability
as defined in FISMA
```
(C) availability, which means ensuring timely and
reliable access to and use of information
```
A loss of availability is the disruption of access to or use of information or an information system.

## Potential Impact on Organizations and Individuals

### The `potential impact` is **LOW** if --
As defined in FIPS 199
```
− The loss of confidentiality, integrity, or availability could be expected to have a limited adverse effect on organizational operations, organizational assets, or individuals. (2)

(2) - Adverse effects on individuals may include, but are not limited to, loss of the privacy to which individuals are entitled
under law

AMPLIFICATION: A limited adverse effect means that, for example, the loss of confidentiality, integrity, or availability might: 

  (i) cause a degradation in mission capability to an extent and duration that the organization is able to perform its primary functions, but the effectiveness of the functions is noticeably reduced; 
  (ii) result in minor damage to organizational assets; 
  (iii) result in minor financial loss; or (iv) result in minor harm to individuals.
```

### The `potential impact` is **MODERATE** if--
As defined in FIPS 199
```
− The loss of confidentiality, integrity, or availability could be expected to have a serious adverse effect on organizational operations, organizational assets, or individuals.

AMPLIFICATION: A serious adverse effect means that, for example, the loss of confidentiality, integrity, or availability might:
 
  (i) cause a significant degradation in mission capability to an extent and duration that the organization is able to perform its primary functions, but the effectiveness of the functions is significantly reduced;
  (ii) result in significant damage to organizational assets;
  (iii) result in significant financial loss; or
  (iv) result in significant harm to individuals that does not involve loss of life or serious life threatening injuries.
```

### The `potential impact` is **HIGH** if--
As defined in FIPS 199
```
− The loss of confidentiality, integrity, or availability could be expected to have a severe or catastrophic adverse effect on organizational operations, organizational assets, or individuals.

AMPLIFICATION: A severe or catastrophic adverse effect means that, for example, the loss of confidentiality, integrity, or availability might:

  (i) cause a severe degradation in or loss of mission capability to an extent and duration that the organization is not able to perform one or more of its primary functions;
  (ii) result in major damage to organizational assets;
  (iii) result in major financial loss; or
  (iv) result in severe or catastrophic harm to individuals involving loss of life or serious life threatening injuries.
```

## Security Categorization Applied to Information Types
```
The security category of an information type can be associated with both user information and system information3 and can be applicable to information in either electronic or non-electronic form. It can also be used as input in considering the appropriate security category of an information system (see description of security categories for information systems below). Establishing an appropriate security category of an information type essentially requires determining the potential impact for each security objective associated with the particular information type.
```
```
SC information type = {
  (confidentiality, impact), 
  (integrity, impact), 
  (availability, impact)
},

where the acceptable values for potential impact are LOW, MODERATE, HIGH, or NOT APPLICABLE.
```

There are further examples within [FIPS 199](https://csrc.nist.gov/pubs/fips/199/final)