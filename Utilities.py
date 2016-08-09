import csv
from CompanyDoc import CompanyDoc


def load_data(file_path, has_header):
    with open(file_path, "rt", encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        companies = []
        descriptions = []
        row_count = 0
        for row in reader:
            if has_header and row_count != 0:
                company = CompanyDoc(row[0], row[1], row[2].split("\""))
                companies.append(company)
                descriptions.append(row[1])
            row_count += 1
    return companies, descriptions


def output_results(km, k, vectorizer, results):
    # write cluster files
    for cluster in results:
        with open("Output/cluster_" + str(cluster), "w") as file:
            for company in results[cluster]:
                file.write(company.name + "\n\t" + company.description + "\n\t" + str(company.keywords) + "\n")

    # write file showing what the top features for each cluster are
    write_top_terms_in_cluster(k, km, vectorizer)
    pass


def write_top_terms_in_cluster(k, km, vectorizer):
        order_centroids = km.cluster_centers_.argsort()[:, ::-1]
        terms = vectorizer.get_feature_names()
        with open("Output/_Cluster_Top_Terms.txt", "w") as file:
            for i in range(k):
                file.write("Cluster %d:" % i + "\n")
                file.write("\tTop 10 Dimensions: ")
                for ind in order_centroids[i, :10]:
                    file.write(' %s' % terms[ind] + ", ")
                file.write("\n")
