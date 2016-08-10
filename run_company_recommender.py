from CompanyRecommender import CompanyRecommender


def main():
    # set some variables
    k = 700  # I'm using K-means to generate clusters. Define the number of clusters here
    data_dir = "Data/company_descs_5k.csv"  # the directory where the provided input file lives

    # Initialize build CompanyRecommender object
    cr = CompanyRecommender(data_dir, k)

    # User interface play loop
    play = True
    while play:
        user_input = input("Please type the name of a company (or type 'q' to quit):\n")
        if user_input == "q":
            play = False
        else:
            print("Similar Companies: " + cr.get_recommendations(user_input) + "\n")


if __name__ == '__main__':
    main()
