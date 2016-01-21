# coding=utf-8

from openprovider.modules import E, OE, common
from openprovider.models import Model, DomainDetails


def _additional_data(data):
    if not data:
        return None

    items = [E(key, value) for key, value in data.items()]
    return E.additionalData(*items)


def _nameservers(nameservers):
    items = [E.item(E.name(ns.name), OE('ip', ns.ip), OE('ip6', ns.ip6)) for ns in nameservers]
    return E.array(*items)


def _dnssec_keys(keys):
    items = [E.item(E.flags(key.flags), E.alg(key.alg), E.protocol(getattr(key, 'protocol', 3)), E.pubKey(key.pubkey)) for key in keys]
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
        return self.check_domain_request([domain])[0].status

    def check_many(self, domains):
        """
        Check availability for a number of domains. Returns a dictionary
        mapping the domain names to their statuses as a string
        ("active"/"free").
        """
        return dict((item.domain, item.status) for item in self.check_domain_request(domains))

    def check_domain_request(self, domains):
        """
        Return the availability of one or more domain names.

        The availability is a model containing a domain and a status. It can also have a premium
        attribute in case the domain has non-default costs.
        """
        request = E.checkDomainRequest(
            E.domains(
                E.array(
                    *[E.item(
                        E.name(domain.split(".")[0]),
                        E.extension(domain.split(".")[1])
                    ) for domain in domains]
                )
            )
        )

        response = self.request(request)
        return [Model(item) for item in response.data.array.item]

    def create_domain_request(self, domain, period, owner_handle, admin_handle, tech_handle,
            billing_handle=None, reseller_handle=None, ns_group=None, ns_template_name=None,
            name_servers=None, use_domicile=False, promo_code=None, autorenew=None, comments=None,
            dnssec_keys=None, application_mode=None, is_private_whois_enabled=None,
            additional_data=None):

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
                OE('isPrivateWhoisEnabled', is_private_whois_enabled, transform=int),
                _additional_data(additional_data),
        )
        response = self.request(request)
        return response.as_model(Model)

    def delete_domain_request(self, domain, request_type='delete'):
        self.request(E.deleteDomainRequest(_domain(domain), E('type', request_type)))

    def modify_domain_request(self, domain, owner_handle=None, admin_handle=None, tech_handle=None,
            billing_handle=None, reseller_handle=None, ns_group=None, ns_template_name=None,
            name_servers=None, use_domicile=False, promo_code=None, autorenew=None, comments=None,
            dnssec_keys=None, application_mode=None, is_private_whois_enabled=None,
            is_locked=None):

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
                OE('isPrivateWhoisEnabled', is_private_whois_enabled, transform=int),
                OE('isLocked', is_locked, transform=int),
        )
        response = self.request(request)
        return response.as_model(Model)

    def retrieve_domain_request(self, domain, additional_data=False, registry_details=False):
        request = E.retrieveDomainRequest(
                _domain(domain),
                E.withAdditionalData(int(additional_data)),
                E.withRegistryDetails(int(registry_details)),
        )
        response = self.request(request)
        return response.as_model(DomainDetails)

    def retrieve_price_domain_request(self, domain, operation=None):
        request = E.retrievePriceDomainRequest(
                _domain(domain),
                OE('operation', operation),
        )
        response = self.request(request)
        return response.as_model(Model)

    def transfer_domain_request(self, domain, period, auth_code, owner_handle, admin_handle,
            tech_handle, billing_handle=None, reseller_handle=None, ns_group=None,
            ns_template_name=None, name_servers=None, use_domicile=False, at=None, promo_code=None,
            dnssec_keys=None):

        request = E.transferDomainRequest(
                _domain(domain),
                E.period(period),
                OE('authCode', auth_code),
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
                OE('dnssecKeys', dnssec_keys, transform=_dnssec_keys),
        )
        response = self.request(request)
        return response.as_model(Model)

    def trade_domain_request(self, domain, period, owner_handle, admin_handle, tech_handle,
            billing_handle=None, reseller_handle=None, auth_code=None, ns_group=None,
            ns_template_name=None, name_servers=None, use_domicile=None, promo_code=None,
            dnssec_keys=None):

        request = E.tradeDomainRequest(
                _domain(domain),
                E.period(period),
                E.ownerHandle(owner_handle),
                E.adminHandle(admin_handle),
                E.techHandle(tech_handle),
                OE('billingHandle', billing_handle),
                OE('resellerHandle', reseller_handle),
                OE('authCode', auth_code),
                OE('nsGroup', ns_group),
                OE('nsTemplateName', ns_template_name),
                OE('nameServers', name_servers, transform=_nameservers),
                OE('useDomicile', use_domicile, transform=int),
                OE('promoCode', promo_code),
                OE('dnssecKeys', dnssec_keys, transform=_dnssec_keys),
        )
        response = self.request(request)
        return response.as_model(Model)

    def search_domain_request(self, limit=None, offset=None, extension=None,
            domain_name_pattern=None, contact_handle=None, ns_group_pattern=None, status=None,
            with_addition_data=None):

        request = E.searchDomainRequest(
                OE('limit', limit),
                OE('offset', offset),
                OE('extension', extension),
                OE('domainNamePattern', domain_name_pattern),
                OE('contactHandle', contact_handle),
                OE('nsGroupPattern', ns_group_pattern),
                OE('status', status),
                OE('withAdditionalData', with_addition_data),
        )
        response = self.request(request)
        return response.as_models(DomainDetails)

    def renew_domain_request(self, domain, period):
        request = E.renewDomainRequest(
                _domain(domain),
                E.period(period),
        )
        response = self.request(request)
        return response.as_model(Model)

    def request_auth_code_domain_request(self, domain, auth_code_type=None):
        request = E.requestAuthCodeDomainRequest(
                _domain(domain),
                OE('authCodeType', auth_code_type),
        )
        response = self.request(request)
        return response.as_model(Model)

    def reset_auth_code_domain_request(self, domain):
        request = E.resetAuthCodeDomainRequest(_domain(domain))
        response = self.request(request)
        return response.as_model(Model)

    def approve_transfer_domain_request(self, domain, approve, registrar_tag=None):
        request = E.approveTransferDomainRequest(
                _domain(domain),
                E.approve(int(approve)),
                OE('registrarTag', registrar_tag),
        )
        response = self.request(request)
        return response.as_model(Model)

    def restore_domain_request(self, domain):
        request = E.restoreDomainRequest(_domain(domain))
        response = self.request(request)
        return response.as_model(Model)

    def try_again_domain_request(self, domain):
        request = E.tryAgainDomainRequest(_domain(domain))
        response = self.request(request)
        return response.as_model(Model)
