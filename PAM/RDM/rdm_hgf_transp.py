import numpy as np

def RDM_hgf_transp(r, ptrans):
    """Transform parameters to their native space for the Racing Diffusion Model (RDM)"""

    # Initialize empty arrays for transformed parameter vector and structure
    pvec = np.empty(len(ptrans))
    pvec[:] = np.nan
    pstruct = {}

    try:
        # Extract the first column of 'y' and remove irregular trials
        y = r['y'][:, 0]  
        y = np.delete(y, r['irr'])  # Remove irregular trials based on 'irr' indices
    except Exception as e:
        # Set y to NaN if there is an error
        y = np.nan

    # Apply exponential transformation to "a"
    pvec[0] = np.exp(ptrans[0])
    pstruct['a_a'] = pvec[0]

    # Transform "ba" in the range (-1, 1)
    pvec[1] = ptrans[1]
    pstruct['b_a'] = pvec[1]

    # Apply exponential transformation to "Vv"
    pvec[2] = np.exp(ptrans[2])
    pstruct['a_v'] = pvec[2]

    # Apply exponential transformation to "Vi"
    pvec[3] = np.exp(ptrans[3])
    pstruct['b_val'] = pvec[3]

    # Transform "bv" in the range (-1, 1)
    pvec[4] = ptrans[4]
    pstruct['b_v'] = pvec[4]

    # Transform "Ter" using a sigmoid, centered at the minimum value of y
    if not np.isnan(y).all():  # Check if 'y' is not all NaN
        pvec[5] = np.min(y) / (1 + np.exp(-ptrans[5]))
        pstruct['Ter'] = pvec[5]
    else:  # In case of NaN or missing values, pass 'Ter' directly
        pvec[5] = ptrans[5]
        pstruct['Ter'] = pvec[5]

    return ([pvec, pstruct])
