import numpy as np
import os, sys
import gmsh

# ========================================================= #
# ===  make__lift                                       === #
# ========================================================= #

def make__lift():

    # ------------------------------------------------- #
    # --- [1]  make geometry                        --- #
    # ------------------------------------------------- #
    import nkGmshRoutines.geometrize__fromTable as geo
    inpFile = "dat/geometry.conf"
    dimtags = geo.geometrize__fromTable( inpFile=inpFile )

    entities = gmsh.model.occ.getEntities(3)
    
    print( entities )
    print( dimtags )

    return()

    


# ========================================================= #
# ===   実行部                                          === #
# ========================================================= #

if ( __name__=="__main__" ):
    
    # ------------------------------------------------- #
    # --- [1] initialization of the gmsh            --- #
    # ------------------------------------------------- #
    gmsh.initialize()
    gmsh.option.setNumber( "General.Terminal", 1 )
    gmsh.option.setNumber( "Mesh.Algorithm"  , 5 )
    gmsh.option.setNumber( "Mesh.Algorithm3D", 4 )
    gmsh.option.setNumber( "Mesh.SubdivisionAlgorithm", 0 )
    gmsh.model.add( "model" )
    
    # ------------------------------------------------- #
    # --- [2] Modeling                              --- #
    # ------------------------------------------------- #
    make__lift()
    gmsh.model.occ.synchronize()
    gmsh.model.occ.removeAllDuplicates()
    gmsh.model.occ.synchronize()

    gmsh.write( "msh/model.geo_unrolled" )

    
    # ------------------------------------------------- #
    # --- [3] Mesh settings                         --- #
    # ------------------------------------------------- #
    gmsh.option.setNumber( "Mesh.CharacteristicLengthMin", 0.02 )
    gmsh.option.setNumber( "Mesh.CharacteristicLengthMax", 0.02 )

    # ------------------------------------------------- #
    # --- [4] post process                          --- #
    # ------------------------------------------------- #
    gmsh.model.occ.synchronize()
    gmsh.model.mesh.generate(3)
    gmsh.write( "msh/model.msh" )
    gmsh.finalize()
