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

For an easy-to-run version, download the executable for the project you want from the project's [Releases](../../releases) page. Alternatively, you can run the Python source code directly.

### How to Run on macOS

1. Go to the project's [Releases](../../releases) page and download the executable for the project you want:
   - `cardiotree_classifier_mac` - CardioTree Classifier
   - `empowering_data_womens_wellness_mac` - Empowering Data: Women's Wellness
   - `talking_data_comparing_favorites_mac` - Talking Data: Comparing Favorites

2. The downloaded file will usually be in your `Downloads` folder.

3. Open Terminal and navigate to your Downloads folder:

```bash
cd ~/Downloads
```

4. Make the downloaded file executable. Replace `<filename>` with the name of the file you downloaded:

```bash
chmod +x <filename>
```

5. Remove macOS's quarantine attribute:

```bash
xattr -d com.apple.quarantine <filename>
```

6. Run the executable:

```bash
./<filename>
```

### Run from Source Code

**1. Clone the repository**

```bash
git clone https://github.com/KaileyLiou/data-science-ai.git
cd data-science-ai
```

**2. Install dependencies**

```bash
pip install pandas numpy matplotlib scikit-learn
```

**3. Run a specific project**

Navigate into the project folder and execute its `main.py` file:

```bash
cd <project_folder_name>
python main.py
```
