class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Paso 1: Verificar longitudes (optimización temprana)
        if len(s) != len(t):
            return False
        
        # Paso 2: Contar frecuencias manualmente con diccionario
        char_count = {}
        
        # Contar caracteres de s (incrementar)
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        # Restar caracteres de t (decrementar)
        for char in t:
            if char not in char_count:
                return False  # Carácter en t que no existe en s
            char_count[char] -= 1
            if char_count[char] < 0:
                return False  # Más repeticiones en t que en s
        
        return True