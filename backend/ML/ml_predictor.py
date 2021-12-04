from .ml_trainer import trainer
from .Matrix_gen import generate_responsibility_matrix,percent_to_hr,random_engg_levels

def predictor(Maxlevels):
    model=trainer()
    while(len(Maxlevels)!=10*4):
        Maxlevels.append(0.0)
    responsibility_matrix = generate_responsibility_matrix(Maxlevels)
    probability_impact_row = []
    for col in range(160): probability_impact_row.append(round(sum(row[col] for row in responsibility_matrix),1))
    hr_row = percent_to_hr(probability_impact_row) #doubt needs change?
    y_hat=model.predict([probability_impact_row]) #doubt change ?
    return y_hat[0] #doubt change?

