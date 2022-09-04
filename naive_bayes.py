class NaiveBayes: 
    def __init__(self, classified_data):
        self.data = classified_data
        self.classes = [i for i in self.data.keys()]
        self.scam = self.data[self.classes[0]]
        self.error = self.data[self.classes[1]]
        self.link = self.data[self.classes[2]]
        self.yes_scam = 4
        self.no_scam = 6
        self.total = 10
    
    def error_counts(self, error_input, scam_input):

        count = 0
        for i in range(len(self.scam)): 
            if self.error[i] == error_input and self.scam[i] == scam_input:
                count += 1 
        return count
    
    def link_counts(self, link_input, scam_input):
        count = 0
        for i in range(len(self.scam)): 
            if self.link[i] == link_input and self.scam[i] == scam_input:
                count += 1 
        return count
    
    def classify(self, unclassified_data): 
        scam = []
        data_error = unclassified_data['Error']
        data_link = unclassified_data['Link']

        for i in range(len(data_error)):

            error = data_error[i]
            link = data_link[i]

            yes_scam = (self.yes_scam / self.total) * ((self.error_counts(error, 'Yes')) / self.yes_scam) * (self.link_counts(link, 'Yes') / self.yes_scam)
            no_scam = (self.no_scam / self.total) * ((self.error_counts(error, 'No')) / self.no_scam) * (self.link_counts(link, 'No') / self.no_scam)
            prediction = max(yes_scam, no_scam)
            if prediction == yes_scam: 
                scam.append('Yes')
            else: 
                scam.append('No')
        return scam



        

data = {'Scam': ['No', 'Yes', 'Yes', 'No', 'No', 'Yes', 'No', 'No', 'Yes', 'No'], 'Errors': ['No', 'Yes', 'Yes', 'No', 'No', 'Yes','Yes','No','Yes','No'], 'Links':['No', 'Yes', 'Yes','No', 'Yes','Yes','No','Yes', 'No','Yes']}
un_data = {'Error': ['No', 'Yes', 'Yes', 'No'], 'Link' : ['No', 'Yes', 'No','Yes']}
n = NaiveBayes(data)
meep = n.classify(un_data)
print(meep)