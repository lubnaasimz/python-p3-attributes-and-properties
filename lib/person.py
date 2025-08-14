APPROVED_JOBS = [ 
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="Polly", job="Legal"):
        self._name = "Polly"  # Default name
        self._job = "Legal"   # Default job
        self.name = name      # Validate through property
        self.job = job        # Validate through property

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name.title()  # Convert to title case
        else:
            print("Name must be string between 1 and 25 characters.")
            self._name = "Polly"  
    def get_job(self):
        return self._job
    
    def set_job(self, job):
        if job in APPROVED_JOBS:
            self._job = job
        else:
            print("Job must be in list of approved jobs.")
            self._job = "Legal" 
    
    name = property(get_name, set_name)
    job = property(get_job, set_job) 