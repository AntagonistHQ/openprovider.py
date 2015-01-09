from openprovider.models import Nameserver

def nameservers():
    """Return the name servers for example.com."""
    return [
        Nameserver(name='a.iana-servers.net', ip='199.43.132.53', ip6='2001:500:8c::53'),
        Nameserver(name='b.iana-servers.net', ip='199.43.133.53', ip6='2001:500:8d::53'),
    ]
