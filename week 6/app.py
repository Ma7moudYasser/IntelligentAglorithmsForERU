from fastapi import FastAPI
import pickle
from ant_colony_algorithm import AntColony

app = FastAPI()

with open('ant_colony.pkl', 'rb') as f:
    ant_colony = pickle.load(f)


@app.get("/")
def read_root():
    return {"message": "Ant Colony Optimization API"}


@app.get("/run_optimization")
def run_optimization(max_iter: int = 100):
    best_path, all_paths = ant_colony.run(max_iter=max_iter)
    return {"best_path": best_path, "all_paths": all_paths}
