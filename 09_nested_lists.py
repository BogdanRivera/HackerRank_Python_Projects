if __name__ == '__main__':
    names = []
    scores = []
    for _ in range(int(input())):
        name = input("Give me a name: ")
        score = float(input("Give me a score: "))
        names.append(name)
        scores.append(score)
    names_f=dict(zip(names,scores))
    
    
    
