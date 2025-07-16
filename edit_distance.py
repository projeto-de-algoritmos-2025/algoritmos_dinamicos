class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        
        # Criar uma matriz de dp com (m+1) linhas e (n+1) colunas
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Inicializar a primeira coluna
        for i in range(m + 1):
            dp[i][0] = i
        
        # Inicializar a primeira linha
        for j in range(n + 1):
            dp[0][j] = j
        
        # Preencher a matriz dp
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j],    # Exclusão
                                      dp[i][j - 1],    # Inserção
                                      dp[i - 1][j - 1]) # Substituição
        return dp[m][n]