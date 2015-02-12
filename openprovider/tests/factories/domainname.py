import uuid

def domainname(sld=None, tld='nl'):
    """Generate a psuedorandom domain name."""
    if sld is None:
        sld = uuid.uuid4()
    return 'ci-%s.%s' % (sld, tld)
