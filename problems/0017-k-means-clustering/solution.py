import numpy as np
def euclidian(a, b):
	return np.linalg.norm(a-b, axis=1)

def k_means_clustering(points: list[tuple[float, ...]], k: int, initial_centroids: list[tuple[float, ...]], max_iterations: int) -> list[tuple[float, ...]]:
	points = np.array(points)
	centroids = np.array(initial_centroids)
	for iteration in range(max_iterations):
		dists = np.array([euclidian(points, centroid) for centroid in centroids])
		assignments = np.argmin(dists, axis=0)

		new_centroids = np.array([points[assignments == i].mean(axis=0) if len(points[assignments == i]) > 0 else centroids[i]for i in range(k)])

		centroids = new_centroids
		centroids = np.round(centroids, 4)
	return [tuple(centroid) for centroid in centroids]