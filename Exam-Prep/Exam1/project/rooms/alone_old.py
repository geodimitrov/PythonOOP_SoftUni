from rooms.room import Room

class AloneOld(Room):
    MEMBERS = 1

    def __init__(self, family_name, pension):
        super().__init__(family_name, pension, AloneOld.MEMBERS)
        self.room_cost = 10

    def __repr__(self):
        return f"{self.family_name} with {self.members_count} members. Budget: {self.budget:.2f}$, Expenses: {self.expenses * 30:.2f}$\n" \
            + f"--- Appliances monthly cost: {self.expenses * 30:.2f}$\n"