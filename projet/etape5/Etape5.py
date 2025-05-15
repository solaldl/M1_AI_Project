import os
os.system("sudo apt-get install libtbb-dev")
os.system("sudo apt-get install libopenblas-base")

import re

def extract_objective_value(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            if "objective value:" in line:
                match = re.search(r'[-+]?\d*\.\d+|\d+', line)
                if match:
                    return float(match.group())
    return None

tbb_path = '/snap/blender/4300/lib'

os.environ['LD_LIBRARY_PATH'] = f"{tbb_path}:{os.environ.get('LD_LIBRARY_PATH', '')}"

contenuFichierZIMPL = """
  set V     :=  {1..num_villes};
  set E     := { <i , j > in V * V with i < j };
  set P[]  := powerset (V ) ;
  set K     := indexset (P ) ;

  param px[V]:= read "../../Data/pb-etape5/tspnum_villes.txt" as "1n" skip 4;
  param py[V]:= read "../../Data/pb-etape5/tspnum_villes.txt" as "2n" skip 4;

  defnumb dist(a, b) := sqrt((px[a] - px[b])^2 + (py[a] - py[b])^2);

  var x [E] binary ;
  minimize cost : sum <i,j> in E : dist (i,j) * x [i,j] ;
  subto two_connected : forall <v> in V do
      (sum <v, j> in E : x [v, j] ) + (sum<i, v> in E : x [i, v] ) == 2;
  subto no_subtour :
    forall <k> in K with card(P[k]) > 2 and card(P[k]) < card(V) - 2 do
        sum <i, j> in E with <i> in P[k] and <j> in P[k] : x[i, j] <= card(P[k]) - 1;
"""

for num_villes in range(6, 20):
    fichier_zpl = f'projet/etape5/town{num_villes}.zpl'
    with open(fichier_zpl, 'w') as f:
        f.write(contenuFichierZIMPL.replace("num_villes", str(num_villes)))
    os.system(f'projet/solvers/SCIP/bin/scip -f {fichier_zpl} > projet/etape5/log{num_villes}')
    print("Pour ",num_villes," villes  \t",extract_objective_value(f'projet/etape5/log{num_villes}'))