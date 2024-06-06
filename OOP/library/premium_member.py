from .member import Member

class PremiumMember(Member):
    def __init__(self, name, member_id, membership_level):
        super().__init__(name, member_id)
        self.__membership_level = membership_level

    def __str__(self):
        return f"{super().__str__()}, Membership Level: {self.__membership_level}"
