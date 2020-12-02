

def npz_save(arq,data):
    import numpy as np
    np.savez(arq,**data)


def npz_load(arq):
    import numpy as np
    f =  np.load(arq)
    dados = {}
    for i in f.files:
        dados[i] = f[i]
    return(dados)

