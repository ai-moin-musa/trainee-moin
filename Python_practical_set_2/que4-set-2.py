# Data Structure
company = {
    "Project Managers": {
        "Robert Downey": {
            "team_leads": ["Mark", "Samuel", "Paul", "Tom"]
        },
        "Anne Hathaway": {
            "team_leads": ["Chris", "Pratt", "Emma", "Will", "Smith"]
        }
    },
    "Team Leads": {
        "Mark": {"experience": 8, "junior_developers": ["Leonardo", "Alexandra"]},
        "Samuel": {"experience": 8},
        "Paul": {"experience": 8, "senior_developer": ["Fergal"]},
        "Tom": {"experience": 8, "junior_developers": ["Jerry", "John"]},
        "Chris": {
            "experience": 5,
            "team_members": ["James"],
        },
        "Pratt": {"experience": 5},
        "Emma": {"experience": 5},
        "Will": {
            "experience": 5,
            "senior_developers": ["Edge", "Ryan"],
        },
        "Smith": {
            "experience": 5,
            "senior_developers": ["Walker", "Diana"],
        }
    },
    "Senior Developers": {
        "James": {
            "experience": 3,
            "manager": "Chris",
            "team_members": ["Jennifer", "Scott", "Sophie"]
        },
        "Fergal": {"experience": 4.5, "mentor": "Paul"},
        "Edge": {"experience": 3, "manager": "Will"},
        "Ryan": {"experience": 3.5, "manager": "Will"},
        "Walker": {"experience": 2.7, "manager": "Smith"},
        "Diana": {"experience": 2.7, "manager": "Smith"}
    },
    "Junior Developers": {
        "Jerry": {"experience": 1.5, "mentor": "Tom"},
        "John": {"experience": 1.6, "mentor": "Tom"},
        "Leonardo": {"experience": 1, "mentor": "Mark"},
        "Alexandra": {"experience": 1, "mentor": "Mark"}
    }
}

# Methods
def display_employees_by_manager(company, manager_name):
    if "Project Managers" in company and manager_name in company["Project Managers"]:
        employees = []
        team_leads = company["Project Managers"][manager_name].get("team_leads", [])
        for tl in team_leads:
            if tl in company["Team Leads"]:
                employees.append(tl)
                employees.extend(company["Team Leads"][tl].get("junior_developers", []))
                employees.extend(company["Team Leads"][tl].get("senior_developers", []))
        return employees
    return f"No Project Manager named {manager_name} found."


def display_employees_with_experience(company, years):
    employees = []
    for role, group in company.items():
        for name, details in group.items():
            if details.get("experience", 0) > years:
                employees.append(name)
    return employees


def update_experience(company):
    for role, group in company.items():
        for name, details in group.items():
            if 3.5 < details.get("experience", 0) < 4.5:
                details["experience"] = 4.6


def display_tl_with_experience(company):
    tls = {}
    for name, details in company.get("Team Leads", {}).items():
    	if details.get("experience") == 0:
    	      tls[name] = "N/A"
    	else:
              tls[name] = details.get("experience", "N/A")
    return tls


def reassign_team(company, leaving_tl, new_manager):
    if leaving_tl in company["Team Leads"]:
        team_members = company["Team Leads"].pop(leaving_tl).get("senior_developers", [])
        for member in team_members:
            company["Senior Developers"][member]["manager"] = new_manager
    


def has_employee_with_experience_less_than(company, years):
    for role, group in company.items():
        for name, details in group.items():
            if details.get("experience", float("inf")) < years:
                return True
    return False


def promote_to_tl(company, employee_name):
    if employee_name not in company["Team Leads"] and employee_name in company.get("Senior Developers", {}):
        details = company["Senior Developers"].pop(employee_name)
        company["Team Leads"][employee_name] = {
            "experience": details.get("experience", "N/A"),
            "senior_developers": []
        }
    print(company["Team Leads"])
        

# Example Usage
print("Employees under Robert Downey:", display_employees_by_manager(company, "Robert Downey"))
print("\n\n")
print("Employees with experience > 4 years:", display_employees_with_experience(company, 4))
print("\n\n")
update_experience(company)
print("Updated experience:", company)
print("\n\n")
print("Team Leads with experience:", display_tl_with_experience(company))
print("\n\n")
reassign_team(company, "Smith", "Ryan")
print("After reassigning Smith's team to Ryan:", company)
print("\n\n")
print("Any employee with < 2 years of experience:", has_employee_with_experience_less_than(company, 2))
print("\n\n")
print("After promoting Edge to TL:")
promote_to_tl(company, "Edge")
print("\n\n")
