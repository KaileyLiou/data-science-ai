# Girls Who Code Data Science + AI Track

These are the projects I made while completing the Girls Who Code Data Science + AI Track. I worked with different datasets throughout the track and learned more about data cleaning, visualization, and machine learning in Python.

The starting code for these projects was provided as part of the Girls Who Code course templates, including the comments already in the files. I wrote the rest of the code and did the analysis and outputs myself, including the graphs, figures, tables, and confusion matrices.

<table>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/157444f3-97d9-4c49-9a7f-3f57b604c52d" width="450"></td>
    <td><img src="https://github.com/user-attachments/assets/9f84a8fa-3505-4aa9-a439-ee3999c26118" width="450"></td>
  </tr>
</table>

## Projects

| Project | Description |
|---------|-------------|
| [**Cardio Tree Classifier**](./cardiotree_classifier/) | Used a decision tree with health data to predict heart disease. I also looked at which factors were most important to the model. |
| [**Empowering Data: Women's Wellness**](./empowering_data_womens_wellness/) | Looked at a global women's wellness dataset and used data analysis to find patterns in the data. |
| [**Styles & Signs: Final Challenge**](./styles_signs_final_challenge/) | Built and tested a model that recognizes American Sign Language letters using the Sign Language MNIST dataset. |
| [**Talking Data: Comparing Favorites**](./talking_data_comparing_favorites/) | Used survey data to compare people's preferences with statistics and visualizations. |

## Tools

- Python
- pandas
- NumPy
- matplotlib
- scikit-learn

<!-- ## Repository Structure

```text
data-science-ai/
├── cardiotree_classifier/
├── empowering_data_womens_wellness/
├── styles_signs_final_challenge/
└── talking_data_comparing_favorites/
``` -->

## Running the Project

You can download the executables from the [Releases](../../releases) page or run the Python files directly.

### macOS

1. Go to the [Releases](../../releases) page and download the executable for the project you want:
   - `cardiotree_classifier_mac`
   - `empowering_data_womens_wellness_mac`
   - `talking_data_comparing_favorites_mac`

2. Open Terminal and navigate to your Downloads folder:

```bash
cd ~/Downloads
```

3. Make the downloaded file executable:

```bash
chmod +x <filename>
```

4. Remove the macOS quarantine attribute:

```bash
xattr -d com.apple.quarantine <filename>
```

5. Run the executable:

```bash
./<filename>
```

### From Python

Clone the repository and install the required libraries:

```bash
git clone https://github.com/KaileyLiou/data-science-ai.git
cd data-science-ai
pip install pandas numpy matplotlib scikit-learn
```

Then go into the folder for the project you want to run:

```bash
cd <project_folder_name>
python main.py
```
