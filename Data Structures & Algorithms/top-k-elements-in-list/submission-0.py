class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        dicc = {}

        for i in nums:
            if i not in dicc:
                dicc[i] = 1
            else:
                dicc[i] += 1

        ordenados = sorted(dicc.items(), key=lambda x: x[1], reverse=True)

        resultado = []
        for num, freq in ordenados[:k]:
            resultado.append(num)

        return resultado
