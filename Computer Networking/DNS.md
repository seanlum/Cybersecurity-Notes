# Tools for DNS on macOS, Windows, Linux, and Cross-Platform

### IETF RFCs
```
# DOMAIN NAMES - IMPLEMENTATION AND SPECIFICATION
https://datatracker.ietf.org/doc/html/rfc1035

# DOMAIN NAMES - CONCEPTS AND FACILITIES
https://datatracker.ietf.org/doc/html/rfc1034

# DOMAIN ADMINISTRATORS OPERATIONS GUIDE
https://datatracker.ietf.org/doc/html/rfc1033
```

## nslookup

### Getting information on Running nslookup

```
# On Linux or macOS or UNIX
man nslookup
```
#### [nslookup man page](https://linux.die.net/man/1/nslookup)
#### [nslookup on Microsoft Learn](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/nslookup)


### General Usage
```
$ nslookup

# Display Debug information
> set debug
> set d2

# Getting configuration information
> set all

# Setting a searchlist
> set srchlist=<fqdn>/<fqdn>/<fqdn>

# Turn off Debug information 
> set no debug
> set no d2

# Setting The Server
> server <ip_address>
> <fqdn.dns.ext>

# Setting the port
> set port=53
> set port=5353

# Setting the query retry count
> set retry=<int>

# Specifying the timeout length
> set timeout=<time_seconds>
```
### Setting types of DNS Records
```
# Set query type
> set type=<...>
> set querytype=<...>
A: Specifies a computer's IP address.
ANY: Specifies a computer's IP address.
CNAME: Specifies a canonical name for an alias.
GID Specifies a group identifier of a group name.
HINFO: Specifies a computer's CPU and type of operating system.
MB: Specifies a mailbox domain name.
MG: Specifies a mail group member.
MINFO: Specifies mailbox or mail list information.
MR: Specifies the mail rename domain name.
MX: Specifies the mail exchanger.
NS: Specifies a DNS name server for the named zone.
PTR: Specifies a computer name if the query is an IP address; otherwise, specifies the pointer to other information.
SOA: Specifies the start-of-authority for a DNS zone.
TXT: Specifies the text information.
UID: Specifies the user identifier.
UINFO: Specifies the user information.
WKS: Describes a well-known service.
```

### Attempting Domain Transfer
```
$ nslookup
> set type=AXFR
> domain.fqdn.ext
```

### Performing a Reverse Lookup
```
$ nslookup
> set type=PTR
> <ipv4_address>

$ nslookup <ipv4_address>

$ host <ipv4_address>
```

### host command
```
# Documentation
$ man host

$ host
Usage: host [-aCdilrTvVw] [-c class] [-N ndots] [-t type] [-W time]
            [-R number] [-m flag] hostname [server]
       -a is equivalent to -v -t ANY
       -c specifies query class for non-IN data
       -C compares SOA records on authoritative nameservers
       -d is equivalent to -v
       -i IP6.INT reverse lookups
       -l lists all hosts in a domain, using AXFR
       -m set memory debugging flag (trace|record|usage)
       -N changes the number of dots allowed before root lookup is done
       -r disables recursive processing
       -R specifies number of retries for UDP packets
       -s a SERVFAIL response should stop query
       -t specifies the query type
       -T enables TCP/IP mode
       -v enables verbose output
       -V print version number and exit
       -w specifies to wait forever for a reply
       -W specifies how long to wait for a reply
       -4 use IPv4 query transport only
       -6 use IPv6 query transport only
```

### dig command
```
$ dig -h
dig -h                    
Usage:  dig [@global-server] [domain] [q-type] [q-class] {q-opt}
            {global-d-opt} host [@local-server] {local-d-opt}
            [ host [@local-server] {local-d-opt} [...]]
Where:  domain	  is in the Domain Name System
        q-class  is one of (in,hs,ch,...) [default: in]
        q-type   is one of (a,any,mx,ns,soa,hinfo,axfr,txt,...) [default:a]
                 (Use ixfr=version for type ixfr)
        q-opt    is one of:
                 -4                  (use IPv4 query transport only)
                 -6                  (use IPv6 query transport only)
                 -b address[#port]   (bind to source address/port)
                 -c class            (specify query class)
                 -f filename         (batch mode)
                 -i                  (use IP6.INT for IPv6 reverse lookups)
                 -k keyfile          (specify tsig key file)
                 -m                  (enable memory usage debugging)
                 -p port             (specify port number)
                 -q name             (specify query name)
                 -t type             (specify query type)
                 -u                  (display times in usec instead of msec)
                 -x dot-notation     (shortcut for reverse lookups)
                 -y [hmac:]name:key  (specify named base64 tsig key)
        d-opt    is of the form +keyword[=value], where keyword is:
                 +[no]aaonly         (Set AA flag in query (+[no]aaflag))
                 +[no]additional     (Control display of additional section)
                 +[no]adflag         (Set AD flag in query (default on))
                 +[no]all            (Set or clear all display flags)
                 +[no]answer         (Control display of answer section)
                 +[no]authority      (Control display of authority section)
                 +[no]besteffort     (Try to parse even illegal messages)
                 +bufsize=###        (Set EDNS0 Max UDP packet size)
                 +[no]cdflag         (Set checking disabled flag in query)
                 +[no]cl             (Control display of class in records)
                 +[no]cmd            (Control display of command line)
                 +[no]comments       (Control display of comment lines)
                 +[no]crypto         (Control display of cryptographic fields in records)
                 +[no]defname        (Use search list (+[no]search))
                 +[no]dnssec         (Request DNSSEC records)
                 +domain=###         (Set default domainname)
                 +[no]edns[=###]     (Set EDNS version) [0]
                 +ednsflags=###      (Set EDNS flag bits)
                 +[no]ednsnegotiation (Set EDNS version negotiation)
                 +ednsopt=###[:value] (Send specified EDNS option)
                 +noednsopt          (Clear list of +ednsopt options)
                 +[no]expire         (Request time to expire)
                 +[no]fail           (Don't try next server on SERVFAIL)
                 +[no]identify       (ID responders in short answers)
                 +[no]idnout         (convert IDN response)
                 +[no]ignore         (Don't revert to TCP for TC responses.)
                 +[no]keepopen       (Keep the TCP socket open between queries)
                 +[no]multiline      (Print records in an expanded format)
                 +ndots=###          (Set search NDOTS value)
                 +[no]nsid           (Request Name Server ID)
                 +[no]nssearch       (Search all authoritative nameservers)
                 +[no]onesoa         (AXFR prints only one soa record)
                 +[no]opcode=###     (Set the opcode of the request)
                 +[no]qr             (Print question before sending)
                 +[no]question       (Control display of question section)
                 +[no]recurse        (Recursive mode)
                 +retry=###          (Set number of UDP retries) [2]
                 +[no]rrcomments     (Control display of per-record comments)
                 +[no]search         (Set whether to use searchlist)
                 +[no]short          (Display nothing except short
                                      form of answer)
                 +[no]showsearch     (Search with intermediate results)
                 +[no]split=##       (Split hex/base64 fields into chunks)
                 +[no]stats          (Control display of statistics)
                 +subnet=addr        (Set edns-client-subnet option)
                 +[no]tcp            (TCP mode (+[no]vc))
                 +time=###           (Set query timeout) [5]
                 +[no]trace          (Trace delegation down from root [+dnssec])
                 +tries=###          (Set number of UDP attempts) [3]
                 +[no]ttlid          (Control display of ttls in records)
                 +[no]vc             (TCP mode (+[no]tcp))
        global d-opts and servers (before host name) affect all queries.
        local d-opts and servers (after host name) affect only that lookup.
        -h                           (print help and exit)
        -v                           (print version and exit)

```

## macOS
```

# Display DNS resolver information
$ scutil --dns

# Display DNS Server
$ nslookup
> server

# Multicast DNS (mDNS) & DNS Service Discovery (DNS-SD) Test Tool
$ dns-sd -h 

$ dscacheutil -q host -a name <domain>: Query the DNS and local resolver cache

$ networksetup -getdnsservers <networkservice>: Show configured DNS servers
```