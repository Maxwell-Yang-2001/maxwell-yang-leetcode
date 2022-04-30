class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # variables would look like: { var_name: set_number }
        variables = dict()
        # sets would look like: [ { var_name: rel_val } ]
        sets = []
        
        for i, eq in enumerate(equations):
            a, b, val = eq[0], eq[1], values[i]
            # to make logic simpler - when a is not in a set, b would never be in a set
            if a not in variables:
                a, b, val = b, a, 1 / val
            if a in variables:
                if b in variables:
                    if variables[a] != variables[b]:
                        # 2 different sets - merge set with b to set with a; otherwise it is a useless equation
                        set_a, set_b = sets[variables[a]], sets[variables[b]]
                        multiplier = set_a[a] / val / set_b[b]
                        for var in set_b:
                            set_a[var] = set_b[var] * multiplier
                            variables[var] = variables[a]
                        set_b.clear()
                else:
                    # a is already in a set, just add b to the same set with correct value
                    variables[b] = variables[a]
                    curr_set = sets[variables[b]]
                    curr_set[b] = curr_set[a] / val
            else:
                # neither are present, use a new set with a being 1.0
                variables[a] = variables[b] = len(sets)
                sets.append(dict())
                curr_set = sets[-1]
                curr_set[a] = 1.0
                curr_set[b] = curr_set[a] / val
        
        result = []
        for q in queries:
            # did not appear in equations or not in same set - cannot be determined
            if q[0] not in variables or q[1] not in variables or variables[q[0]] != variables[q[1]]:
                result.append(-1.0)
            else:
                result.append(sets[variables[q[0]]][q[0]] / sets[variables[q[1]]][q[1]])

        return result