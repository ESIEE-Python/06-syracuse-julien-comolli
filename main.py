"""
Module suite de syracuse.
"""

# imports
from plotly.graph_objects import Scatter, Figure

### NE PAS MODIFIER ###
def syr_plot(lsyr):
    """
    Dessine le plot.
    """
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({  'layout':   { 'title': {'text': title},
                                'xaxis': {'title': {'text':"x"}},
                                'yaxis': {'title': {'text':"y"}},
                                }
                }
    )

    x = [ i for i in range(len(lsyr)) ]
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color = "blue")
    fig.add_trace(t)
    fig.show()
    # fig.write_html('fig.html', include_plotlyjs='cdn')
    # return None
#######################


def syracuse_l(n):
    """retourne la suite de Syracuse de source n
l
    Args:
        n (int): la source de la suite

    Returns:
        list: la suite de Syracuse de source n
    """

    l = [ ]
    l.append(n)
    while n != 1:
        # Transformation des conditions en arithmétique
        # pour éviter d'utiliser des if (plus rapide)
        n = n % 2 * (3 * n + 1) + (1 - n % 2) * n / 2
        l.append(int(n))

    return l

def temps_de_vol(l):
    """Retourne le temps de vol d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol
    """

    n = len(l)
    return n

def temps_de_vol_en_altitude(l):
    """Retourne le temps de vol en altitude d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol en altitude
    """

    for i in range(len(l)):
        if l[i+1] < l[0]:
            # Ici c'est le rang pas l'indice du tableau
            n = i + 1
            break
    return n


def altitude_maximale(l):
    """retourne l'altitude maximale d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: l'altitude maximale
    """

    n = max(l)
    return n


#### Fonction principale


def main():
    """
    Fonctione principale.
    """

    # vos appels à la fonction secondaire ici
    lsyr = syracuse_l(6)
    print(lsyr)
    syr_plot(lsyr)
    print(temps_de_vol(lsyr))
    print(temps_de_vol_en_altitude(lsyr))
    print(altitude_maximale(lsyr))


if __name__ == "__main__":
    main()
