"""Classes for melon orders."""


class DomesticMelonOrder():
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = "domestic"
        self.tax = 0.08

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class InternationalMelonOrder():
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.country_code = country_code
        self.shipped = False
        self.order_type = "international"
        self.tax = 0.17

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class AbstractMelonOrder():

    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty):
        self.species = species
        self.qty = qty
        self.shipped = False

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    
    

class DomesticMelonOrder_New(AbstractMelonOrder):
    tax = .08
    order_type = "domestic"
    """A melon order within the USA."""

class InternationalMelonOrder_New(AbstractMelonOrder):
    tax =.17
    order_type = "international"
    def __init__(self,species,qty,country_code):
        super().__init__(species,qty)
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


    """An international (non-US) melon order."""
    

order1 = InternationalMelonOrder_New('watermelon', 6, 'USA')
order2 = DomesticMelonOrder_New('oranges',12)
order1.mark_shipped()
print(order2.get_total())

print(order1.tax)
print(order2.order_type)
print(order1.shipped)
print(order1.get_country_code())