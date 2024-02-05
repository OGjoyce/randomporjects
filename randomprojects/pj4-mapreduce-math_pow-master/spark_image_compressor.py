# coding=utf-8

"""
  ___                _
 / __|_ __  __ _ _ _| |__
 \__ \ '_ \/ _` | '_| / /
 |___/ .__/\__,_|_| |_\_\.
     |_|

  ___                        ___
 |_ _|_ __  __ _ __ _ ___   / __|___ _ __  _ __ _ _ ___ ______ ___ _ _
  | || '  \/ _` / _` / -_) | (__/ _ \ '  \| '_ \ '_/ -_|_-<_-</ _ \ '_|
 |___|_|_|_\__,_\__, \___|  \___\___/_|_|_| .__/_| \___/__/__/\___/_|
                |___/                     |_|

    Este archivo es que tienen que modificar para obtener el resultado
    deseado
"""

import pyspark
import numpy as np
from helper_functions import *
from pyspark import SparkContext, SparkConf
# esta sera la unica variable global
B_SIZE = 8

############ AQUI TIENEN QUE DEFINIR SUS FUNCIONES DE AYUDA ###############
#(idx, (img, QF)
def generate_Y_cb_cr_matrices_flatMap(pair):
    idx = pair[0]
    img, QF = pair[1]
    out = []
    #image = truncate((None, (img, None)))[1][0]
    height, width = img.shape[0:2]
    for index, canal in enumerate(convert_to_YCrCb(img)):
        out.append(((idx, index), (canal, QF, (height, width))))
    return out

def generate_sub_blocks_flatMap(pair):
    idx, idxCanal = pair[0]
    canal, QF, size= pair[1]
    no_rows = canal.shape[0]
    no_cols = canal.shape[1]
    no_vert_blocks = no_cols / B_SIZE
    no_horz_blocks = no_rows / B_SIZE
    out = []
    for j in range(no_vert_blocks):
        for i in range(no_horz_blocks):
            i_start = i*B_SIZE
            i_end = i_start +B_SIZE
            j_start = j * B_SIZE
            j_end = j_start + B_SIZE
            cur_block = canal[i_start : i_end, j_start: j_end]
            par = ((idx, idxCanal), (cur_block, (i_start, j_start),QF, size))
            out.append(par)
    return out

def apply_transformations_map(pair):
    idx, idxCanal = pair[0]
    cur_block, pos, QF, size= pair[1]
    dct = dct_block(cur_block.astype(np.float32)-128)
    q = quantize_block(dct, idxCanal == 0, QF)
    inv_q = quantize_block(q, idxCanal == 0, QF, inverse = True)
    inv_dct = dct_block(inv_q, inverse=True)
    return ((idx, idxCanal), (inv_dct, pos, size))
# ((idx, idxCanal), (inv_dct,pos,size))
def combine_sub_block_map1(pair):
    idx, idxCanal = pair[0]
    lista = list(pair[1])
    inv_dct, pos, size = lista[0]
    no_rows = size[0]
    no_cols = size[1]
    if (idxCanal == 0):
        dst = np.zeros((no_rows, no_cols), dtype='float32')
        for value in lista:
            inv_dct, pos, size = value
            dst[pos[0]: pos[0]+ B_SIZE, pos[1]:pos[1]+ B_SIZE] = inv_dct
    else:
        dst = np.zeros((no_rows/2, no_cols/2), dtype='float32')
        for value in lista:
            inv_dct, pos, size = value
            dst[pos[0]: pos[0]+ B_SIZE, pos[1]:pos[1]+ B_SIZE] = inv_dct
    #out.append(par)
    dst = dst + 128
    dst[dst>255] = 255
    dst[dst<0] = 0
    dst = resize_image(dst, no_cols, no_rows)
    par = (idx, (dst, idxCanal, size))
    return par

def combine_sub_block_map2(pair):
    idx = pair[0]
    lista = list(pair[1])
    dst, idxCanal, size= lista[0]
    no_rows = size[0]
    no_cols = size[1]
    reimg = np.zeros((no_rows, no_cols, 3), dtype='uint8')
    for i in lista:
        dst, idxCanal, size= i
        reimg[:,:,idxCanal] = dst
    return (idx,to_rgb(reimg))

def generate_Y_cb_cr_matrices(rdd):
    """
    Esta funcion tiene que generar un nuevo rdd transformado

    recuerden que a este nivel todavia son imagenes completas miren que es
    lo que pasa cuando utilizan la funcion convert_to_YCrCb(img) en
    helper_functions ¿deberia usar map, flatMap, o no usar ninguna de estas?
    """
    rdd = rdd.flatMap(generate_Y_cb_cr_matrices_flatMap)
    return rdd


def generate_sub_blocks(rdd):
    """
    Esta funcion tiene que generar un nuevo rdd transformado

    a este nivel ustedes devuelven ya un rdd con varios subblocks, piensen muy
    bien que informacion quieren guardar en los pares (key, value), recuerden
    que el key y value pueden ser una tupla con varios elementos

    ¿sera que es necesario guardar de donde viene ese bloque y en que posicion
    estaba?
    """
    rdd = rdd.flatMap(generate_sub_blocks_flatMap)
    return rdd


def apply_transformations(rdd):
    """
    Esta funcion tiene que generar un nuevo rdd transformado

    aqui cada bloque tiene que ser transformado piensen como pueden hacerlo de
    una manera mas optima aunque para este proyecto solo vamos a medir que
    utilicen Spark correctamente y que funcione, no que sea el algoritmo mas
    optimo
    """
    rdd = rdd.map(apply_transformations_map)
    return rdd


def combine_sub_blocks(rdd):
    """
    Esta funcion tiene que generar un nuevo rdd transformado

    Cuando ya tengan un rdd de subblocks transformados esos subblocks van a
    venir de diferentes imagenes, tienen que combinar los bloques para
    re-construir la imagen. Su rdd deberia de contener valores que son
    arrays de numpy de size (height, width)
    """
    rdd = rdd.groupByKey()
    rdd = rdd.map(combine_sub_block_map1)
    rdd = rdd.groupByKey()
    rdd = rdd.map(combine_sub_block_map2)
    return rdd


def run(images, batch_size=64, threads=8):
    """
    Esta funcion tiene que retornar una lista de python

    Retorna una lista de python donde todas las imagenes ya han sido procesadas
    el formato retornado en la lista deberia ser que por cada elemento se
    deberia de encontrar una tupla de la forma (image_id, image_matrix) donde
    image_matrix es un arreglo de numpy de size (height, width, 3)
    """
    # inicializamos spark
    url = 'local[{0}]'.format(threads)
    # lo configuramos
    conf = SparkConf().setAppName("SparkImageCompressor").setMaster(url)
    # y creamos el contexto
    sc = SparkContext(conf=conf)
    # cuantas imagenes hay
    size = len(images)
    # cuantas iteraciones vamos a tener que hacer
    total = int(np.ceil(float(size)/batch_size))
    # aqui es donde iremos guardando el resultado
    output = []
    # Partitions esto ayuda a que tengamos repartido el dataset en todos los
    # threads por lo general se quiere que hayan 2 particiones por thread en
    # este caso lo hacemos con repartition despues de una transformacion
    # o en el momento de crear el RDD (VEAN LAS NOTAS DE SPARK DEL PROYECTO)
    # para ver como pueden utilizar esto para que sea mas eficiente
    global P
    P = threads * 2
    # iteramos
    # xrange = range solo que xrange no crea el arreglo online, xrange es mas
    # eficiente en terminos de memoria
    for i in xrange(total):
        # calculamos los limites para agarrar un nuevo batch de imagenes
        START = i * batch_size
        END = min((i + 1) * batch_size, size)
        # obtenemos el batch de imagenes
        batch = images[START:END]
        # truncamos el batch de imagenes
        # en este momento rdd tiene pares (idx, (img, QF))
        rdd = sc.parallelize(batch, P).map(truncate).repartition(P)
        rdd =  generate_Y_cb_cr_matrices(rdd)
        rdd = generate_sub_blocks(rdd)
        rdd = apply_transformations(rdd)
        rdd = combine_sub_blocks(rdd)
        ##########################
        #    AQUI SU SOLUCION    #
        ##########################
        # pueden agregar cualquier otra funcion que quieran para hacer en el
        # rdd aqui pueden escribir todas las funciones que quieran y crean que
        # sean necesarias
        output += rdd.collect()
    # le damos stop al contexto de spark para finalizar
    sc.stop()
    # devolvemos el resultado
    return  output
