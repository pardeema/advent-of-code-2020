FILE='input.txt'

with open(FILE, 'r') as f:
    treemap = f.read().split('\n')
    
treemap = [i for i in treemap if i!=''] #Cleanup
width = len(treemap[0])
height = len(treemap)

def tree_finder(slopex, slopey):
    posy = 0 
    posx=0
    trees=0

    while posy < height:
        if posx > width-1: #Adjust width to 0 index
            posx = posx - width  #But subtract actual width from current pos
        #check location of treemap[posy][posx] - y first because rows
        if treemap[posy][posx] == '#':
            trees +=1

        posx+=slopex
        posy+=slopey
    return trees

def main():
    #Pt1 - Slopex 3, Slopey 1
    trees1 = tree_finder(3,1)
    print("pt1: {}".format(trees1))

    #Other slopes for pt2: (1,1), (5,1), (7,1), (1,2)
    trees2 = tree_finder(1,1)
    trees3 = tree_finder(5,1)
    trees4 = tree_finder(7,1)
    trees5 = tree_finder(1,2)

    print('pt2: {}'.format(trees1*trees2*trees3*trees4*trees5))

if __name__ == '__main__':
    main()