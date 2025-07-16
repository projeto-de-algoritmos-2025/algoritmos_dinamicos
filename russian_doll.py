import bisect

class Solution:
    def maxEnvelopes(self, envelopes):
        # Ordenar os envelopes por largura crescente e, em caso de empate, por altura decrescente
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        # Inicializar uma lista para manter as alturas da subsequência crescente
        dp = []
        
        for _, h in envelopes:
            # Usar busca binária para encontrar a posição onde a altura atual pode ser inserida
            idx = bisect.bisect_left(dp, h)
            if idx == len(dp):
                dp.append(h)
            else:
                dp[idx] = h
        
        return len(dp)
        