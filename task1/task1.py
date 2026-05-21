import numpy as np
import matplotlib.pyplot as plt


# Given points in the cartesian plane
points = np.array([
    [2, 10],
    [2, 5],
    [8, 4],
    [5, 8],
    [7, 5],
    [6, 4],
    [1, 2],
    [4, 9]
])

 # Array of initial centroids

centroids = np.array([
    [2, 10],   # C1
    [5, 8],    # C2
    [1, 2]     # C3
])

# K-Means Clustering Implementation

max_iter = 100
tol = 1e-4
iterations_taken = 0

for iteration in range(max_iter):

    iterations_taken = iteration + 1


    clusters = []

# Assign points to nearest centroid
    for point in points:

        # Calculate distance from point to each centroid
        distances = np.linalg.norm(point - centroids, axis=1)

        # Find nearest centroid index
        cluster = np.argmin(distances)

        clusters.append(cluster)

    clusters = np.array(clusters)

    # Update centroids by calculating mean of points in each cluster
    new_centroids = []

    for i in range(3):

        # Get all points in cluster i
        cluster_points = points[clusters == i]

        # Keep the centroid if a cluster becomes empty
        if len(cluster_points) == 0:
            new_centroid = centroids[i]
        else:
            # Calculate mean
            new_centroid = cluster_points.mean(axis=0)

        new_centroids.append(new_centroid)

    new_centroids = np.array(new_centroids)

    # Stop when centroids stop moving meaningfully
    if np.allclose(centroids, new_centroids, atol=tol):
        centroids = new_centroids
        break

    # Update centroid values
    centroids = new_centroids

print(f"Total iterations taken: {iterations_taken}")

print("\nCluster labels for each point:")
for point, cluster in zip(points, clusters):
    print(f"Point {point} -> Cluster {cluster + 1}")

print("\nFinal centroids:")
print(centroids)

    

colors = ['pink', 'blue', 'green']

for i in range(3):

    cluster_points = points[clusters == i]

    plt.scatter(
        cluster_points[:,0],
        cluster_points[:,1],
        color=colors[i],
        label=f'Cluster {i+1}'
    )

# Plot centroids
plt.scatter(
    centroids[:,0],
    centroids[:,1],
    color='red',
    marker='*',
    s=250,
    label='Centroids'
)

plt.legend()
plt.grid(False)
plt.show()