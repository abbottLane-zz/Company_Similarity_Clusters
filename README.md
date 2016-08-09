# Company_Similarity_Clusters
This program takes information about different companies and clusters them using K-means. You can then query the program to find companies similar to the one you provide.

To run the program:
1. From the terminal, naviage to the project folder
2. Make sure a folder named "Data" lives at the project root, and in "Data/input_file.csv", where "input_file.csv" is a data file of the expected format (not included here on github)
3. Type "python3 run_company_recommender.py"
4. Follow the prompt and type in one of the company names from the input data file. 
5. A list of most similar companies will be displayed in order from most similar to least. Note that the cosine spatial distance from the queried company is also reported. 
