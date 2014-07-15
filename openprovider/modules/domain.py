# coding=utf-8

from openprovider.modules import common


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
        return dict([(i.domain, i.status) for i in items])

    def _check_cmd(self, domains):
        e = self.e
        return e.checkDomainRequest(
            e.domains(
                e.array(
                    *[e.item(
                        e.name(domain.split(".")[0]),
                        e.extension(domain.split(".")[1])
                    ) for domain in domains]
                )
            )
        )
