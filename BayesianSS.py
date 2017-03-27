# -*- coding: utf-8 -*-
import pymc as mc
import ss_data as data

def score_eval(cost = c, delivery_time = d, guarantee = g, quality = q):
    value = (c/9 + d/2 + g + q/2)/4
    return value

score = pymc.Deterministic(eval = score_eval,
                  name = 'supplier_score',
                  parents = {'cost': cost,
                          'delivery_time': delivery_time,
                          'guarantee': guarantee,
                          'quality': quality},
                  doc = 'The score the supplier obtains, based in cost, delivery time, guarantee and quality.',
                  trace = True,
                  verbose = 0,
                  dtype=float,
                  plot=False,
                  cache_depth = 2)

#cost =
#delivery_time =
#guarantee =
#quality =
#M = mc.MCMC([score, cost, delivery_time, guarantee, quality])
