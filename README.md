# k-means

k-meas is an exercise in which two datasets are analysed using the k-means algorithm. The project involved refactoring an initial app provided as coursework to better suit multiple applications, implementing dataset-specific functions and analysing the impact of selected number of clusters, iterations and distance calculating method on the results.

## features

- generalised k-means algorithm
- analysis of two datasets: top baby names by state and healthcare noshows

## getting started

### dependencies

- Python 3.x
- Python packages listed in `requirements.txt`

```
pip install -r requirements.txt
```

### installation

- clone the repository or download the zip

### run

2 ways to interact with the program:

1. run the file `corrected_app/main.py` using the command:

```
python -m corrected_app.main
```

2. run the cells from jupyter notebooks in `corrected_app/top_baby_names/top_baby_names_results_analysis.ipynb` and `corrected_app/healthcare_noshows/healthcare_noshows.results_analysis.ipynb`

### output 

1. the output of running the file `corrected_app/main.py` will be printed final clusters and centroids from the selected loop
2. the output of running the jupyter notebooks will be charts showing the impact of selected number of clusters, iterations and distance calculating method
