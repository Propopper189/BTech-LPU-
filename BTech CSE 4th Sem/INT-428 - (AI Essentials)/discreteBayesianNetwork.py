from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Step 1: Define Network
model = DiscreteBayesianNetwork([
    ('Rain', 'Sprinkler'),
    ('Rain', 'Wet_Grass'),
    ('Sprinkler', 'Wet_Grass')
])

# --------------------------------
# Step 2 : Define CPDs
# ---------------------------------

# P(Rain)
cpd_rain = TabularCPD(
    variable='Rain',
    variable_card=2,
    values=[[0.7], [0.3]]  # No Rain, Rain
)

# P(Sprinkler | Rain)
cpd_sprinkler = TabularCPD(
    variable='Sprinkler',
    variable_card=2,
    values=[
        [0.6, 0.1],  # Sprinkler Off
        [0.4, 0.9]   # Sprinkler On
    ],
    evidence=['Rain'],
    evidence_card=[2]
)

# P(Wet_Grass | Rain, Sprinkler)
cpd_wet_grass = TabularCPD(
    variable='Wet_Grass',
    variable_card=2,
    values=[
        [0.99, 0.8, 0.9, 0.1],  # Dry
        [0.01, 0.2, 0.1, 0.9]   # Wet
    ],
    evidence=['Rain', 'Sprinkler'],
    evidence_card=[2, 2]
)

# -----------------------------------
# Step 3 : Add CPDs
# -----------------------------------
model.add_cpds(cpd_rain, cpd_sprinkler, cpd_wet_grass)

# Validate model
print("Model is valid:", model.check_model())

# -----------------------------------
# Step 4 : Perform Inference
# -----------------------------------
inference = VariableElimination(model)

# Query: Probability of Rain given Grass is Wet
result = inference.query(
    variables=['Rain'],
    evidence={'Wet_Grass': 1}  # 1 = Wet
)

print("\nProbability of Rain given Wet Grass:")
print(result)