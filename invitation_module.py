import csv


class Invitation:
    def __init__(self, city, country, x_coordinate, y_coordinate, reimbursement):
        self.city = city
        self.country = country
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.reimbursement = reimbursement
    
    def generate_invitation(self):
        invitation_text = f"""
Dear employee of office {self.city}, {self.country}
the winter party is near, it will be celebrated at location {self.x_coordinate},{self.y_coordinate}
you will get reimbursed {self.reimbursement} DKK for the travelled distance to the party!
        """
        return invitation_text.strip()

def read_csv_and_generate_invivations(filename):
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            invitation =Invitation(
                city = row['A'],
                country = row['B'],
                x_coordinate = row['C'],
                y_coordinate = row['D'],
                reimbursement = row['E']
            )
            invitation_text = invitation.generate_invitation()
            office_code = row['A'].replace(",", "")
            with open(f'invitation_{office_code}.txt', 'w') as invitation_file:
                invitation_file.write(invitation_text)
                print(f"Invitation for office {office_code} has been written to invitation_{office_code}.txt")
