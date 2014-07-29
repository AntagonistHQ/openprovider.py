# coding=utf-8

from openprovider.modules import E, OE, common
from openprovider.models import Model


def _nameservers(nameservers):
    items = [E.item(E.name(ns.name), OE('ip', ns.ip), OE('ip6', ns.ip6)) for ns in nameservers]
    return E.array(*items)


def _dnssec_keys(keys):
    items = [E.item(E.flags(key.flags), E.alg(key.alg), E.pubKey(key.pubkey)) for key in keys]
    return E.array(*items)


def _domain(domain):
    sld, tld = domain.split('.', 1)

    return E.domain(
        E.name(sld),
        E.extension(tld),
    )


class DomainModule(common.Module):
    """Bindings to API methods in the domain module."""

    def check(self, domain):
        """
        Check availability for a single domain. Returns the domain's status as
        a string (either "active" or "free").
        """
        response = self.request(self._check_cmd([domain]))
        return response.data.array[0].item[0].status

    def check_many(self, domains):
        """
        Check availability for a number of domains. Returns a dictionary
        mapping the domain names to their statuses as a string
        ("active"/"free").
        """
        response = self.request(self._check_cmd(domains))
        items = response.data.array[0].item
        return dict((i.domain, i.status) for i in items)

    def _check_cmd(self, domains):
        return E.checkDomainRequest(
            E.domains(
                E.array(
                    *[E.item(
                        E.name(domain.split(".")[0]),
                        E.extension(domain.split(".")[1])
                    ) for domain in domains]
                )
            )
        )

    def create_domain_request(self, domain, period, owner_handle, admin_handle, tech_handle,
            billing_handle=None, reseller_handle=None, ns_group=None, ns_template_name=None,
            name_servers=None, use_domicile=False, promo_code=None, autorenew=None, comments=None,
            dnssec_keys=None, application_mode=None):

        request = E.createDomainRequest(
                _domain(domain),
                E.period(period),
                E.ownerHandle(owner_handle),
                E.adminHandle(admin_handle),
                E.techHandle(tech_handle),
                OE('billingHandle', billing_handle),
                OE('resellerHandle', reseller_handle),
                OE('nsGroup', ns_group),
                OE('nsTemplateName', ns_template_name),
                OE('nameServers', name_servers, transform=_nameservers),
                OE('useDomicile', use_domicile, transform=int),
                OE('promoCode', promo_code),
                OE('autorenew', autorenew),
                OE('comments', comments),
                OE('dnssecKeys', dnssec_keys, transform=_dnssec_keys),
                OE('applicationMode', application_mode),
        )
        response = self.request(request)
        return response.as_model(Model)

    def delete_domain_request(self, domain, request_type='delete'):
        self.request(E.deleteDomainRequest(_domain(domain), E('type', request_type)))

    def modify_domain_request(self, domain, owner_handle=None, admin_handle=None, tech_handle=None,
            billing_handle=None, reseller_handle=None, ns_group=None, ns_template_name=None,
            name_servers=None, use_domicile=False, promo_code=None, autorenew=None, comments=None,
            dnssec_keys=None, application_mode=None):

        request = E.modifyDomainRequest(
                _domain(domain),
                OE('ownerHandle', owner_handle),
                OE('adminHandle', admin_handle),
                OE('techHandle', tech_handle),
                OE('billingHandle', billing_handle),
                OE('resellerHandle', reseller_handle),
                OE('nsGroup', ns_group),
                OE('nsTemplateName', ns_template_name),
                OE('nameServers', name_servers, transform=_nameservers),
                OE('useDomicile', use_domicile, transform=int),
                OE('promoCode', promo_code),
                OE('autorenew', autorenew),
                OE('comments', comments),
                OE('dnssecKeys', dnssec_keys, transform=_dnssec_keys),
                OE('applicationMode', application_mode),
        )
        self.request(request)

    def retrieve_domain_request(self, domain, additional_data=False, registry_details=False):
        request = E.retrieveDomainRequest(_domain(domain))
        response = self.request(request)
        return response.as_model(Model)
