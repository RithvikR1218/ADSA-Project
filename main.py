import function
edges = ""
print("\n*********************************************")
print("Genome Assembling Software - De Brujin Graphs")
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

        cycle = bool(input("Enter if genome is cyclic (true / false) : "))
        
        kmers = function.kmer_set(seq, length, cycle)

        if len(kmers) != 0:
            print("K-mers obtained successfully")
        else:
            continue

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
        function.graph_plot(edges, width=500, height=500)

    elif (k == 3):
        print("Exiting......")
        break
    else:
        print("Invalid entry, please try again......")
