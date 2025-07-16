import bisect

class Solution:
    def jobScheduling(self, startTime, endTime, profit):
        # Combinar os arrays em uma lista de tuplas e ordenar por endTime
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        n = len(jobs)
        dp = [0] * (n + 1)
        # Extrair os tempos de término para busca binária
        end_times = [0] + [job[1] for job in jobs]
        
        for i in range(1, n + 1):
            start, end, p = jobs[i - 1]
            # Encontrar o último job que não conflita com o job atual
            # Usamos bisect_right para encontrar o ponto de inserção
            j = bisect.bisect_right(end_times, start) - 1
            # Atualizar dp[i] com o máximo entre incluir ou não o job atual
            dp[i] = max(dp[i - 1], dp[j] + p)
        
        return dp[n]