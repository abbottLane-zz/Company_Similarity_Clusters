from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from Utilities import output_results, load_data


class CompanyRecommender:
    def __init__(self, data_dir, k):
        self.data_dir = data_dir
        self.k = k
        self.results = {}
        self.company_to_cluster = {}
        self.companies = []
        self.descriptions = []
        self.km = None
        self.vectorizer = None
        self.__initialize_clusters()

    def __initialize_clusters(self):
        # Load the data
        self.companies, self.descriptions = load_data(self.data_dir, has_header=True)

        # Vectorize the data using TF-IDF to help reduce dimensionality
        self.vectorizer = TfidfVectorizer(max_df=0.5, min_df=2, stop_words='english', use_idf=True, ngram_range=(1, 2))
        X = self.vectorizer.fit_transform(self.descriptions)
        print("n_samples: %d, n_features: %d" % X.shape)

        # Initialize K-means algorithm preferences
        self.km = KMeans(n_clusters=self.k, init='k-means++', max_iter=100, n_init=1, verbose=False)

        # Use k-means to generate clusters
        self.km.fit(X)

        # initialize results dictionary
        labels = self.km.labels_
        for i in range(0, self.k, 1):
            self.results[i] = []

        # assign results by label
        for i in range(0, len(labels), 1):
            self.results[labels[i]].append(self.companies[i])
            self.company_to_cluster[self.companies[i].name] = labels[i]

        # Write cluster results to Output file
        output_results(self.km, self.k, self.vectorizer, self.results)
        pass

    def get_recommendations(self, company_name):
        # Look up the company's cluster by name
        if company_name in self.company_to_cluster:
            cluster_no = self.company_to_cluster[company_name]
            cluster = self.results[cluster_no]
            # Append all the companies similar to the given company to a string and return
            similar_str ="["
            for company in cluster:
                if company_name != company.name:
                    similar_str += company.name + ", "
            similar_str = similar_str[:len(similar_str)-2] + "]"
        else:
            similar_str = "Sorry, that company name does not appear in the given data. "
        return similar_str
