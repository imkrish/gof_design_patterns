from abc import ABCMeta, abstractmethod


class Site(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, units, rate):
        self.__tax_rate = 0.125
        self.__units = units
        self.__rate = rate

    # Template Method
    def get_billable_amount(self):
        return self.get_base() + self.get_tax() - self.get_discount()

    def get_base(self):
        return self.__units * self.__rate

    def get_tax(self):
        return self.get_base() * self.__tax_rate

    @abstractmethod
    def get_discount(self):
        raise NotImplementedError()


class ResidentialSite(Site):

    def __init__(self):
        super().__init__(3, 100)

    def get_discount(self):
        return 0


class BusinessSite(Site):

    def __init__(self):
        super().__init__(5, 200)

    def get_base(self):
        return super().get_base() * 0.5

    def get_tax(self):
        return super().get_tax() * 0.2

    def get_discount(self):
        return self.get_base() * 0.1

if __name__ == "__main__":
    resSite = ResidentialSite()
    print("\nResidential Amount: " + str(resSite.get_billable_amount()))

    busSite = BusinessSite()
    print("\nBusiness Amount: " + str(busSite.get_billable_amount()))
