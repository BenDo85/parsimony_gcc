from ortools.sat.python import cp_model

# https://developers.google.com/optimization/cp/queens?hl=fr

model = cp_model.CpModel()
n = 5

# Création des variables
matrix = [model.NewIntVar(0, n - 1, f"x_{i}") for i in range(n)]

# Contraintes pour les lignes
special_row_vars = [model.NewBoolVar(f'special_row[{i}]') for i in range(n)]
for i in range(n):
    model.Add(sum(matrix[i]) == 0).OnlyEnforceIf(special_row_vars[i])
    model.Add(sum(matrix[i]) == 1).OnlyEnforceIf(special_row_vars[i].Not())

model.Add(sum(special_row_vars) == 1)

# Contraintes pour les colonnes
model.Add(sum(column_sum == 2 for column_sum in column_sums) == n)


# Création des contraintes
# Matrice parent-enfant

solver = cp_model.CpSolver()
status = solver.Solve(model)

if status == cp_model.OPTIMAL:
    # Affichage de la solution
    for i in range(n):
        print([solver.Value(matrix[i][j]) for j in range(n)])
else:
    print("Pas de solution trouvée.")
