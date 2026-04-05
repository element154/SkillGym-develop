---
license: cc-by-4.0
---

# Dataset Card for CrediBench 1.1

<!-- Provide a quick summary of the dataset. -->

CrediBench 1.1 is a large-scale, temporal webgraph constituted of web data pulled from [Common Crawl](https://commoncrawl.org/overview). 
A prior version of the paper is [available here](https://arxiv.org/abs/2509.23340) (NPGML workshop @ NeurIPS 2025), with the latest version still under review. 
CrediBench 1.0, presented in this prior work, constituted of a static webgraph with 1 month's data, while the current version contains 3 months of data (October to December 2024, surrounding the U.S Federal elections, a period of increased misinformation). 
We are actively constructing and uploading more monthly graphs as well.  


## Dataset Details

### Dataset Description

<!-- Provide a longer summary of what this dataset is. -->
This dataset is composed of monthly slices of large-scale web networks. These webgraphs contain 1+ billion edges, and 45+ million nodes per month.
In these webgraphs, the nodes represent a website domain (e.g, `google.com`) and an edge represents a directed hyperlink relation (e.g, an edge from `cbc.ca` to `reuters.com` indicates that a page on `cbc.ca`'s website contains a hyperlink to a `reuters.com` page).
These webgraphs are supplemented with text attributes, partly from Common Crawl and from web scraping, as text features play an important role in misinformation detection. 
Additionally, we supplement them with credibility scores as made available by [Lin et al.](https://github.com/hauselin/domain-quality-ratings/tree/main/data), to enable supervised and semi-supervised learning as explained in our paper. 

- **Curated by** a team of collaborators from the Complex Data Lab @ Mila - Quebec AI Institute, the University of Oxford, McGill University, Concordia University, UC Berkeley, University of Montreal, and AITHYRA.
- **Funding:** This research was supported by the Engineering and Physical Sciences Research Council (EPSRC) and the AI Security Institute (AISI) grant:
*Towards Trustworthy AI Agents for Information Veracity and the EPSRC Turing AI World-Leading Research Fellowship No. EP/X040062/1 and EPSRC AI
Hub No. EP/Y028872/1*. This research was also enabled in part by compute resources provided by Mila (mila.quebec) and Compute Canada.
- **License:** CC-BY-4.0 (as retributed from Common Crawl).

Dataset Statistics: 
| Month | V | E | Min. deg. | Mean deg. | Max. deg. | Leaves (deg. = 1) | Edge Density | 
| -- | -- | -- | -- | -- | -- | -- | -- |
| October 2024 | 50,288,479 | 1,074,971,387 | 1 | 42.75 | 17,112,352 | 30,278 | 4.3e-07 | 
| November 2024 | 27,567,417 | 555,905,375 | 1 | 40.33 | 9,019,038 | 30,553 | 7.3e-07 | 
| December 2024 | 45,030,252 | 1,014,523,551 | 1 | 45.06 | 14,719,077 | 28,857 | 5.0e-07 | 
| February 2025 | 49,639,664 | 1,167,748,533 | 1 | 47.05 | 17,078,954 | 24,430 | 4.7e-07 | 
<!-- | January 2025 |  -->
<!-- | March 2025 | 50,162,733 | 1,212,826,396 | 1 | 48.36 | 16,691,193 | 22,629 | 4.8e-07 |  -->
<!-- | April 2025 | 17,998,846 | 349,717,108 | 1 | 38.86 | 5,284,367 | 25,606 | 1.1e-06 | -->
<!-- | May 2025 | 5,833,993 | 87,752,862 | 1 | 30.08 | 1,581,282 | 17,683 | 2.6e-06 |  -->
<!-- | June 2025 | 9,974,275 | 152,449,542 | 1 | 30.57 | 3,381,364 | 25,447 | 1.5e06 |  -->

### Resources

<!-- Provide the basic links for the dataset. -->

- **[Repository](https://github.com/ekmpa/CrediGraph)** 
- **[Paper](https://arxiv.org/abs/2509.23340)**
- **[Common Crawl](https://commoncrawl.org/overview)** is our primary data source, supplemented with web scraping and multiple datasets for credibility signals:
  - [DQR](https://github.com/hauselin/domain-quality-ratings/tree/main/data) for credibility scores for supervised learning, and
  - [Yasin et al.](https://doi.org/10.1016/j.dib.2023.109959)'s phishing domains,
  - [Potpelwar et al.](https://doi.org/10.1016/j.dib.2025.111972)'s malware domains, and
  - [Aung et al.](https://dl.acm.org/doi/10.1145/3486622.3493983)'s legitimate domains, for semi-supervised learning.

## Uses

<!-- Address questions around how the dataset is intended to be used. -->
This dataset is intended as a data source for research efforts against misinformation online. Specifically, as the first large-scale, text-attributed webgraph that is also dynamic,
CrediBench stands as an ideal data source for efforts to develop methods for unreliable domain detection based on spatio-temporal cues. 

### Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the dataset will not work well for. -->
This dataset is not intended for LLM training. Designed for the goal of misinformation detection at the domain level and web scale, this dataset contains numerous 
domains and content pages that contain innapropriate content which may be harmful if used for training conversational AI, or other types of generative AI outside the scope of our task. 


### Data Collection and Processing

<!-- This section describes the data collection and processing process such as data selection criteria, filtering and normalization methods, tools and libraries used, etc. -->
The process of collection, processing and use is detailed in our team's paper. We collect data through our proposed CrediBench pipeline (available at our repository), 
which builds a month's worth of data by pulling from Common Crawl, builds the graph from it and processes it to discard isolated and low-degree nodes. 
Each edge has a timestamp, given as the date of the first day of week of the crawl, in format YYYYMMDD.


## Citation

<!-- If there is a paper or blog post introducing the dataset, the APA and Bibtex information for that should go in this section. -->

**BibTeX:**

```
@article{kondrupsabry2025credibench,
  title={{CrediBench: Building Web-Scale Network Datasets for Information Integrity}},
  author={Kondrup, Emma and Sabry, Sebastian and Abdallah, Hussein and Yang, Zachary and Zhou, James and Pelrine, Kellin and Godbout, Jean-Fran{\c{c}}ois and Bronstein, Michael and Rabbany, Reihaneh and Huang, Shenyang},
  journal={arXiv preprint arXiv:2509.23340},
  year={2025},
  note={New Perspectives in Graph Machine Learning Workshop @ NeurIPS 2025},
  url={https://arxiv.org/abs/2509.23340}
}
```

**APA:**

```
Kondrup, E., Sabry, S., Abdallah, H., Yang, Z., Zhou, J., Pelrine, K., Godbout, J.-F., Bronstein, M., Rabbany, R., & Huang, S. (2025).
CrediBench: Building Web-Scale Network Datasets for Information Integrity.
New Perspectives in Graph Machine Learning Workshop @ NeurIPS 2025. arXiv:2509.23340. https://arxiv.org/pdf/2509.23340
```

## Dataset Card Authors / Contact

For any questions on the dataset, please contact [Emma Kondrup](mailto:emma.kondrup@mila.quebec), [Sebastian Sabry](mailto:sebastian.sabry@mcgill.ca), or [Shenyang (Andy) Huang](mailto:shenyang.huang@mail.mcgill.ca).
