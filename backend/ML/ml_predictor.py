from .ml_trainer import trainer
from .Matrix_gen import generate_responsibility_matrix,percent_to_hr,random_engg_levels,gen_probability_impact_row

def predictor(Maxlevels):
    model=trainer()
    teams=len(Maxlevels)//4
    responsibility_matrix = generate_responsibility_matrix(Maxlevels)
    probability_impact_row = gen_probability_impact_row(responsibility_matrix,teams)
    hr_row = percent_to_hr(probability_impact_row)
    y_hat=model.predict([probability_impact_row]) 
    print("Maxlvl: ",Maxlevels)
    print("HR::",hr_row)
    return hr_row

