# Girls Who Code Data Science + AI Track

This repository contains the projects I completed as part of the Girls Who Code Data Science + AI Track. Throughout the track, I explored the data science workflow, from cleaning and visualizing data to building and evaluating machine learning models in Python. Each folder represents a different project that builds on skills introduced throughout the courses.

<table>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/157444f3-97d9-4c49-9a7f-3f57b604c52d" width="450"></td>
    <td><img src="https://github.com/user-attachments/assets/9f84a8fa-3505-4aa9-a439-ee3999c26118" width="450"></td>
  </tr>
</table>

## Projects

| Project | Description |
|---------|-------------|
| [**Cardio Tree Classifier**](./cardiotree_classifier/) | Built a decision tree classifier to predict heart disease outcomes and explored feature importance to better understand the model's decisions. |
| [**Empowering Data: Women's Wellness**](./empowering_data_womens_wellness/) | Analyzed a global women's wellness dataset to identify trends and communicate insights through data visualizations and storytelling. |
| [**Styles & Signs: Final Challenge**](./styles_signs_final_challenge/) | Trained and evaluated machine learning models to classify American Sign Language letters using the Sign Language MNIST dataset. |
| [**Talking Data: Comparing Favorites**](./talking_data_comparing_favorites/) | Explored survey data using descriptive statistics and visualizations to compare preferences across different groups. |

## Skills & Technologies

- **Programming:** Python
- **Data Analysis:** pandas, NumPy
- **Data Visualization:** matplotlib
- **Machine Learning:** scikit-learn (Decision Trees, Neural Networks)

## Repository Structure

```text
data-science-ai/
├── cardiotree_classifier/
├── empowering_data_womens_wellness/
├── styles_signs_final_challenge/
└── talking_data_comparing_favorites/
```

## Running the Project

For an easy-to-run version, download the executable from the project's [Releases](../../releases) page. Alternatively, you can run the Python source code directly.

### How to Run on macOS
1. Download the file from the project's **Releases** page (assets → main).
2. Open Terminal and navigate to your download folder:
3. Run these commands:

   ```bash
   cd ~/Downloads
   chmod +x main
   xattr -d com.apple.quarantine main
   ./main
   ```

### Run from Source Code

**1. Clone the repository**

```bash
git clone https://github.com/KaileyLiou/data-science-ai.git
```

**2. Install dependencies**

```bash
pip install pandas numpy matplotlib scikit-learn
```

**3. Run a specific project**

Navigate into any project folder and execute its main Python file:

```bash
cd <project_folder_name>
python main.py
```

