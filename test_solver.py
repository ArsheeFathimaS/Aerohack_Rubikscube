import solver as sv

# Example: scrambled cube string (must be 54 characters)
cubestring = "DUUBULDBFRBFRRULLLBRDFFFBLURDBFDFDRFRULBLUFDURRBLBDUDL"

# Solve (19 = max move length, 2 = timeout seconds)
solution = sv.solve(cubestring, 19, 2)
print("Solution:", solution)