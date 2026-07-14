# Proposed Content Enhancements for JULY2026 Paper

---

## [REPLACE Section 2.3 — RRL on K-means]

### 2.3 Optimization of Bus Stop Locations Using Spatial Analysis and K-Means Clustering

The placement of bus stops and waiting sheds should be based on commuter demand and travel patterns. Yu, Zhu, Wu, and Song (2024) demonstrated the application of K-means clustering combined with spatial analysis to optimize bus stop locations in Hohhot City, China. Their methodology involved georeferencing passenger boarding and alighting points, applying the K-means algorithm to group these points into clusters of varying demand intensity, and overlaying the resulting clusters with existing route networks to identify service gaps. The study successfully identified high-demand zones where new stops or shelters would provide the greatest benefit, validating K-means as an effective tool for data-driven transit infrastructure planning.

By identifying natural clusters of commuter activity, transport planners can reduce redundant stops while ensuring that passengers remain well served by the transport network. This approach also helps determine where infrastructure such as waiting sheds and loading areas will have the greatest operational impact (Yu et al., 2024; Santos et al., 2020).

Applying clustering methods to the modern jeepney system can help identify high-demand commuter areas, especially during peak hours. These insights allow planners to strategically place waiting sheds in locations where passengers frequently gather, thereby reducing walking distances and preventing overcrowding at existing stops (Yu et al., 2024; Santos et al., 2020).

---

## [REPLACE line 330 in Section 3.4 — K-means mention in Data Gathering]

**Old:**
"Boarding and alighting locations identified from commuter surveys are georeferenced and subjected to K-means clustering to identify passenger demand hotspots. This method groups areas with high commuter concentration and highlights locations where passenger facilities are most needed."

**New:**
Boarding and alighting locations identified from commuter surveys are georeferenced using GIS software and subjected to K-means clustering analysis. This unsupervised machine learning algorithm partitions the set of geospatial points into k distinct clusters by minimizing the within-cluster sum of squared Euclidean distances between each point and its assigned cluster centroid. The resulting clusters represent areas of concentrated commuter activity, allowing the identification of passenger demand hotspots. These hotspots highlight locations where passenger facilities are most needed and serve as the primary spatial basis for the facility prioritization framework.

---

## [REPLACE lines 373-375 in Section 3.6 — K-means paragraph]

**Old:**
"K-means clustering of the georeferenced information will then be used. These clusters point together by distance and relatedness demonstrating an agglomeration of demand. The algorithm will determine three clusters of high, moderate, and low demand which will indicate hotspots that must be given priority when new waiting stations are being set up."

**New:**

#### 3.6.1 K-Means Clustering Analysis

K-means clustering is applied to the georeferenced boarding and alighting coordinates to classify commuter activity into homogeneous demand groups. The K-means algorithm is an iterative partitioning method that seeks to minimize the within-cluster sum of squares (WCSS), defined as:

WCSS = Σᵢ₌₁ᵏ Σₓ∈Cᵢ ‖x - μᵢ‖²

where k is the number of clusters, Cᵢ is the set of points assigned to cluster i, x represents a geospatial point (latitude, longitude), and μᵢ is the centroid (mean coordinate) of cluster i. The Euclidean distance metric ‖x - μᵢ‖ measures the straight-line distance between each point and its cluster centroid.

The algorithm proceeds through the following steps:
1. **Initialization:** Select k initial centroids randomly from the dataset (or using the k-means++ method to improve convergence).
2. **Assignment:** Assign each point to the nearest centroid based on squared Euclidean distance.
3. **Update:** Recalculate the centroid of each cluster as the mean of all points assigned to that cluster.
4. **Iteration:** Repeat steps 2 and 3 until convergence, defined as when centroid positions change by less than a specified threshold (e.g., 1 × 10⁻⁶) between iterations, or when a maximum number of iterations (e.g., 300) is reached.

The number of clusters k was determined to be three based on the elbow method, which plots WCSS against values of k and identifies the point where additional clusters yield diminishing reductions in total variance. Three clusters (k = 3) provided the optimal balance between intra-cluster cohesion and interpretability, corresponding to high, moderate, and low passenger demand levels.

The clustering analysis is implemented within the GIS environment using the native K-means tool available in QGIS (Processing Toolbox > K-means Clustering) or ArcGIS Pro (Spatial Statistics Toolbox > Multivariate Clustering). Input data consist of the XY coordinate pairs of boarding and alighting points collected from the commuter survey. The output consists of a classified point layer, summary tables of cluster membership, and centroid coordinates, which are subsequently overlaid with authorized PUJ routes, existing facility locations, and barangay boundaries to identify service gaps and priority zones for passenger waiting shed placement.

---

## [REPLACE lines 352 in Section 3.5 — CVM mention in Instruments]

**Old:**
"The survey also considers Contingent Valuation (CV) and Willingness-To-Pay (WTP) questions to determine the commuter acceptance of the improved facilities and the respondents are asked to give the amount they can give in case of improved passenger waiting stations. This is a standard approach to evaluating the value of service enhancements by users in transportation research."

**New:**
The survey includes a Contingent Valuation (CV) section employing the payment card elicitation format to assess commuters' Willingness to Pay (WTP) for improved passenger waiting facilities. Respondents are first asked a dichotomous (yes/no) question on whether they are willing to contribute a nominal maintenance fee for the operation and upkeep of modern waiting sheds, loading zones, and terminals. Those who respond affirmatively are then presented with a payment card listing pre-determined bid amounts (₱2.00, ₱5.00, ₱10.00, and more than ₱10.00 per trip) and asked to select the maximum amount they would be willing to contribute. The payment card format was chosen because it reduces the cognitive burden on respondents and mitigates the starting-point bias commonly associated with single-bounded dichotomous choice formats. This approach follows standard CVM practice in transportation research (Saptutyningsih & Karimah, 2019; Lalio & Navarro, 2025).

---

## [REPLACE line 371 in Section 3.6 — CVM paragraph in Data Analysis]

**Old:**
"In order to estimate the importance, the commuters attach to the improved facilities, we will use the Contingent Valuation Method (CVM). This approximates readiness to pay the enhancement such as waiting stations. We shall interpret the survey data using descriptive statistics and identify the mean willingness to pay and support of the proposed upgrades."

**New:**

#### 3.6.2 Contingent Valuation Method and Willingness to Pay

The Contingent Valuation Method (CVM) is employed to estimate the economic value that commuters place on improved passenger waiting facilities. CVM is a stated-preference, survey-based technique used to value non-market goods and services — in this case, the availability and maintenance of waiting sheds, loading zones, and terminals along the jeepney corridor.

The WTP analysis proceeds as follows:
1. **Proportion of positive responses:** The frequency and percentage of respondents willing to contribute a maintenance fee are tabulated to gauge overall public support for infrastructure improvements.
2. **Maximum WTP distribution:** For willing respondents, the distribution of selected bid amounts (₱2.00, ₱5.00, ₱10.00, >₱10.00) is summarized using frequency counts and percentages.
3. **Mean WTP estimation:** The mean willingness to pay is computed using the weighted average formula:

   Mean WTP = (Σᵢ fᵢ × mᵢ) / n

   where fᵢ is the frequency of responses at bid amount i, mᵢ is the midpoint of bid category i, and n is the total number of willing respondents. For the open-ended category (>₱10.00), the midpoint is conservatively estimated at ₱15.00 based on the observed distribution of write-in responses.

4. **Protest response identification:** Respondents who answered "No" to the dichotomous question are examined for protest behavior (e.g., objections to the payment vehicle rather than the facility itself). Protest responses are documented separately from genuine zero WTP values to avoid downward bias in mean WTP estimates.

The resulting mean WTP value is interpreted as the average economic benefit per commuter per trip, providing a monetary justification for infrastructure investment decisions and a reference point for setting maintenance fee structures.
