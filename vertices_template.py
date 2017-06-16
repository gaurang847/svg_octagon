import numpy


x = numpy.array([  92.38795325,   86.97599225,   79.3223236,    73.9103626,    73.9103626,
    79.3223236,    86.97599225,   92.38795325,
  101.62674858,   90.80282657,   75.49548928,   64.67156728,   64.67156728,
    75.49548928,   90.80282657,  101.62674858,
  110.8655439,    94.6296609,    71.66865496,   55.43277195,   55.43277195,
    71.66865496,   94.6296609,   110.8655439 ,
  120.10433923,   98.45649522,   67.84182063,   46.19397663,   46.19397663,
    67.84182063,   98.45649522,  120.10433923,
  129.34313455,  102.28332954,   64.01498631,   36.9551813,    36.9551813,
    64.01498631,  102.28332954,  129.34313455,
  138.58192988,  106.11016387,   60.18815198,   27.71638598,   27.71638598,
    60.18815198,  106.11016387,  138.58192988,
  147.8207252,   109.93699819,   56.36131766,   18.47759065,   18.47759065,
    56.36131766,  109.93699819,  147.8207252 ,
  157.05952053,  113.76383252,   52.53448334,    9.23879533,    9.23879533,
    52.53448334,  113.76383252,  157.05952053,
  166.29831585,  117.59066684,   48.70764901,    0.,            0.,
    48.70764901,  117.59066684,  166.29831585,
    0.,            0.,            0.,            0.,            0.,            0.,
     0,            0.        ])

y = numpy.array([  86.97599225,  92.38795325,   92.38795325,   86.97599225,   79.3223236,
    73.9103626,    74.,           79.3223236, 
   90.80282657,  101.62674858,  101.62674858,   90.80282657,   75.49548928,
    64.67156728,   65.,           75.49548928,
   94.6296609,   110.8655439,   110.8655439,    94.6296609,    71.66865496,
    55.43277195,   55.,           71.66865496,
   98.45649522,  120.10433923,  120.10433923,   98.45649522,   67.84182063,
    46.19397663,   46.,           67.84182063,
  102.28332954,  129.34313455,  129.34313455,  102.28332954,   64.01498631,
    36.9551813,    37.,           64.01498631,
  106.11016387,  138.58192988,  138.58192988,  106.11016387,   60.18815198,
    27.71638598,   28.,           60.18815198,
  109.93699819,  147.8207252,   147.8207252,   109.93699819,   56.36131766,
    18.47759065,   18.,           56.36131766,
  113.76383252,  157.05952053,  157.05952053,  113.76383252,   52.53448334,
     9.23879533,    9.,           52.53448334,
  117.59066684,  166.29831585,  166.29831585,  117.59066684,   48.70764901,
     0.,            0.,           48.70764901,
    0.,            0.,            0.,            0.,            0.,            0.,
     0.,            0.        ])

x = x.reshape((10,8))
y = y.reshape((10,8))

i = 7

while i > 0:
    for j in range(8):
        tx1 = x[j][i]
        tx4 = x[j][i - 1]
        tx2 = x[j+1][i]
        tx3 = x[j+1][i-1]
        ty1 = y[j][i]
        ty4 = y[j][i - 1]
        ty2 = y[j+1][i]
        ty3 = y[j+1][i-1]
        print '<a xlink:href="#"><polygon class="teal" points="', tx1, ty1, tx2, ty2, tx3, ty3, tx4, ty4, '" /></a>'
    i-=1