# coding=utf-8

"""
Provides a mapping from OpenProvider API error codes to Python exceptions.
"""

from openprovider.exceptions import *  # NOQA

MAPPING = {
    0: OpenproviderError,           # No errors
    1: BadRequest,                  # No changes in the data
    10: ServiceUnavailable,         # Registry currently not reachable
    11: ServerError,                # ERROR CODA response error
    12: OpenproviderError,          # This is not an error.
    15: ServiceUnavailable,         # EU registration currently closed.
    16: RuleViolation,              # Domain is blocked or reserved by EURid
    17: ServiceUnavailable,         # Error communicating with registry
    18: OpenproviderError,          # Data is already up-to-date
    98: NoSuchElement,              # Requested data not in data-set
    99: NoSuchElement,              # No data returned
    100: ValidationError,           # Empty initials!
    101: ValidationError,           # Invalid initials!
    102: ValidationError,           # Empty first name!
    103: ValidationError,           # Invalid first name!
    104: ValidationError,           # Invalid insertion!
    105: ValidationError,           # Empty last name field!
    106: ValidationError,           # Invalid lastname!
    107: ValidationError,           # Empty gender field!
    108: ValidationError,           # Invalid gender field!
    110: ValidationError,           # Empty street name field!
    111: ValidationError,           # Invalid street name!
    112: ValidationError,           # Empty house number field!
    113: ValidationError,           # Invalid housenumber!
    114: ValidationError,           # Invalid suffix field!
    115: ValidationError,           # Empty zipcode field!
    116: ValidationError,           # Invalid zipcode!
    117: ValidationError,           # Empty city field!
    118: ValidationError,           # Invalid city!
    119: ValidationError,           # Invalid state!
    120: ValidationError,           # Empty country field!
    121: ValidationError,           # Invalid country code!
    130: ValidationError,           # Empty telephone country code field!
    131: ValidationError,           # Invalid telephone country code!
    132: ValidationError,           # Empty telephone regioncode field!
    133: ValidationError,           # Invalid telephone region code number!
    134: ValidationError,           # Empty telephone subscribers number!
    135: ValidationError,           # Invalid telephone subscribers number!
    136: ValidationError,           # Incomplete telephone number!
    137: ValidationError,           # Invalid mobile country code!
    138: ValidationError,           # Invalid mobile region code!
    139: ValidationError,           # Invalid mobile subscribers number!
    140: ValidationError,           # Incomplete mobile number!
    141: ValidationError,           # Invalid fax country code!
    142: ValidationError,           # Invalid fax region code!
    143: ValidationError,           # Invalid fax subscribers number!
    144: ValidationError,           # Incomplete fax number!
    145: ValidationError,           # Empty e-mail address!
    146: ValidationError,           # Invalid e-mail!
    150: ValidationError,           # Invalid fiscal number!
    151: ValidationError,           # Invalid birthdate!
    152: ValidationError,           # Invalid birthcity!
    160: ValidationError,           # Empty companyname field!
    161: ValidationError,           # Invalid company name!
    162: ValidationError,           # Invalid vat number!
    163: ValidationError,           # Invalid Chambre of Commerce number!
    164: ValidationError,           # Invalid Chambre of Commerce region!
    165: ValidationError,           # Invalid Chambre of Commerce date!
    166: ValidationError,           # Empty mainoffice!
    167: ValidationError,           # Invalid mainoffice!
    168: ValidationError,           # Empty website field!
    169: ValidationError,           # Invalid website field!
    170: ValidationError,           # Empty type field!
    171: UniqueViolation,           # A contact person with type already exists
    172: ValidationError,           # Invalid customer type
    173: ServerError,               # ERROR while saving contact data
    174: ServerError,               # ERROR requesting external contactdata
    175: RuleViolation,             # Owner is not a citizen of an .EU member-state
    176: NoSuchElement,             # Customer handle not found
    177: NoSuchElement,             # External customer handle not found
    178: ServerError,               # Updating customer data with Registry Failed
    180: ValidationError,           # Empty search field!
    181: ValidationError,           # Choose a search type!
    182: ValidationError,           # Companyname already exists!
    183: RuleViolation,             # Customer is not an individual one
    184: RuleViolation,             # Customer is not a contact person
    185: RuleViolation,             # You cannot delete yourself as a reseller!
    186: RuleViolation,             # Company is still connected to handles!
    187: RuleViolation,             # Customer is still attached to some domains!
    190: ValidationError,           # Invalid username!
    191: ValidationError,           # Username already exists!
    192: RuleViolation,             # Password doesn't match verification!
    193: NoSuchElement,             # Handle is not recognized by the system
    194: NoSuchElement,             # Company is not known within the system!
    195: ValidationError,           # Invalid handle
    196: AuthenticationError,       # Authentication/Authorization Failed
    199: ServerError,               # An unknown error has occurred!
    200: ValidationError,           # Empty or invalid nameserver group name field!
    201: NoSuchElement,             # Nameserver group name not found in system!
    202: UniqueViolation,           # Nameserver group name already exists!
    203: RuleViolation,             # The nameservergroup attached to some domains
    220: ValidationError,           # Choose a group or individual nameservers!
    221: RuleViolation,             # 2 nameservers or a group required
    222: UniqueViolation,           # Invalid or double nameserver
    223: ValidationError,           # Empty nameservers/nameserver group name
    224: ValidationError,           # Nameserver not found in the Openprovider system
    225: ValidationError,           # Empty nameserver name NS-1 field!
    226: ValidationError,           # Invalid nameserver hostname
    227: ValidationError,           # Invalid nameserver IPv4 address
    228: ValidationError,           # Invalid nameserver IPv6 address
    229: ValidationError,           # Neither IPv4 nor IPv6 are specified
    230: UniqueViolation,           # Nameserver is already present in your account
    231: ValidationError,           # IP is not specified
    232: ValidationError,           # Empty nameserver IP-2 field!
    233: ValidationError,           # Invalid characters in nameserver IP-2 address
    234: ValidationError,           # Can t resolve IP address from host
    235: ValidationError,           # Empty nameserver name NS-3 field!
    236: ValidationError,           # Invalid nameserver name NS-3 field!
    237: ValidationError,           # Empty nameserver IP-3 field!
    238: ValidationError,           # Invalid characters in nameserver IP-3 address
    240: ValidationError,           # Empty nameserver name NS-4 field!
    241: ValidationError,           # Invalid nameserver name NS-4 field!
    242: ValidationError,           # Empty nameserver IP-4 field!
    243: ValidationError,           # Invalid characters in nameserver IP-4 address
    244: RuleViolation,             # The nameservercheck returned errors
    245: ValidationError,           # Nameserver-update failed
    299: ServerError,               # An unknown nameserver-error has occurred
    300: ValidationError,           # Your request contains an empty domain name!
    301: ValidationError,           # Your request contains only numbers!
    302: ValidationError,           # Your request has more than 63 characters!
    303: ValidationError,           # Your request contains invalid characters!
    304: ValidationError,           # Your request begins with an - !
    305: ValidationError,           # Your request ends with an - !
    306: ValidationError,           # Your request contains an empty extension!
    307: ValidationError,           # Your request contains an invalid extension!
    308: AuthenticationError,       # Openprovider doesn't have your signature
    309: AuthenticationError,       # You have not signed the latest contract
    310: InsufficientFunds,         # Credit is not enough!
    311: BadStateException,         # The domain you want to register is not free!
    312: BadStateException,         # The domain you want to register is free!
    313: BadStateException,         # The domain you want to transfer is free!
    315: ValidationError,           # Empty period!
    316: ValidationError,           # Invalid period!
    317: InvalidAuthorizationCode,  # Empty authorization code!
    318: InvalidAuthorizationCode,  # Authorization code is incorrect or missing.
    319: ValidationError,           # Authorization code for this extension cannot be requested
    320: NoSuchElement,             # The domain is not in your account
    321: RuleViolation,             # Domains with extension cannot be traded
    322: RuleViolation,             # Domains with extension cannot be transferred
    323: BadStateException,         # This is an internal transfer
    324: RuleViolation,             # This domain cannot be renewed yet
    325: RuleViolation,             # This domain is already renewed
    326: RuleViolation,             # This domain is already in your account
    327: RuleViolation,             # This domain already exists but NOT active
    328: RuleViolation,             # This domain is locked
    329: RuleViolation,             # Locking not possible for extension
    330: ValidationError,           # Empty owner handle!
    331: ValidationError,           # Invalid owner handle!
    332: ValidationError,           # Empty admin handle!
    333: ValidationError,           # Invalid admin handle!
    334: ValidationError,           # Empty tech handle!
    335: ValidationError,           # Invalid tech handle!
    336: RuleViolation,             # The owner-data differs too too much
    337: RuleViolation,             # The entered owner does not equal the whois
    338: ValidationError,           # Authorization code for this extension cannot be resetted
    339: InProgress,                # Not all external handles are created
    340: ServiceUnavailable,        # The registry is down for maintainance
    341: ServerError,               # ERROR saving domain data
    345: ValidationError,           # Bad provider specified
    346: UniqueViolation,           # Reseller cannot add duplicate domain
    347: ValidationError,           # Wrong auto renew value
    348: ValidationError,           # Can not reset authorization code for domain using registrar domicile
    349: ValidationError,           # Current method is not supported, connect to support please
    351: ValidationError,           # Authorization code type parameter can not be an array
    352: ValidationError,           # Authorization code validity has expired
    353: ValidationError,           # Domain is not known by registry
    354: ValidationError,           # There is no a transfer to approve or you are not permited to
    355: ValidationError,           # Incorrect domain deletion type specified
    356: ValidationError,           # Domain is not known by 3rd party registrar
    357: ValidationError,           # Bad routeId on domain during transfer action
    358: InvalidAuthorizationCode,  # Authorization code is invalid (undocumented code)
    359: ValidationError,           # Invalid domain type specified
    360: RuleViolation,             # Nameservers in different subnets required
    361: RuleViolation,             # Owner or administrative contact not German
    362: RuleViolation,             # Domain is already registered with us
    363: RuleViolation,             # Domain is not registered with us
    364: RuleViolation,             # Owner handle must differ from the current one
    365: RuleViolation,             # This domain belongs to other reseller.
    366: BadStateException,         # This action is prohibitted for current status
    367: BadStateException,         # Domain cannot be locked because of its status
    368: ValidationError,           # This domain cannot be deleted because renewal date is too close.
    369: ValidationError,           # Transfer is prohibited by the current domain owner
    370: ValidationError,           # Empty application mode!
    371: ValidationError,           # application mode is out of the current date
    372: ValidationError,           # Invalid default billing handle!
    373: ValidationError,           # Invalid billing handle!
    374: ValidationError,           # Domain `additionalData` parameter is missing
    375: ValidationError,           # Domain `additionalData` parameter is invalid
    376: ValidationError,           # Restore operation is not allowed for this domain
    377: ValidationError,           # Wrong application mode
    378: ValidationError,           # Domain preregistration is closed for this TLD
    379: ValidationError,           # You are about to register the premium domain. If you accept this registration fee, re-send the createDomainRequest and add the parameters acceptPremiumFee with value 1 .
    380: ValidationError,           # Need first name to register an .it domain
    381: ValidationError,           # Need state to register an .it domain
    382: ValidationError,           # Need fiscal number to register an .it domain
    383: ValidationError,           # Need birthdate to register an .it domain
    384: ValidationError,           # Need birthcity to register an .it domain
    385: ValidationError,           # Need vatnumber to register an .it domain
    386: ValidationError,           # Need Chambre of Commerce number
    387: ValidationError,           # Need Chambre of Commerce region
    388: ValidationError,           # Need Chambre of Commerce date
    389: RuleViolation,             # Owner should match the administrative contact
    390: RuleViolation,             # The entered owner does not match the whois
    391: RuleViolation,             # The entered owner does match the whois
    392: NoSuchElement,             # The form could not be found
    393: InProgress,                # The authorisation code was sent to the owner
    394: ServerError,               # The authorisation code could not be sent
    395: ValidationError,           # Domain name is in Early Access Program state
    396: ValidationError,           # The extension is locked, try again after the General Availability opens
    397: ValidationError,           # Domain status transition is not allowed
    398: ValidationError,           # Invalid queue status set
    399: ServerError,               # An unknown domain error has occurred
    400: ValidationError,           # Empty name field!
    401: ValidationError,           # Invalid name!
    402: ValidationError,           # Empty e-mail address!
    403: ValidationError,           # Invalid e-mail address!
    404: ValidationError,           # Empty subject field!
    405: ValidationError,           # Empty question field!
    420: ValidationError,           # Name is mandatory
    421: ValidationError,           # Name is invalid
    422: ValidationError,           # E-mail is mandatory
    423: ValidationError,           # E-mail is invalid
    424: ValidationError,           # Sender is mandatory
    425: ValidationError,           # Sender is invalid
    500: RuleViolation,             # Domain is not registered with Openprovider
    501: ValidationError,           # The domainname is too short
    502: ServerError,               # An database error has occurred
    503: ServerError,               # Could not retreive whois information
    504: BadStateException,         # Application Pending
    505: RuleViolation,             # You can only register 1 .EU domain at a time
    506: ValidationError,           # Registration LEFT is invalid
    507: ValidationError,           # Richt on name is invalid
    508: ValidationError,           # Supplier of documentary evidence is invalid
    509: ValidationError,           # Prior LEFT country is invalid
    510: ValidationError,           # Document language is invalid
    511: ValidationError,           # 3rd party emailaddress in invalid
    512: BadStateException,         # Domain is blocked
    513: BadStateException,         # Domain is reserved
    514: BadStateException,         # The domain is already being transferred
    515: ValidationError,           # Invalid status for domain
    516: ServerError,               # Unknown whois for extension
    600: ServerError,               # DRS has sent wrong operation type
    601: ServerError,               # DRS callback message has already been processed
    602: ServerError,               # DRS callback notification was NOT sent to the customer
    800: NoSuchElement,             # Unknown DNS zone
    801: ValidationError,           # Invalid domain name
    802: ValidationError,           # Invalid extension
    803: ValidationError,           # Invalid record type
    804: ValidationError,           # Invalid IPv4 IP address
    805: UniqueViolation,           # A zone already exists for this domain
    806: ValidationError,           # You did not enter all data
    807: RuleViolation,             # A slave zone can only contain 1 master ip
    808: ValidationError,           # Invalid record type
    810: RuleViolation,             # Record can not be deleted
    811: RuleViolation,             # SOA record can not be deleted
    812: ValidationError,           # Name of record not entered
    813: ValidationError,           # Type of record not entered
    814: ValidationError,           # Value of record not entered
    815: ValidationError,           # Invalid value for TTL (numerical, min 600)
    816: ValidationError,           # Invalid value for priority
    817: UniqueViolation,           # Duplicate record
    820: ValidationError,           # Invalid A record
    821: ValidationError,           # Invalid CNAME record
    822: ValidationError,           # Invalid MX record
    823: ValidationError,           # Invalid NS record
    824: ValidationError,           # Invalid SOA record
    825: ValidationError,           # Invalid PTR record
    826: ValidationError,           # Invalid AAAA record
    827: ValidationError,           # Invalid TXT record
    828: ValidationError,           # Invalid SPF record
    829: ValidationError,           # Invalid record name
    830: RuleViolation,             # PTR record is not equal to the A record
    832: ValidationError,           # Invalid SRV-record
    833: ValidationError,           # Invalid SRV-weight
    834: ValidationError,           # Invalid SRV-port
    835: ValidationError,           # Invalid SRV-address
    850: ValidationError,           # You did not choose a valid zone type
    851: ValidationError,           # You did not yet define your mail servers
    852: ValidationError,           # Enter at least 1 mail server
    853: ValidationError,           # Invalid value for mail server
    854: ValidationError,           # Enter both subdomain and where to point to
    855: ValidationError,           # Invalid value for the subdomain
    856: ValidationError,           # Invalid value for the subdomain
    857: ValidationError,           # You entered duplicate subdomains
    858: ValidationError,           # You entered duplicate mail servers
    860: ServerError,               # DNS zone could not be added
    870: ValidationError,           # Invalid name for the template
    871: BadRequest,                # Wrong orderBy field.
    872: NoSuchElement,             # Zone specified is not found.
    873: NoSuchElement,             # Template specified is not found.
    874: ValidationError,           # Template ID is empty.
    875: RuleViolation,             # Not enough nameservers given
    876: RuleViolation,             # It is not possible to use MX records that point to an IP address in the range 79.99.129.0/24.
    890: RuleViolation,             # Incorrect DNSSEC record format.
    891: RuleViolation,             # DNSSEC is not supported for this extension
    892: RuleViolation,             # Protocol field of the dnskey record must be 3
    893: RuleViolation,             # Algorithm field has wrong value
    894: RuleViolation,             # Digest type field has wrong value
    895: RuleViolation,             # DNSSEC keys and digests should be BASE64 encoded
    896: RuleViolation,             # DNSSEC processing error
    900: AuthenticationError,       # Login failed
    901: AuthenticationError,       # Empty username field!
    902: AuthenticationError,       # Empty password field!
    910: BadRequest,                # The form you sent was not recognized
    911: BadRequest,                # The version of the command sent is not valid
    912: ServerError,               # Error occured with IMAP connection
    920: InsufficientFunds,         # Your account balance is insufficient
    921: ValidationError,           # Invalid characters in amount!
    922: ValidationError,           # The amount is too small!
    923: LimitReached,              # Credit card payments limited to € 1000,00
    924: ValidationError,           # Invalid currency.
    925: ValidationError,           # Invalid invoice
    926: ValidationError,           # Empty invoice number
    950: ValidationError,           # Payment ID is invalid
    951: ValidationError,           # Confirmation code is invalid
    952: RuleViolation,             # The confirmation checkbox is not checked
    953: NoSuchElement,             # The payment could not be found
    954: UniqueViolation,           # The payment is already confirmed
    955: ValidationError,           # Amount is empty
    956: ValidationError,           # Payment method is empty
    999: ServerError,               # An unknown error occurred
    1000: ValidationError,          # Empty field for the type SSL cerificate!
    1001: ValidationError,          # Empty field for the number of servers
    1002: ValidationError,          # Empty field for the years
    1003: ValidationError,          # Empty field for the CSR!
    1004: ValidationError,          # Empty field for the server
    1005: ValidationError,          # Empty field for the address
    1006: ValidationError,          # Invalid field for the address
    1007: ValidationError,          # Empty field for the zipcode
    1008: ValidationError,          # Invalid field for the zipcode
    1009: ValidationError,          # Empty field for the city
    1010: ValidationError,          # Invalid field for the city
    1011: ValidationError,          # Empty field for the state
    1012: ValidationError,          # Invalid field for the state
    1013: ServerError,              # An unexpected error occured!
    1015: ValidationError,          # Invalid country for the ssl certificate
    1016: ValidationError,          # Invalid company name for the ssl certificate
    1017: ValidationError,          # Invalid phone for the ssl certificate
    1020: ValidationError,          # Invalid product
    1021: ValidationError,          # Invalid period
    1022: ValidationError,          # Selected no or invalid webserver software
    1023: ValidationError,          # Entered invalid subdomain in the hostnames
    1024: ValidationError,          # Invalid alternative names
    1025: RuleViolation,            # Alt Names are not supported by this product
    1026: ValidationError,          # Invalid wildcard format
    1027: RuleViolation,            # Wildcards are not supported by this product
    1028: RuleViolation,            # CSR Common Name MUST contain ONE wildcard
    1029: RuleViolation,            # Subject Alternative Names MUST be present
    1030: ValidationError,          # Invalid CSR
    1031: ValidationError,          # Found no or invalid common name (CN) in CSR
    1032: RuleViolation,            # This product can not have additional features
    1033: LimitReached,             # Limit of alternative domain names exceeded
    1034: RuleViolation,            # Chosen features set is not supported
    1035: RuleViolation,            # Multiple features are not allowed
    1040: ValidationError,          # Selected no handle
    1041: ValidationError,          # Selected invalid handle
    1045: ValidationError,          # Invalid e-mail address for approver
    1046: RuleViolation,            # E-mail address for approver is not allowed
    1047: ServerError,              # Cannot retrieve valid emails for Intranet Server Name
    1048: RuleViolation,            # Invalid signature algorithm
    1083: BadStateException,        # Certificate reissue from incomplete order
    1084: RuleViolation,            # Order does not belong to this reselleraccount
    1085: BadRequest,               # SSL plugin does not support this method
    1086: ServerError,              # An unknown error occurred when processing
    1087: InProgress,               # Order is being processed by CA
    1088: BadStateException,        # SSL certificate request has been rejected
    1089: BadStateException,        # SSL certificate has been revoked
    1090: ValidationError,          # Revocation reason can not be empty
    1091: AuthenticationError,      # Payment required for the successful order
    1092: BadStateException,        # Product is currently disabled
    1093: ValidationError,          # Empty order id
    1094: ValidationError,          # Invalid order id
    1095: ValidationError,          # Invalid order status
    1096: ValidationError,          # Invalid product's category
    1097: ValidationError,          # Empty product ID.
    1098: ValidationError,          # Invalid product ID.
    1099: ServerError,              # An unknown error occurred
    1100: ValidationError,          # Valid customer name required
    1101: ValidationError,          # Valid company name required
    1102: ValidationError,          # Valid domain name required
    1103: ValidationError,          # Valid e-mail address required
    1105: ValidationError,          # Logo required
    1106: ValidationError,          # Invalid logo file type: should be gif or jpg
    1107: ValidationError,          # Invalid logo dimensions: 600px by 280px max
    1108: ValidationError,          # Invalid product id(s)
    1109: ValidationError,          # Empty product id(s)
    1110: ValidationError,          # Tutorial ID is empty
    1111: ValidationError,          # Tutorial ID is invalid
    1112: ValidationError,          # Tutorial Order ID is empty
    1113: ValidationError,          # Tutorial Order ID is invalid
    1201: ValidationError,          # Bad CMN-object type
    1202: ValidationError,          # CMN-object ID is invalid or empty
    1203: ValidationError,          # CMN-object cannot be found
    1204: ValidationError,          # Operation is not supported by the object
    1800: ValidationError,          # TLD does not exist in Openprovider
    1901: ValidationError,          # Fiscal number [owner] is required
    1902: ValidationError,          # A VAT number of the owner is required
    1903: ValidationError,          # A company registration number is required
    1910: RuleViolation,            # Admin and owner for an .ES must be the same.
    1920: RuleViolation,            # A company needs a valid SIREN/SIRET number
    1921: ValidationError,          # No birth date has been entered
    1922: ValidationError,          # Birth date is not formatted as dd-mm-yyyy
    1923: ValidationError,          # No birth place has been entered
    1924: RuleViolation,            # Owner and administrative contact arent French
    1925: ValidationError,          # No passport number has been entered
    1926: ValidationError,          # Please check customer's details.
    2001: ServerError,              # Uploading the file failed.
    2002: ValidationError,          # The filetype is not supported.
    2003: ServerError,              # An error has occurred while processing file
    3001: ValidationError,          # Title is required parameter
    3002: ServerError,              # License cannot be created. Try again later
    3003: RuleViolation,            # You have not changed any option.
    3004: ServerError,              # License cannot be upgraded
    3005: ServiceUnavailable,       # Cannot connect to the server
    3006: ServiceUnavailable,       # Service temporarily unavailable
    3007: NoSuchElement,            # No license product exists for given ID.
    3008: ValidationError,          # Empty license product ID.
    3009: ValidationError,          # Wrong orderBy field.
    3010: ValidationError,          # License ID is empty.
    3011: NoSuchElement,            # No license found for given ID.
    3012: ValidationError,          # License's title is empty.
    3013: ValidationError,          # Invalid 'domains' specified.
    3014: ValidationError,          # Ivalid 'langPacks' specified.
    3015: ValidationError,          # Invalid 'features' specified.
    3016: ValidationError,          # Invalid 'keyType' specified.
    3017: ValidationError,          # keyType' is empty.
    3018: ValidationError,          # period' is invalid.
    3019: ValidationError,          # options' parameter is empty.
    3020: ValidationError,          # options' parameter is invalid.
    3021: NoSuchElement,            # A license with such an ID does not exist.
    3022: ValidationError,          # Cannot create a license. Check Zipcode.
    3023: ValidationError,          # Cannot create a license. Check State.
    3024: ValidationError,          # os is invalid
    3025: ValidationError,          # version is invalid
    3026: ValidationError,          # Operation is not supported for this license.
    3027: ValidationError,          # Invalid virtualization specified
    3028: ValidationError,          # Invalid type specified
    3029: ValidationError,          # Invalid pack specified
    3999: ValidationError,          # Unknown error.
    4001: BadRequest,               # Wrong command name.
    4002: AuthenticationError,      # Access denied.
    4003: AuthenticationError,      # Command's parameter(s) access violation.
    4004: ServerError,              # Bad reply
    4005: Maintenance,              # Disabled for maintenance
    4006: BadRequest,               # Wrong message format
    5001: ValidationError,          # Empty active flag.
    5002: ValidationError,          # Invalid contact ID.
    5003: ValidationError,          # Empty contact ID.
    5004: RuleViolation,            # Cannot remove last admin contact.
    5005: RuleViolation,            # Contact cannot remove himself.
    5006: ValidationError,          # Bad password specified.
    5007: ValidationError,          # Passwords are not equal.
    5008: ValidationError,          # Bad IP list value.
    6001: ValidationError,          # AdditionalData: Invalid birth city.
    6002: ValidationError,          # AdditionalData: Invalid birth address.
    6003: ValidationError,          # AdditionalData: Empty birth country.
    6004: ValidationError,          # AdditionalData: Invalid birth country.
    6005: ValidationError,          # AdditionalData: Invalid birth date.
    6006: ValidationError,          # AdditionalData: Invalid birth state.
    6007: ValidationError,          # AdditionalData: Invalid birth zipcode
    6008: ValidationError,          # AdditionalData: Invalid headquarters address
    6009: ValidationError,          # AdditionalData: Invalid headquarters city
    6010: ValidationError,          # AdditionalData: Empty headquarters country
    6011: ValidationError,          # AdditionalData: Invalid headquarters country
    6012: ValidationError,          # AdditionalData: Invalid headquarters state
    6013: ValidationError,          # AdditionalData: Invalid headquarters zipcode
    6014: ValidationError,          # AdditionalData: Invalid socialsecurity number
    6015: ValidationError,          # AdditionalData: Invalid city.
    6016: ValidationError,          # AdditionalData: Invalid number.
    6017: ValidationError,          # AdditionalData: Invalid subscription date.
    6200: RuleViolation,            # Cannot delete a customer that has domain(s).
    6206: ValidationError,          # Cannot delete a customer that assigned as default handle(s).
    7000: ValidationError,          # Question ID is empty
    7001: ValidationError,          # Question ID is invalid
    7002: ValidationError,          # Category ID is empty
    7003: ValidationError,          # Category ID is invalid
    8000: ValidationError,          # Reseller ID is invalid
    8001: ValidationError,          # Reseller ID is empty
    8002: ServerError,              # Reseller cannot be created
    8003: ValidationError,          # Reseller status is invalid
    9000: ValidationError,          # Contract ID is invalid
    9001: ValidationError,          # Contract ID is empty
    9002: ValidationError,          # IP Address is invalid
    9003: ValidationError,          # IP Address is empty
    10001: ValidationError,         # Invalid email specified.
    10002: ValidationError,         # Invalid username specified.
    10003: ValidationError,         # No email nor username are specified.
    10004: ValidationError,         # Invalid password specified.
    10005: ValidationError,         # Access denied.
    11001: ValidationError,         # Reseller has no active subscription
    11010: ValidationError,         # Your request contains an invalid domain
    11011: LimitReached,            # SE subscription limit is exceeded
    11013: ValidationError,         # IP is invalid.
    11014: LimitReached,            # Domain IP users limit is exceeded.
    11015: ValidationError,         # This domain IP user does not exist
    11016: ValidationError,         # This domain IP user exists already
    11017: ValidationError,         # Cannot delete domain with bound IP users
    11101: ValidationError,         # Invalid options specified
    11102: ValidationError,         # You selected current options for upgrade
    11999: ServerError,             # An unknown error has occurred.
    13000: ValidationError,         # Incorrect PromoCode
    14000: ValidationError,         # TmchMark ID is invalid
    14001: ValidationError,         # Owner type is invalid
    14002: ValidationError,         # Period is invalid
    14003: ValidationError,         # Service type is invalid
    14004: ValidationError,         # Notification frequency is invalid
    14005: ValidationError,         # Gsc class is invalid
    14006: ValidationError,         # Jurisdiction is invalid
    14100: ValidationError,         # Document ID is invalid
    14101: ValidationError,         # Document mime-type is invalid
    14102: ValidationError,         # Document size is invalid
    14200: ValidationError,         # Smd is not base64 format
    14201: ValidationError,         # Smd is into revocation file
    14202: ValidationError,         # Smd file is wrong
    14299: ValidationError,         # Smd revocation file is inaccessible
    14500: ServiceUnavailable,      # Error when connecting to TMCH
    14999: ValidationError,         # An unknown error has occurred
    15000: ValidationError,         # This type of reseller has not enough rights for this operation
    16000: ValidationError,         # Extensions are required to create promocode
    16001: ValidationError,         # Extensions are incorrect
    16002: ValidationError,         # Reseller cannot use this flatfee
    16003: ValidationError,         # Id of flatfee is incorrect
    16004: ValidationError,         # Flatfee product type required
    16005: ValidationError,         # Flatfee product type incorrect
    16006: ValidationError,         # Autorenew option value incorrect
    16007: ValidationError,         # Flatfee status incorrect
    17000: ValidationError,         # DocuSign document ID is invalid
    17001: ValidationError,         # You must sign a contract
    17002: ValidationError,         # Was timed out, please try again
    17003: ValidationError,         # Fax pending
    17100: ServiceUnavailable,      # DocuSign server is unavailable, please try again in a few minutes
    19000: ValidationError,         # Domain name is premium. Please contact support to purchase.
    19001: ServerError,             # Can not create domain.
    19002: ValidationError,         # Domain is premium, but price has not yet been published by registry
    19003: ValidationError,         # Locking is not possible for domains with `Whois Privacy Protection` option enabled
    19004: ValidationError,         # Transfer cannot be started. Requested domain is still in AGP (Addition grace period)
    19005: ValidationError,         # Invalid fee amount for `Early Access Program` period
    19006: ValidationError,         # Domain can not be anonymized as this TLD does not yet support whois privacy
    19007: ValidationError,         # Domain can not be anonymized as this TLD does not yet support whois privacy for legal persons
    20000: ValidationError,         # This email address has been verified already
    20001: InProgress,              # Verification email in progress
    20002: ValidationError,         # Required argument is missed
}


def from_code(code):
    """
    Return the specific exception class for the given code, or
    OpenproviderError if no specific exception class is available.

    @param code: The error code from Openprovider.
    """
    if code in MAPPING:
        return MAPPING[code]
    else:
        return OpenproviderError
