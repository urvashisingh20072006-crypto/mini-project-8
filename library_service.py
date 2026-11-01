from datetime import date, timedelta


class LibraryManager:

    library_name = "BBDIT Library"
    max_active_loans_default = 3

    def __init__(self):
        self.catalogue = {}
        self.members = {}
        self.loans = {}

    def register_item(self, item):

        if item.item_id in self.catalogue:
            print("Item ID already exists!")
            return

        self.catalogue[item.item_id] = item

        print("Item registered successfully!")

    def register_member(self, member):

        if member.member_id in self.members:
            print("Member ID already exists!")
            return

        self.members[member.member_id] = member

        print("Member registered successfully!")

    def borrow_item(self, member_id, item_id):

        if member_id not in self.members:
            print("Member not found!")
            return

        if item_id not in self.catalogue:
            print("Item not found!")
            return

        member = self.members[member_id]
        item = self.catalogue[item_id]

        if not item.available:
            print("Item is already borrowed!")
            return

        if item.loan_period_days() <= 0:
            print("This item cannot be borrowed!")
            return

        if member.borrowed_count >= member.borrowing_limit:
            print("Borrowing limit reached!")
            return

        issue_date = date.today()
        due_date = issue_date + timedelta(
            days=item.loan_period_days()
        )

        item.mark_borrowed()
        member.add_loan(item_id)

        self.loans[item_id] = {
            "member_id": member_id,
            "issue_date": issue_date.isoformat(),
            "due_date": due_date.isoformat(),
            "returned": False
        }

        print("Item borrowed successfully!")
        print("Issue Date:", issue_date)
        print("Due Date:", due_date)

    def return_item(self, item_id):

        if item_id not in self.loans:
            print("No loan record found!")
            return

        loan = self.loans[item_id]

        if loan["returned"]:
            print("Item already returned!")
            return

        member_id = loan["member_id"]
        member = self.members[member_id]

        return_date = date.today()
        due_date = date.fromisoformat(loan["due_date"])

        overdue_days = max(0, (return_date - due_date).days)

        fine = self.calculate_fine(overdue_days)

        self.catalogue[item_id].mark_returned()
        member.remove_loan(item_id)

        loan["returned"] = True
        loan["return_date"] = return_date.isoformat()
        loan["fine"] = fine

        print("Item returned successfully!")
        print("Overdue Days:", overdue_days)
        print("Fine: ₹", fine)


    def get_data(self):

        return {
        "items": [
            item.to_dict()
            for item in self.catalogue.values()
        ],

        "members": [
            member.to_dict()
            for member in self.members.values()
        ],

        "loans": [
            {
                "item_id": item_id,
                **loan
            }
            for item_id, loan in self.loans.items()
        ]
    }

    @staticmethod
    def calculate_fine(overdue_days):
        fine_per_day = 5
        return overdue_days * fine_per_day

    @classmethod
    def update_default_limit(cls, new_limit):
        cls.max_active_loans_default = new_limit

    