import pandas as pd

def summary(df):
    """
    Input: a DataFrame with columns "age", "weight", "height", "systolic_bp", "cholesterol"
    Outpput: aggregated metrics in a DataFrame, with mean values, medians, smallest and largest values for columns mentioned in function input.
    """
    age  = df['age']
    weig = df['weight']
    heig = df['height']
    syst = df['systolic_bp']
    chol = df['cholesterol']

    summary = pd.DataFrame({
        "Age": [age.mean(), age.median(), age.min(), age.max()],
        "Weight": [weig.mean(), weig.median(), weig.min(), weig.max()],
        "Height": [heig.mean(), heig.median(), heig.min(), heig.max()],
        "Blood Pressure": [syst.mean(), syst.median(), syst.min(), syst.max()],
        "Cholesterol": [chol.mean(), chol.median(), chol.min(), chol.max()]
    }, index=["Mean","Median","Min", "Max"])

    return summary