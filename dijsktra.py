def antecedents(pere, depart, extremite, trajet):
    if extremite == depart:
        return [depart] + trajet
    else:
        return antecedents(pere, depart, pere[extremite], [extremite] + trajet)


def cherche_plus_court(graphe, etape, fin, visites, dist, pere, depart):
    # si on arrive à la fin, on affiche la distance et les peres
    if etape == fin:
        return dist[fin], antecedents(pere, depart, fin, [])

    # si c'est la première visite, c'est que l'étape actuelle est le départ : on met dist[etape] à 0
    if len(visites) == 0:
        dist[etape] = 0

    # on commence à tester les voisins non visités
    for voisin in graphe[etape]:
        if voisin not in visites:
            # la distance est soit la distance calculée précédemment soit l'infini
            dist_voisin = dist.get(voisin, float('inf'))

            # on calcule la nouvelle distance calculée en passant par l'étape
            candidat_dist = dist[etape] + graphe[etape][voisin]

            # on effectue les changements si cela donne un chemin plus court
            if candidat_dist < dist_voisin:
                dist[voisin] = candidat_dist
                pere[voisin] = etape

    # on a regardé tous les voisins : le noeud entier est visité
    visites.append(etape)

    # on cherche le sommet *non visité* le plus proche du départ
    non_visites = dict((s, dist.get(s, float('inf'))) for s in graphe if s not in visites)
    if non_visites.get is not None:
        noeud_plus_proche = min(non_visites, key=non_visites.get)

    # on applique récursivement en prenant comme nouvelle étape le sommet le plus proche
    return cherche_plus_court(graphe, noeud_plus_proche, fin, visites, dist, pere, depart)


def dijkstra(graphe, debut, fin):
    print("Calcul du plus court chemin entre {} et {} par l'algorithme de Dijkstra".format(debut, fin))
    return cherche_plus_court(graphe, debut, fin, [], {}, {}, debut)


def demande_graphe():
    graphe = {}
    ajoutpoint = True
    print("""On peut renseigner les voisins même s'ils n'ont pas été définis
L'ordre des points n'a pas d'importance, les sommets seront demandés par la suite""")
    while ajoutpoint:
        tmp_point = demande_point()
        tmp_voisins = {}
        ajoutvoisin = True
        while ajoutvoisin:
            tmp_voisin = demande_voisin(tmp_point)
            tmp_voisins[tmp_voisin[0]] = tmp_voisin[1]
            ajoutvoisin = ouinon("Faut il un autre voisin ? (Y/n)")
        graphe[tmp_point] = tmp_voisins
        ajoutpoint = ouinon("Faut il un autre point ? (Y/n)")

    return graphe


def ouinon(texte):
    yes = {'yes', 'y', 'ye', ''}
    no = {'no', 'n'}
    print(texte)
    choice = input().lower()
    if choice in yes:
        return True
    elif choice in no:
        return False
    else:
        print("Please respond with 'yes' or 'no'")


def demande_point():
    point = input("Selectionner le nom du point :\n")
    return point


def demande_voisin(point_pere):
    point = input("Selectionner le nom du voisin de {} :\n".format(point_pere))
    ponde = int(input("Selectionner la ponderation :\n"))
    return point, ponde


if __name__ == "__main__":

    # On détermine le tableau en dictionnaire. Chaque point a un dictionnaire de ses voisins avec leur pondération
    # graphe = demande_graphe()
    graphe = {'a': {'b': 4, 'c': 6}, 'b': {'d': 5}, 'c': {'d': 9}}


    print(graphe)

    entree = input("Renseigner le point d'entree :\n")
    sortie = input("Renseigner le point de sortie :\n")

    longueur, chemin = dijkstra(graphe, entree, sortie)

    print('Plus court chemin : {} de longueur : {}'.format(chemin, longueur))
