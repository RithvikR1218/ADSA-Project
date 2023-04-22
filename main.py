import function
edges = ""
print("\n*********************************************")
print("Genome Sequencing Software - De Brujin Graphs")
print("*********************************************")

while True:

    print("\n****")
    print("Menu")
    print("****\n")

    print("1 -> Begin sequencing")
    print("2 -> Display graph")
    print("3 -> Exit\n")

    k = int(input("Enter your choice : "))

    if(k == 1):

        seq = input("Enter genome sequence : ")

        length = int(input("Enter length of k-mers : "))
        
        kmers = function.kmer_set(seq, length, True)

        print("K-mers obtained successfully")

        w = int(input("Enter 1 to display k-mers, 0 to skip : "))
        if (w == 1):
            print("K-mers are : ")
            print(kmers)

        print("Obtaining graph edges.........")

        edges = function.edge_set(kmers)

        w = int(input("Enter 1 to display edges, 0 to skip : "))

        if (w == 1):
            print("Edges are : ")
            print(edges)
        
        print("\nSEQUENCING COMPLETE")

    elif (k == 2):

        if (edges == ""):
            print("ERROR: No genome sequence entered......")
            continue

        print("GRAPHING....")
        function.plot_debruijn_graph(edges, width=500, height=500)

    elif (k == 3):
        print("Exiting......")
        break
    else:
        print("Invalid entry, please try again......")
