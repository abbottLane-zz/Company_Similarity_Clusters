# Company_Similarity_Clusters
This program takes information about different companies and clusters them using K-means. You can then query the program to find companies similar to the one you provide.

To run the program:
1. From the terminal, naviage to the project folder
2. Make sure a folder named "Data" lives at the project root, and in "Data/input_file.csv", where "input_file.csv" is a data file of the expected format (not included here on github)
3. Type "python3 run_company_recommender.py"
4. Follow the prompt and type in one of the company names from the input data file. 

For example:

Please type the name of a company (or type 'q' to quit): <------program prompt
Microgon <----this is what you type
Similar Companies: [

Alpha Membrane : 0.772669822503

fluXXion : 0.811542176181

Clean Filtration Technologies : 0.878610443091

Intelligene : 0.881296033412

KA Electronik : 0.981061594931

Celetronix India : 0.987207561355

]

Note that the similar companies also report their cosine spatial distance from the queried company. 
