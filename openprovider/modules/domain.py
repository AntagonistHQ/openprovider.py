# coding=utf-8

from openprovider.modules import common


class DomainModule(common.Module):
    def check(self, domain):
        """
        Check availability for a single domain. Returns the domain's status
        as a string (either "active" or "free").
        """
        e = self.e
        (name, extension) = domain.split(".")

        response = self.request(
            e.checkDomainRequest(
                e.domains(
                    e.array(
                        e.item(
                            e.name(name),
                            e.extension(extension))))))

        return response.data.array[0].item[0].status
