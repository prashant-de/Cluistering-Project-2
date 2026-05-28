# AI Use Disclosure

### 1) Which AI tool you used
* **Gemini** 

---

### 2) Which part of the assignment the AI assisted with
* **Data Preprocessing & Visualization:** The AI assisted with implementing the **2D mesh grid generation code** based on the South Korea territory boundary data, as well as creating the **4-panel Matplotlib visualization plot** to clearly demonstrate the data preprocessing flow.

---

### 3) How the AI helped you
* **Code Generation & Optimization:** The AI helped write the logic utilizing `numpy.meshgrid` and the `shapely` library to efficiently filter out grid points located strictly inside the territory boundary.
* **Visualization Layout Design:** The AI provided the structure for the 4-panel chart layout (`plt.subplots(1, 4)`) and refined visual elements (such as color mapping, transparency, and positioning the legend outside the plot) to intuitively show the data pipeline from raw boundary to the final clustered result.

---

### 4) What part you completed on your own
* **Core Algorithm Implementation:** I independently developed the core **K-Means clustering algorithm (Step 2) from scratch** using pure Python and NumPy, without relying on external machine learning libraries like scikit-learn. This included writing the entire logic for initializing random centroids, calculating Euclidean distances, assigning points to clusters, updating centroids, and managing the convergence loop (`while` loop).
* **Data Integration & Debugging:** I successfully connected the grid data format (`points` array) generated in the preprocessing step with my custom K-Means algorithm, ensuring the entire script executed seamlessly without errors.

---

### 5) Exact prompts if applicable 
> "I have a CSV file containing the boundary coordinates of South Korea. Can you write a Python script using the Shapely library that generates a 100x100 mesh grid over this area and filters out only the points inside the boundary?"

> "Can you write a Matplotlib code snippet that takes this preprocessed data and visualizes the whole process in a 4-panel horizontal subplot? The final panel should display the K-Means clusters with their final centroids marked as stars."
