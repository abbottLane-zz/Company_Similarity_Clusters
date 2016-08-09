import csv
import operator

from CompanyDoc import CompanyDoc
from scipy import spatial


def load_data(file_path, has_header):
    with open(file_path, "rt", encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        companies = []
        descriptions = []
        company_idx_map = {}
        row_count = 0
        company_idx = 0
        for row in reader:
            if has_header and row_count != 0:  # Skip the header
                company = CompanyDoc(row[0], row[1], row[2].split("\""))
                companies.append(company)
                descriptions.append(row[1])
                company_idx_map[row[0]] = company_idx
                company_idx += 1
            row_count += 1
    return companies, descriptions, company_idx_map


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


def get_cluster_of_vectors(cluster, vector_array, company_idx_map):
    vectors = list()
    for company in cluster:
        vectors.append((vector_array[company_idx_map[company.name]], company))
    return vectors


def sort_company_vectors(cluster_company_vectors, centroid_vector):
    company_vector_tuples = list()
    for vec in cluster_company_vectors:
        distance = spatial.distance.cosine(vec[0], centroid_vector)
        company_vector_tuples.append((vec[1], distance))
    company_vector_tuples.sort(key=operator.itemgetter(1))
    return company_vector_tuples


def get_sorted_companies(cluster, company_name, company_idx_map, vector_array):
    centroid_company_idx = company_idx_map[company_name]
    centroid_vector = vector_array[centroid_company_idx]
    cluster_company_vectors = get_cluster_of_vectors(cluster, vector_array, company_idx_map)
    sorted_company_vectors = sort_company_vectors(cluster_company_vectors, centroid_vector)
    return sorted_company_vectors
