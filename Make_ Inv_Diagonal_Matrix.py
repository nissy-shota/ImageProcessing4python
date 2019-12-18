import numpy as np

m_size = 3
M = np.diag( [1] * m_size ).astype(np.float)[::,::-1]

"""
M = np.diag( [1] * m_size ).astype(np.float)
何かしたい処理をする（BroadCast）
M = M*3
ひっくり返す．
M = M[::,::-1]
"""