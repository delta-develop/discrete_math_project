
class CustomSet(set):

    def __init__(self,*content):
        self.content = set(content)

    
    def difference(A, B):
        return A.content - B.content

        
    def union(A, B):
        return A.content | B.content

        
    def intersection(A, B):
        return A.content & B.content

    
    def symetric_difference(A,B):
        return A.content ^ B.content 

        
    def is_subset(A, B):
        if len(A.content) > len(B.content):
            return False
        
        if A.content == B.content:
            return True
        
        if all([item in B.content for item in A.content]):
            return True
        
        return False
    
    def __str__(self):
        return f"{self.content}"
    


if __name__ == "__main__":
    set_1 = CustomSet(1,2,3,4,5,6,7,8,9,0)
    set_2 = CustomSet(5,6,7,8,9,10,11,12,13,14,15)
    set_3 = CustomSet(1,2,3)
    set_4 = CustomSet(20,21,22)

    union = set_1.union(set_2)
    intersection = set_1.intersection(set_2)
    difference = set_1.difference(set_2)
    symetric_difference = set_1.symetric_difference(set_2)
    is_subset_1 = set_3.is_subset(set_1)
    is_subset_2 = set_4.is_subset(set_2)




    print(f"Conjunto 1: {set_1}")
    print(f"Conjunto 2: {set_2}")
    print(f"Conjunto 3: {set_3}")
    print(f"Conjunto 4: {set_4} \n")


    print(f"Unión: {union}")
    print(f"Intersección: {intersection}")
    print(f"Diferencia: {difference}")
    print(f"Diferencia simétrica: {symetric_difference}")
    print(f"¿Es conjunto 3 subconjunto de conjunto 1? {'Sí' if is_subset_1 else 'No'}")
    print(f"¿Es conjunto 4 subconjunto de conjunto 2? {'Sí' if is_subset_2 else 'No'}")