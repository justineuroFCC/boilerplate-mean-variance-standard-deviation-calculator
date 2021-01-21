import numpy as np

def calculate(list):
  if (len(list)<9):
    raise ValueError("List must contain nine numbers.")
  else:
    df = np.reshape(np.array(list),(3,3))
    calculations = {
      'mean': [np.average(df,0).tolist(), np.average(df,1).tolist(), np.average(list).tolist()],
      'variance': [np.var(df,0).tolist(), np.var(df,1).tolist(), np.var(list).tolist()],
      'standard deviation': [np.std(df,0).tolist(), np.std(df,1).tolist(), np.std(list).tolist()],
      'max': [np.max(df,0).tolist(), np.max(df,1).tolist(), np.max(list).tolist()],
      'min': [np.min(df,0).tolist(), np.min(df,1).tolist(), np.min(list).tolist()],
      'sum': [np.sum(df,0).tolist(), np.sum(df,1).tolist(), np.sum(list).tolist()]
    }
    return calculations
