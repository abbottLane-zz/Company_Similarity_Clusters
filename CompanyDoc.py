class CompanyDoc:
    def __init__(self, name, description, keywords):
        self.name = name
        self.description = description
        self.keywords = keywords

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_keywords(self):
        return self.keywords
